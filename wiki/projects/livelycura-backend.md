---
type: project
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, livelycura, backend, graphql, erp]
sources:
  - ../sources/livelycura-project-knowledge-harvest-batch-1.md
  - ../sources/livelycura-project-knowledge-harvest-batch-2.md
  - ../sources/livelycura-project-knowledge-harvest-batch-3.md
  - ../sources/livelycura-project-knowledge-harvest-batch-4.md
  - ../sources/livelycura-stock-sales-hermes-supplement-1.md
  - ../sources/livelycura-stock-sales-hermes-supplement-2.md
  - ../sources/livelycura-stock-sales-hermes-supplement-3.md
  - ../sources/graphql-product-bora-paystack-hermes-chain.md
  - ../sources/ride-ordering-livelycura-hermes-chain.md
  - ../sources/portfolio-carousel-skills-livelycura-hermes-supplement.md
  - ../sources/product-lab-badge-mls-hermes-chain.md
confidence: high
---

# LivelyCura Backend

## Summary

Shared TypeScript API and domain runtime for the LivelyCura/SERLP product family.

## Purpose

Provides GraphQL and supporting HTTP/subscription services for ERP, commerce, administration, mobile applications, MLS, courier operations, notifications, and agent workflows.

## Stack

- Node `>=22.13.0`, TypeScript, Express 4, Apollo Server 4, GraphQL and WebSocket subscriptions.
- MongoDB/Mongoose, JWT/auth middleware, DataLoader, GraphQL Shield.
- Winston, AJV, `http-errors`, GraphQL Codegen.
- Vitest unit/integration suites.
- Mastra/AI SDK with OpenAI model defaults for project agents.
- Yarn.

## Architecture

`src/main.ts` and `src/app.ts` compose process startup. `servers` owns transports; `graphql` owns schema/resolvers; `services` owns domain behavior; `models` owns persistence; `dataloaders`, `middlewares`, `routes`, `controllers`, `cronJobs`, `pubsub`, and `logger` own infrastructure concerns.

Agent behavior is domain-scoped under `src/services/agent/domains`. MLS result validation and explanation use MLS-owned workflows rather than general helpers from unrelated domains.

MLS is a complete domain boundary across models, services, GraphQL, Shield, and DataLoaders. Its catalog/runtime records use namespace-scoped names: `Sample`, `TestDefinition`, `TestDefinitionVersion`, `TestRequest`, and `TestResult`.

Custom apps form another explicit boundary across models, services, GraphQL, and Shield. Organization/app assignment, banner configuration, and banner-event analytics are distinct responsibilities.

## Folder Ownership

- `src/graphql/<domain>`: thin schema and resolver layer.
- `src/services/<domain>`: validation, authorization, orchestration, and business rules.
- `src/models/<domain>`: Mongoose persistence.
- `src/services/agent/domains/<domain>`: domain agent/workflow logic.
- `tests/unit` and `tests/integration`: Vitest suites with separate configurations.
- `scripts/migrations`: runner-owned schema/data evolution using imported domain models and the application-managed database lifecycle.

## Commands

- `yarn dev`, `yarn build`, `yarn start`
- `yarn generate`
- `yarn lint`, `yarn format:check`
- `yarn test`, `yarn test:unit`, `yarn test:integration`, `yarn test:ci`
- `yarn emails` for local React email-template work

## Runtime/Deployment

Dockerfile plus database, development, and production Compose files. GitHub workflows cover CI, staging, and production. `build:digitalocean` provides the PaaS build path.

## Durable Conventions

