#!/usr/bin/env python3
"""Canonical structural validator for the Obsidian knowledge vault."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
STRUCTURE_FILE = ROOT / "schema" / "vault-structure.json"
FRONTMATTER_SCHEMA_FILE = ROOT / "schema" / "wiki-frontmatter.schema.json"

errors: list[str] = []
counts: defaultdict[str, int] = defaultdict(int)


def fail(message: str) -> None:
    errors.append(message)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing JSON file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON: {path.relative_to(ROOT)}:{exc.lineno}:{exc.colno}: {exc.msg}")
    return None


def strip_code(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"~~~.*?~~~", "", text, flags=re.DOTALL)
    return re.sub(r"`[^`\n]*`", "", text)


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        fail(f"missing frontmatter opener: {path.relative_to(ROOT)}")
        return {}, text

    try:
        end = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        fail(f"missing frontmatter closer: {path.relative_to(ROOT)}")
        return {}, text

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
        if match:
            fields[match.group(1)] = (match.group(2) or "").strip().strip('"\'')
    return fields, "\n".join(lines[end + 1 :])


def extract_raw_source_references(text: str, raw_relative: str) -> set[str]:
    prefix = rf"(?:\.\./)*{re.escape(raw_relative)}/"
    patterns = [
        rf"\]\(<({prefix}[^>\n]+)>\)",
        rf"\]\(({prefix}[^)\n]+)\)",
        rf"`({prefix}[^`\n]+)`",
        rf"^\s*-\s+({prefix}.+?)\s*$",
        rf"^\s*-\s+[^:\n]+:\s+({prefix}.+?)\s*$",
    ]
    references: set[str] = set()
    for pattern in patterns:
        for candidate in re.findall(pattern, text, flags=re.MULTILINE):
            candidate = unquote(candidate.strip().strip("<>\"'"))
            if not Path(candidate).suffix or any(char in candidate for char in "*?[]"):
                continue
            references.add(candidate)
    return references


def validate_structure(config: dict[str, Any]) -> None:
    index_text = strip_code((ROOT / "index.md").read_text(encoding="utf-8"))
    for relative in config.get("required_directories", []):
        path = ROOT / relative
        if not path.is_dir():
            fail(f"missing required directory: {relative}")
        else:
            counts["required_directories"] += 1

    for page_type, relative in config.get("templates", {}).items():
        path = ROOT / relative
        if not path.is_file():
            fail(f"missing {page_type} template: {relative}")
            continue
        fields, _ = parse_frontmatter(path)
        if fields.get("type") != "template":
            fail(f"template type must be 'template': {relative}")
        link_target = Path(relative).with_suffix("").as_posix()
        if f"[[{link_target}|" not in index_text and f"[[{link_target}]]" not in index_text:
            fail(f"{page_type} template is not linked from index.md: {relative}")
        else:
            counts["template_index_links"] += 1
        counts["templates"] += 1

    for document, relative in config.get("schema_documents", {}).items():
        path = ROOT / relative
        if not path.is_file():
            fail(f"missing {document} schema document: {relative}")
            continue
        if f"]({relative})" not in index_text:
            fail(f"{document} schema document is not linked from index.md: {relative}")
        else:
            counts["schema_document_index_links"] += 1
        counts["schema_documents"] += 1

    old_templates = ROOT / "wiki" / "templates"
    if old_templates.exists():
        fail("legacy directory still exists: wiki/templates")


def validate_obsidian_configuration() -> None:
    templates = load_json(ROOT / ".obsidian" / "templates.json")
    if isinstance(templates, dict) and templates.get("folder") != "_template":
        fail(".obsidian/templates.json must set folder to '_template'")

    core_plugins = load_json(ROOT / ".obsidian" / "core-plugins.json")
    if isinstance(core_plugins, dict) and core_plugins.get("templates") is not True:
        fail("Obsidian core Templates plugin must be enabled")

    counts["obsidian_configuration"] += 2


def validate_agent_skills(config: dict[str, Any]) -> None:
    skills_root = ROOT / ".agents" / "skills"
    for name in config.get("required_agent_skills", []):
        skill_file = skills_root / name / "SKILL.md"
        if not skill_file.is_file():
            fail(f"missing project-local skill: .agents/skills/{name}/SKILL.md")
            continue

        fields, body = parse_frontmatter(skill_file)
        if fields.get("name") != name:
            fail(f"skill name mismatch in {skill_file.relative_to(ROOT)}")
        if not fields.get("description"):
            fail(f"skill description missing in {skill_file.relative_to(ROOT)}")
        if not body.strip():
            fail(f"skill body missing in {skill_file.relative_to(ROOT)}")

        clean_body = strip_code(body)
        for relative in re.findall(r"\]\((references/[^)#]+)(?:#[^)]+)?\)", clean_body):
            linked = skill_file.parent / relative
            if not linked.is_file():
                fail(f"missing skill support file: {linked.relative_to(ROOT)}")

        counts["agent_skills"] += 1


def validate_wiki_pages(config: dict[str, Any]) -> None:
    required_frontmatter = set(config.get("required_frontmatter", []))
    allowed_statuses = set(config.get("allowed_statuses", []))
    required_sections: dict[str, list[str]] = config.get("required_sections", {})
    section_overrides: dict[str, list[str]] = config.get("section_overrides", {})
    page_type_directories: dict[str, str] = config.get("page_type_directories", {})
    allowed_types = set(required_sections) | {"template"}
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    for path in sorted((ROOT / "wiki").rglob("*.md")):
        fields, body = parse_frontmatter(path)
        missing = sorted(required_frontmatter - fields.keys())
        if missing:
            fail(f"missing frontmatter {missing}: {path.relative_to(ROOT)}")

        page_type = fields.get("type")
        status = fields.get("status")
        if page_type not in allowed_types:
            fail(f"invalid page type {page_type!r}: {path.relative_to(ROOT)}")
        expected_directory = page_type_directories.get(page_type, "")
        if expected_directory and (ROOT / expected_directory) not in path.parents:
            fail(
                f"page type {page_type!r} must live under {expected_directory}: "
                f"{path.relative_to(ROOT)}"
            )
        if status not in allowed_statuses:
            fail(f"invalid status {status!r}: {path.relative_to(ROOT)}")
        for key in ("created", "updated"):
            value = fields.get(key, "")
            if value and not date_pattern.fullmatch(value):
                fail(f"invalid {key} date {value!r}: {path.relative_to(ROOT)}")

        headings = [match.group(1).strip() for match in re.finditer(r"^##\s+(.+?)\s*$", body, flags=re.MULTILINE)]
        page_sections = required_sections.get(page_type, []) if page_type is not None else []
        relative_path = path.relative_to(ROOT).as_posix()
        for prefix, override_sections in section_overrides.items():
            if relative_path.startswith(prefix.rstrip("/") + "/"):
                page_sections = override_sections
                break
        for required in page_sections:
            if not any(heading == required or heading.startswith(required + " ") for heading in headings):
                fail(f"missing section '## {required}': {path.relative_to(ROOT)}")

        counts["wiki_pages"] += 1


def validate_source_records(config: dict[str, Any]) -> None:
    canonical_paths: dict[str, str] = config.get("canonical_paths", {})
    policy: dict[str, bool] = config.get("source_record_policy", {})
    raw_relative = canonical_paths.get("raw_sources", "raw/sources").rstrip("/")
    records_relative = canonical_paths.get("wiki_sources", "wiki/sources").rstrip("/")
    raw_root = (ROOT / raw_relative).resolve()
    records_root = (ROOT / records_relative).resolve()

    if not raw_root.is_dir() or not records_root.is_dir():
        return

    raw_files = {
        path.resolve()
        for path in raw_root.rglob("*")
        if path.is_file()
        and not any(part.startswith(".") for part in path.relative_to(raw_root).parts)
    }
    source_records = sorted(records_root.rglob("*.md"))
    raw_owners: defaultdict[Path, set[Path]] = defaultdict(set)
    record_references: dict[Path, set[Path]] = {}
    index_text = strip_code((ROOT / "index.md").read_text(encoding="utf-8"))

    for path in source_records:
        references: set[Path] = set()
        for relative in extract_raw_source_references(
            path.read_text(encoding="utf-8"), raw_relative
        ):
            target = (path.parent / relative).resolve()
            if raw_root not in target.parents:
                fail(f"raw source reference escapes {raw_relative}: {path.relative_to(ROOT)}")
                continue
            if not target.is_file():
                fail(
                    f"missing raw source referenced by {path.relative_to(ROOT)}: "
                    f"{target.relative_to(ROOT)}"
                )
                continue
            references.add(target)
            raw_owners[target].add(path)

        record_references[path] = references
        if policy.get("require_raw_reference", True) and not references:
            fail(f"source record has no valid raw source reference: {path.relative_to(ROOT)}")
        if not policy.get("allow_aggregation", True) and len(references) > 1:
            fail(f"source record aggregates raw sources: {path.relative_to(ROOT)}")

        link_target = path.relative_to(ROOT).with_suffix("").as_posix()
        if policy.get("require_index_link", True):
            if f"[[{link_target}|" not in index_text and f"[[{link_target}]]" not in index_text:
                fail(f"source record is not linked from index.md: {path.relative_to(ROOT)}")
            else:
                counts["source_record_index_links"] += 1

    if policy.get("require_raw_coverage", True):
        for path in sorted(raw_files):
            if path not in raw_owners:
                fail(f"raw source has no source record: {path.relative_to(ROOT)}")

    if not policy.get("allow_shared_evidence", True):
        for path, owners in sorted(raw_owners.items()):
            if len(owners) > 1:
                fail(f"raw source is shared by source records: {path.relative_to(ROOT)}")

    counts["raw_sources"] = len(raw_files)
    counts["raw_sources_covered"] = len(raw_files & raw_owners.keys())
    counts["raw_sources_shared"] = sum(len(owners) > 1 for owners in raw_owners.values())
    counts["source_record_raw_references"] = sum(map(len, record_references.values()))
    counts["source_records"] = len(source_records)
    counts["source_records_aggregating_raw"] = sum(
        len(references) > 1 for references in record_references.values()
    )


def validate_json_files() -> None:
    paths = [
        ROOT / "schema" / "vault-structure.json",
        ROOT / "schema" / "wiki-frontmatter.schema.json",
        ROOT / ".obsidian" / "app.json",
        ROOT / ".obsidian" / "appearance.json",
        ROOT / ".obsidian" / "community-plugins.json",
        ROOT / ".obsidian" / "core-plugins.json",
        ROOT / ".obsidian" / "graph.json",
        ROOT / ".obsidian" / "templates.json",
    ]
    for path in paths:
        if load_json(path) is not None:
            counts["json_files"] += 1


def validate_stale_template_references() -> None:
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts or ".obsidian" in path.parts or path.name == "log.md":
            continue
        clean = strip_code(path.read_text(encoding="utf-8"))
        if "wiki/templates" in clean:
            fail(f"stale wiki/templates reference: {path.relative_to(ROOT)}")


def note_files() -> list[Path]:
    excluded_roots = {".git", ".obsidian", ".agents"}
    return [
        path
        for path in ROOT.rglob("*.md")
        if not any(part in excluded_roots for part in path.relative_to(ROOT).parts)
    ]


def validate_wikilinks() -> None:
    notes = note_files()
    by_stem: defaultdict[str, list[Path]] = defaultdict(list)
    for note in notes:
        by_stem[note.stem].append(note)

    checked = 0
    for path in notes:
        clean = strip_code(path.read_text(encoding="utf-8"))
        for raw in re.findall(r"\[\[([^\]]+)\]\]", clean):
            target = raw.split("|", 1)[0].split("#", 1)[0].strip()
            if not target:
                continue

            target_path = Path(target)
            if target_path.suffix == "":
                target_path = target_path.with_suffix(".md")

            if target.startswith("./") or target.startswith("../"):
                resolved = (path.parent / target_path).resolve()
                exists = resolved.is_file() and ROOT in resolved.parents
            elif "/" in target:
                exists = (ROOT / target_path).is_file()
            else:
                local = path.parent / target_path
                exists = local.is_file() or bool(by_stem.get(Path(target).stem))

            if not exists:
                fail(f"broken wikilink [[{raw}]] in {path.relative_to(ROOT)}")
            checked += 1

    counts["wikilinks"] = checked


def main() -> int:
    structure = load_json(STRUCTURE_FILE)
    schema = load_json(FRONTMATTER_SCHEMA_FILE)
    if not isinstance(structure, dict) or not isinstance(schema, dict):
        structure = structure if isinstance(structure, dict) else {}

    validate_structure(structure)
    validate_obsidian_configuration()
    validate_agent_skills(structure)
    validate_wiki_pages(structure)
    validate_source_records(structure)
    validate_json_files()
    validate_stale_template_references()
    validate_wikilinks()

    if errors:
        print(f"VAULT_VALIDATION=FAIL errors={len(errors)}")
        for message in errors:
            print(f"- {message}")
        return 1

    print("VAULT_VALIDATION=PASS")
    for key in sorted(counts):
        print(f"{key.upper()}={counts[key]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
