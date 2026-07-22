---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, process-control, standalone, provenance, correction, collision]
sources:
  - ../../raw/sources/2026-07-21-standalone-scope-correction-ownership-chain.txt
confidence: high
---

# Standalone Scope Correction Ownership Chain

## Source

- Raw file: `../../raw/sources/2026-07-21-standalone-scope-correction-ownership-chain.txt`
- Date: 2026-07-21
- Author: Hermes audit synthesis
- Ingested: 2026-07-21

## Core Claims

Three default-profile records separate unsupported repository-derived integration, explicit archive-scope correction, corrective writes/deletions, and final validation closure. One exact ID collides with a different populated coder-profile conversation already classified, so the frozen exact-ID ledger advances by two rather than three.

## Useful Details

### `20260721_155121_9e9cc3`

- Process-control record owning unsupported Standalone raw/source/project/manual/checkpoint/index/log writes derived from repository inspection despite zero direct conversation records.
- Owns the later user correction requiring evidence from the explicitly requested archive, but ends before implementing that correction.
- Historical validation eventually passed at 62 pages and 486 links; this validated file/schema shape, not provenance correctness.

### `20260721_162605_759657`

- Process-control continuation owning corrective raw/source writes, provenance rules, renames/placeholders, unsupported-rule removal, false 30-root completion removal, and five explicitly approved deletions.
- The first deletion was blocked before confirmation. The user approved the exact deletion set in this record; the retry succeeded.
- Ends before the correction log and post-edit canonical validation.

### Default `20260721_164555_84be3a`

- Replay-heavy human-intent shell owning only cleanup-log patches, focused residual checks, final validation, `git diff --check`, and synthesis.
- Historical final validation passed at 59 pages and 481 links with six templates/index links.
- Owns no earlier correction write or deletion.

### Same-ID Collision

A different coder-store conversation shares `20260721_164555_84be3a`:

- Coder body: 137 messages, no parent, title `Approved Wiki Project Cleanup`, archive-coverage process record already classified.
- Default body: 103 messages, parent `20260721_162605_759657`, cleanup-closure record audited here.

These are materially different conversations, not aliases. The frozen 130 denominator remains exact-ID-based, so the default body adds detail to a store-qualified composite but does not increment the exact-ID count again.

## Connections

- [[hermes-conversation-harvest-scope-correction|Hermes Conversation Harvest Scope Correction]]
- [[standalone-projects-project-knowledge-harvest-batch-1|Standalone Projects Knowledge Harvest — Batch 1]]
- [[hermes-no-cwd-process-triage-batch-1|Hermes No-CWD Process Triage — Batch 1]]
- [[portfolio-batch1-integration-standalone-reconnaissance|Portfolio Batch 1 Integration And Standalone Reconnaissance]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- Passing schema/link validation did not make repository-only project claims valid conversation-harvest knowledge.
- Let’s Ride was initially reduced to a provenance placeholder but later direct Hermes evidence supports its current active foundation page; only the naming correction remains current from this chain.
- The frozen exact-ID denominator collapses one materially different cross-store collision. It remains frozen for continuity but is not a physically faithful conversation count.
- Original raw manifests and log entries preserve superseded claims intentionally and must not be treated as current guidance.
- No target record owns schema v2, templates, or validator infrastructure.

## Open Questions

- Should a future coverage model use store-qualified composite IDs and recalculate the denominator?
- What validator or manifest check should detect populated same-ID cross-store collisions automatically?
- Should the immutable raw correction add an external annotation index for later supersession without modifying raw evidence?
