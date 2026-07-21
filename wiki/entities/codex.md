---
type: entity
status: active
created: 2026-07-20
updated: 2026-07-20
tags: [codex, agent, tooling, memory]
sources:
  - ../sources/shared-brain-all-agents-directive.md
  - ../sources/hermes-persistent-memory-import.md
aliases: [OpenAI Codex, Codex CLI]
---

# Codex

## Summary

Codex is a coding-agent interface connected to the same Obsidian second brain as every Hermes profile. Its global instructions provide compact shared context while repository `AGENTS.md` files retain project-specific authority.It can read, search, create, and update the Obsidian vault while retaining a compact persistent memory across conversations.

## Known Facts

- Codex global instructions live at `/Users/acazumah/.codex/AGENTS.md`.
- Codex reads global guidance once per run and then layers project-root-to-current-directory `AGENTS.md` files, with more specific guidance appearing later.
- `/Users/acazumah/.codex/config.toml` exposes `OBSIDIAN_VAULT_PATH=/Users/acazumah/Documents/Work Space` to Codex shell environments.
- Codex should retrieve relevant vault pages rather than load the entire knowledge base into every task.
- Durable user corrections, workflows, project conventions, and reusable lessons should be integrated into the vault under its schema.
- Current repositories and live system state remain authoritative for changeable facts.

## Related

- [[hermes-agent|Hermes Agent]]
- [[obsidian|Obsidian]]
- [[../concepts/hermes-obsidian-memory-architecture|Hermes–Codex–Obsidian Shared Brain Architecture]]
- [[../syntheses/personal-operating-manual|Personal Operating Manual]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]

## Supporting Sources

- [[../sources/shared-brain-all-agents-directive|Shared Brain Across Hermes Profiles And Codex]]
- [[../sources/hermes-persistent-memory-import|Hermes Persistent Memory Import]]

## Open Questions

- Whether frequently repeated Codex workflows should become shared skills or remain repository instructions.
