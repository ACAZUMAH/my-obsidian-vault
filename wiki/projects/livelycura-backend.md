---
type: project
status: active
created: 2026-07-21
updated: 2026-10-10
tags: [project, livelycura, backend, graphql, erp]
sources:
  - ../sources/livelycura-marketplace-single-delivery.md
  - ../sources/livelycura-independent-fleet-and-platform-dispatch.md
  - ../sources/livelycura-graphql-contract-compatibility.md
  - ../sources/livelycura-result-link-environments.md
  - ../sources/livelycura-lab-order-agent-environment-correction.md
  - ../sources/marketplace-scoped-admin-catalog-order-restructure.md
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
  - ../sources/livelycura-backend-graphql-test-organization-decision.md
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

The CRM domain owns the shared threaded support-case model described in [[../concepts/livelycura-customer-support-architecture|LivelyCura Customer Support Architecture]]. Verified marketplace/custom-app/storefront context derives case ownership and customer channel scope; Admin and Pharmacy Portal responder access remains owner- and permission-scoped.

`src/main.ts` and `src/app.ts` compose process startup. `servers` owns transports; `graphql` owns schema/resolvers; `services` owns domain behavior; `models` owns persistence; `dataloaders`, `middlewares`, `routes`, `controllers`, `cronJobs`, `pubsub`, and `logger` own infrastructure concerns.

Agent behavior is domain-scoped under `src/services/agent/domains`. MLS result validation and explanation use MLS-owned workflows rather than general helpers from unrelated domains.

MLS is a complete domain boundary across models, services, GraphQL, Shield, and DataLoaders. Its catalog/runtime records use namespace-scoped names: `Sample`, `TestDefinition`, `TestDefinitionVersion`, `TestRequest`, and `TestResult`.

Custom apps form another explicit boundary across models, services, GraphQL, and Shield. Organization/app assignment, banner configuration, and banner-event analytics are distinct responsibilities.

Marketplace administration supports independent catalog sources and order modes. Marketplace-owned products/linking and bidding remain intact; Admin-owned business-product configurations classify and publish ordinary ERP products with canonical marketplace category IDs without modifying ordinary product/category records. Ordinary fulfillment Orders carry `marketplaceId` when created directly by a marketplace or from accepted bids.

## Folder Ownership

- `src/graphql/<domain>`: thin schema and resolver layer.
- `src/services/<domain>`: validation, authorization, orchestration, and business rules.
- `src/models/<domain>`: Mongoose persistence.
- `src/services/agent/domains/<domain>`: domain agent/workflow logic.
- `tests/unit` and `tests/integration`: Vitest suites with separate configurations; GraphQL tests live under `tests/unit/graphql/<domain>`.
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

