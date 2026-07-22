#!/usr/bin/env python3
"""Unified command entry point for canonical vault validation and advisory audit."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def run_script(name: str, arguments: list[str] | None = None) -> int:
    command = [sys.executable, str(SCRIPTS / name), *(arguments or [])]
    return subprocess.run(command, cwd=ROOT, check=False).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("validate", help="run the canonical structural validator")

    audit = subparsers.add_parser("audit", help="run the read-only semantic/provenance audit")
    audit.add_argument("--json", action="store_true", help="emit machine-readable audit JSON")
    audit.add_argument("--strict", action="store_true", help="exit 1 when any audit finding exists")

    check = subparsers.add_parser("check", help="run canonical validation, then the advisory audit")
    check.add_argument(
        "--strict-audit",
        action="store_true",
        help="fail the combined check when the advisory audit reports any finding",
    )

    args = parser.parse_args()
    if args.command == "validate":
        return run_script("validate_vault.py")
    if args.command == "audit":
        forwarded = [flag for flag, enabled in (("--json", args.json), ("--strict", args.strict)) if enabled]
        return run_script("audit_vault.py", forwarded)

    validation = run_script("validate_vault.py")
    if validation != 0:
        print("WIKI_CHECK=FAIL stage=validation")
        return validation
    audit_arguments = ["--strict"] if args.strict_audit else []
    audit_result = run_script("audit_vault.py", audit_arguments)
    if audit_result != 0:
        print("WIKI_CHECK=FAIL stage=audit")
        return audit_result
    print("WIKI_CHECK=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