- Do not mix domain concerns for convenience. MLS validation, result delivery, and marketplace bidding own separate helpers, interfaces, models, and services.
- Use the existing project agent/workflow infrastructure for AI workflows.
- Use existing React email templates for email delivery.
- New backend tests use Vitest; the family migrated from Jest and older README references to Mocha are stale.
- OpenAI is the active provider behind agent model defaults.
- Result validation never modifies entered measurements. It validates structured output against allowed field keys and records an immutable attempt against a values hash.
- Focus changes precisely. Do not remove adjacent GraphQL queries, filters, loaders, Shield rules, or services merely because one write path is being changed.
- Reuse first-class records and established relationships: TestDefinitions reference Departments, Samples, and existing product Categories; category add/remove services propagate to a linked product instead of creating a second taxonomy or link model.
- Use intent-specific lifecycle services and mutations. Publish, activate, deactivate, archive, and test-request status transition are separate operations; activation changes only the selected definition.
- Archivable MLS/HRM records use `archived`, `archivedAt`, `archivedBy`, and optional `archivedReason` alongside status and soft deletion.
- Custom-app reads never create assignments. Admin operations explicitly assign or unassign a fixed managed-app enum; banner creation requires that assignment, and customer-facing reads additionally require the assignment to be enabled plus the banner to be published, active, in schedule, and target-compatible.
- Preserve established notification payloads unless the contract itself must change. The courier client maps the existing nested delivery-task identifier to its canonical route parameter; the backend does not emit duplicate aliases for the same ID.
- One active `SaleItem` represents one customer-facing product line per sale; batch and bundle-component relief remains movement-level. Returns reference the sold line by `saleItemId` even when no inventory record exists.
- `SaleItem.lineCost` is the exact sale-time COGS source. Do not reconstruct posting totals from rounded weighted unit cost when exact line cost is available.
- Application-startup migrations use the runner-owned connection and imported models. Stream production-sized work, update dependent references before soft-deleting duplicates, backfill before making contracts required, and preserve rerun idempotence.
- Exact `lineCost` propagates through accounting contracts, services, fixtures, and explicit zero-cost cases; do not retain `unitCost × quantity` reconstruction after the required-field migration.
- Sale-return identity is `{saleReturnId, saleItemId}`. Remove obsolete inventory fields/data/indexes idempotently, reject conflicting active financial rows instead of merging them, and establish replacement active uniqueness only after conflict checks.
- When a non-null Product contract exposes legacy null/missing flags, repair persisted data and normalize create/update writes. Do not mask invalid storage with fallback field resolvers after migration is selected.
- Migration conflict diagnostics stringify malformed historical identifiers defensively so formatting cannot obscure the primary failure.

## Constraints

- A result normally finalizes only from `PENDING_REVIEW` with a current passing validation for the exact persisted values hash.
- Flagged or unavailable AI output requires an authorized override and reason; finalized values are immutable.
- Sending requires `FINAL`, resolves recipients from the customer record, and requires a phone number because OTP access is mandatory.
- Previous active delivery links are revoked when a new delivery is issued.
- Marketplace bidding must remain untouched by MLS implementation work.
- A lab-linked sale item must still follow the ordinary sale, stock, COGS, and invoice path. The lab request is created inside the same transaction, not through a parallel lab-sale API.
- Each test `SaleItem` has quantity one and maps idempotently to at most one `TestRequest`; a customer/patient is required.
- Employee department remains optional. When supplied it must be active and belong to the same organization; an update may explicitly clear it.
- Product stock-behavior fields remain non-null; migration and write normalization keep `manufacturable`, `isStockItem`, and `isBundle` within their required domain.

## Decisions And Rationale

- Human-in-the-loop MLS flow: draft, AI validation, scientist review/correction or override, finalization, explicit delivery, phone/OTP access, report, explanation.
- Explanations are pre-generated at finalization, but generation failure is logged and does not block the reviewed result.
- Result delivery email uses `testResultAvailableEmail` so branding and sending conventions remain centralized.
- Current request grouping uses the sale as the commercial boundary and one `TestRequest` per lab-linked `SaleItem`. The request pins the active definition/version and starts at the definition's first workflow step.
- TestDefinition owns product linkage and category IDs. Billing, audit, and inventory remain with the sale/order systems rather than being duplicated in laboratory definition configuration.
- Courier target architecture supports any merchant, courier companies and standalone riders, fixed quotes, separate rider payout, prepaid or COD collection, and separate remittance. This is current product direction, not fully implemented persistence.
- Custom-app ownership is three-part: Admin Portal assigns apps to organizations, Pharmacy Portal manages assigned-app banners, and the branded mobile app consumes only its own enabled organization/app pair and reports impressions/clicks.
- Order Live Activities remain deferred on a local feature branch. The active backend branch has no Live Activity implementation.

## Verification Expectations

Run generation, lint/format, Vitest unit and integration suites, build, then live HTTP/GraphQL/subscription smoke checks for runtime changes. For stock/schema evolution, test migration reruns, reference repointing, movement-based `lineCost` backfill, zero-quantity behavior, active uniqueness, malformed-identifier diagnostics, and transaction boundaries without opening a second database connection. Product non-null changes must cover null/missing legacy fields, create defaults, and update null suppression. For sales/MLS integration, verify ordinary and lab-linked sales, transaction rollback, one-request-per-item idempotency, lifecycle permissions, and definition/version pinning. For custom apps, verify assignment ownership, no write-on-read behavior, enablement, banner lifecycle/targeting, and analytics. For courier changes, verify the full ERP creation through rider completion and cash-remittance journey, not only isolated service tests.

## Evidence

