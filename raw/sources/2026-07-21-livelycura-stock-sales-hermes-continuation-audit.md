# Sanitized Read-Only Evidence Report

## Record identity

| Field | Evidence |
|---|---|
| Exact ID | `20260629_193407_346702` |
| Logical store | Coder-profile SQLite store: `/Users/acazumah/.hermes/profiles/coder/state.db` |
| Row locator | `sessions.id = '20260629_193407_346702'`; `messages.session_id = '20260629_193407_346702'` |
| Parent | `20260629_173939_b6748a` — `Stock and Sales Review` |
| Date | 2026-06-29 19:34:07 UTC–2026-07-12 18:39:56 UTC |
| Historical cwd | `NULL` |
| Indexed title | `Stock and Sales Review #2` |
| Source/state | TUI primary session, unarchived, ended by context compression |
| Frozen cutoff | 2026-07-21 17:12:06 GMT; all record rows precede the cutoff |
| Minimal safe quotation | None |
| Record quality | **`substantive`** |
| Confidence | **High** for transcript attribution and current static source; **medium-high** for mobile runtime behavior because no device rebuild/runtime check was reported |

## Replay de-duplication

The child is not a duplicate, but it begins with a large replay of its parent.

- Exact parent content is replayed through child message `7861`, including:
  - the original stock/sales review request;
  - all user corrections about connection ownership, batching, imported models, and required `lineCost`;
  - the parent’s implementation/tool history through its abrupt endpoint.
- The compaction payload is reference-only.
- Independent child evidence begins after that replay boundary.
- Therefore, the parent’s stock behavior, sale-item identity, return identity, exact COGS, and migration corrections are **not reattributed** to this child.

Unique child requests/corrections were:

1. A reported full backend test run exposed two stale fixtures after `lineCost` became required.
2. SERLP Mobile crashed because `ExpoInAppUpdates` was unavailable.
3. The user rejected the first custom lazy-loader workaround and required alignment with existing LivelyCura apps.
4. A production sale-return failure exposed a stale unique inventory index; the user requested a plan and then approved implementation.

## Unique durable evidence and status

### 1. Parent follow-up closure: migration tests and required exact `lineCost`

**Unique child outcome**

- Completed the parent’s pending migration-test and required-`lineCost` follow-up.
- Added focused stock/sale migration tests using imported model collections.
- Tightened sale and return accounting contracts so `lineCost` is required.
- Removed runtime accounting fallbacks that reconstructed COGS from `unitCost × quantity`.
- Updated remaining service call sites and fixtures to carry exact `lineCost`.
- After the user’s broader test run exposed two old fixtures, those fixtures were corrected—including explicit zero-cost cases—and the full historical test command passed.

**Promotion status:** **`promote/current`**, primarily as completion provenance for claims already promoted from the parent.

**Current static reconciliation**

Current LivelyCura Backend retains:

- `tests/unit/scripts/migrations/stockSaleItemMigrations.test.ts`;
- required exact `lineCost` contracts and posting behavior;
- runner-owned migration connection lifecycle;
- model-collection migration access;
- later transactional evolution of the duplicate-sale-item merge.

The current test suite uses Vitest conventions, while the historical session ran Jest. The behavior and coverage remain, but the exact runner/tooling is superseded.

### 2. SERLP Mobile native update-check correction

**Unique child correction and outcome**

- The initial custom helper that silently loaded the optional native module was explicitly rejected.
- The accepted implementation followed the existing Courier Mobile pattern:
  - no static `expo-in-app-updates` import;
  - production-only, non-web execution;
  - dynamic import inside the effect;
  - the update module is passed into the checker;
  - failures do not block application startup.
- The session reported formatting and TypeScript checks passing.

**Promotion status:** **`promote/current`** for the final family-reference pattern; **`historical/superseded`** for the rejected custom loader.

**Current static reconciliation**

`serlp-mobile/src/navigation/hooks/useOpenStoreAppUpdate.ts` still matches the corrected structure on:

