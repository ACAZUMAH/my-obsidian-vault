#!/usr/bin/env python3
"""Read-only semantic and provenance audit for the Obsidian knowledge vault."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import unquote

from validate_vault import extract_raw_source_references, strip_code

ROOT = Path(__file__).resolve().parents[1]
SEVERITY_ORDER = {"high": 0, "medium": 1, "low": 2, "info": 3}


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    message: str
    remediation: str


def split_frontmatter(path: Path) -> tuple[list[str], str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return [], "\n".join(lines)
    try:
        end = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        return [], "\n".join(lines)
    return lines[1:end], "\n".join(lines[end + 1 :])


def frontmatter_scalar(lines: list[str], key: str) -> str:
    prefix = f"{key}:"
    for line in lines:
        if line.startswith(prefix):
            return line[len(prefix) :].strip().strip('"\'')
    return ""


def frontmatter_list(lines: list[str], key: str) -> list[str]:
    prefix = f"{key}:"
    for index, line in enumerate(lines):
        if not line.startswith(prefix):
            continue
        value = line[len(prefix) :].strip()
        if value == "[]" or not value and index + 1 >= len(lines):
            return []
        if value.startswith("[") and value.endswith("]"):
            return [item.strip().strip('"\'') for item in value[1:-1].split(",") if item.strip()]
        items: list[str] = []
        for continuation in lines[index + 1 :]:
            match = re.match(r"^\s+-\s+(.+?)\s*$", continuation)
            if not match:
                break
            items.append(match.group(1).strip().strip('"\''))
        return items
    return []


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def resolve_wikilink(source: Path, target: str, by_stem: dict[str, list[Path]]) -> Path | None:
    clean = target.split("|", 1)[0].split("#", 1)[0].strip()
    if not clean:
        return None
    candidate = Path(clean)
    if candidate.suffix == "":
        candidate = candidate.with_suffix(".md")
    if clean.startswith("./") or clean.startswith("../"):
        resolved = (source.parent / candidate).resolve()
        return resolved if resolved.is_file() and ROOT in resolved.parents else None
    if "/" in clean:
        resolved = ROOT / candidate
        return resolved if resolved.is_file() else None
    local = source.parent / candidate
    if local.is_file():
        return local
    matches = by_stem.get(Path(clean).stem, [])
    return matches[0] if len(matches) == 1 else None


def audit_source_frontmatter() -> list[Finding]:
    findings: list[Finding] = []
    raw_relative = "raw/sources"
    for path in sorted((ROOT / "wiki" / "sources").glob("*.md")):
        frontmatter, _ = split_frontmatter(path)
        declared = {
            (path.parent / unquote(item)).resolve()
            for item in frontmatter_list(frontmatter, "sources")
            if item
        }
        body_references = {
            (path.parent / unquote(item)).resolve()
            for item in extract_raw_source_references(path.read_text(encoding="utf-8"), raw_relative)
        }
        if body_references and not declared:
            findings.append(
                Finding(
                    "medium",
                    "SOURCE_FRONTMATTER_EMPTY",
                    relative(path),
                    "The body references raw evidence, but the machine-readable sources list is empty.",
                    "Populate frontmatter sources with the existing raw-evidence path or paths.",
                )
            )
        elif declared != body_references:
            findings.append(
                Finding(
                    "medium",
                    "SOURCE_FRONTMATTER_MISMATCH",
                    relative(path),
                    "Frontmatter sources and body raw-evidence references do not identify the same files.",
                    "Reconcile the frontmatter list with the Source section without changing raw evidence.",
                )
            )
    return findings


def audit_index_dates(by_stem: dict[str, list[Path]]) -> list[Finding]:
    findings: list[Finding] = []
    index_path = ROOT / "index.md"
    pattern = re.compile(
        r"^\s*-\s+\[\[([^\]]+)\]\].*?\bUpdated:\s*(\d{4}-\d{2}-\d{2})\b",
        flags=re.MULTILINE,
    )
    for raw_target, indexed_date in pattern.findall(strip_code(index_path.read_text(encoding="utf-8"))):
        target = resolve_wikilink(index_path, raw_target, by_stem)
        if target is None:
            continue
        frontmatter, _ = split_frontmatter(target)
        page_date = frontmatter_scalar(frontmatter, "updated")
        if page_date and indexed_date != page_date:
            findings.append(
                Finding(
                    "low",
                    "INDEX_UPDATED_MISMATCH",
                    relative(target),
                    f"index.md reports Updated: {indexed_date}, but page frontmatter reports {page_date}.",
                    "Refresh the index entry metadata from the page frontmatter.",
                )
            )
    return findings


def audit_wiki_graph(wiki_pages: list[Path], by_stem: dict[str, list[Path]]) -> list[Finding]:
    findings: list[Finding] = []
    inbound: Counter[Path] = Counter()
    note_roots = [ROOT / "index.md", ROOT / "welcome.md", ROOT / "schema", ROOT / "scripts", ROOT / "wiki"]
    note_files: list[Path] = []
    for root in note_roots:
        if root.is_file():
            note_files.append(root)
        elif root.is_dir():
            note_files.extend(root.rglob("*.md"))

    for source in note_files:
        text = strip_code(source.read_text(encoding="utf-8"))
        for raw_target in re.findall(r"\[\[([^\]]+)\]\]", text):
            target = resolve_wikilink(source, raw_target, by_stem)
            if target is not None and target in wiki_pages and target != source:
                inbound[target] += 1

    for path in wiki_pages:
        if inbound[path] == 0:
            findings.append(
                Finding(
                    "medium",
                    "ORPHAN_WIKI_PAGE",
                    relative(path),
                    "No inbound wikilink was found from the index, schema, scripts, welcome page, or another wiki page.",
                    "Link the page from its owner or index it; merge or remove it only with explicit authorization.",
                )
            )

    titles: defaultdict[str, list[Path]] = defaultdict(list)
    for path in wiki_pages:
        _, body = split_frontmatter(path)
        match = re.search(r"^#\s+(.+?)\s*$", body, flags=re.MULTILINE)
        if match:
            titles[match.group(1).strip().casefold()].append(path)
    for paths in titles.values():
        if len(paths) > 1:
            joined = ", ".join(relative(path) for path in paths)
            findings.append(
                Finding(
                    "medium",
                    "DUPLICATE_WIKI_TITLE",
                    relative(paths[0]),
                    f"Multiple wiki pages share the same H1 title: {joined}.",
                    "Confirm ownership and merge or disambiguate only with explicit authorization.",
                )
            )
    return findings


def audit_markdown_assets() -> list[Finding]:
    assets = sorted((ROOT / "raw" / "assets").rglob("*.md"))
    if not assets:
        return []
    referenced: set[Path] = set()
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or path.is_relative_to(ROOT / "raw"):
            continue
        text = strip_code(path.read_text(encoding="utf-8"))
        for raw_target in re.findall(r"\]\(([^)]+)\)", text):
            target = unquote(raw_target.strip().strip("<>\"'"))
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            if resolved.is_file() and (ROOT / "raw" / "assets") in resolved.parents:
                referenced.add(resolved)
    return [
        Finding(
            "info",
            "UNREFERENCED_MARKDOWN_ASSET",
            relative(path),
            "A Markdown file under raw/assets is not referenced by durable vault content.",
            "Classify it as an attachment or ingest it through the raw-source and Source Record path.",
        )
        for path in assets
        if path.resolve() not in referenced
    ]


def collect_findings() -> list[Finding]:
    wiki_pages = sorted((ROOT / "wiki").rglob("*.md"))
    all_notes = [path for path in ROOT.rglob("*.md") if ".git" not in path.parts]
    by_stem: defaultdict[str, list[Path]] = defaultdict(list)
    for path in all_notes:
        by_stem[path.stem].append(path)
    findings = audit_source_frontmatter()
    findings.extend(audit_index_dates(by_stem))
    findings.extend(audit_wiki_graph(wiki_pages, by_stem))
    findings.extend(audit_markdown_assets())
    return sorted(findings, key=lambda item: (SEVERITY_ORDER[item.severity], item.path, item.code))


def print_text(findings: list[Finding]) -> None:
    counts = Counter(item.severity for item in findings)
    status = "PASS" if not findings else "FINDINGS"
    print(
        f"VAULT_AUDIT={status} findings={len(findings)} "
        f"high={counts['high']} medium={counts['medium']} low={counts['low']} info={counts['info']}"
    )
    for item in findings:
        print(f"- [{item.severity.upper()}] {item.code} {item.path}: {item.message}")
        print(f"  Remediation: {item.remediation}")
    print("AUDIT_MODE=READ_ONLY")


def print_json(findings: list[Finding]) -> None:
    counts = Counter(item.severity for item in findings)
    payload = {
        "status": "pass" if not findings else "findings",
        "read_only": True,
        "counts": {
            "findings": len(findings),
            "high": counts["high"],
            "medium": counts["medium"],
            "low": counts["low"],
            "info": counts["info"],
        },
        "findings": [asdict(item) for item in findings],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument("--strict", action="store_true", help="exit 1 when any finding exists")
    args = parser.parse_args()

    findings = collect_findings()
    if args.json:
        print_json(findings)
    else:
        print_text(findings)
    return 1 if args.strict and findings else 0


if __name__ == "__main__":
    sys.exit(main())
