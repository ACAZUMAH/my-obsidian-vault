---
name: agent-context
description: Save, resume, and recover agent session handoffs so work continues across account switches, usage-limit cutoffs, and different agents (Claude Code, Codex, Hermes). Use when the user says save context, checkpoint, handoff, "I'm switching accounts", resume, continue where we left off, or pick up; at the start of repository work when an open handoff exists; and proactively after verified milestones in substantive work.
version: 1.0.0
author: ACAZUMAH
license: MIT
metadata:
  hermes:
    tags: [handoff, session-continuity, multi-agent, account-switching, context]
    related_skills: [vault-maintenance, llm-wiki-ingest]
---

# Agent Context Handoffs

## Overview

The user switches Claude, Codex, and Hermes accounts often, and sessions can end abruptly at usage limits. Native session stores are per agent and may be tied to the account. A handoff snapshot is the agent-neutral, account-neutral point to continue from.

Helper script (standard library only, Python 3.9+):

```bash
CTX="${OBSIDIAN_VAULT_PATH:-/Users/acazumah/Documents/Work Space}/.agents/skills/agent-context/scripts/agent_context.py"
python3 "$CTX" status            # open handoffs for the current repository
python3 "$CTX" status --all      # open handoffs everywhere
python3 "$CTX" new <topic>       # create a prefilled snapshot; prints its path
python3 "$CTX" transcripts       # native Claude/Codex transcripts for this repository
python3 "$CTX" digest <jsonl>    # compact user/assistant digest of one transcript
python3 "$CTX" hook              # Claude Code SessionStart hook (hook JSON on stdin)
```

## Storage Contract

- Path: `raw/agent-contexts/<workstream>/<YYYY-MM-DDTHHMMSSZ>--<topic>.md` (UTC).
- `workstream` is the main repository folder name, so worktrees map to the same workstream. It matches `wiki/projects/<repo>.md`. Outside a repository it is the folder name, or pass `--workstream`.
- `topic` is a kebab-case task slug. Parallel tasks in one repository get distinct topics.
- Append-only: every save is a new file created by `new`. Never edit, rename, or delete an earlier snapshot. Only the file just created in the current save may be edited.
- Self-contained: resume reads only the newest snapshot per topic, so carry forward everything from the previous one that is still true.
- Local-only: the folder is gitignored except its README. Never commit or push snapshots; the vault repository is public.
- No secrets: never copy tokens, passwords, API keys, `.env` values, credentialed connection strings, or account emails/IDs. Reference them by name and location only.
- Refer to vault pages with backticked paths, not wikilinks. The canonical validator scans these files, and a broken wikilink fails `python3 scripts/wiki_tool.py check`.

## Save

Save when:

- the user asks (save context, checkpoint, handoff, "I'm switching accounts", "I'm about to hit my limit");
- a milestone is verified, the user makes a decision or correction, or the authorization state changes;
- a long or risky operation is about to start;
- a turn ends with work in progress and the newest snapshot no longer matches reality;
- the work is complete: save a final snapshot with `--status done`.

Do not save on every turn or for trivial question-and-answer exchanges.

Steps:

1. Run `status` to find the previous snapshot for the topic.
2. Run `new <topic>`, adding `--status blocked` or `--status done` when it applies. The script fills `workstream`, `agent`, `session_id`, `saved`, `cwd`, `branch`, `head`, `dirty_files`, and `previous`.
3. Fill every section using the spec below.
4. Tell the user in one line: snapshot path and status.

Section spec (dense; aim for under ~150 lines):

- **Objective**: the user's actual ask, quoting their decisive words, plus scope boundaries.
- **Authorization State**: what the user explicitly approved (quote it), what has been proposed but not approved, and standing prohibitions (for example "do not commit or push"). A question about whether work can continue is not authorization. This section is what keeps the next agent from overstepping.
- **Current State**: done and verified (and how it was verified); done but not verified; in progress (the exact stopping point); working tree (branch, uncommitted files, running servers or processes, temporary files).
- **Decisions And Constraints**: decisions with their rationale, user corrections, and the project conventions that mattered.
- **Failed Approaches And Gotchas**: what was tried, why it failed, and the traps to avoid.
- **Next Steps**: ordered and concrete. The first step must be executable immediately. Mark the steps that need user approval.
- **References**: files with line numbers, verification commands, PR or issue URLs, vault pages as backticked paths, and the native transcript path or session ID.

## Resume

Run this at the start of repository work when `status` shows an open handoff, or when the user says continue, resume, or pick up. In Claude Code, a SessionStart hook in `~/.claude/settings.json` runs `hook` and injects open handoffs for the session's start directory automatically. For work in a different repository, run `status --cwd <repo>` yourself.

1. Run `status` (or `status --all` when the workstream is unclear). If several topics are open and the request does not pick one, ask which.
2. Read the newest snapshot in full. Read `previous` only to resolve ambiguity.
3. Verify against live state: branch, `HEAD`, and uncommitted files against the snapshot. Run `transcripts`; if a transcript shows activity after `saved`, or the repository moved, run Recover for the gap.
4. Read only the relevant sections of `wiki/projects/<workstream>.md`.
5. Report in five lines or fewer: where it stands, the next step, and pending approvals. Continue only with steps the Authorization State covers; otherwise wait for the user's instruction.

## Recover

Use this when no snapshot exists or the newest one is stale, for example when the previous account hit its limit mid-task.

1. Run `transcripts` to list the newest native transcripts for the repository, ordered by last recorded activity (file mtimes are unreliable). For Hermes, use the profile's own session tooling.
2. Run `digest <path> --turns 60` on the most relevant transcript, widening `--turns` as needed. Never load raw JSONL wholesale.
3. Cross-check against `git status`, `git log -5 --oneline`, and `git diff --stat`.
4. Save a reconstructed snapshot with `new <topic> --recovered-from <path>`. Mark anything inferred as unverified.
5. Continue as in Resume step 5.

Codex compaction records are encrypted, so context from before a Codex compaction may be unrecoverable. Say so rather than guessing.

## Relation To The Wiki

- Handoffs are operational state, not evidence for durable knowledge. Durable preferences, decisions, and lessons still go through normal vault capture (`llm-wiki-ingest`, `vault-maintenance`) in the session that produced them. A snapshot may note where something was promoted.
- Do not create Source Records for handoffs and do not list them in `index.md`.
- Keep old snapshots. Prune only when the user asks.

## Pitfalls

- Editing or overwriting an earlier snapshot instead of creating a new one.
- Copying secrets or account identifiers into a snapshot.
- Using wikilinks inside snapshots.
- Trusting the snapshot over live repository state: current code and Git state win.
- Executing next steps that the Authorization State does not cover.
