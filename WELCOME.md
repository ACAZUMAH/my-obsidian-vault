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
raw/sources/       Sanitized source evidence and provenance
        │
        ▼
wiki/sources/      Structured source summaries
        │
        ├───────────────┐
        ▼               ▼
wiki/entities/     wiki/concepts/
projects/things    reusable ideas and mechanisms
        │               │
        └───────┬───────┘
                ▼
wiki/syntheses/  operating manuals and cross-source conclusions
                │
                ▼
index.md         canonical navigation map
```

`log.md` is the append-only history of durable vault operations. `AGENTS.md` defines the schema, provenance rules, contradiction handling, and concurrent-edit protocol.

## Agent Workflow

Agents should:

1. Read `AGENTS.md` and `index.md` before changing the vault.
2. Search existing notes before creating new pages.
3. Retrieve the smallest relevant set of synthesis and project pages.
4. Treat live repositories as current implementation evidence and conversations as intent, correction, and rationale evidence.
5. Promote only durable knowledge; keep temporary task state in sessions.
6. Reread shared notes immediately before focused edits because multiple agents may work simultaneously.
7. Update `index.md` and append exactly one `log.md` entry for durable wiki operations.
8. Validate frontmatter, links, provenance, and secret hygiene before committing.

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
