---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, audit, locator-correction, compflow, memory]
sources:
  - ../../raw/sources/2026-07-21-invalid-backend-auth-locators-audit.txt
  - ../../raw/sources/2026-07-21-invalid-workspace-memory-locators-audit.txt
confidence: high
---

# Invalid Hermes Locator Correction — Backend Auth And Workspace Memory

## Source

- Raw files: `../../raw/sources/2026-07-21-invalid-backend-auth-locators-audit.txt`, `../../raw/sources/2026-07-21-invalid-workspace-memory-locators-audit.txt`
- Date: 2026-07-21
- Author: Hermes audit synthesis
- Ingested: 2026-07-21

## Core Claims

Seven selector-supplied IDs are invalid. Direct read-only verification found zero session rows and zero message rows in both the coder and default live stores. They are not shells, do not belong to the frozen 130-record denominator, contribute +0 coverage, and own no project or memory claim.

## Useful Details

### Invalid IDs

- `20260713_201517_37251f`
- `20260714_130217_33cce1`
- `20260714_221929_58010f`
- `20260715_170835_50bb8f`
- `20260715_223341_f7fb60`
- `20260719_175837_1ec339`
- `20260719_180345_da029a`

No parent, child, replay boundary, request, correction, implementation, verification, commit, successor, or title may be attributed to these locators.

### Correct Backend Authentication Lineage

The real CompFlow chain is:

- Root already classified: `20260711_165753_68ff6f`.
- Pending continuations: `20260711_221940_e79205`, `20260712_021621_84e0f7`, `20260712_031059_c7fd2c`, `20260712_102048_b1481f`, and `20260712_155404_4a08ff`.

No live coder record title matches “Hermes Workspace Memory Setup.” Existing canonical-vault/bootstrap ownership remains attributed to the verified July 20–21 chain, not these invalid IDs.

## Connections

- [[compflow-checkcity-hermes-conversation-harvest-supplement-1|CompFlow And CheckCity Hermes Conversation Harvest — Supplement 1]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]
- [[../concepts/hermes-obsidian-memory-architecture|Hermes–Codex–Obsidian Shared Brain Architecture]]

## Contradictions Or Tensions

- The earlier selector surfaced timestamp-shaped IDs that do not exist in its claimed source stores; title-shaped metadata must not substitute for verified database locators.
- `#2` or chain-like naming is not evidence of `parent_session_id` lineage.
- Nearby valid sessions cannot be substituted silently; corrected targets must be recorded explicitly.

## Open Questions

- What defect in the earlier pending-record selector produced nonexistent IDs?
- Are there any valid memory-setup records under different titles, or was that candidate entirely spurious?