- Fleet GraphQL mirrors the established HRM module architecture. Define named, documented resolver functions that call feature services directly; let GraphQL Shield own endpoint permission and tenant-context checks; compose feature SDL through one interpolated `#graphql` template; and compose the root map explicitly by `Query`, `Mutation`, and object type. Do not add a Fleet principal/module/facility validation layer between Shield and services. Source: [[../sources/livelycura-independent-fleet-and-platform-dispatch|Fleet GraphQL architecture correction]].
- Fleet services receive one typed parameter named `data`. Resolvers pass generated GraphQL data directly and add only an authenticated actor user ID when required; services fetch the user rather than receiving a full user document. Do not restore `{ principal, input }` wrappers or positional actor arguments. Source: [[../sources/livelycura-independent-fleet-and-platform-dispatch|Fleet feature-slice correction]].
- Fleet service errors start with the missing entity and name the scope as facility when `facilityId` is supplied, otherwise organization. Avoid Fleet prefixes and workspace wording. Source: [[../sources/livelycura-independent-fleet-and-platform-dispatch|Fleet error-scope correction]].
- Fleet-owned service, helper, resolver, loader, and model file basenames omit redundant `Fleet`; functions, GraphQL fields/types, and Fleet-owned interfaces follow the same naming. Rename affected clients and regenerate contract types together. Model/collection symbols and the module identifier remain stable pending explicit persistence work. List queries use established filters and apply both date bounds to the intended field; interval records use overlap filtering. Source: [[../sources/livelycura-independent-fleet-and-platform-dispatch|Fleet naming and filter corrections]].
- Exception (2026-10-10): Fleet jobs are `FleetJob`. Folders are `graphql|services|models/fleet/fleetJobs`, and the names become `FleetJob*` types/inputs/enums, `getFleetJobs`/`getFleetJobById`, `create|assign|release|start|complete|cancel|failFleetJob`, `fleetJobId` on fuel, expenses, inspections, maintenance, defects and incidents, and audit entity `FleetJob`. There is no migration and permissions stay `fleet.dispatch.*`. Departure operations, `FleetJobModel` and the `fleetjobs` collection are unchanged. Source: [[../sources/livelycura-independent-fleet-and-platform-dispatch|Fleet jobs naming decision]].
- Fleet services follow the repository's feature-owned service pattern: entity services query and persist their own models, helpers remain free of database operations, and only concrete multi-document workflows own Mongoose sessions. Do not restore a feature-wide transaction/idempotency wrapper, generic record persistence helper, or generic list-query service. Source: [[../sources/livelycura-independent-fleet-and-platform-dispatch|Fleet architecture corrections]].
- Fleet update services call the owning model's appropriate update method (`updateOne`, `findByIdAndUpdate`, or `findOneAndUpdate`) instead of mutating a loaded document and calling `.save()`. Use `$set`, `$unset`, and `$push` deliberately, request `{ new: true }` when returning the updated record, and keep transaction sessions on every write. Source: [[../sources/livelycura-independent-fleet-and-platform-dispatch|Fleet model update-method correction]].
- Complete Fleet one feature at a time. Each backend slice includes documented feature services, named thin resolvers, feature-owned type definitions, Shield mappings, generated contracts, and compile-clean consumers before its frontend is exposed. Operators and Vehicles are the first accepted slices; later draft domains still require the same pass.

- Fleet models omit `deletedAt` and custom `version`; Fleet inputs do not require `expectedVersion`. Keep archive metadata and transaction-based operational checks consistent across models, services, loaders, and GraphQL. This correction is Fleet-specific.

- Perform business/input validation in services. Models should follow reference schemas without custom validation hooks/validators, immutability flags, or arbitrary length/range constraints. Current user corrections override stale skill examples.
- Reuse Departments/MLS archive semantics: ARCHIVED status and archived/archivedAt/archivedBy/archivedReason metadata, returning the archived entity. INACTIVE and deletedAt are different lifecycle operations. Inspect existing implementations before asking for an architectural choice already resolved in the codebase.

- Fleet people records must use a general name covering riders and drivers, capture fuller registration profiles, and omit the rejected custom revision counter. Keep these records independent of platform Courier; see [[../sources/livelycura-independent-fleet-and-platform-dispatch|Fleet ownership and profile corrections]].
- Keep the Fleet operator profile, lifecycle, and volatile dispatch state separate. Profile updates must not change status or live state. Purpose-specific work-state operations track online presence, accepting work, capacity, heartbeat expiry, and current coordinates; derive current load and actual availability from authoritative jobs and lifecycle state. Passenger/non-delivery work remains exclusive, while delivery batching may use configured capacity. Source: [[../sources/livelycura-independent-fleet-and-platform-dispatch|Fleet operator work-state correction]].
- Organization module resolvers filter persisted values against the current GraphQL `Module` enum before serialization. This lets login tolerate deferred cleanup of retired values such as `COURIER` without restoring them to the public enum or organization-module model. Source: [[../sources/livelycura-independent-fleet-and-platform-dispatch|Fleet operator frontend and retired module login correction]].
- Apply the same compatibility boundary to enum-list fields when cleanup is explicitly deferred: `MarketingMessage.app` omits historical values such as `CUSTOMER` that the current `MobileApps` enum cannot serialize, preserving the containing record without restoring the retired enum member. Source: [[../sources/livelycura-graphql-contract-compatibility|GraphQL contract compatibility]].
- Keep Courier requestor identity separate from Courier provider ownership. `Customer`, `Facility`, and `Organization` remain valid delivery requestors, and delivery tasks retain their applicable customer/facility/organization references for request, order, billing, and remittance workflows. These references do not grant an organization or facility ownership of riders or fulfillment. Source: [[../sources/livelycura-graphql-contract-compatibility|Courier requestor identity correction]].

