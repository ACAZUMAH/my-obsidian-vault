---
type: source
status: active
created: 2026-11-23
updated: 2026-11-23
tags: [shared-brain, vault-operations, publishing, capture, multi-agent]
sources:
  - ../../raw/sources/2026-11-23-vault-capture-first-auto-publish-directive.md
source_date: 2026-11-23
ingested: 2026-11-23
confidence: high
---

# Vault Capture-First Auto-Publish Directive

## Source

- Raw file: [Directive: capture to the vault first and push every vault change right away](../../raw/sources/2026-11-23-vault-capture-first-auto-publish-directive.md)
- Date: 2026-11-23
- Author: The user (verbatim message) plus the same-session implementation record
- Ingested: 2026-11-23

## Core Claims

- Agents add vault-worthy knowledge immediately and tell the user afterward. They do not ask permission first.
- Every vault change is pushed right away, in the same turn it is made.
- The push goes through `python3 scripts/wiki_tool.py publish -m "<message>" -- <paths>`. It commits only the named files and is gated by a secret scan and by canonical validation of the exact committed tree.
- Destructive or evidence-altering changes still need approval: deleting, merging, renaming, or moving pages, changing raw evidence, and discarding one side of a contradiction.

## Useful Details

- The publish unit is one coherent change, not each file write, so no pushed commit leaves the vault half-updated.
- The private-index design matters because several agents share one working tree. `git add -A` would publish other agents' unfinished work.
- Named shared files (`index.md`, `log.md`, manuals) are committed whole, including concurrent lines already in them. If those lines break validation, the publish blocks rather than pushing a broken tree.
- If the push fails on the network, the commit stays local and the next publish pushes it. A diverged remote goes to the user and is never force-pushed.
- Secret scanning reduces leaks but does not prove absence. The rule against writing secrets or private identifiers into the vault is unchanged.

## Connections

- [[../syntheses/personal-operating-manual|Personal Operating Manual]] (Knowledge And Memory).
- [[agent-context-handoffs-directive|Agent Context Handoffs Directive]]: handoff snapshots remain local-only and are never published.
- [[../concepts/hermes-obsidian-memory-architecture|Hermes–Codex–Obsidian Shared Brain Architecture]]: one vault shared by all agents, which is why publishing is path-scoped.

## Contradictions Or Tensions

- Supersedes "never commit or push the vault unless asked" (global Claude instructions), "push only when explicitly requested" (workflow guide, lint checklist, ingest skill), "ask whether to file" (Query Workflow), and "apply only approved fixes" (Lint Workflow, now limited to destructive repairs).
- The repository is public, so auto-publishing removes the human review step before content becomes public. The gates are the mitigation, and they are not proof.

## Open Questions

- Should the uncommitted backlog left by earlier sessions be published in one pass?
- Should a Claude Code hook enforce publishing as a backstop when an agent forgets?
