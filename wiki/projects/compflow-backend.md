---
type: project
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, compflow, backend, graphql, payroll]
sources:
  - ../sources/compflow-project-knowledge-harvest-batch-1.md
  - ../sources/compflow-hermes-project-knowledge-harvest-supplement-1.md
  - ../sources/compflow-checkcity-hermes-conversation-harvest-supplement-1.md
  - ../sources/compflow-proper-stack-hermes-continuations.md
  - ../sources/compflow-backend-auth-hermes-continuations.md
confidence: high
---

# CompFlow Backend

## Summary

ComplianceFlow API and domain runtime for OTP authentication, organizations, employees, subscription onboarding/payment, roles, and payroll.

## Purpose

Provides shared GraphQL, WebSocket, health, and payment-webhook services for [[compflow|CompFlow Public Frontend]], [[compflow-admin|CompFlow Admin]], and [[compflow-client-portal|CompFlow Client Portal]].

## Stack

- Node `>=22.13.0`, Yarn 1, TypeScript 5.9.
- Express 4, Apollo Server 5, GraphQL 16, GraphQL WS subscriptions.
- MongoDB/Mongoose 9, DataLoader, GraphQL Shield.
- AJV, JWT, `http-errors`, Winston, Helmet, Morgan.
- Paystack and Moolre payment integration code.
- PDFKit for payroll reports/payslips; React Email and Resend for email.
- Jest, Supertest, and MongoDB Memory Server.

## Architecture

`src/main.ts` loads environment/process entry behavior and starts `src/app.ts`. Startup creates Express and a shared HTTP server, applies middleware and routes, connects MongoDB, mounts GraphQL HTTP at `/graphql` and WebSocket subscriptions at `/subscriptions`, attaches centralized errors, listens, then triggers migrations asynchronously. Current source does not await migration completion before readiness and catches/logs migration failures.

The accepted bootstrap keeps process entry, startup orchestration, Express creation, Apollo HTTP, GraphQL subscriptions, GraphQL error formatting, database ownership, JWT middleware, request context, and DataLoader creation as explicit responsibilities. JWT middleware enriches the request; GraphQL context spreads that request with request-scoped loaders and IP metadata.

GraphQL domains cover auth, users, employees, organizations, roles, subscription plans/checkouts, and payroll. Resolvers remain thin while services own validation, scope, orchestration, payment, and lifecycle behavior. GraphQL Shield maps operations to permissions.

## Folder Ownership

- `src/graphql/<domain>`: schema and thin resolvers.
- `src/graphql/shield`: authentication and named permission rules.
- `src/services/<domain>`: validation, authorization scope, orchestration, and side effects.
- `src/models/<domain>`: Mongoose documents and indexes.
- `src/common`: database, enums, helpers, interfaces, and validators.
- `src/servers`: Express/Apollo/WebSocket composition.
- `src/routes`: health/root and payment-webhook HTTP routes.
- `src/dataloaders`, `src/middlewares`, `src/logger`: request/runtime infrastructure.
- `tests`: Jest transport, auth, authorization, migration, payroll, and subscription suites.

## Commands

- `yarn dev` — Nodemon development process.
- `yarn build` — TypeScript compilation then alias rewriting.
- `yarn start` — compiled `dist/src/main.js`.
- `yarn test` — Jest in-band.
- `yarn generate` — configured script, currently blocked because tracked `codegen.ts` is absent.

## Runtime/Deployment

HTTP defaults to port 4000. Runtime exposes `/health`, `/graphql`, `/subscriptions`, `/webhooks/paystack`, and `/webhooks/moolre`. No Dockerfile, Compose file, or GitHub deployment workflow was found in the current checkout.

## Durable Conventions

- Authentication is OTP-only. Login begins by email or phone and completes with `completeLoginWithToken`; portal access is checked during completion.
- Authentication uses Winston and AJV rather than the rejected password/Bcrypt/Zod/Pino scaffold. OTP delivery is owned by Resend plus React Email, while tests may mock transport/rendering without replacing the production template path.
- Resolvers pass input and principal context to services; services own scope and domain decisions.
- Ordinary tenant users resolve to their organization. Admin/SuperAdmin may operate without membership and may provide organization scope.
- By-ID tenant operations fetch the entity first, derive organization scope from the persisted record, then apply platform-role bypass or tenant membership checks; clients should not provide redundant organization identity for authorization.
- Lists sanitize page/limit, fetch `limit + 1`, and use `getPageConnection` for `hasNextPage`.
- Bootstrap data such as the developer platform role is registered as an idempotent migration, not exposed as an ad hoc package seed. Current startup triggering is not fail-closed.
- Use separate permissioned payroll lifecycle operations: create, approve, mark paid, and cancel.
- Self-service organization creation happens only after verified signup, authenticated checkout, and successful payment; enterprise/contact-sales plans remain admin-created.
- Email and SMS OTP delivery may run concurrently; authentication may proceed when at least one configured channel succeeds and must fail when all configured channels fail.
- Moolre and Paystack remain separate provider adapters behind an explicit switch. Moolre uses callback-token validation under the available contract; Paystack retains signature verification. Mocked provider tests are not live-payment evidence.
- Payroll uses employee snapshots, tax rules, PAYE/SSNIT calculations, integer minor units, separate run/run-item models, explicit draft/approve/paid transitions, and real PDFKit reports/payslips.
- GraphQL Shield uses explicit root-operation rules plus coverage tests. Current `fallbackRule: allow` makes exhaustive coverage a security invariant rather than a convenience.
- Preserve webhook verification and sanitized provider responses; never log or persist secrets into knowledge artifacts.

