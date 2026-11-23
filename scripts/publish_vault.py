#!/usr/bin/env python3
"""Commit and push exactly the named vault files behind secret-scan and validation gates.

The vault is a public repository that several agents edit at once in one working
tree. This command therefore never stages "everything dirty". It builds the commit
in a private index from HEAD plus only the named paths, scans the added lines for
secrets, runs the canonical validator on that exact tree, commits it with
compare-and-swap, and pushes. Other agents' uncommitted work stays untouched,
except that a named shared file (index.md, log.md, a manual) is committed whole,
including any concurrent lines it already holds.

Exit codes: 0 pushed or nothing to publish; 1 usage or git error; 2 blocked by a
gate (nothing committed); 3 committed locally but the push failed.
"""

from __future__ import annotations

import argparse
import fcntl
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK_WAIT_SECONDS = 120

REFUSED_PREFIXES = ("raw/agent-contexts/",)
REFUSED_EXCEPTIONS = {"raw/agent-contexts/README.md"}
REFUSED_NAME = re.compile(r"(^|/)\.env(\..*)?$|\.(pem|key|p12|pfx)$", re.IGNORECASE)

SECRET_PATTERNS = [
    ("private-key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("aws-access-key", re.compile(r"\b(AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("github-token", re.compile(r"\b(gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b")),
    ("slack-token", re.compile(r"\bxox[abposr]-[A-Za-z0-9-]{10,}")),
    ("anthropic-or-openai-key", re.compile(r"\bsk-(ant-)?[A-Za-z0-9_-]{20,}")),
    ("google-api-key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("stripe-key", re.compile(r"\b(sk|rk)_(live|test)_[A-Za-z0-9]{16,}")),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
    ("credentialed-url", re.compile(r"[a-z][a-z0-9+.-]*://[^/\s:@'\"`]+:[^/\s@'\"`]{3,}@", re.IGNORECASE)),
    (
        "secret-assignment",
        re.compile(
            r"(password|passwd|secret|api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret)"
            r"[\"']?\s*[:=]\s*[\"']?[A-Za-z0-9/+_\-.]{12,}",
            re.IGNORECASE,
        ),
    ),
]
EMAIL = re.compile(r"\b([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Za-z]{2,})\b")
ALLOWED_EMAIL_LOCAL = re.compile(r"^(no-?reply|do-?not-?reply)$", re.IGNORECASE)
ALLOWED_EMAIL_DOMAIN = re.compile(
    r"(^|\.)(example\.(com|org|net)|users\.noreply\.github\.com|anthropic\.com)$|\.(test|invalid|example|localhost)$",
    re.IGNORECASE,
)


class GitError(RuntimeError):
    pass


def git(*args: str, env: dict | None = None, check: bool = True, input_text: str | None = None) -> str:
    full_env = dict(os.environ, GIT_LITERAL_PATHSPECS="1", **(env or {}))
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        env=full_env,
        input=input_text,
        capture_output=True,
        text=True,
        check=False,
    )
    if check and result.returncode != 0:
        raise GitError(f"git {' '.join(args[:3])}: {result.stderr.strip() or result.stdout.strip()}")
    return result.stdout


def normalize(raw_paths: list[str]) -> list[str]:
    tracked_in_head = set(git("ls-tree", "-r", "--name-only", "HEAD").splitlines())
    resolved: list[str] = []
    for raw in raw_paths:
        candidate = Path(raw) if os.path.isabs(raw) else ROOT / raw
        try:
            relative = candidate.resolve(strict=False).relative_to(ROOT.resolve()).as_posix()
        except ValueError:
            raise GitError(f"outside the vault: {raw}") from None
        if candidate.is_dir():
            raise GitError(f"directories are not accepted; name each file: {relative}")
        if relative.startswith(".git/") or relative == ".git":
            raise GitError(f"refused: {relative}")
        if relative.startswith(REFUSED_PREFIXES) and relative not in REFUSED_EXCEPTIONS:
            raise GitError(f"refused: {relative} is local-only (agent handoff snapshots are never published)")
        if REFUSED_NAME.search(relative):
            raise GitError(f"refused: {relative} looks like a credential file")
        if not candidate.exists() and relative not in tracked_in_head:
            raise GitError(f"not found and not tracked: {relative}")
        if candidate.exists() and subprocess.run(
            ["git", "check-ignore", "-q", "--", relative], cwd=ROOT, check=False
        ).returncode == 0:
            raise GitError(f"refused: {relative} is gitignored")
        if relative not in resolved:
            resolved.append(relative)
    return resolved


def redact(value: str) -> str:
    return value if len(value) <= 8 else f"{value[:4]}…{value[-2:]}"


def scan(diff: str) -> list[str]:
    findings: list[str] = []
    current = "?"
    for line in diff.splitlines():
        if line.startswith("+++ "):
            current = line[6:] if line.startswith("+++ b/") else line[4:]
            continue
        if not line.startswith("+") or line.startswith("+++"):
            continue
        added = line[1:]
        for name, pattern in SECRET_PATTERNS:
            match = pattern.search(added)
            if match:
                findings.append(f"{current}: {name}: {redact(match.group(0))}")
        for match in EMAIL.finditer(added):
            local, domain = match.group(1), match.group(2)
            if not (ALLOWED_EMAIL_LOCAL.match(local) or ALLOWED_EMAIL_DOMAIN.search(domain)):
                findings.append(f"{current}: email-address: {redact(match.group(0))}")
    return findings


def validate_tree(index_env: dict) -> tuple[bool, str]:
    workdir = Path(tempfile.mkdtemp(prefix="vault-publish-"))
    try:
        git("checkout-index", "-a", f"--prefix={workdir}/", env=index_env)
        result = subprocess.run(
            [sys.executable, str(workdir / "scripts" / "validate_vault.py")],
            cwd=workdir,
            capture_output=True,
            text=True,
            check=False,
        )
        return result.returncode == 0, (result.stdout + result.stderr).strip()
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


def acquire_lock():
    lock_path = ROOT / git("rev-parse", "--git-path", "vault-publish.lock").strip()
    handle = open(lock_path, "w")
    deadline = time.monotonic() + LOCK_WAIT_SECONDS
    while True:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            return handle
        except BlockingIOError:
            if time.monotonic() > deadline:
                raise GitError("another publish held the lock for too long; retry") from None
            time.sleep(0.5)


def publish(paths: list[str], message: str, push: bool, dry_run: bool) -> int:
    branch = git("symbolic-ref", "--quiet", "--short", "HEAD", check=False).strip()
    if not branch:
        raise GitError("HEAD is detached; publish needs a branch")
    upstream = git("rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}", check=False).strip()
    if push and not upstream:
        raise GitError(f"branch {branch} has no upstream to push to")

    relative = normalize(paths)
    lock = acquire_lock()
    index_fd, index_path = tempfile.mkstemp(prefix="vault-publish-index-")
    os.close(index_fd)
    index_env = {"GIT_INDEX_FILE": index_path}
    try:
        parent = git("rev-parse", "HEAD").strip()
        git("read-tree", parent, env=index_env)
        git("add", "-A", "--", *relative, env=index_env)
        changed = git("diff", "--cached", "--name-status", parent, env=index_env).strip()
        if not changed:
            print("PUBLISH=NOOP reason=no-changes-in-named-paths")
            return 0
        print(changed)

        findings = scan(git("diff", "--cached", "-U0", "--no-color", "--no-ext-diff", parent, env=index_env))
        if findings:
            print("\n".join(findings))
            print("PUBLISH=BLOCKED stage=secret-scan (remove or redact the values; never bypass)")
            return 2

        ok, output = validate_tree(index_env)
        if not ok:
            print("\n".join(output.splitlines()[-25:]))
            print("PUBLISH=BLOCKED stage=validation (the exact tree being committed fails the canonical validator)")
            return 2
        if dry_run:
            print("PUBLISH=DRY-RUN gates=pass")
            return 0

        tree = git("write-tree", env=index_env).strip()
        commit = git("commit-tree", tree, "-p", parent, "-F", "-", input_text=message).strip()
        git("update-ref", "-m", f"publish: {message.splitlines()[0]}", f"refs/heads/{branch}", commit, parent)
        short = commit[:7]
        synced = subprocess.run(
            ["git", "reset", "-q", commit, "--", *relative],
            cwd=ROOT,
            env=dict(os.environ, GIT_LITERAL_PATHSPECS="1"),
            capture_output=True,
            text=True,
            check=False,
        )
        if synced.returncode != 0:
            print(f"warning: committed {short}, but the shared index was busy; run `git reset -q -- <paths>` later")
        if not push:
            print(f"PUBLISH=COMMITTED commit={short} push=skipped")
            return 0

        remote = upstream.split("/", 1)[0]
        pushed = subprocess.run(
            ["git", "push", "--quiet", remote, f"{branch}:{upstream.split('/', 1)[1]}"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if pushed.returncode != 0:
            print(pushed.stderr.strip())
            if "non-fast-forward" in pushed.stderr or "fetch first" in pushed.stderr:
                print(
                    f"PUBLISH=COMMITTED commit={short} push=diverged (the remote has commits this checkout lacks; "
                    "the user must decide how to integrate them, never force-push)"
                )
            else:
                print(f"PUBLISH=COMMITTED commit={short} push=failed (commit is local; the next publish pushes it)")
            return 3
        print(f"PUBLISH=PUSHED commit={short} branch={branch}")
        return 0
    finally:
        os.unlink(index_path)
        lock.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-m", "--message", action="append", required=True, help="commit message; repeat for paragraphs")
    parser.add_argument("--no-push", action="store_true", help="commit locally without pushing")
    parser.add_argument("--dry-run", action="store_true", help="run the gates without committing")
    parser.add_argument("paths", nargs="+", help="vault-root-relative or absolute file paths you created, edited, or deleted")
    args = parser.parse_args()
    message = "\n\n".join(part.strip() for part in args.message) + "\n"
    try:
        return publish(args.paths, message, push=not args.no_push, dry_run=args.dry_run)
    except GitError as error:
        print(f"PUBLISH=ERROR {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
