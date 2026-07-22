---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, livelycura, sales, returns, migrations, accounting, react-native]
sources:
  - ../../raw/sources/2026-07-21-livelycura-stock-sales-hermes-continuation-audit.md
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
---

# LivelyCura Stock And Sales Hermes Supplement — 2

## Source

- Raw report: [2026-07-21-livelycura-stock-sales-hermes-continuation-audit.md](../../raw/sources/2026-07-21-livelycura-stock-sales-hermes-continuation-audit.md)
- Exact Hermes continuation: `20260629_193407_346702`
- Parent: `20260629_173939_b6748a`
- Target repositories: LivelyCura Backend, SERLP Mobile, and LivelyCura Pharmacy Portal

## Core Claims

- Required exact `lineCost` must propagate through accounting contracts, services, fixtures, and zero-cost cases. Do not retain deprecated `unitCost × quantity` fallbacks after migration.
- When a financial line changes identity, migrate persistence fields, indexes, services, GraphQL contracts, clients, and presentation together. Detect conflicting active financial rows before establishing replacement uniqueness and never merge them silently.
- Sale-return identity is product-line based through `{saleReturnId, saleItemId}`. Obsolete inventory identity and one-batch/expiry presentation are misleading because restoration may span multiple inventory movements.
- Optional native modules must not be statically imported on startup when they may be absent. Follow the family reference pattern: production-only/non-web gate, dynamic import inside the effect, injected checker module, and soft failure.
- Static/type checks do not prove native runtime behavior; rebuild and exercise the relevant client.

## Useful Details

- The child’s independent evidence begins after replay of the parent through message `7861`.
- Current backend source retains migration tests, required exact `lineCost`, model-collection migrations, and the sale-return inventory-removal migration/index cleanup.
- Current Pharmacy Portal submits `saleItemId + quantity` and no longer queries or displays one arbitrary return inventory batch.
- Current SERLP Mobile retains the accepted dynamic update-module pattern; the rejected custom lazy-loader is superseded.
- The temporary deprecated GraphQL inventory bridge was later removed and is historical only.

## Historical Verification Boundary

- The session reported eight focused suites with 39 tests, then a full historical backend run with 18 suites and 172 tests after stale fixtures were corrected.
- SERLP Mobile formatting and type checking passed, but no rebuilt-client/device launch was reported.
- Pharmacy Portal type-check and production build passed.
- Sale-return cleanup reported three focused unit suites with nine tests, backend build success, and one integration suite with 20 tests; Jest also emitted an open-handle warning.
- The record compressed before final full-suite reporting; [[livelycura-stock-sales-hermes-supplement-3|Supplement 3]] attributes the successor's unique verification and diagnostic-hardening outcomes.
- No build, test, migration, database, service, deployment, or native runtime command was run during this harvest.

## Connections

- [[../projects/livelycura-backend|LivelyCura Backend]]
- [[../projects/serlp-mobile|SERLP Mobile]]
- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- Historical tests used Jest; current repositories use Vitest conventions.
- The temporary GraphQL compatibility field is absent from current source and must not be treated as current architecture.
- The generic migration runner catches and logs migration failures. Whether a conflicting financial-identity migration should fail application startup closed remains unresolved.
- Static source cannot prove that every deployed database dropped the stale inventory index or that SERLP Mobile starts correctly on a rebuilt native client.

## Open Questions

- Should the generic migration runner fail startup closed when a financial migration rejects conflicting rows?
- Which later record owns compatibility-field removal and repository publication? Supplement 3 confirms they are not exact-session outcomes of this child.
