# Welcome to My Obsidian Vault

This repository contains a persistent, LLM-maintained second brain shared by Obsidian, Hermes Agent profiles, and Codex.

> [!WARNING]
> This GitHub repository is public. Never commit credentials, tokens, passwords, private keys, connection strings, private exports, or sensitive identifiers. Use `[REDACTED]` when provenance requires acknowledging that sensitive material existed.

## Start Here

- [[index|LLM Wiki Index]] — content-oriented map of the entire vault.
- [[AGENTS|Vault Operating Schema]] — rules for ingesting, linking, maintaining, and validating knowledge.
- [[wiki/syntheses/personal-operating-manual|Personal Operating Manual]] — durable communication and working preferences.
- [[wiki/syntheses/software-development-operating-manual|Software Development Operating Manual]] — development conventions and project map.
- [[wiki/syntheses/new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]] — the pre-feature foundation for backend, web, and mobile projects.
- [[wiki/syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]] — resumable repository and conversation-ingestion checkpoint.

## How The Vault Fits Together

```text
raw/sources/ ──▶ wiki/sources/ ──▶ wiki knowledge ──▶ index.md
immutable         Source Records     maintained         navigation
evidence          (concise links)    synthesis
                                         ▲
_template/ ───────────────────────────────┘  page scaffolds

schema/              machine-readable paths and page contracts
.agents/skills/      repository-local capabilities for compatible agents
scripts/             canonical validation and automation
```

`log.md` is the append-only history of durable vault operations. Raw evidence remains immutable; Source Records provide concise provenance and retrieval without copying the full evidence. `AGENTS.md` defines the human-readable operating contract; `schema/` provides its machine-readable structural subset.

## Agent Workflow

Agents should:

1. Read `AGENTS.md` and `index.md` before changing the vault.
2. Search existing notes before creating new pages.
3. Retrieve the smallest relevant set of synthesis and project pages.
4. Treat live repositories as current implementation evidence and conversations as intent, correction, and rationale evidence.
5. Promote only durable knowledge; keep temporary task state in sessions.
6. Reread shared notes immediately before focused edits because multiple agents may work simultaneously.
7. Update `index.md` and append exactly one `log.md` entry for durable wiki operations.
8. Run `python3 scripts/validate_vault.py` after durable structural changes.
9. Validate provenance, secret hygiene, and the exact Git diff before committing.

## Core Repository Infrastructure

- `_template/` contains source, concept, entity, project, question, and synthesis scaffolds. Obsidian's core Templates plugin is configured to use this folder.
- `schema/` defines canonical paths, frontmatter, page types, statuses, and required sections for automation.
- `.agents/skills/` contains five upstream Obsidian skills plus the repository-owned ingest, query, lint, and `vault-maintenance` procedures.
- `scripts/validate_vault.py` is the canonical structural validator and uses only the Python standard library. It enforces complete raw-evidence coverage and Source Record index connections.

## Repository Safety

The root `.gitignore` intentionally excludes:

- Obsidian workspace state and installed plugin payloads.
- OS metadata and editor temporary files.
- Environment files, credentials, certificates, keys, local databases, and archives.
- Dependency, build, coverage, cache, and log output.
- Tool-local Hermes, Codex, and Claude state.

A `.gitignore` is not a secret scanner. Always inspect the staged file list and staged diff before pushing.

## Canonical Location

Local vault:

```text
/Users/acazumah/Documents/Work Space
```

GitHub:

```text
https://github.com/ACAZUMAH/my-obsidian-vault
```
