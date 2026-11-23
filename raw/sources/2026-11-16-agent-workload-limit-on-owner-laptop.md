# Agent workload limit on the owner's laptop

- Date: 2026-11-16
- Author: the user (product owner), during LivelyCura Claude Code sessions (the SERLP marketing site redesign and a parallel multi-agent build)
- Recorded from: the user's own messages (quoted verbatim) and the incidents they reacted to

## What happened

- A 9-agent SERLP site build workflow (three agents at once, each driving its own headless Chrome) plus the site's dev server filled the 16 GB laptop's memory, and macOS force-quit everything twice.
- In another session, six parallel builders each running tsc, vitest and an in-memory MongoDB force-quit the laptop three times.
- The owner works in split view on two tasks at once, so the machine is already loaded when agents run.
- After one run was then held to strictly one agent at a time (about 9 hours), the owner corrected that too.

## The user's words (verbatim)

- "continue but please I am using split view and I working on two different tasks reduce the number agent you are using, you max out the laptops ram and the laptop forces quits"
- "doesn't mean do it one agent at a time … maybe 4 agents at a time … space will still be left for me to do other things"

## What was adopted in response

- Workflows cap concurrent agents at about four (a limiter around `agent()` calls instead of unbounded fan-out).
- Heavy commands (tsc, vitest or jest, builds, codegen, in-memory MongoDB) run through a shared machine-wide limiter script, `/tmp/lc-heavy/run.sh "<label>" <command>`, with two slots and a free-memory wait; test runners use `--maxWorkers=2`.
- Headless Chrome captures run one at a time (the same script with `LC_HEAVY_SLOTS=1`), and agents reuse the already-running dev server instead of starting their own.
