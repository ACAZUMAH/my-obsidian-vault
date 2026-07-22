# Sanitized Ride Ordering Chain Audit

## Executive finding

The indexed chain contains **two distinct projects**:

1. **Let’s Ride Backend** — the ride-ordering foundation initially created under the historical name/path `Cando-Backend`.
2. **LivelyCura Backend** — stock, sales, returns, COGS, payment rollback, and migration work that began later in the first record and dominated continuations #2–#4.

The chain title therefore becomes misleading after the initial scaffold.

### Canonical identity and repositories

| Project | Historical target | Current canonical target | Finding |
|---|---|---|---|
| **Let’s Ride Backend** | `/Users/acazumah/Documents/Kusantec/Cando-Backend` | `/Users/acazumah/Documents/Kusantec/letsride-backend` | The later explicit user correction establishes **Let’s Ride Backend** as canonical. The historical folder is absent; the renamed repository exists. |
| **LivelyCura Backend** | `/Users/acazumah/Documents/LivelyCura/livelycura-backend` | Same | Owns all stock/sales work after the chain changes subject. |

The current Let’s Ride repository still contains stale internal identifiers: `package.json` names the package `cando-backend`, and the README title remains “Cando Backend.” Those labels are superseded by the canonical project name.

---

## Scope, provenance, and de-duplication

- Source: read-only SQLite database  
  `/Users/acazumah/.hermes/profiles/coder/state.db`
- Logical locators: exact `sessions.id` and `messages.session_id`.
- Frozen cutoff: **2026-07-21 17:12:06 GMT**.
- All four records are `source='cli'`, non-subagent, unarchived rows.
- No post-cutoff messages exist.
- No standalone transcript files were inferred.
- Exact-match replay counts are lower bounds because compaction rewrote some context and tool identifiers.

| ID | Metadata and coverage | Replay control | Classification |
|---|---|---|---|
| `20260628_134341_c8f843` | 2026-06-28 14:17–23:06 UTC; cwd `/Users/acazumah/Documents`; title `Ride Ordering Backend Setup`; U/A/T 10/125/238 | Original record | **substantive** |
| `20260628_230635_e39d3a` | 2026-06-28 23:06–2026-06-29 00:01 UTC; cwd absent; title `#2`; U/A/T 15/125/216 | 180/356 rows and 9/15 user rows exactly match parent; additional semantic replay | **substantive**, not a whole-record duplicate |
| `20260629_000111_f4ffc6` | 2026-06-29 00:01–00:17 UTC; cwd absent; title `#3`; U/A/T 13/146/282 | 233/441 rows and 12/13 user rows exactly match parent; the nonmatching user row is compaction context | **substantive** because it performs unique implementation |
| `20260629_001748_68c46e` | Started 2026-06-29 00:17 UTC; last message 16:22 UTC; metadata ended 2026-07-21 by `ws_orphan_reap`; cwd `/Users/acazumah`; title `#4`; U/A/T 13/123/232 | 107/368 rows and 7/13 user rows exactly match parent; replay runs through the prior integration-test result | **substantive** because it completes migrations/tests and handles new corrections |

The late #4 `ended_at` is metadata cleanup, not evidence of three weeks of implementation.

---

## Per-record evidence

### 1. `20260628_134341_c8f843`

**Unique requests and corrections**

- Create only the foundation for a motorbike/tricycle ride-ordering backend.
- Use Node.js, TypeScript, Express, Apollo GraphQL, Mongoose/MongoDB, security/logging middleware, environment configuration, health checks, and scalable folders.
- Explicitly exclude users, drivers/riders, trips, bookings, payments, wallets, locations, notifications, administration, models, and all real business logic.
- Correct the first scaffold to include:
  - `src/main.ts` as the process entry point;
  - separate Express application creation;
  - GraphQL subscriptions;
  - central GraphQL error formatting;
  - startup orchestration in `app.ts`.
- Later switch to LivelyCura and correct sale-return design:
  - remove the duplicated `inventoryReliefItems` snapshot;
  - require `saleItemId` for returns;
  - restore inventory from original `SALE` movements;
  - preserve `SALE_RETURN.sourceItemId` as the `SaleReturnItem` ID.
- Final request begins the “one sale line per product” redesign, but does not complete within this ID.

**Reported outcomes**