- Current package/scripts, server and domain source, MLS/courier models and services, tests, Docker/Compose, and workflows.
- Sessions `019f7d44…`, `019f6d9c…`, `019f5cbd…`, and `019f56a3…` in [[../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]].
- Sessions `019ec6f5…`, `019eb927…`, `019e7553…`, and `019e4af8…` in [[../sources/livelycura-project-knowledge-harvest-batch-2|LivelyCura Project Knowledge Harvest — Batch 2]].
- Sessions `019e88a0…`, `019e02a9…`, and `019e0007…` in [[../sources/livelycura-project-knowledge-harvest-batch-3|LivelyCura Project Knowledge Harvest — Batch 3]].
- Sessions `019e239f…` and `019dfd88…` plus current sale/MLS and courier-notification source in [[../sources/livelycura-project-knowledge-harvest-batch-4|LivelyCura Project Knowledge Harvest — Batch 4]].
- Direct Hermes session `20260629_173939_b6748a` plus current stock/sale/migration source in [[../sources/livelycura-stock-sales-hermes-supplement-1|LivelyCura Stock And Sales Hermes Supplement — 1]].
- Direct continuation `20260629_193407_346702` plus current exact-cost and sale-return migration source in [[../sources/livelycura-stock-sales-hermes-supplement-2|LivelyCura Stock And Sales Hermes Supplement — 2]].
- Direct continuation `20260712_183956_816de0` in [[../sources/livelycura-stock-sales-hermes-supplement-3|LivelyCura Stock And Sales Hermes Supplement — 3]] closes the historical full-suite report and adds defensive migration diagnostics; full suites preceded the final patch.
- Two substantive records in [[../sources/graphql-product-bora-paystack-hermes-chain|GraphQL Product And Bora Paystack Hermes Chain]] establish the rejected fallback resolver and accepted Product migration/write-normalization correction.
- Four substantive records in [[../sources/ride-ordering-livelycura-hermes-chain|Ride Ordering And LivelyCura Hermes Chain]] provide earlier direct ownership for product-level sale lines, movement-based returns/rollback, exact-cost migrations, interface extraction, transaction typing, and historical Jest CI closure; later stock/sales supplements remain authoritative for the final current contract.
- The unique tail of `20260624_105536_89348f` in [[../sources/portfolio-carousel-skills-livelycura-hermes-supplement|Portfolio Carousel, Skills, And LivelyCura Hermes Supplement]] adds historical MLS-sale fallback resolution through the canonical TestDefinition-to-product relationship, backend type-check evidence, and a 10/10 integration-file pass; its replayed Portfolio prefix adds no backend attribution.
- Five substantive records in [[../sources/product-lab-badge-mls-hermes-chain|Product Lab Badge And MLS Hermes Chain]] complete the canonical `testDefinitionId` badge request, refresh repair, stock/non-stock behavior, BOM-backed bundle design, UOM-aware relief, and sold-line return ownership. Later movement-ledger supplements remain authoritative for current reversal mechanics.

## Contradictions

- Current `createBillOfMaterial.ts` appears to assert manufacturability before accepting “manufacturable or bundle,” potentially blocking pure bundle products from BOM creation despite the accepted bundle contract; focused execution is pending.
- README still describes Mocha, Swagger/OpenAPI boilerplate, and an old logger path; current package scripts and source use Vitest and the present architecture.
- Courier current model is simplified single pickup/drop-off with task pricing/payment allocations. It does not yet express the approved provider agreement, separate collection, payout, and remittance lifecycles.
- An older architecture document proposed one parent clinical request with many tests and one draft invoice. Later explicit sale-integration decisions and current code instead create one request per lab-linked sale item inside the ordinary sale transaction.
- Early lab research later proposed a `JIT_BOM`/backflush fulfillment mode that would sell test services without finished inventory and consume components at test processing. No such mode exists in current code; later implementation keeps the ordinary inventory movement and COGS path, so the proposal remains historical research.
- The historical seeded-MLS cleanup was reported as registered and build-passing, but its current script is absent from the migration index and contains a questionable repeated filter property. Treat it as stale historical code; it was not reported as run against live data.
- The local Live Activities branch preserves APNs/FCM and persistence work, but active code contains no such feature. The deferred branch must be revalidated before reuse.
- Historical duplicate-sale-item migration guidance required cursor plus explicit batch accumulation. Current source instead streams duplicate groups and processes one group transactionally at a time; it still materializes one group, so production group-size bounds remain relevant. Current `mongoose` use starts a transaction session but does not take over connection ownership.
- Current sale-return inventory cleanup throws on conflicting active financial rows, but the generic migration runner catches and logs failures without rethrowing. The migration remains unapplied, yet whether application startup should fail closed is unresolved.
- Current source later removed the temporary sale-return compatibility field, but Stock/Sales #3 retained it and did not own the later commit/removal.

## Confidence

High for current implementation and MLS decisions; medium for the courier target until it is implemented and verified end to end.

## Open Questions

- How should provider agreements, quote acceptance, COD collection, rider payout, and remittance be added without overloading `DeliveryTask`?
- Does MLS eventually need a clinical encounter/order aggregate above per-test requests, or should the sale remain the only grouping boundary?
- Which old README sections should be rewritten or removed?
- Should the stale seeded-catalog cleanup migration be repaired and registered, or removed after environment history is confirmed?
