---
type: project
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, portfolio, backend, graphql, cms]
sources:
  - ../sources/portfolio-project-knowledge-harvest-batch-1.md
confidence: high
---

# Portfolio Backend

## Summary

Express/Apollo/MongoDB API and CMS runtime for the public portfolio and administrative portal.

## Purpose

Owns authentication, profile and SEO content, projects/case studies, experience, education, skills, testimonials, media, resumes, leads, availability, analytics, and public aggregate portfolio data.

## Stack

- Node.js, Yarn 1, strict TypeScript ES2022/CommonJS.
- Express 4, Apollo Server 4, GraphQL 16, GraphQL Shield.
- MongoDB/Mongoose 8, request-scoped DataLoader.
- GraphQL WebSocket subscriptions, Socket.IO, object-storage client libraries, Winston.
- Jest/ts-jest configuration with `--passWithNoTests`.

## Architecture

`src/main.ts` starts `src/app.ts`, which composes Express, a shared HTTP server, database connection, Apollo HTTP, subscriptions, Socket.IO, and shutdown behavior. GraphQL schemas/resolvers are composed centrally. Thin resolvers delegate to domain services, models own persistence, and request context owns DataLoaders and principal state.

## Folder Ownership

- `src/graphql/<domain>`: schemas and resolvers.
- `src/graphql/shield`: operation/field permissions.
- `src/services/<domain>`: validation, public transformations, queries, and business operations.
- `src/models/<domain>`: Mongoose persistence.
- `src/dataloaders`: request-batched relationships.
- `src/servers`: Express, Apollo, and subscription composition.
- `src/common`: shared enums, helpers, and interfaces.

## Commands

- `yarn dev` — development runtime.
- `yarn build` — TypeScript compilation and alias rewrite.
- `yarn start` — compiled runtime.
- `yarn generate` — GraphQL contract generation.
- `yarn lint` — ESLint.
- `yarn test` — Jest, currently allowed to pass with no tests.

## Runtime/Deployment

Compiles to `dist/src/main.js`, connects to MongoDB, and serves HTTP, GraphQL, WebSocket, and Socket.IO traffic. No tracked CI, container, hosting manifest, backend README, or explicit Node-version contract was found.

## Durable Conventions

- One owned folder per domain across GraphQL, services, models, and interfaces.
- Keep resolvers thin and service functions documented.
- Compose GraphQL permissions centrally and create DataLoaders per request.
- Public project queries filter visibility and redact intended case-study detail while preserving unrelated media fields.
- Shared enums are canonical; do not duplicate domain constants.

## Constraints

- Production disables introspection and suppresses stack traces.
- Public projects include public, restricted-summary, and protected visibility modes; detailed fields differ by mode.
- Current startup does not automatically seed content.
- The test script can report success with no test files.

## Decisions And Rationale

The backend mirrors established folder/layer conventions instead of placing feature logic in resolvers or a monolithic module. Project access rules belong in Shield and explicit public transformations; restricted summary behavior must not indiscriminately remove media or unrelated fields.

## Verification Expectations

Run generation after schema changes, then lint, focused authorization/service tests, full tests, and build. Start with safe configuration and exercise HTTP GraphQL, subscriptions, auth, public visibility modes, media, leads, analytics, and shutdown. Treat an empty passing Jest run as no coverage.

## Evidence

- Clean `main@c211320705f5`, current package/config/startup/server/GraphQL/service/model structure.
- Historical architecture, visibility correction, and reported builds in [[../sources/portfolio-project-knowledge-harvest-batch-1|Portfolio Project Knowledge Harvest — Batch 1]].

## Contradictions

- Historical summaries reported visibility tests, while later commands found no tests; current repository has no tracked test files.
- Root documentation says content is seeded automatically, while the startup seed call is disabled.
- Express 4 runtime uses Express 5 type declarations.
- GraphQL Codegen CLI appears in both runtime and development dependencies.

## Confidence

High for current static architecture and ownership; medium for runtime, external storage, subscriptions, and authorization behavior because no current commands or services were run.

## Open Questions

- Should startup seeding be restored or documentation corrected?
- What Node, CI, container, and production deployment contracts are intended?
- Which focused authorization, visibility, subscription, and media tests should be added first?