- branch `feature/stock-behavior`;
- HEAD `646c0b016627`;
- clean working tree.

This confirms source presence, not device/runtime success. The session did not report rebuilding a native client or reproducing the launch flow on iOS/Android.

### 3. Sale-return identity cleanup

**Unique child diagnosis**

The sale-return transition from inventory-level to sale-item-level identity was incomplete:

- creation used `saleItemId`;
- the database/model still retained inventory-based fields and uniqueness;
- multiple product-level return rows therefore collided when the obsolete inventory key was null;
- Pharmacy Portal still carried inventory-era return state and batch/expiry presentation.

**Unique child implementation**

The child:

- removed `inventoryId` from active `SaleReturnItem` interfaces, model, builder output, and indexes;
- registered a runner-owned migration using `SaleReturnItemModel.collection`;
- made the migration:
  - drop inventory-based indexes;
  - unset historical inventory IDs;
  - detect conflicting active `{saleReturnId, saleItemId}` rows;
  - refuse to silently merge duplicate financial rows;
  - create an active partial unique `{saleReturnId, saleItemId}` index;
  - support safe reruns;
- added builder, migration, service, and multi-product integration coverage;
- removed inventory IDs from Pharmacy Portal return form state and mutation payloads;
- removed inventory queries and misleading single-batch/expiry columns from return details.

**Promotion status:** **`promote/current`** for the database/model/service/client cleanup.

**Current static reconciliation**

Current backend source confirms the implementation:

- `scripts/migrations/migrateRemoveSaleReturnItemInventory.ts`
- `scripts/migrations/index.ts`
- `src/common/interfaces/selling/saleReturnItems.ts`
- `src/models/selling/saleReturnItems/index.ts`
- `src/services/selling/saleReturns/createSaleReturn/buildSaleReturnItems.ts`
- `tests/unit/scripts/migrations/migrateRemoveSaleReturnItemInventory.test.ts`
- `tests/integration/selling/saleReturnWorkflow.test.ts`

Current Pharmacy Portal confirms that sale returns submit `saleItemId + quantity` and no longer query/display a single inventory batch:

- `src/selling/saleDetail/hooks/useProcessReturnForm.ts`
- `src/selling/saleDetail/components/ProcessReturnModal.tsx`
- `src/selling/saleReturnDetail/hooks/useSaleReturnQuery.ts`
- `src/selling/saleReturnDetail/components/SaleReturnProductsSection.tsx`

Backend and Pharmacy Portal are both clean on `feature/stock-behavior`, at `02656a8fb0bd` and `2a5e51d605a7` respectively.

### 4. GraphQL compatibility strategy

The child planned and partially implemented a staged compatibility bridge:

- retain `SaleReturnItem.inventory` temporarily;
- deprecate it;
- return null;
- remove it after clients stopped querying it.

Current backend source has removed the field and resolver entirely.

**Promotion status:** **`historical/superseded`** for the temporary bridge; the durable rule is staged client/server contract cleanup, not permanent retention of a null field.

## Historical verification boundary

The following are session-reported historical results, not fresh verification:

### Migration/accounting closure

- Backend build passed.
- Eight focused suites reported **39 tests passing**.
- After the user’s broader test run revealed stale fixtures:
  - two focused suites reported **8 tests passing**;
  - the full historical backend test command reported **18 suites and 172 tests passing**.

### SERLP Mobile

- Scoped formatting passed.
- TypeScript checking passed.
- No fresh native build, simulator/device launch, or store-update execution was reported.

### Sale-return cleanup

- Pharmacy Portal type-check and production build passed.
- Backend dependency state initially blocked verification; lockfile dependencies were restored.
- Three focused backend unit suites reported **9 tests passing**.
- Backend build passed.
- The sale-return integration workflow reported **1 suite and 20 tests passing**, including the multi-product inventory-free return case.
- Jest emitted a force-exit/open-handle warning after that passing integration run.
- The record compressed before a full backend suite or final completion summary was recorded.

Current source and later commits corroborate present implementation, but they do not retroactively complete the child’s missing final full-suite verification.

