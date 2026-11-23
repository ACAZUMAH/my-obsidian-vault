# Agent Contexts

Session handoff snapshots that let Claude Code, Codex, and Hermes continue work across account switches, usage-limit cutoffs, and agent changes.

Everything in this folder except this README is gitignored and stays on this machine. Snapshots can hold client project state, so they never go into the public vault repository.

## Layout

```text
raw/agent-contexts/
  <workstream>/                          # main repository folder name, e.g. bora-capital-backend
    <YYYY-MM-DDTHHMMSSZ>--<topic>.md     # one snapshot per save (UTC), append-only
```

The newest file per topic is the current state. Earlier files are history and are never edited.

## Use

The procedure lives in the [`agent-context` skill](../../.agents/skills/agent-context/SKILL.md). Quick commands:

```bash
CTX="/Users/acazumah/Documents/Work Space/.agents/skills/agent-context/scripts/agent_context.py"
python3 "$CTX" status --all      # every open handoff
python3 "$CTX" status            # open handoffs for the current repository
python3 "$CTX" new <topic>       # start a new snapshot
python3 "$CTX" transcripts       # native transcripts to recover from
```

When switching accounts, ask the outgoing agent to "save context". In the new session, ask it to "resume". If the old session died before it could save, the new agent recovers the state from the native transcript.
