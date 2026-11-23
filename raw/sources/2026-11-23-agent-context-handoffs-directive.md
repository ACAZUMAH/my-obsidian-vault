# Directive: save agent contexts so work continues across accounts

- Date: 2026-11-23
- Author: the user, in a Claude Code session in the vault
- Recorded from: the user's own message (quoted verbatim) and the implementation that followed in the same session

## The user's words (verbatim)

> I have added a folder in the raw folder called agent-contexts, I want us to save all the contexts of the agents, because these days I switch accounts a lot and carrying the context across has become difficult so saving them and when I log into a different account the agent can continue from there

## Context

- The user created `raw/agent-contexts/` (empty) before the request.
- The vault repository is public on GitHub, and `.gitignore` already excluded `.hermes/`, `.codex/`, and `.claude/` as agent-local state.
- Native transcripts persist on disk regardless of the signed-in account: Claude Code at `~/.claude/projects/<encoded-cwd>/*.jsonl`, Codex at `~/.codex/sessions/YYYY/MM/DD/*.jsonl` (with `cwd` in the `session_meta` record). Codex compaction records are encrypted.
- Transcript file mtimes on this machine were rewritten in bulk (every Claude Code transcript showed the same `00:55` time), so the last record's own timestamp is the reliable activity time.

## Implementation decisions (agent, same session)

- Snapshots are curated handoffs, not copied transcripts. The native transcripts already exist locally; copies would be huge, full of tool noise, and more likely to carry secrets. A snapshot records the objective, authorization state, current state, decisions, failed approaches, next steps, and references.
- The layout is `raw/agent-contexts/<workstream>/<UTC-stamp>--<topic>.md`, append-only, so raw-layer immutability holds; the newest file per topic is the current state.
- Everything except `raw/agent-contexts/README.md` is gitignored because snapshots can hold client project state and the repository is public.
- An `agent-context` skill in `.agents/skills/` with a standard-library helper script (`new`, `status`, `transcripts`, `digest`) implements save, resume, and recover. Recover rebuilds state from native transcripts when a session died before it could save.
- `~/.claude/CLAUDE.md` and `~/.codex/AGENTS.md` gained a Session Handoffs section, because agents working in other repositories never read the vault's `AGENTS.md`. Hermes profile memories were not changed in this session.
