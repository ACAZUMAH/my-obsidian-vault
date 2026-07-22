---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, livelycura, serlp, stock, sales, migrations, accounting]
sources:
  - ../../raw/sources/2026-07-21-livelycura-stock-sales-hermes-audit.md
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
---

# LivelyCura Stock And Sales Hermes Supplement — 1

## Source

- Raw report: [2026-07-21-livelycura-stock-sales-hermes-audit.md](../../raw/sources/2026-07-21-livelycura-stock-sales-hermes-audit.md)
- Exact Hermes session: `20260629_173939_b6748a`
- Target repositories: LivelyCura Backend and SERLP Mobile

## Core Claims

- One active `SaleItem` represents one customer-facing product line per sale; inventory-batch and bundle-component relief remains movement-level.
- Returns identify the sold line through `saleItemId`, including non-stock lines without inventory records.
- `SaleItem.lineCost` is the exact sale-time COGS amount. Weighted unit cost is a summary and may round; accounting posting sums exact line costs.
- Product stock behavior uses compatible `isStockItem`, `isBundle`, `manufacturable`, `sellable`, and `purchasable` flags, with mobile forms enforcing valid combinations.
- Application-startup migrations use the runner-owned connection and imported models. They stream production-sized work, repoint dependent references before duplicate deletion, backfill before tightening required contracts, preserve idempotence, and require focused migration/reference-integrity tests.

## Useful Details

## Current Reconciliation

- Current backend source retains required `lineCost`, the active sale/product uniqueness rule, exact COGS posting, registered stock/merge/backfill/cleanup migrations, and migration integration coverage.
- Current SERLP Mobile source reads and writes the stock flags and keys return quantities/inputs by sale-item ID.
- The current duplicate merge streams groups and processes one group transactionally at a time rather than retaining the historical explicit batch-array/flush implementation.
- The merge migration imports `mongoose` only to start a transaction session; it does not open or close its own database connection.

## Historical Verification Boundary

- The session reported passing backend builds, 16 focused unit tests, 17 focused integration tests, and SERLP Mobile type/format checks before its final follow-up.
- The final request for migration tests and fully required `lineCost` contracts did not complete inside this exact ID. Current source and later history contain the follow-up, but they are not reattributed to the parent session.
- No build, test, migration, database, service, or deployment command was run during this harvest.

## Connections

- [[../projects/livelycura-backend|LivelyCura Backend]]
- [[../projects/serlp-mobile|SERLP Mobile]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- Historical cursor-plus-explicit-batch-array behavior is superseded by the current streaming per-group transactional merge.
- “No mongoose import” overstates the accepted rule. The durable constraint is runner-owned connection lifecycle, not a ban on transaction-session access.
- Direct continuation `20260629_193407_346702` is processed in [[livelycura-stock-sales-hermes-supplement-2|LivelyCura Stock And Sales Hermes Supplement — 2]]. It closes exact-cost migration tests, corrects optional native-module loading, and completes sale-return identity cleanup; successor `20260712_183956_816de0` remains pending.

## Open Questions

- What production upper bound exists for duplicate items within one sale/product group, since current code materializes one group before processing it?
- Does successor `20260712_183956_816de0` resolve final full-suite and migration-failure behavior?
