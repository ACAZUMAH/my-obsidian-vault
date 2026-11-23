# Vault Script Commands

Repository-owned automation is standard-library-only. The wrapper resolves the vault from its own file location, so an absolute script path works from any current working directory. The examples below assume the vault root. Validation and audit are read-only; `publish` only commits and pushes the files it is given. No command mutates raw evidence or repairs findings automatically.

## Unified Commands

```bash
python3 scripts/wiki_tool.py validate
python3 scripts/wiki_tool.py audit
python3 scripts/wiki_tool.py check
python3 scripts/wiki_tool.py publish -m "<message>" -- <path> [<path> ...]
```

| Command | Purpose | Default exit behavior |
| --- | --- | --- |
| `validate` | Run the canonical structural validator | Nonzero on structural failure |
| `audit` | Report advisory semantic and provenance findings | Zero when the audit completes, even with findings |
| `audit --strict` | Run the same audit as a policy gate | Nonzero when any finding exists |
| `audit --json` | Emit machine-readable audit output | Same as non-strict audit |
| `check` | Run validation, then the advisory audit | Nonzero only when validation or execution fails |
| `check --strict-audit` | Run both stages as a strict gate | Nonzero when validation fails or the audit finds anything |
| `publish` | Commit and push exactly the named files behind secret-scan and validation gates | 0 pushed or no-op; 1 usage or Git error; 2 blocked by a gate; 3 committed locally but not pushed |

`wiki_tool.py` delegates to the authoritative scripts rather than reimplementing their checks. Use `python3 scripts/wiki_tool.py --help` for the live interface.

## Canonical Structural Validation

`validate_vault.py` checks:

- Required directories, registered automation files, and template files from `schema/vault-structure.json`.
- Registered schema documents and their direct `index.md` connections.
- Obsidian core Templates configuration.
- Project-local Agent Skills and their linked support files.
- Wiki frontmatter keys, types, statuses, and required sections.
- Source Record raw-evidence coverage, raw-link existence, aggregation policy, and `index.md` connections.
- JSON syntax for tracked vault configuration.
- Stale references to the removed `wiki/templates/` path.
- Real Obsidian wikilinks while ignoring fenced and inline code examples.

A zero exit code is the canonical structural result. It does not prove semantic correctness or the absence of secrets.

## Advisory Audit

`audit_vault.py` reports evidence-backed issues separately from structural validation:

- Empty or mismatched machine-readable Source Record provenance.
- `index.md` updated-date drift.
- Orphan wiki pages and duplicate H1 ownership.
- Unreferenced Markdown files under `raw/assets/` that need classification.

The audit always prints `AUDIT_MODE=READ_ONLY`. Findings are advisory unless `--strict` or `check --strict-audit` is explicitly selected.

## Gated Publishing

`publish_vault.py` implements the vault's Capture And Publish rule (see [AGENTS.md](../AGENTS.md)). Several agents edit this public repository at once in one working tree, so it never stages "everything dirty":

1. It takes an exclusive lock, so parallel publishes run one at a time.
2. It builds the commit in a private Git index from `HEAD` plus only the named paths, then syncs just those paths in the shared index. Other agents' staged or unstaged work is untouched. A named shared file is committed whole, including any concurrent lines it already holds.
3. It refuses directories, paths outside the vault, gitignored paths (`raw/agent-contexts/`), and credential-looking files.
4. It scans added lines for private keys, cloud and SaaS tokens, JWTs, credentialed URLs, secret assignments, and personal email addresses. Automated no-reply and example addresses are allowed. Findings print redacted and block with `PUBLISH=BLOCKED stage=secret-scan`.
5. It runs the canonical validator on a checkout of the exact tree being committed. A failure blocks with `PUBLISH=BLOCKED stage=validation`.
6. It commits with compare-and-swap on the branch ref and pushes to the upstream. A network failure leaves the commit local for the next publish to push; a diverged remote prints `push=diverged` and is never force-pushed.

Options: `--dry-run` runs the gates without committing; `--no-push` commits without pushing; `-m` may repeat for extra paragraphs such as trailers. Pattern scanning reduces leaks but cannot prove that secrets are absent.

## Optional Git Hook

The tracked hook runs the non-strict combined check before a commit. It is inactive until explicitly enabled:

```bash
git config core.hooksPath .githooks
```

Disable it without deleting the tracked hook:

```bash
git config --unset core.hooksPath
```

The hook blocks structural failures but prints semantic findings without blocking the commit. Use the canonical [Vault Lint Checklist](../schema/lint-checklist.md) for secret scanning, semantic judgment, exact diff review, and commit-scope checks that automation cannot prove.
