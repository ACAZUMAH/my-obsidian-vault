---
type: source
status: active
created: 2026-09-29
updated: 2026-09-29
tags: [shared-brain, claude-code, agent-skills, obsidian-cli]
sources:
  - ../../raw/sources/2026-09-29-claude-code-shared-brain-integration.md
source_date: 2026-09-29
ingested: 2026-09-29
confidence: high
---

# Claude Code Shared Brain Integration

## Source

- Raw file: [2026-09-29-claude-code-shared-brain-integration.md](../../raw/sources/2026-09-29-claude-code-shared-brain-integration.md)
- Date: 2026-09-29
- Author: User directive; integration performed by Claude Code
- Ingested: 2026-09-29

## Core Claims

- Claude Code joins Hermes profiles and Codex as a consumer of the one canonical vault.
- Its global instruction layer is `~/.claude/CLAUDE.md`, which carries a compact pointer and shared operating expectations rather than a long-form copy.
- The vault's project-local skills are the single source for Claude Code's Obsidian and LLM-wiki skills.

## Useful Details

- Skills are exposed through symlinks `~/.claude/skills/<name>` → `<vault>/.agents/skills/<name>`. Skill updates belong in the vault; the direction preserves vault portability.
- `OBSIDIAN_VAULT_PATH` is set in `~/.claude/settings.json`, matching the Codex environment.
- The Obsidian CLI needs the app running and `vault="Work Space"` as its first parameter when invoked outside the vault directory.

## Connections

- [[../concepts/hermes-obsidian-memory-architecture|Hermes–Codex–Obsidian Shared Brain Architecture]]
- [[../entities/claude-code|Claude Code]]
- [[../entities/codex|Codex]]
- [[shared-brain-all-agents-directive|Shared Brain Across Hermes Profiles And Codex]]
- [Project-Local Agent Skills](../../schema/local-skills.md)

## Contradictions Or Tensions

- The vault-maintenance pitfall forbids symlinks from the vault to profile-local skill folders. This integration uses the opposite direction, so it does not conflict, but Claude Code sessions depend on the vault path remaining stable.

## Open Questions

- Whether Claude Code session transcripts should enter the harvest checkpoint process alongside Hermes sessions.
