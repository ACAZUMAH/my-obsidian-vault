---
type: source
status: active
created: 2026-10-12
updated: 2026-10-12
tags: [bora-capital, backend, graphql, error-handling, apollo]
sources:
  - ../../raw/sources/2026-10-12-bora-error-format-consistency.md
source_date: 2026-10-12
ingested: 2026-10-12
confidence: high
---

# Bora Error Format Consistency

## Source

- Raw file: [Verified review items and fixes](../../raw/sources/2026-10-12-bora-error-format-consistency.md)
- Date: 2026-10-12
- Author: User-supplied review items, reproduced and fixed by the agent with user approval
- Ingested: 2026-10-12

## Core Claims

- Every error response, GraphQL or Express/REST, is `errors: [{ message, extensions: { code } }]`. Codes come from one `getErrorCode(status)`, in which unlisted 4xx statuses map to `BAD_REQUEST`.
- Apollo Server 5 attaches `originalError` to its own request errors, so `formatGraphqlErrors` must recognize Apollo client error codes before unwrapping. They return `BAD_REQUEST` with the real message and are not reported to Sentry.
- `hideSchemaDetailsFromClientErrors` is on outside development, so real validation messages do not leak field suggestions.

## Useful Details

- Persisted-query error codes are deliberately not remapped; Apollo Client's retry protocol depends on them.
- Tests for the formatter run real `ApolloServer.executeOperation`. A hand-built `GraphQLError` does not reproduce Apollo's `originalError`.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[bora-bcl-error-passthrough-and-secret-files|Bora BCL Error Passthrough And Secret-File Boundary]]

## Contradictions Or Tensions

- The earlier formatter test asserted that a plain `GraphQLError` passes through without a code. That test stays, but it does not represent Apollo's real request errors.

## Open Questions

- None.
