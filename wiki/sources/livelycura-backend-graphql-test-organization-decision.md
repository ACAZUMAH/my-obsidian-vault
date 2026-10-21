---
type: source
status: active
created: 2026-07-31
updated: 2026-07-31
tags: [livelycura, backend, graphql, tests, ci]
sources:
  - ../../raw/sources/2026-07-31-livelycura-backend-graphql-test-organization-decision.md
---

# LivelyCura Backend GraphQL Test Organization Decision

## Source

- Raw file: [2026-07-31-livelycura-backend-graphql-test-organization-decision.md](../../raw/sources/2026-07-31-livelycura-backend-graphql-test-organization-decision.md)
- Date: 2026-07-31
- Author: user correction and CI evidence
- Ingested: 2026-07-31

## Core Claims

- Backend GraphQL tests follow domain folders such as `tests/unit/graphql/courier/` and `tests/unit/graphql/selling/`.
- Backend unit tests must be hermetic: they validate the backend schema, resolvers, Shield rules, and services without reading sibling application repositories.

## Useful Details

- Cross-repository file reads can pass in the shared local workspace while failing in a repository-scoped GitHub runner.
- Courier schema contracts inspect the executable schema and Shield map directly; order-owned dispatch contracts remain in the selling domain.

## Connections

- [[../projects/livelycura-backend|LivelyCura Backend]]

## Contradictions Or Tensions

- The removed `courierContracts.test.ts` attempted to validate live portal/mobile operation files but violated repository isolation and the established domain-folder layout.

## Open Questions

- Cross-application operation validation may later belong in an explicitly provisioned integration workspace, not the backend unit suite.
