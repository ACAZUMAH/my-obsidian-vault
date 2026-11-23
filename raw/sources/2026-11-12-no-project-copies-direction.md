# Direction: never make a copy of a project to do work

Date: 2026-11-12
Source: the owner's message in a Claude Code session on LivelyCura (paraphrased; the quoted phrase is the owner's own words, with an expletive left out), plus the session facts that led to it.

## What happened

- 2026-11-11: a proposed "hotfix" session for the customer portal created a second copy of the portal repository (a git worktree folder on its own branch). The owner found the folder, did not know where it came from, and had the fix moved into the branch they were on and the folder and branch deleted.
- 2026-11-12: for a small backend change (an optional cancel reason), the agent asked where the change should go. The recommended option, "Own branch", mentioned in its description that it would live in "a second folder next to the backend". The owner picked it, and the agent created a second copy of the backend repository as a git worktree folder. The backend's own folder had many uncommitted files of other work and a running dev server.
- The owner objected strongly: "why ... do you always have to make a copy of the project to add an update, you were already working on a different branch".

## Direction

- Never make a copy of a project folder (a git worktree) to do a piece of work, and never start side sessions that do.
- Work happens in the project's existing folder, on the current branch or a branch made there.
- When a separate branch cannot be made in the existing folder without disturbing something (uncommitted work, a running dev server), say so plainly, in its own sentence, before acting, and offer in-place choices. Mentioning a second folder inside an option's description does not count as asking.