- Do not mix domain concerns for convenience. MLS validation, result delivery, and marketplace bidding own separate helpers, interfaces, models, and services.
- Use the existing project agent/workflow infrastructure for AI workflows.
- Use existing React email templates for email delivery.
- New backend tests use Vitest; the family migrated from Jest and older README references to Mocha are stale.
- Keep GraphQL tests grouped under their owning domain folder. Backend unit tests are repository-hermetic and must not read Pharmacy Portal, Courier Mobile, or other sibling repositories merely because those folders exist in the local workspace.
- OpenAI is the active provider behind agent model defaults.
- Result validation never modifies entered measurements. It validates structured output against allowed field keys and records an immutable attempt against a values hash.
- Focus changes precisely. Do not remove adjacent GraphQL queries, filters, loaders, Shield rules, or services merely because one write path is being changed.
- Keep `MarketplaceBusinessProductListing` separate from ERP Product and Category. It stores canonical marketplace category IDs and publication state, never copied product details or organization-category projections. “Listing” is the domain term; the old physical collection name is retained only for deployed-data compatibility.
- Gate Marketplace Products, Business Products, Bidding, and Direct Orders through the selected marketplace's independent settings. Do not infer one capability from another.
- Reuse first-class records and established relationships: TestDefinitions reference Departments, Samples, and existing product Categories; category add/remove services propagate to a linked product instead of creating a second taxonomy or link model.
- Use intent-specific lifecycle services and mutations. Publish, activate, deactivate, archive, and test-request status transition are separate operations; activation changes only the selected definition.
- Archivable MLS/HRM records use `archived`, `archivedAt`, `archivedBy`, and optional `archivedReason` alongside status and soft deletion.
- Custom-app reads never create assignments. Admin operations explicitly assign or unassign a fixed managed-app enum; banner creation requires that assignment, and customer-facing reads additionally require the assignment to be enabled plus the banner to be published, active, in schedule, and target-compatible.
- Preserve established notification payloads unless the contract itself must change. The courier client maps the existing nested delivery-task identifier to its canonical route parameter; the backend does not emit duplicate aliases for the same ID.
- Generate pickup verification codes idempotently when an assigned delivery becomes ready, but do not send pickup codes by SMS. Expose the stored code only through an ERP-client task field after normal organization/facility task visibility succeeds; rider and other clients receive `null`. Drop-off code delivery remains a separate workflow.
- Keep COD collection and cash remittance as separate integer-minor-unit amounts. `cashOnDeliveryAmount` is the full amount collected from the customer; order-owned `cashRemittanceAmount` is `order.total - order.deliveryFee`, so the rider retains the delivery charge. Generic delivery creation defaults remittance to the full COD amount when no split is supplied.
- `cashRemittanceAmount` is stored on every delivery task; the 2026-10-05 courier provider-model cleanup migration backfilled older tasks, so read paths use the stored amount without a derivation fallback. The same migration renamed the exception review flag to `exceptionReviewRequired`/`exceptionReviewReason` and removed the single-value provider, remittance-route, payment-route and remittance-action fields.
- Remittance is receiver-confirmed: the requesting merchant confirms receipt from the rider; riders never confirm their own handover. The 2026-09-17 Courier boundary correction supersedes the previous company-provider intermediate receipt design. Source: [[../sources/livelycura-independent-fleet-and-platform-dispatch|Independent Fleet and platform dispatch decision]].
- Courier deliveries are single tasks: one pickup and one drop-off. Split marketplace fulfillment and multi-stop routes (parent/child tasks, manual multi-pickup routes, grouped marketplace routes) were removed for launch; rebuild multi-stop only if usage needs it. Source: [[../sources/livelycura-marketplace-single-delivery|Marketplace single delivery decision]].
- A marketplace order owns exactly one delivery task, created at award and priced into the buyer's delivery fee before payment. Bid orders carry no delivery task, and facilities cannot dispatch, re-dispatch, or manually move marketplace delivery statuses. One facility wins the whole order with a full-coverage bid.
- LivelyCura pays marketplace riders from the buyer's prepaid delivery fee; the winning facility is never billed or credit-checked for it. The automatic rider request goes out on payment confirmation, retries once when the facility marks READY, and then falls to Admin. Riders may release a marketplace delivery until pickup is verified, which re-offers the same task to other riders.
- Only the winning facility's staff read the marketplace task's pickup code and rider name, read-only on the bid order. Facilities cannot cancel an awarded, paid bid; Admin owns cancel-with-full-refund and failed-delivery handling.
- Customers cancel their own non-marketplace orders only while PLACED or ACCEPTED; marketplace buyers may cancel until pickup with a full refund. A delivery cancelled while the order is being prepared is replaced immediately and re-requested automatically when a rider had been requested or assigned, so a rider is found during preparation. Customers get the tracking link by SMS at pickup; the public tracking query exposes only status, a customer-safe timeline and the ETA. Source: [[../sources/livelycura-marketplace-single-delivery|Marketplace single delivery decision]].
- Marketplace delivery tasks are requested by the MarketplaceOrder (`requestedByModel = MarketplaceOrder`, no organization, facility or customer); the PLATFORM payer is derived, never stored. Courier settlements are keyed by the accepting offer (`deliveryTaskOfferId`), so a task re-accepted after a rider release or a parcel return gets a new settlement and at most one is RESERVED.
- A marketplace task stays DRAFT until payment; payment confirmation publishes it and opens the automatic rider request inside the provider transaction without ever failing the payment. Award, cancellation, and return confirmation each own one transaction; the marketplace status change is the award fence.
- After a failed LivelyCura-paid delivery the parcel returns to the facility on the same task (no return-to-origin task); cancellation and re-dispatch are blocked while a rider holds the parcel, until Admin confirms the return.
- Existing data moves to the single-delivery model through the registered migration `2026-10-05-single-delivery-courier-marketplace` (backfills settlement payer and offer identity and request triggers, cancels untaken multi-stop route tasks, removes route and split-era fields, sets the payment window, then rebuilds the courier and marketplace indexes). Test data is migrated, not deleted.
- Order-owning businesses confirm final COD receipt through an order-scoped mutation protected by entity-scoped `orders.update`. This path delegates to the courier settlement service and does not require Courier-module permissions.
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
- Sending requires `FINAL`, resolves recipients from the customer record, and requires a phone number because online report access requires OTP.
- Result links in SMS and email use the environment's customer portal: local `http://localhost:5173/`, staging `https://staging.livelycura.com/`, production `https://livelycura.com/`. Preserve the result-access path/token; do not substitute the ERP portal. See [[../sources/livelycura-result-link-environments|Result Link Environments]].
- Keep result-link origin and channel sender identities separate. The user-approved SMS sender is `LivelyCura`; result email reuses `livelyCuraBranding.emailFrom` (`LivelyCura <no-reply@serlp.com>` at the 2026-09-10 correction). Do not infer an email-domain change from an SMS-only instruction or portal URL. See [[../sources/livelycura-result-link-environments|Result Link Environments]].
- Previous active delivery links are revoked when a new delivery is issued.
- Result email includes a real finalized-report PDF attachment plus the secure link. Preserve visible finalized values and exclude internal findings/staff-only fields; a portal PDF-download feature alone does not satisfy this contract. See [[../sources/livelycura-result-link-environments|Result Link Environments]].
- Result-access OTP uses the LivelyCura SMS sender. A privacy-preserving accepted response is not a delivery receipt; inactive links do not trigger SMS. Log delivery failures without exposing codes, recipient numbers, tokens, or provider credentials.
- Marketplace bidding must remain untouched by MLS implementation work.
- Sale POS creates test requests for lab-linked products, including non-stock lab services. Placing an Order POS order alone does not create a request; ordinary accounting and inventory responsibilities remain with the selling domain.
- Each lab `SaleItem` has quantity one and maps idempotently to at most one `TestRequest`; a customer/patient is required. The request is created in the sale transaction.
- Synced laboratory services explicitly set `isStockItem: false`; generic product creation otherwise defaults it to true. Verify non-stock sales with a facility price but zero inventory records. Non-stock bundles still use their component inventory.
- Employee department remains optional. When supplied it must be active and belong to the same organization; an update may explicitly clear it.
- Product stock-behavior fields remain non-null; migration and write normalization keep `manufacturable`, `isStockItem`, and `isBundle` within their required domain.

