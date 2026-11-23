---
type: source
status: active
created: 2026-11-12
updated: 2026-11-12
tags: [preferences, git, branches, worktrees, decision]
sources:
  - ../../raw/sources/2026-11-12-no-project-copies-direction.md
source_date: 2026-11-12
ingested: 2026-11-12
confidence: high
---

# No Project Copies Direction

## Source

- Raw file: [Direction: never make a copy of a project to do work](../../raw/sources/2026-11-12-no-project-copies-direction.md)
- Date: 2026-11-12
- Author: The owner (paraphrased, with one short quote), relayed by the Claude Code session
- Ingested: 2026-11-12

## Core Claims

- Agents never create a second copy of a project folder (a git worktree) to do work, and never start side sessions that do.
- Work happens in the existing folder, on the current branch or on a branch made there.
- If a separate branch would disturb uncommitted work or a running dev server in that folder, the agent says so plainly before acting and offers in-place choices; a mention of "a second folder" inside an option's description is not consent.

## Useful Details

- It happened twice: a portal JSON-LD hotfix copy on 2026-11-11, and a backend copy for the optional cancel reason on 2026-11-12, which the owner had picked from a recommended option without reading it as "a copy of the project".
- In-place alternatives: put the change on the current branch and split it into its own commit and branch when committing, or wait until the other work is committed.

## Connections

- [[../syntheses/personal-operating-manual|Personal Operating Manual]] (Change And Remediation Work).
- [[livelycura-customer-portal-redesign-direction|LivelyCura Customer Portal Redesign Direction]] is the work during which both copies were made.

## Contradictions Or Tensions

- Some tools default to isolated worktrees for parallel work. For this owner, the existing folder wins unless they ask for a copy in their own words.

## Open Questions

- None.