## Constraints

- `pageInfo.total` is the returned-edge count, not a total database count.
- Draft payroll runs alone may be approved; approved runs alone may be marked paid.
- Tenant users cannot select another organization; payroll by-ID access checks the persisted run's organization.
- Checkout rejects an existing business and reuses an existing pending checkout for the owner.
- Payment reference, amount, and success status are verified before organization/owner creation.
- The README's database-bypass command is not implemented in current source.

## Decisions And Rationale

- The backend belongs in its own `compflow-backend` repository with Yarn; this was an explicit user correction after an accidental root-monorepo scaffold.
- Public plan lookup is open, but checkout requires an authenticated verified principal so business ownership is bound before payment.
- Organization and owner records are created after payment success, avoiding a fully provisioned tenant before subscription confirmation.
- Payroll run items snapshot employee calculations at run creation; later reports and payslips read the persisted snapshot.
- Shield permissions plus service-level organization assertions separate operation authorization from tenant data scope.

## Verification Expectations

Repair or remove stale generation/database-bypass documentation before relying on those paths. For runtime work, run Jest, build, then live `/health`, GraphQL HTTP, subscription, OTP, organization-scope, payroll-transition, and payment-webhook tests with safe test configuration. Verify both Paystack and Moolre paths, replay/idempotency behavior, failed amount/status handling, and tenant/admin authorization. No live payment, database, migration, or deployment should be inferred from static tests alone.

## Evidence

- Current package/README, startup/server/routes, GraphQL/shield, auth/scope, subscription/payment, payroll services/models, tests inventory, and clean Git state at `main` commit `b512a40b7b9e`.
- Current repository evidence in [[../sources/compflow-project-knowledge-harvest-batch-1|CompFlow Project Knowledge Harvest — Batch 1]]; no historical CompFlow Codex session was discovered.
- Hermes session `20260710_173537_54b264` historically scaffolded and verified the separate backend baseline. First commit `5ffd875` preserves its Express/Apollo/WebSocket, REST/GraphQL health, Jest/Supertest, port `4000`, and initial admin-overview lineage; see [[../sources/compflow-hermes-project-knowledge-harvest-supplement-1|CompFlow Hermes Project Knowledge Harvest — Supplement 1]].
- Hermes sessions `20260710_190402_e7ba9f` and `20260711_165753_68ff6f` directly establish the corrected file-level startup architecture, OTP/Winston/AJV contract, Resend/React Email ownership, and payment-before-provisioning behavior; see [[../sources/compflow-checkcity-hermes-conversation-harvest-supplement-1|CompFlow And CheckCity Hermes Conversation Harvest — Supplement 1]]. Historical reports attributed three passing foundation tests and later two suites/four auth tests plus successful builds and transport smokes; none were rerun during the harvest.
- Four substantive continuations in [[../sources/compflow-proper-stack-hermes-continuations|CompFlow Proper Stack Hermes Continuations]] establish removal of fake overview contracts, database-managed plans, record-derived organization scope, shared pagination, developer-role migration ownership, historical verification, and the current startup-order contradiction.
- Five continuations in [[../sources/compflow-backend-auth-hermes-continuations|CompFlow Backend Authentication Hermes Continuations]] establish customer-driven onboarding, Moolre/Paystack and dual-channel OTP ownership, payroll implementation/modular correction, service separation, RBAC/Shield, organization review/resubmission, and exact incomplete verification boundaries.

## Contradictions

- The session reported a REST admin-overview smoke path and two backend tests; the first Git commit records GraphQL `adminOverview` and three tests, while current source has removed `adminOverview` entirely. These are successive historical states, not interchangeable current contracts.
- README says `SKIP_DB_CONNECTION=true yarn dev` provides a transport-only smoke run, but startup always calls `connectToDb` and the connector does not read that flag.
- `package.json` invokes GraphQL Codegen with `codegen.ts`, but no tracked config exists; the frontend configs also expect an absent root `schema.graphql`.
- A legacy aggregate payroll model file coexists with the split payroll models exported by the active model index.
- `src/dataloaders/index.ts` preserves the request-context boundary but currently returns an empty loader set.
- The generic legacy `initializeBusinessSubscription` service coexists with the newer verified platform-signup/checkout path, while current GraphQL exposes the platform path.
- `adminOverview` was deliberately removed from backend schema/resolvers/Shield/tests, but Admin still queries it and silently falls back.
- The role migration is registered and startup-triggered, but migrations run after server readiness, are not awaited, and errors are logged rather than failing startup.
- Historical Atlas diagnosis reached DNS/TCP but failed TLS before authentication. Allowlisting was plausible but not proven; current live connectivity is unknown.
- Four payroll files whose deletion was historically approval-blocked remain at current HEAD, including an unexported aggregate model and root helpers that coexist with modular replacements.
- Moolre was requested as a temporary hackathon default, but the later switch back to Paystack was never completed in source defaults.
- The final #6 permission patches were not reverified after the last full-suite failure; an earlier 5-suite/10-test green state preceded those changes.

## Confidence

High for current static architecture, authorization, onboarding, and payroll rules; medium for live integrations and deployment because no service, test, database, payment, or build was executed.

## Open Questions

- Should the database-bypass path be implemented for tests or removed from README?
- How should the canonical GraphQL schema artifact and backend Codegen config be produced?
- Can the legacy subscription initializer and aggregate payroll model be removed after usage history is confirmed?
- What is the intended production deployment and migration-release procedure?
- Should migrations be awaited and fail closed before GraphQL readiness?