## Decisions And Rationale

- Separate independent company Fleet operations from the LivelyCura delivery network. Admin owns standalone rider/network dispatch; optional Fleet network participation is an explicit integration. Courier carries Customer, Facility, or Organization requestor references for delivery, order, billing, and remittance, with no company ownership or facility-management scope. Build and verify the backend according to existing repository structure before client work. The retired company Courier was preproduction, so remove it without migration, cutover, materialization, reconciliation, or compatibility layers. Source: [[../sources/livelycura-independent-fleet-and-platform-dispatch|Independent Fleet and platform dispatch decision]].

- Human-in-the-loop MLS flow: draft, AI validation, scientist review/correction or override, finalization, explicit delivery, phone/OTP access, report, explanation.
- Explanations are pre-generated at finalization, but generation failure is logged and does not block the reviewed result.
- Result delivery email uses `testResultAvailableEmail` so branding and sending conventions remain centralized.
- The latest 2026-09-09 correction restores the sale as the lab-request boundary and withdraws the intervening Order POS change. Requests pin the active definition/version and start at the definition's first workflow step. See [[../sources/livelycura-lab-order-agent-environment-correction|Lab Sale And Agent Environment Corrections]].
- TestDefinition owns product linkage and category IDs. Billing, audit, and inventory remain with the sale/order systems rather than being duplicated in laboratory definition configuration.
- The retired company Courier architecture was preproduction. Remove its company-provider ownership and legacy preservation code directly. Current platform Courier keeps only the requestor, rider, delivery, billing, and remittance contracts required by active workflows.
- Courier GraphQL contract tests inspect the backend executable schema and Shield map inside the courier and selling test domains. Cross-application operation validation requires an explicitly provisioned integration workspace and does not belong in the backend unit suite.
- Pickup verification is an operational handoff between ERP dispatch staff and the arriving rider. Keeping the code in authorized order/task views avoids repeated SMS cost while preserving the six-digit proof gate and preventing the rider from reading the answer through its own API client.
- Custom-app ownership is three-part: Admin Portal assigns apps to organizations, Pharmacy Portal manages assigned-app banners, and the branded mobile app consumes only its own enabled organization/app pair and reports impressions/clicks.
- Order Live Activities remain deferred on a local feature branch. The active backend branch has no Live Activity implementation.
- Marketplace Orders describe bidding demand and lifecycle. Direct Orders describe ordinary organization fulfillment, including accepted manual/automatic bids; accepted bids intentionally appear in both views.