- Let’s Ride foundation was created at the historical `Cando-Backend` path.
- Dependency installation, build, and typecheck were reported passing.
- The corrected architecture added subscription-server cleanup, `/subscriptions`, `formatGraphqlErrors`, `createExpressApp`, and `main.ts`.
- Runtime reached `main.ts → StartServer → connectDB` but failed because no local MongoDB listener was available.
- Express, GraphQL, health, and WebSocket endpoints were therefore **not successfully exercised against a connected database**.
- The LivelyCura return correction was reported implemented with:
  - build success;
  - three focused unit suites/14 tests plus one additional four-test suite;
  - three integration suites/25 tests.

**Current static reconciliation**

- Current Let’s Ride source retains the accepted composition:
  - `src/main.ts`;
  - `src/app.ts`;
  - `src/servers/createExpressApp.ts`;
  - `createGraphqlServer.ts`;
  - `createGraphqlSubscriptionServer.ts`;
  - `formatGraphqlErrors.ts`;
  - Mongo-before-listen startup;
  - HTTP and GraphQL health checks.
- Current source contains no ride models or ride/payment/logistics business modules.
- Historical `src/server.ts` compatibility export is now absent; `main.ts` and `app.ts` are authoritative.
- Current LivelyCura source retains movement-based return identity and restoration.

**Promotion**

- Let’s Ride architecture and deliberate business-logic exclusion: **promote/current**.
- Historical Cando naming: **historical/superseded**.
- Successful Let’s Ride runtime/database proof: **incomplete**.
- LivelyCura return rule: **promote/current as supporting provenance**, but already promoted from later stock/sales records.
- Final one-line-per-product request in this exact ID: **incomplete**.

**Confidence:** High.

---

### 2. `20260628_230635_e39d3a`

**Unique decisions after replay**

- `unitPrice` is product-level; the difficult value is batch-sensitive `unitCost`.
- Use exact `lineCost` for COGS.
- Run duplicate-sale-item merge before `lineCost` repair/backfill.
- Historical sales cannot be assumed to have inventory movements because movements were introduced later.
- Backfill hierarchy:
  1. original `SALE` movement cost;
  2. historical `SaleItem.unitCost × quantity`;
  3. zero when no defensible cost exists.
- Do not use current inventory cost by default because it may not represent sale-time cost.
- The user approved the final plan and requested implementation.

**Outcome boundary**

- The record produced the accepted architecture and migration plan.
- It compressed immediately after the implementation request.
- No implementation or verification is attributable to this exact ID; those begin in #3.

**Durable rules**

- `SaleItem` is the customer-facing product line.
- `InventoryMovement` is the batch/component stock ledger.
- One active line per `{saleId, productId}`.
- `lineCost` is exact accounting value; weighted `unitCost` is a summary.
- Manual batches, FEFO allocations, and bundle components may create multiple movements but not multiple sale lines.
- Returns remain `saleItemId`-based.
- Merge migrations must repoint movement and return references before soft-deleting duplicates.

**Promotion**

- Accepted design and rationale: **promote/current**, largely supporting rules already present in the canonical LivelyCura page.
- Exact-ID implementation: **incomplete**.

**Confidence:** High.

---

### 3. `20260629_000111_f4ffc6`

**Fresh request boundary**

- No independent human request survives after replay; the child executes the inherited `implement` instruction.
- The compaction summary is reference-only, not a new user directive.

**Unique implementation**

The child implemented the core LivelyCura redesign across:

- Sale item schema/interfaces/GraphQL;
- product-grouped sale formatting;
- generated sale-item IDs linked to movement deltas;
- exact `lineCost` calculation;
- COGS posting;
- returns and return-cost reversal;
- cancellation and payment-failure inventory rollback;
- generated GraphQL types and focused tests.

Important payment-safety outcome:

- Payment failure/cancellation rollback now derives stock reversal from original `SALE` movements rather than the deprecated `SaleItem.inventoryId` assumption.

**Historical verification**

- Initial build failed on an inventory/source-item type mismatch; the corrected build passed.
- Three focused unit suites passed with 13 tests.
- Integration attempts initially failed while tests still assumed inventory-level sale items.
- After fixture and lookup corrections, three integration suites passed with 25 tests.
- Jest still emitted a forced-exit/open-handle warning.
- The record ended without a final assistant summary.
- Its preserved task state still showed additional tests and migrations pending.

