# Decision: surface open agent-context handoffs with a Claude Code SessionStart hook

- Date: 2026-11-23
- Author: the user, in the same Claude Code session that built the agent-context handoff layer
- Recorded from: the user's own message (quoted verbatim) and the implementation that followed

## The user's words (verbatim)

> Add the hook

This answered the agent's question whether to add a Claude Code startup hook that shows open handoffs automatically, raised because an instruction-only check depends on the agent remembering to run it.

## Implementation (agent, same session)

- `agent_context.py hook` reads the SessionStart JSON on stdin and maps its `cwd` to a workstream; worktrees map to the main repository. It prints a `hookSpecificOutput.additionalContext` block plus a short `systemMessage` only when open handoffs exist. Otherwise it prints nothing.
- Any error exits 0 silently, so a broken hook never blocks session start. Measured runtime: about 35 ms.
- Registered in `~/.claude/settings.json` under `hooks.SessionStart` with matcher `startup|resume|clear` and a 15-second timeout. Compaction is excluded because the running session already holds its own context.
- The hook covers only the session's start directory. Work in another repository still needs `agent_context.py status --cwd <repo>`.
- Codex and Hermes have no equivalent hook; Codex keeps the instruction-based check.
