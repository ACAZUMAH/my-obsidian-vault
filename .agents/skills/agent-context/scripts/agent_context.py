#!/usr/bin/env python3
"""Save, find, and recover agent session handoffs across accounts and agents.

Snapshots live in <vault>/raw/agent-contexts/<workstream>/<UTC-stamp>--<topic>.md.
Each save creates a new file; the newest file per topic is the current state.

Commands:
  new TOPIC         Create a prefilled snapshot skeleton and print its path.
  status            Show the latest snapshot per topic (one workstream or all).
  hook              Claude Code SessionStart hook: inject open handoffs as context.
  transcripts       List native Claude Code / Codex transcripts for a repository.
  digest FILE       Print a compact user/assistant digest of a native transcript.

Standard library only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path

VAULT = Path(
    os.environ.get("OBSIDIAN_VAULT_PATH")
    or Path(__file__).resolve().parents[4]
)
CONTEXTS = VAULT / "raw" / "agent-contexts"
HOME = Path.home()
STAMP_FORMAT = "%Y-%m-%dT%H%M%SZ"
STATUSES = ("in-progress", "blocked", "done")
SECTIONS = (
    "Objective",
    "Authorization State",
    "Current State",
    "Decisions And Constraints",
    "Failed Approaches And Gotchas",
    "Next Steps",
    "References",
)


def kebab(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "general"


def git(cwd: Path, *args: str) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(cwd), *args],
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return result.stdout.strip() if result.returncode == 0 else ""


def repo_root(cwd: Path) -> Path:
    """Main checkout root, so worktrees map to the same workstream."""
    common = git(cwd, "rev-parse", "--path-format=absolute", "--git-common-dir")
    if common:
        path = Path(common)
        return path.parent if path.name == ".git" else path
    return cwd


def workstream_for(cwd: Path) -> str:
    return kebab(repo_root(cwd).name)


def detect_agent() -> tuple[str, str]:
    if os.environ.get("CLAUDECODE"):
        return "claude-code", os.environ.get("CLAUDE_CODE_SESSION_ID", "")
    for key in ("CODEX_THREAD_ID", "CODEX_SESSION_ID"):
        if os.environ.get(key):
            return "codex", os.environ[key]
    profile = os.environ.get("HERMES_PROFILE")
    if profile or os.environ.get("HERMES_HOME"):
        return f"hermes:{profile or 'default'}", os.environ.get("HERMES_SESSION_ID", "")
    return "unknown", ""


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip()
    return fields


def snapshots(workstream_dir: Path) -> list[Path]:
    return sorted(p for p in workstream_dir.glob("*--*.md") if p.is_file())


def latest_by_topic(workstream_dir: Path) -> dict[str, Path]:
    latest: dict[str, Path] = {}
    for path in snapshots(workstream_dir):
        topic = path.stem.split("--", 1)[1]
        latest[topic] = path  # sorted ascending, so last wins
    return latest


def cmd_new(args: argparse.Namespace) -> int:
    cwd = Path(args.cwd).resolve()
    workstream = kebab(args.workstream) if args.workstream else workstream_for(cwd)
    topic = kebab(args.topic)
    agent, session_id = detect_agent()
    agent = args.agent or agent
    session_id = args.session_id or session_id
    now = dt.datetime.now(dt.timezone.utc)

    directory = CONTEXTS / workstream
    directory.mkdir(parents=True, exist_ok=True)
    previous = latest_by_topic(directory).get(topic)
    path = directory / f"{now.strftime(STAMP_FORMAT)}--{topic}.md"
    if path.exists():
        print(f"refusing to overwrite existing snapshot: {path}", file=sys.stderr)
        return 1

    in_git = bool(git(cwd, "rev-parse", "--is-inside-work-tree"))
    dirty = git(cwd, "status", "--porcelain") if in_git else ""
    fields = {
        "type": "agent-context",
        "workstream": workstream,
        "topic": topic,
        "status": args.status,
        "agent": agent,
        "session_id": session_id,
        "saved": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "cwd": str(cwd),
        "branch": git(cwd, "branch", "--show-current") if in_git else "",
        "head": git(cwd, "rev-parse", "--short", "HEAD") if in_git else "",
        "dirty_files": str(len(dirty.splitlines())) if in_git else "",
        "previous": previous.name if previous else "",
        "recovered_from": args.recovered_from or "",
    }
    lines = ["---", *(f"{k}: {v}" for k, v in fields.items()), "---", ""]
    lines.append(f"# {workstream} — {topic}")
    for section in SECTIONS:
        lines += ["", f"## {section}"]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(path)
    if previous:
        print(f"previous: {previous}", file=sys.stderr)
    return 0


def open_handoffs(directory: Path, include_done: bool = False) -> list[tuple[str, Path, dict[str, str]]]:
    """Newest snapshot per topic, newest first, skipping finished topics unless asked."""
    result = []
    for topic, path in sorted(latest_by_topic(directory).items(), key=lambda kv: kv[1].name, reverse=True):
        fields = parse_frontmatter(path)
        if fields.get("status") == "done" and not include_done:
            continue
        result.append((topic, path, fields))
    return result


def cmd_hook(args: argparse.Namespace) -> int:
    """Claude Code SessionStart hook: surface open handoffs for the session's repository.

    Prints nothing when there are none. Never fails the session: any error exits 0 silently.
    """
    try:
        payload: dict = {}
        if not sys.stdin.isatty():
            raw = sys.stdin.read()
            if raw.strip():
                payload = json.loads(raw)
        cwd = Path(payload.get("cwd") or os.getcwd()).resolve()
        directory = CONTEXTS / workstream_for(cwd)
        entries = open_handoffs(directory)
        if not entries:
            return 0
        lines = [f"Open agent-context handoffs for workstream `{directory.name}` (newest snapshot per topic):"]
        for topic, path, fields in entries:
            lines.append(
                f"- [{fields.get('status', '?')}] `{topic}`: saved {fields.get('saved', '?')} by "
                f"{fields.get('agent', '?')} on branch `{fields.get('branch') or '-'}`. Snapshot: {path}"
            )
        lines.append(
            "If the user's request continues one of these, or they say resume/continue/pick up, follow the "
            "agent-context skill's Resume procedure: read that snapshot in full, verify it against live Git "
            "state, and act only within its Authorization State. If the request is unrelated, ignore this note."
        )
        topics = ", ".join(topic for topic, _, _ in entries)
        print(json.dumps({
            "systemMessage": f"agent-context: open handoff in {directory.name}: {topics}",
            "hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "\n".join(lines)},
        }))
    except Exception:  # a broken hook must never block session start
        return 0
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    if args.all:
        directories = sorted(p for p in CONTEXTS.iterdir() if p.is_dir()) if CONTEXTS.is_dir() else []
    else:
        name = kebab(args.workstream) if args.workstream else workstream_for(Path(args.cwd).resolve())
        directories = [CONTEXTS / name]

    shown = 0
    for directory in directories:
        for topic, path, fields in open_handoffs(directory, args.include_done):
            shown += 1
            print(
                f"{fields.get('status', '?'):<11} {directory.name}/{topic}  saved={fields.get('saved', '?')}  "
                f"agent={fields.get('agent', '?')}  branch={fields.get('branch') or '-'}\n"
                f"            {path}"
            )
    if not shown:
        target = "any workstream" if args.all else directories[0].name
        print(f"no open handoffs for {target}")
    return 0


def claude_dir_name(path: Path) -> str:
    return re.sub(r"[^A-Za-z0-9]", "-", str(path))


def codex_cwd(path: Path) -> str:
    try:
        with path.open(encoding="utf-8", errors="replace") as handle:
            for _, line in zip(range(40), handle):
                record = json.loads(line)
                payload = record.get("payload") or {}
                if record.get("type") in ("session_meta", "turn_context") and payload.get("cwd"):
                    return payload["cwd"]
    except (OSError, json.JSONDecodeError):
        pass
    return ""


def last_activity(path: Path) -> str:
    """Timestamp of the last record; file mtimes are unreliable (backup/sync touches)."""
    try:
        with path.open("rb") as handle:
            handle.seek(0, os.SEEK_END)
            handle.seek(max(0, handle.tell() - 262144))
            tail = handle.read().decode("utf-8", errors="replace").splitlines()
    except OSError:
        return ""
    for line in reversed(tail):
        match = re.search(r'"timestamp":\s*"([^"]+)"', line)
        if match:
            return match.group(1)[:19] + "Z"
    return ""


def cmd_transcripts(args: argparse.Namespace) -> int:
    root = repo_root(Path(args.cwd).resolve())
    cutoff = dt.datetime.now().timestamp() - args.days * 86400
    candidates: list[tuple[str, Path]] = []

    prefix = claude_dir_name(root)
    projects = HOME / ".claude" / "projects"
    if projects.is_dir():
        for directory in projects.iterdir():
            if directory.name == prefix or directory.name.startswith(prefix + "-"):
                candidates += [("claude-code", path) for path in directory.glob("*.jsonl")]

    sessions = HOME / ".codex" / "sessions"
    if sessions.is_dir():
        for path in sessions.rglob("*.jsonl"):
            if path.stat().st_mtime < cutoff:  # coarse prefilter only
                continue
            cwd = codex_cwd(path)
            if cwd and (cwd == str(root) or cwd.startswith(str(root) + os.sep)):
                candidates.append(("codex", path))

    since = dt.datetime.fromtimestamp(cutoff, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    found = [
        (stamp, agent, path)
        for agent, path in candidates
        if (stamp := last_activity(path)) and stamp >= since
    ]
    found.sort(reverse=True)
    for stamp, agent, path in found[: args.limit]:
        size_kb = path.stat().st_size // 1024
        print(f"last={stamp}  {agent:<11} {size_kb:>6} KB  {path}")
    if not found:
        print(f"no native transcripts for {root} in the last {args.days} days")
    print("hermes: inspect profile session stores with Hermes' own session tooling", file=sys.stderr)
    return 0


NOISE_PREFIXES = (
    "<system-reminder>",
    "<command-",
    "<local-command",
    "# AGENTS.md instructions",
    "<environment_context>",
    "<permissions",
    "<user_instructions>",
    "Caveat:",
)


def text_blocks(content: object, wanted: set[str]) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = [
            block.get("text", "")
            for block in content
            if isinstance(block, dict) and block.get("type") in wanted
        ]
        return "\n".join(part for part in parts if part)
    return ""


def digest_records(path: Path) -> list[tuple[str, str, str]]:
    turns: list[tuple[str, str, str]] = []
    with path.open(encoding="utf-8", errors="replace") as handle:
        for line in handle:
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            stamp = (record.get("timestamp") or "")[:19]
            kind = record.get("type")
            if kind in ("user", "assistant") and not record.get("isSidechain"):
                message = record.get("message") or {}
                text = text_blocks(message.get("content"), {"text"})
                turns.append((stamp, kind, text))
            elif kind == "response_item":
                payload = record.get("payload") or {}
                role = payload.get("role")
                if payload.get("type") == "message" and role in ("user", "assistant"):
                    text = text_blocks(payload.get("content"), {"input_text", "output_text", "text"})
                    turns.append((stamp, role, text))
    return [
        (stamp, role, text.strip())
        for stamp, role, text in turns
        if text.strip() and not text.lstrip().startswith(NOISE_PREFIXES)
    ]


def cmd_digest(args: argparse.Namespace) -> int:
    path = Path(args.transcript).expanduser()
    turns = digest_records(path)
    selected = turns[-args.turns :] if args.turns else turns
    print(f"# digest of {path.name}: showing {len(selected)} of {len(turns)} text turns\n")
    for stamp, role, text in selected:
        if len(text) > args.chars:
            text = text[: args.chars] + f" …[+{len(text) - args.chars} chars]"
        print(f"[{stamp}] {role.upper()}:\n{text}\n")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    new = sub.add_parser("new", help="create a snapshot skeleton")
    new.add_argument("topic")
    new.add_argument("--cwd", default=os.getcwd())
    new.add_argument("--workstream")
    new.add_argument("--agent")
    new.add_argument("--session-id")
    new.add_argument("--status", choices=STATUSES, default="in-progress")
    new.add_argument("--recovered-from")
    new.set_defaults(func=cmd_new)

    status = sub.add_parser("status", help="latest snapshot per topic")
    status.add_argument("--cwd", default=os.getcwd())
    status.add_argument("--workstream")
    status.add_argument("--all", action="store_true", help="every workstream")
    status.add_argument("--include-done", action="store_true")
    status.set_defaults(func=cmd_status)

    hook = sub.add_parser("hook", help="Claude Code SessionStart hook (reads hook JSON on stdin)")
    hook.set_defaults(func=cmd_hook)

    transcripts = sub.add_parser("transcripts", help="native transcripts for a repository")
    transcripts.add_argument("--cwd", default=os.getcwd())
    transcripts.add_argument("--days", type=int, default=30)
    transcripts.add_argument("--limit", type=int, default=10)
    transcripts.set_defaults(func=cmd_transcripts)

    digest = sub.add_parser("digest", help="compact digest of a native transcript")
    digest.add_argument("transcript")
    digest.add_argument("--turns", type=int, default=40, help="last N text turns; 0 = all")
    digest.add_argument("--chars", type=int, default=1500, help="truncate each turn")
    digest.set_defaults(func=cmd_digest)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