**Current static reconciliation**

Current LivelyCura source still confirms:

- active uniqueness on `{saleId, productId}`;
- `SaleItem.lineCost` required;
- new sale items written with `inventoryId: null`;
- grouping by product;
- inventory deltas carrying `sourceItemId`;
- exact COGS summation from `lineCost`;
- return identification through `saleItemId`.

**Promotion**

- Core code implementation: **promote/current**.
- Replay-only parent content: **reference-only**.
- Migration completion and database execution within this ID: **incomplete**.

**Confidence:** High.

---

### 4. `20260629_001748_68c46e`

**Replay boundary**

- The initial build/test sequence through the prior 25-test integration pass is replay from #3.
- The preserved task list is runtime context.
- Unique work starts when the child resumes remaining tests and migrations.

**Unique outcomes**

1. **Completed remaining feature work**
   - Added the duplicate-sale-item merge migration.
   - Added the `lineCost` backfill migration.
   - Registered both migrations.
   - Added/updated broader sale, return, invoice, accounting, cancellation, and payment rollback tests.
   - Reported build success, four unit suites/18 tests, and four integration suites/41 tests.

2. **Project structure correction**
   - User required types/interfaces to move out of `formatSaleItems.ts`.
   - Types moved into the project interfaces layer.
   - An initial missing-import build failure was corrected; build then passed.

3. **Mongoose transaction typing correction**
   - A compile failure exposed an ambiguous `Model.create` return type.
   - `upsertCustomer` gained an explicit document return type.
   - Transactional creation used array input/destructuring, and update used a guaranteed-document return.
   - Build passed afterward.

4. **Lint correction**
   - Removed an unused test import.
   - Lint and build passed.

5. **CI unit closure**
   - Updated stock-availability mocks and product-level movement expectations.
   - Restored a temporary backward-compatible `lineCost`/`unitCost × quantity` fallback to satisfy legacy fixtures.
   - Updated cancellation and customer-session expectations.
   - Focused five-suite/28-test run passed.
   - All four historical unit-test shards passed:
     - 90 suites/354 tests;
     - 90 suites/427 tests;
     - 90 suites/380 tests;
     - 89 suites/371 tests.
   - Final lint and build passed.

**Current static reconciliation**

- Types remain in the common interfaces layer.
- Current sale creation still uses product-level sale items and movement-level allocations.
- Current exact COGS code now sums required `lineCost` directly; the temporary fallback introduced here is **superseded**.
- Both migrations remain registered.
- Later current source contains dedicated migration integration coverage for reruns, reference repointing, movement-based backfill, zero-quantity behavior, and active uniqueness.
- Those migration tests were added later and must not be retroactively attributed to this exact record.
- Current tests use Vitest conventions; this chain’s verification used Jest.

**Promotion**

- Migrations, interfaces ownership, typing correction, and CI closure: **promote/current**.
- Temporary COGS fallback: **historical/superseded**.
- Replayed #3 implementation/test results: **reference-only**.
- Production database migration, deployment, and provider-runtime evidence: **incomplete**.

**Confidence:** High.

---

## Current architecture and implementation status

### Let’s Ride Backend

**Current static architecture**

- Node.js/TypeScript.
- Express 5 and Apollo Server 5.
- HTTP GraphQL endpoint plus `graphql-ws` subscription server.
- `main.ts` loads environment configuration and invokes `StartServer`.
- `app.ts` creates Express/HTTP, connects MongoDB, starts GraphQL, installs 404/error handling, then listens.
- Separate Express, GraphQL, subscription, and error-formatting factories.
- Mongoose connection is required before the server listens.
- Minimal HTTP and GraphQL health surfaces only.

**Status**

- Foundation is present.
- No domain models, services, authentication, payments, wallets, rides, bookings, drivers, riders, routing, pricing, location tracking, notifications, or administration exist.
- No current test files were found.
- No Dockerfile, Compose, workflow, or deployment configuration was found.
- Historical build/typecheck passed, but successful database-backed runtime was not demonstrated.
- Current package/README branding still needs reconciliation from Cando to Let’s Ride.

### LivelyCura stock/sales work

**Current static status**

