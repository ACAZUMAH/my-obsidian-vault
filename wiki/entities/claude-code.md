---
type: entity
status: active
created: 2026-09-29
updated: 2026-09-29
tags: [claude-code, agent, tooling, memory]
sources:
  - ../sources/claude-code-shared-brain-integration.md
aliases: [Claude Code CLI, Claude Code Desktop]
---

# Claude Code

## Summary

Claude Code is Anthropic's coding agent, connected to the same Obsidian second brain as every Hermes profile and Codex. Its global instructions provide compact shared context, repository `CLAUDE.md` or `AGENTS.md` files retain project-specific authority, and the vault's project-local skills supply its Obsidian and LLM-wiki procedures.

## Known Facts

- Global instructions live at `/Users/acazumah/.claude/CLAUDE.md`.
- `/Users/acazumah/.claude/settings.json` exposes `OBSIDIAN_VAULT_PATH=/Users/acazumah/Documents/Work Space`.
- `~/.claude/skills/` symlinks the nine vault skills from `<vault>/.agents/skills/`; the vault copy is authoritative.
- Claude Code also keeps a per-repository auto-memory under `~/.claude/projects/<encoded-path>/memory/`. That store is session-adjacent context, not vault integration; durable knowledge still requires promotion into the vault.
- Current repositories and live system state remain authoritative for changeable facts.

## Related

- [[codex|Codex]]
- [[hermes-agent|Hermes Agent]]
- [[obsidian|Obsidian]]
- [[../concepts/hermes-obsidian-memory-architecture|Hermes–Codex–Obsidian Shared Brain Architecture]]
- [[../syntheses/personal-operating-manual|Personal Operating Manual]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]

## Supporting Sources

- [[../sources/claude-code-shared-brain-integration|Claude Code Shared Brain Integration]]

## Open Questions

- Whether Claude Code per-repository auto-memory should be periodically reconciled into the vault.
