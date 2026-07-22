---
type: project
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, lets-ride, backend, node, graphql]
sources:
  - ../sources/hermes-conversation-harvest-scope-correction.md
  - ../sources/ride-ordering-livelycura-hermes-chain.md
aliases: [letsride-backend, Cando Backend]
confidence: high
---

# Let's Ride Backend

## Summary

Foundation-only TypeScript backend for a future motorbike/tricycle ride-ordering product. The canonical name is Let’s Ride Backend; Cando Backend is a superseded historical name that still appears in current package and README metadata.

## Purpose

Establish the production-minded HTTP, GraphQL, subscription, database, security, logging, health, and shutdown foundation before adding ride-domain business logic.

## Stack

- Node.js and TypeScript.
- Express 5 and Apollo Server 5.
- MongoDB/Mongoose.
- GraphQL over HTTP and `graphql-ws` subscriptions.
- Environment validation, security/logging middleware, and Yarn.

## Architecture

`src/main.ts` loads environment configuration and starts the process. `src/app.ts` creates Express/HTTP, connects MongoDB, starts GraphQL and subscriptions, installs not-found/error handling, and listens only after the database is ready. Express, GraphQL, subscriptions, and GraphQL error formatting have separate factories.

## Folder Ownership

- `src/main.ts`: process entry.
- `src/app.ts`: startup/shutdown orchestration.
- `src/servers/createExpressApp.ts`: Express composition.
- `src/servers/createGraphqlServer.ts`: Apollo composition.
- `src/servers/createGraphqlSubscriptionServer.ts`: WebSocket subscription composition and cleanup.
- `src/servers/formatGraphqlErrors.ts`: central GraphQL error normalization.
- Health surfaces: minimal HTTP and GraphQL readiness checks.

## Commands

Historical dependency installation, build, and type-check passed. Use live package scripts as the source of truth before execution; no current command was run during the knowledge audit.

## Runtime/Deployment

Startup historically reached MongoDB connection and failed because no local MongoDB listener was available. HTTP, GraphQL, subscriptions, and database behavior were therefore not successfully exercised. Current repository has no tests, Docker/Compose, workflow, or deployment configuration.

## Durable Conventions

- Use Let’s Ride Backend as the canonical name.
- Keep process entry, application orchestration, transport composition, and GraphQL error formatting separate.
- Connect MongoDB before accepting traffic.
- Preserve coordinated HTTP/WebSocket shutdown and subscription cleanup.
- Do not infer ride, booking, driver, rider, payment, wallet, routing, pricing, location, notification, or administration behavior: those domains were deliberately excluded from this foundation.

## Constraints

- Current implementation is foundation-only.
- Build/type-check success does not prove database-backed runtime.
- No payment or logistics rule is implemented merely because ride ordering is the product intent.
- Current package and README still use stale Cando branding.

## Decisions And Rationale

The initial minimal scaffold was corrected to use `main.ts` as process entry, `app.ts` as startup orchestration, separate Express/GraphQL/subscription factories, central error formatting, and subscription cleanup. This shape prevents transport and process lifecycle concerns from collapsing into one server file.

## Verification Expectations

Reconcile branding, then run type-check/build and add focused tests for app composition, error formatting, health checks, and coordinated shutdown. Start MongoDB and exercise HTTP health, GraphQL health/query/error behavior, subscription connection/cleanup, and graceful termination. Verify no domain modules were accidentally introduced before their contracts are designed.

## Evidence

- Exact direct chain `20260628_134341_c8f843` through `20260629_001748_68c46e` plus current static source in [[../sources/ride-ordering-livelycura-hermes-chain|Ride Ordering And LivelyCura Hermes Chain]].
- [[../sources/hermes-conversation-harvest-scope-correction|Hermes Conversation Harvest Scope Correction]] establishes the canonical name and provenance boundary.

## Contradictions

- Current package name `cando-backend` and README title “Cando Backend” conflict with the canonical Let’s Ride Backend name.
- The original request named `server.ts`; the accepted correction and current source use `main.ts` plus `app.ts`.
- Historical build success accompanied a failed MongoDB connection, so no successful database-backed runtime can be claimed.
- Current source has no tests or deployment surface.

## Confidence

High for canonical identity and static foundation architecture; medium for runtime behavior until Mongo-backed smoke tests are executed.

## Open Questions

- When should package/README branding be reconciled?
- Which conversation authorizes the first ride-domain module and its API/data contracts?
- What deployment, observability, test, and local-database contracts should be added before domain work?
