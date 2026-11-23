---
type: source
status: active
created: 2026-11-23
updated: 2026-11-23
tags: [shared-brain, session-continuity, handoff, multi-agent, account-switching]
sources:
  - ../../raw/sources/2026-11-23-agent-context-handoffs-directive.md
  - ../../raw/sources/2026-11-23-agent-context-session-start-hook.md
source_date: 2026-11-23
ingested: 2026-11-23
confidence: high
---

# Agent Context Handoffs Directive

## Source

- Raw file: [Directive: save agent contexts so work continues across accounts](../../raw/sources/2026-11-23-agent-context-handoffs-directive.md)
- Raw file: [Decision: SessionStart hook for open handoffs](../../raw/sources/2026-11-23-agent-context-session-start-hook.md)
- Date: 2026-11-23
- Author: The user (verbatim message) plus the same-session implementation record
- Ingested: 2026-11-23

## Core Claims

- The user switches agent accounts often, and carrying context across accounts has become difficult. Agents must save their working context so the agent in the next account can continue.
- Handoffs live in `raw/agent-contexts/` as curated, append-only snapshots (`<workstream>/<UTC-stamp>--<topic>.md`). The newest snapshot per topic is the current state.
- Snapshots are local-only. Everything except the folder README is gitignored because the vault repository is public.
- The `agent-context` skill owns save, resume, and recover. Recover rebuilds state from native Claude Code or Codex transcripts when a session ended before saving.
- In Claude Code, a SessionStart hook surfaces open handoffs automatically, so resuming does not depend on the agent remembering to check.

## Useful Details

- Each snapshot records: Objective, Authorization State, Current State, Decisions And Constraints, Failed Approaches And Gotchas, Next Steps, References. Authorization State carries the user's approvals forward so the next agent does not overstep.
- Native transcripts survive account switches on the same machine. Their file mtimes proved unreliable, so recovery orders transcripts by the last record's timestamp.
- Codex compaction records are encrypted, so context from before a Codex compaction may be unrecoverable.
- Pointers live in `~/.claude/CLAUDE.md` and `~/.codex/AGENTS.md`, since agents working in other repositories never read the vault's `AGENTS.md`. Hermes profiles were not wired in this session.
- The hook (`agent_context.py hook`, matcher `startup|resume|clear`) prints nothing when no handoff is open and exits 0 on any error. It covers only the session's start directory, and Codex and Hermes have no equivalent.

## Connections

- [[../concepts/hermes-obsidian-memory-architecture|Hermes–Codex–Obsidian Shared Brain Architecture]] (Session Handoff Layer).
- [[../syntheses/personal-operating-manual|Personal Operating Manual]] (Knowledge And Memory).
- [[claude-code-shared-brain-integration|Claude Code Shared Brain Integration]] covers the skill-symlink mechanism this reuses.

## Contradictions Or Tensions

- The vault previously excluded temporary task progress outright. This directive creates one bounded exception: local-only handoff snapshots in `raw/agent-contexts/`. They are operational state, not ingest evidence, and need no Source Record.
- Raw files are normally immutable evidence. Handoffs keep that property by being append-only, but they are agent-written summaries rather than primary evidence.

## Open Questions

- Should Hermes profile memories also point to the `agent-context` skill?
- When should old snapshots be pruned?