## Verification Expectations

Run generation, lint/format, Vitest unit and integration suites, build, then live HTTP/GraphQL/subscription smoke checks for runtime changes. For stock/schema evolution, test migration reruns, reference repointing, movement-based `lineCost` backfill, zero-quantity behavior, active uniqueness, malformed-identifier diagnostics, and transaction boundaries without opening a second database connection. Product non-null changes must cover null/missing legacy fields, create defaults, and update null suppression. For sale/MLS integration, verify stock and non-stock lab sales, zero-inventory services, stock-default misclassification, no request merely on order placement, transaction rollback, one-request-per-item idempotency, lifecycle permissions, and definition/version pinning. For custom apps, verify assignment ownership, no write-on-read behavior, enablement, banner lifecycle/targeting, and analytics. For courier changes, verify the full ERP creation through rider completion and cash-remittance journey, not only isolated service tests. Marketplace administration changes additionally require a dry-run migration, exact cross-organization category filtering, publication validation, access-revocation cleanup, referenced-category protection, existing ProductLinking coverage, and Direct Orders coverage.

## Evidence

- [[../sources/livelycura-marketplace-single-delivery|LivelyCura Marketplace Single Delivery]] records the 2026-10-04 removal of split fulfillment and multi-stop routes, and the single LivelyCura-dispatched marketplace delivery task.
- [[../sources/livelycura-lab-order-agent-environment-correction|LivelyCura Lab Sale And Agent Environment Corrections]] records both directions in sequence: the user withdrew Order POS and restored Sale POS, with a verified product-sync stock-default gap.
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
- [[../sources/livelycura-backend-graphql-test-organization-decision|LivelyCura Backend GraphQL Test Organization Decision]] records the CI failure caused by sibling-repository reads and the grouped, hermetic executable-schema replacement.
- [[../sources/marketplace-scoped-admin-catalog-order-restructure|Marketplace-Scoped Admin Catalog And Order Restructure]] records the current marketplace capability, business-product listing, Direct Orders, ERP-isolation, and migration boundary. The listing terminology superseded the earlier configuration name on 2026-09-01 while preserving the deployed collection. The focused marketplace integration suite passed all 6 tests after the rename.

