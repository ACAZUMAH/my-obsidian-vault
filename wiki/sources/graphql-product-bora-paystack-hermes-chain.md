---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, graphql, migrations, livelycura, bora-capital, paystack]
sources:
  - ../../raw/sources/2026-07-21-graphql-product-bora-paystack-hermes-chain-audit.md
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
---

# GraphQL Product And Bora Paystack Hermes Chain

## Source

- Raw report: [2026-07-21-graphql-product-bora-paystack-hermes-chain-audit.md](../../raw/sources/2026-07-21-graphql-product-bora-paystack-hermes-chain-audit.md)
- Exact coder-profile records: `20260627_113946_8a0b7e`, `20260627_153636_3d38e3`
- Actual repositories: LivelyCura Backend, LivelyCura Pharmacy Portal, and Bora Capital Backend

## Core Claims

- Tightened/non-null GraphQL contracts should be satisfied by repairing persisted legacy data and write normalization, not by masking invalid state with fallback field resolvers when migration is the accepted correction.
- Product stock-behavior migration covers null and missing flags; create/update paths preserve required defaults and prevent nullable input from writing those fields back to null.
- Menu registries should emit unique top-level entries and retain a regression test for duplicate labels.
- Every Bora portfolio requires a real Paystack subaccount with dedicated settlement details. Fake subaccounts or staging-only bypasses in production-shared code are unacceptable.
- A migration registry provides once-after-success semantics, not provider-level exactly-once behavior. External side effects require explicit idempotency, stable entity-to-input mapping, and partial-failure recovery.
- Technical disagreement should be stated plainly when warranted rather than hidden behind reflexive agreement.

## Useful Details

- The first record is multi-project despite its GraphQL-only title. It accepted migration/default normalization, removed duplicate Pharmacy navigation, and began Bora subaccount setup.
- The second record’s LivelyCura prefix is replay only. Its unique work adds settlement fields, one-shot setup migration registration, real provider subaccounts, and required subaccount routing.
- Historical checks reported focused LivelyCura and Pharmacy tests/type/build success, then Bora build, six focused deposit tests, and dry-run mapping.
- Actual Paystack-backed provisioning did not complete; the provider rejected invalid settlement details.
- Current Bora source does not enforce distinct settlement account numbers and maps settlement accounts by portfolio result order.
- Current migration can create external side effects before local failure/retry and has no demonstrated provider idempotency.
- Current result/error logging may include settlement details; manual Paystack README commands have no matching package aliases; no focused current migration tests were found.

## Connections

- [[../projects/livelycura-backend|LivelyCura Backend]]
- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]]
- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]]
- [[../syntheses/personal-operating-manual|Personal Operating Manual]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- LivelyCura’s generic migration runner still swallows failures, so a required backfill can remain unapplied while startup continues.
- Bora settlement uniqueness is a business invariant but is not enforced by validation or persistence constraints.
- Order-based account assignment can associate a valid settlement account with the wrong portfolio.
- Startup invokes BCL/Paystack external side effects; retries after partial success are not proven exactly-once.
- Current source contains no claimed V2 fake-configuration cleanup migration, and whether any environment persisted fake records is unresolved.
- No real provider provisioning, production migration, deployment, or payment initialization was demonstrated in the exact records.

## Open Questions

- Should settlement-account input be keyed by stable portfolio identifier rather than array position?
- Where should provider idempotency keys and partial-side-effect reconciliation live?
- Should migration output redact settlement account details before logging?
- Should Bora startup await migrations before listening, and should LivelyCura rethrow failed migrations?
