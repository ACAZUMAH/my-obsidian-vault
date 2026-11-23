# Directive: capture to the vault first and push every vault change right away

- Date: 2026-11-23
- Author: the user, in a Claude Code session in the vault
- Recorded from: the user's own message (quoted verbatim) and the implementation that followed in the same session

## The user's words (verbatim)

> add a rule to the vault that anytime, there are new files written into the vault it should pushed right away, and when ever there is a something that's supposed to go to the vault the agent should add it straight away and tell me, not the other way round

## Rules it replaced

- `~/.claude/CLAUDE.md`: "Never commit or push the vault unless asked; it is a public repository."
- `schema/workflows.md` and `schema/lint-checklist.md`: push only when explicitly requested.
- `.agents/skills/llm-wiki-ingest/SKILL.md`: do not commit or push unless the user requests it.
- `AGENTS.md` Query Workflow: ask whether to file a durable answer.
- `AGENTS.md` Lint Workflow: apply only the fixes the user approves.

## Context

- The vault repository is public on GitHub. A previous user-made commit already published 274 files of harvested project knowledge, so publishing vault knowledge is established practice. What the directive removes is the review moment before each push.
- Several agents (Claude Code, Codex, Hermes profiles) write to one working tree at the same time. At the time of the directive about 150 paths were uncommitted, most of them other sessions' harvest work, and shared files such as `index.md` and `log.md` held lines from several agents.

## Implementation decisions (agent, same session)

- "Pushed right away" means within the same turn, once a coherent change is complete. Pushing after each individual file write would publish half-updated states, such as a Source Record without its `index.md` entry.
- A `publish` command (`scripts/publish_vault.py`, run through `wiki_tool.py publish`) commits exactly the named files. It builds the commit in a private Git index from `HEAD`, so other agents' uncommitted work is never swept in. It takes an exclusive lock and refuses directories, gitignored paths, and credential-looking files. It blocks on secret patterns (tokens, keys, JWTs, credentialed URLs, secret assignments, personal email addresses) and on canonical-validator failure of the exact tree being committed. It commits with compare-and-swap and pushes, and never force-pushes a diverged remote.
- Capture-first applies to adding knowledge. Deleting, merging, renaming, or moving pages, changing raw evidence, and discarding one side of a contradiction still need the user's approval, because they destroy or alter existing knowledge. Lint repairs follow the same split.
- Handoff snapshots in `raw/agent-contexts/` stay local-only.
- Hermes profile memories contained no push prohibition and defer to the vault `AGENTS.md`, so they were not changed.
