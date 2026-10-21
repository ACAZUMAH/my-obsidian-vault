---
type: source
status: active
created: 2026-09-21
updated: 2026-09-21
tags: [checkcity, typescript, tests]
sources:
  - ../../raw/sources/2026-09-21-checkcity-typescript-tests.md
---

# CheckCity TypeScript Tests

## Source

- Raw file: [Direct user correction](../../raw/sources/2026-09-21-checkcity-typescript-tests.md)
- Date: 2026-09-21
- Author: user
- Ingested: 2026-09-21

## Core Claims

Use TypeScript for CheckCity Cart tests instead of mixing JavaScript and TypeScript. Test files without JSX use `.test.ts`; JSX tests use `.test.tsx`.

## Useful Details

A rename alone is insufficient: type mocks and fixtures, include explicit Jest imports where needed, and fix imports when tests move. Preserve the user's folder organization.

## Connections

- [[../projects/livelycura-check-city-app|LivelyCura CheckCity App]]

## Contradictions Or Tensions

Existing JavaScript tests are historical implementation, not a preferred convention.

## Open Questions

- None for the requested Cart scope.
