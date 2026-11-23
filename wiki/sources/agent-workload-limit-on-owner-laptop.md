---
type: source
status: active
created: 2026-11-16
updated: 2026-11-16
tags: [agents, workflows, performance, conventions, correction]
sources:
  - ../../raw/sources/2026-11-16-agent-workload-limit-on-owner-laptop.md
source_date: 2026-11-16
ingested: 2026-11-16
confidence: high
---

# Agent Workload Limit On The Owner's Laptop

## Source

- Raw file: [Agent workload limit on the owner's laptop](../../raw/sources/2026-11-16-agent-workload-limit-on-owner-laptop.md)
- Date: 2026-11-16
- Author: The user (verbatim messages)
- Ingested: 2026-11-16

## Core Claims

- Multi-agent runs on the owner's 16 GB laptop must leave room for the owner's own work: about four agents at once, never an unbounded fan-out.
- Strictly one agent at a time is also wrong; the owner wants roughly four concurrent agents with heavy work throttled.
- Heavy commands (tsc, vitest or jest, builds, codegen, in-memory MongoDB) go through a shared machine-wide two-slot limiter, test runners use `--maxWorkers=2`, and headless Chrome captures run one at a time.

## Useful Details

- The limiter is `/tmp/lc-heavy/run.sh "<label>" <command>` (two slots plus a wait for free memory); `LC_HEAVY_SLOTS=1` restricts a class of jobs, such as Chrome captures, to one at a time. It lives in `/tmp`, so it is lost on restart and must be recreated.
- Agents reuse an already-running dev server rather than starting their own, and stray headless Chrome processes are killed after captures.
- State the expected run time before a long run.

## Connections

- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]] carries the rule under Communication And Execution.
- [[../projects/serlp|SERLP]] is where the force-quits happened during the marketing site redesign.

## Contradictions Or Tensions

- Supersedes an interim rule from the same day (work inline or one agent at a time), which the owner corrected as too slow.

## Open Questions

- None.