## Contradictions

- The intervening 2026-09-09 Order POS direction is withdrawn by the later explicit Sale POS correction. Do not apply the order trigger from old notes, infer staging deployment, or automatically repair existing commercial records.
- Current `createBillOfMaterial.ts` appears to assert manufacturability before accepting “manufacturable or bundle,” potentially blocking pure bundle products from BOM creation despite the accepted bundle contract; focused execution is pending.
- README still describes Mocha, Swagger/OpenAPI boilerplate, and an old logger path; current package scripts and source use Vitest and the present architecture.
- Courier settlement persistence now separates collection, rider payout, remittable cash, and receiver-confirmed handovers; complete provider-agreement and end-to-end staging coverage still need verification.
- An older architecture document proposed one parent clinical request with many tests and one draft invoice. Current guidance retains one request per lab-linked sale item; the intervening Order POS trigger was explicitly withdrawn.
- Early lab research proposed a `JIT_BOM`/backflush mode consuming components during test processing. That remains historical research: ordinary non-stock laboratory-service sales do not themselves authorize or implement processing-time component consumption.
- The historical seeded-MLS cleanup was reported as registered and build-passing, but its current script is absent from the migration index and contains a questionable repeated filter property. Treat it as stale historical code; it was not reported as run against live data.
- The local Live Activities branch preserves APNs/FCM and persistence work, but active code contains no such feature. The deferred branch must be revalidated before reuse.
- Historical duplicate-sale-item migration guidance required cursor plus explicit batch accumulation. Current source instead streams duplicate groups and processes one group transactionally at a time; it still materializes one group, so production group-size bounds remain relevant. Current `mongoose` use starts a transaction session but does not take over connection ownership.
- Current sale-return inventory cleanup throws on conflicting active financial rows, but the generic migration runner catches and logs failures without rethrowing. The migration remains unapplied, yet whether application startup should fail closed is unresolved.
- Current source later removed the temporary sale-return compatibility field, but Stock/Sales #3 retained it and did not own the later commit/removal.

## Confidence

High for current implementation and MLS decisions; medium for the courier target until it is implemented and verified end to end.

## Open Questions

- Should the current delivery-task settlement snapshot eventually move behind a dedicated ledger aggregate once remittance disputes and reconciliation volume grow?
- Does MLS eventually need a clinical encounter aggregate above per-test requests, or should the sale remain the commercial grouping boundary?
- Which old README sections should be rewritten or removed?
- Should the stale seeded-catalog cleanup migration be repaired and registered, or removed after environment history is confirmed?
