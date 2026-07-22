---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, lets-ride, livelycura, backend, stock, accounting, migrations]
sources:
  - ../../raw/sources/2026-07-21-ride-ordering-livelycura-hermes-chain-audit.md
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
---

# Ride Ordering And LivelyCura Hermes Chain

## Source

- Raw report: [2026-07-21-ride-ordering-livelycura-hermes-chain-audit.md](../../raw/sources/2026-07-21-ride-ordering-livelycura-hermes-chain-audit.md)
- Exact coder-profile records: `20260628_134341_c8f843`, `20260628_230635_e39d3a`, `20260629_000111_f4ffc6`, `20260629_001748_68c46e`
- Actual projects: Let’s Ride Backend and LivelyCura Backend

## Core Claims

- Let’s Ride Backend began as a deliberately foundation-only Express/Apollo/Mongoose service under the superseded Cando name. Domain models and ride/payment/logistics business logic were explicitly excluded.
- Accepted foundation ownership uses `main.ts` for process entry, `app.ts` for startup orchestration, separate Express/GraphQL/subscription factories, central GraphQL error formatting, health surfaces, and Mongo-before-listen behavior.
- The chain later switched projects. Its LivelyCura work separated product-level commercial sale lines from batch/component-level inventory movements.
- Exact `lineCost` owns COGS; movement history owns returns, cancellation, and payment-failure stock reversal.
- Duplicate-line migrations repoint dependent references before soft deletion, then backfill exact costs and establish active uniqueness.
- Transactional Mongoose helpers require explicit document return contracts and transaction-safe creation patterns.

## Useful Details

- All four records are substantive after continuation replay de-duplication.
- Let’s Ride build/type-check passed historically, but startup stopped at MongoDB connection; HTTP, GraphQL, subscriptions, and database behavior were not successfully exercised.
- Current Let’s Ride repository contains the accepted foundation and no ride domain logic, tests, Docker/workflows, or deployment configuration.
- Current package/README still use stale Cando branding even though Let’s Ride Backend is canonical.
- LivelyCura #2 produced the accepted migration/accounting plan; #3 implemented product-line sale identity, exact COGS, returns, and rollback; #4 completed migrations, interface ownership, typing corrections, lint, and historical unit shards.
- The temporary `lineCost` fallback added for legacy fixtures is superseded; current COGS uses required exact `lineCost` directly.

## Connections

- [[../projects/lets-ride-backend|Let’s Ride Backend]]
- [[../projects/livelycura-backend|LivelyCura Backend]]
- [[livelycura-stock-sales-hermes-supplement-1|LivelyCura Stock And Sales Hermes Supplement — 1]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- Canonical Let’s Ride naming conflicts with current `cando-backend` package and README labels.
- Historical build success does not prove successful database-backed runtime; current Let’s Ride has no tests or deployment surface.
- The Ride Ordering title becomes misleading once the chain switches to LivelyCura.
- LivelyCura migrations were not run against production and historical Jest evidence is not fresh current Vitest verification.
- Static current source cannot prove deployed migration/index state.

## Open Questions

- When should Let’s Ride internal package/README branding be reconciled?
- What directly relevant future conversation authorizes ride domain implementation beyond the foundation?
- Have all deployed LivelyCura databases completed the duplicate-line and exact-cost migrations?
