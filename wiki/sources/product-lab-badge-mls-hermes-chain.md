---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, livelycura, pharmacy, mls, stock, bundles, bom, returns]
sources:
  - ../../raw/sources/2026-07-21-product-lab-mls-hermes-chain.txt
confidence: high
---

# Product Lab Badge And MLS Hermes Chain

## Source

- Raw file: `../../raw/sources/2026-07-21-product-lab-mls-hermes-chain.txt`
- Date: 2026-07-21
- Author: Hermes audit synthesis
- Ingested: 2026-07-21

## Core Claims

Five substantive records cover two topical lineages. The first completes the previously unanswered Product lab-test badge request. The four-record “MLS Refresh Button Fix” chain repairs refresh behavior, then pivots into stock/non-stock sales, BOM-backed bundles, UOM-aware component relief, and returns. Later stock/sales supplements remain authoritative for the final movement-ledger implementation.

## Useful Details

### Classified Records

- `20260624_123800_8292b3` — substantive Product badge, canonical field, stale-counter-index, and transaction-diagnosis record.
- `20260624_150414_7af362` — substantive MLS refresh/build repair and stock-behavior planning root.
- `20260625_122343_c6ac8f` — substantive stock/non-stock implementation and superseded embedded-bundle design.
- `20260626_114510_a5cc1c` — substantive BOM refactor with a superseded stored-purpose design.
- `20260626_140332_cf7d64` — substantive derived-purpose, bundle-relief, UOM-conversion, and return continuation.

All five are evidence-bearing. Continuation replay and copied correction rows were de-duplicated.

## Product Lab Badge

- `20260624_123800_8292b3` is a topical, not database, successor to `20260624_105536_89348f`.
- The accepted relationship is canonical `testDefinitionId`; proposed compatibility fields and fallback resolver behavior were reverted.
- POS retains a Lab test badge when that field exists.
- The historical Products table gained a Lab test/normal Type column, but current code replaced it with Stock Behavior.
- Browser acceptance was not captured.

## MLS Refresh

- Refresh controls wrap `onRefresh()` so React click events are not passed as Apollo variables.
- Test Definitions and Test Requests retain this handler and accessibility labels.
- Historical focused refresh tests passed; the focused test file is absent from current source.

## Stock, Bundles, And Returns

- Stock/non-stock behavior is item-driven: non-stock/service revenue creates no phantom inventory or COGS.
- Sale-item inventory may be nullable while product identity remains stable.
- Product-owned embedded bundle components were rejected in favor of BOM ownership.
- Stored BOM purpose was rejected. Display purpose derives from the linked product’s current bundle/manufacturable flags.
- Bundle sales must relieve BOM components with UOM conversion; returns must reverse the exact sold-line component quantities.
- Historical `inventoryReliefItems` snapshots were superseded by the later movement-ledger architecture using source-item identity and proportional reversal.

## Historical Verification

Across the five records, reported evidence included backend builds, focused unit/integration suites, frontend lint/type-check/build, refresh tests, and bundle sale/return tests. The larger historical sale-return suite timed out in the last record, and browser acceptance remained incomplete.

## Contradictions Or Tensions

- Products still query `testDefinitionId`, but the table no longer shows the requested Type column.
- `createBillOfMaterial.ts` appears to assert manufacturability before checking “manufacturable or bundle,” potentially blocking a pure bundle (`isBundle: true`, `manufacturable: false`) from receiving a BOM.
- Current movement-ledger return behavior supersedes the historical embedded relief snapshot.

## Connections

- [[portfolio-carousel-skills-livelycura-hermes-supplement|Portfolio Carousel, Skills, And LivelyCura Hermes Supplement]]
- [[ride-ordering-livelycura-hermes-chain|Ride Ordering And LivelyCura Hermes Chain]]
- [[../projects/livelycura-backend|LivelyCura Backend]]
- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]]

## Evidence

- `../../raw/sources/2026-07-21-product-lab-mls-hermes-chain.txt`

## Open Questions

- Does focused execution confirm the apparent pure-bundle BOM creation guard bug?
- Should the Product table restore an explicit Lab test/normal indicator alongside Stock Behavior?
- Where should durable regression coverage for MLS refresh handlers live now that the historical focused test is absent?