## Reusable rules

1. **Exact-cost accounting fixtures:** Once exact `lineCost` is required, every cost-bearing test fixture must provide it; zero-cost cases should state `lineCost: 0` explicitly. Tests must not preserve deprecated `unitCost × quantity` reconstruction.
2. **Identity-transition migrations:** When a financial line changes identity, update the model, persisted fields, indexes, API, generated contracts, clients, and UI together. Remove stale indexes/data idempotently, detect conflicts before establishing replacement uniqueness, and never silently merge conflicting financial rows.
3. **Movement-versus-line presentation:** A product-level return line must not expose one arbitrary batch or expiry when restoration can span multiple inventory movements.
4. **Optional native modules:** Avoid startup-time static imports when a native module may be absent. Follow the project-family reference pattern, gate by platform/build variant, and ensure ancillary update checks cannot block startup. Static/type checks do not replace a rebuilt-client runtime test.
5. **Existing migration rule supported, not duplicated:** Migrations use the runner-owned connection and imported models, backfill before tightening contracts, preserve reference order and rerun safety, and require focused integrity tests.

## Contradictions and open questions

- The accepted temporary GraphQL compatibility field is absent from current source; it was superseded.
- The exact child ended with uncommitted changes and no final summary. Relevant commits were recorded after the child endpoint, so commit containment is current/later evidence.
- Current migration tests use Vitest and transaction-session mocking; historical verification used Jest.
- `migrateRemoveSaleReturnItemInventory` throws when duplicate financial rows exist, but the generic current migration runner catches and logs migration failures without rethrowing. The migration remains unapplied, but whether application startup should fail closed is unresolved.
- Current static source cannot prove that the production stale index was actually removed in every deployed database.
- SERLP Mobile’s source-level crash prevention remains unverified on a rebuilt native client.

## Exact next continuation

The direct successor is:

| Field | Evidence |
|---|---|
| ID | `20260712_183956_816de0` |
| Title | `Stock and Sales Review #3` |
| Parent | `20260629_193407_346702` |
| Start | 2026-07-12 18:39:56 UTC—exactly when this child compressed |
| End | 2026-07-14 13:45:27 UTC |
| Historical cwd | `NULL` |
| Source/state | TUI primary session, unarchived |

Its body was not audited. It should be processed next, de-duplicating any replay of this child, to determine final full-suite, commit, and compatibility-removal attribution.

## Recommended promotion targets

When writes are authorized:

1. Add a new sanitized continuation manifest and grouped source summary rather than modifying the immutable parent raw report.
2. Update `wiki/sources/livelycura-stock-sales-hermes-supplement-1.md` to resolve its pending-continuation note.
3. Update:
   - `wiki/projects/livelycura-backend.md`
   - `wiki/projects/serlp-mobile.md`
   - `wiki/projects/livelycura-pharmacy-portal.md`
4. Promote only the identity-transition and optional-native-module rules to:
   - `wiki/syntheses/software-development-operating-manual.md`
   - `wiki/syntheses/new-project-bootstrap-operating-manual.md`, if considered bootstrap-level.
5. Advance `wiki/syntheses/project-knowledge-harvest-status.md` from **27/130 to 28/130** after centralized promotion; keep `20260712_183956_816de0` pending.
6. Update `index.md` and append exactly one `log.md` entry.

## Completion

- **Exact IDs processed:** 1 — `20260629_193407_346702`
- **Classification:** 1 substantive, with current, superseded, and incomplete-verification components
- **Repositories inspected:** LivelyCura Backend, SERLP Mobile, and LivelyCura Pharmacy Portal, statically/read-only
- **Verification:** historical command evidence plus current static source/Git reconciliation; no fresh project build, test, migration, database, service, deployment, or native runtime execution
- **Files created or modified:** **none**
- **Secrets/full transcripts/tool chatter included:** **none**
- **Primary issue:** the record compresses before final full-suite reporting and hands directly to unaudited continuation `20260712_183956_816de0`.