- One active `SaleItem` per sale/product.
- Batch, FEFO, and bundle-component allocation remains in `InventoryMovement`.
- Inventory movements retain `sourceItemId` for returns and rollback.
- `lineCost` is required and is the exact COGS source.
- `unitCost` is a derived/snapshot summary.
- Returns use `saleItemId` and reverse original movement history.
- Duplicate merge and `lineCost` backfill migrations remain registered.
- Current migration tests cover reruns and reference integrity.

---

## Durable backend, payment, and logistics rules

1. **Separate commercial identity from stock identity.**  
   Sale lines are product-level; stock batches/components are movement-level.

2. **Use exact line cost for accounting.**  
   `lineCost` is authoritative for COGS. Weighted `unitCost` may round and must not reconstruct exact posting after migration.

3. **Preserve movement provenance.**  
   Original sale movements point to the sold `SaleItem`; return movements point to the new `SaleReturnItem`.

4. **Restore and roll back inventory from movement history.**  
   Returns, cancellation, and payment failure must not depend on one deprecated inventory field on the sale line.

5. **Keep manual, FEFO, and bundle allocations explicit.**  
   They may yield many movement rows linked to one product-level sale item. Mixed manual and automatic allocation for one product is rejected in current code.

6. **Migrate financial identity conservatively.**  
   Merge duplicate lines transactionally, repoint dependent references, soft-delete duplicates, backfill exact costs, then establish active uniqueness.

7. **Do not invent historical cost.**  
   Prefer sale movements; otherwise preserve the sale-time cost snapshot. Do not substitute current inventory cost by default.

8. **Transactional Mongoose helpers need explicit contracts.**  
   Use explicit document return types and transaction-safe creation patterns so array/document inference cannot leak into callers.

9. **Let’s Ride remains foundation-only.**  
   No payment or logistics rule should be inferred as implemented merely because the project is intended for ride ordering.

---

## Contradictions and unresolved evidence

- Canonical **Let’s Ride Backend** conflicts with stale current package/README “Cando” labels.
- The initial request named `server.ts` as startup; the accepted correction and current source use `main.ts` plus `app.ts`.
- The historical session claimed the only runtime blocker was MongoDB, but build success does not prove HTTP, GraphQL, subscriptions, or database behavior.
- Current Let’s Ride has no tests or deployment surface.
- LivelyCura migrations were created but were not run against a production database in this chain.
- No payment-provider call or end-to-end payment runtime was performed.
- No deployment occurred in any exact record.
- Historical Jest passes are not fresh proof of the current Vitest codebase.
- The historical compatibility fallback from `lineCost` to `unitCost × quantity` is no longer current COGS behavior.
- `SaleItem.inventoryId` remains nullable/indexed for compatibility even though it no longer defines line identity.
- Static current source cannot prove that deployed databases have completed the migrations or rebuilt indexes.

---

## Promotion and coverage targets

If promotion is later authorized:

1. Create one sanitized source summary for this exact four-record chain, explicitly separating Let’s Ride from LivelyCura.
2. Expand `wiki/projects/lets-ride-backend.md` with:
   - direct conversation provenance;
   - current repository;
   - foundation architecture;
   - deliberate absence of business logic;
   - MongoDB/runtime gap;
   - stale Cando branding contradiction.
3. Add the chain as supporting provenance to `wiki/projects/livelycura-backend.md`; do **not** duplicate stock/sales rules already promoted from later supplements.
4. Record #3 and #4’s exact implementation ownership without assigning their work to earlier IDs.
5. Advance the checkpoint only after authorized integration:
   - current: **33/130**;
   - these four independently classified non-subagent continuations: **+4**;
   - resulting checkpoint: **37/130 classified, 93 pending**.
6. Update `index.md` and append exactly one log entry.
7. No new cross-project operating-manual rule is required; the core stock/accounting/migration rules already exist there.

## Completion statement

- Exact IDs processed: **4/4**.
- Record-quality count: **4 substantive**, 0 whole-record duplicates, 0 interrupted, 0 unrelated, 0 process-control.
- Replayed prefixes were de-duplicated at every continuation.
- Verification level: historical command evidence plus current static source inspection; **no fresh builds, tests, services, databases, provider calls, or deployments**.
- Files created or modified: **none**.
- No secrets, credentials, full transcripts, private fixtures, or tool chatter are included.