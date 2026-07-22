## Sanitized Read-Only Evidence Report

### Session metadata

| Field | Evidence |
|---|---|
| Exact ID | `20260629_173939_b6748a` |
| Profile/store | Coder-profile store: `~/.hermes/profiles/coder/state.db`; `profile_name` column is null |
| Logical locator | `sessions.id = '20260629_173939_b6748a'`; `messages.session_id = '20260629_173939_b6748a'` |
| Date | 2026-06-29, `17:39:39.905Z`–`19:34:07.396Z` |
| Historical cwd | `NULL` |
| Indexed title | `Stock and Sales Review` |
| Source/state | TUI, primary session, unarchived, no parent |
| Stored messages | 310: 5 user, 103 assistant, 202 tool; all active, none compacted |
| Minimal safe quotation | None |

### Classification and project identity

- **Record quality:** `substantive`
- **Exact project family:** **LivelyCura**
- **Primary repository:** **LivelyCura Backend** — `~/Documents/LivelyCura/livelycura-backend`
- **Mobile consumer repository:** **SERLP Mobile** — `~/Documents/LivelyCura/serlp-mobile`
- **Not implicated:** the SERLP marketing website or unrelated LivelyCura applications.
- **Identity confidence:** **High.** The user explicitly named SERLP Mobile, later supplied exact LivelyCura Backend migration paths, and the session’s implementation and verification consistently targeted these two repositories. The generic title and missing cwd are therefore misleading routing metadata, not an identity gap.

### Promotion status

This is a substantive, mixed-status record:

- **`promote/current`**
  - Product-level `SaleItem` and movement-level batch relief.
  - Sale returns keyed by `saleItemId`.
  - Exact `lineCost` as the COGS source.
  - SERLP Mobile product stock flags and return-contract alignment.
  - Migration runner owns the database lifecycle; migrations use imported models rather than creating their own connections.
- **`historical/superseded`**
  - The exact session-era cursor-plus-explicit-batch-array implementation was later replaced by a streaming, per-group transactional merge.
  - The session-era “no `mongoose` import at all” implementation summary no longer describes current source.
- **`incomplete`**
  - The final request to add migration tests and make all relevant `lineCost` contracts required did not reach a reported completion or verification inside this exact ID. The record ends immediately after one successful interface patch.
  - Current code and later Git history contain the broader implementation and tests, but that is follow-up evidence, not completion evidence for this session.

### Durable corrections, decisions, and rationale

#### Explicit user corrections

1. **Migrations must not manage their own database connection.**
   - The application server and migration runner already establish the connection.
   - Migration scripts should import the domain models and operate through their collections.
   - Rationale: avoid lifecycle conflicts and production-only connection failures.

2. **Large production migrations must follow the repository’s established cursor-and-batching pattern.**
   - Merely setting a cursor `batchSize` was explicitly rejected.
   - The accepted session-era approach streamed duplicate groups, accumulated bounded batches, and flushed writes in dependency-safe order.
   - Rationale: avoid loading the full production dataset into memory.

3. **Migration write order must preserve references before deleting duplicates.**
   - Update the retained sale item, repoint inventory movements and return items, then soft-delete duplicates.

4. **Once legacy data is backfilled, `lineCost` should remain required.**
   - The user rejected making the field optional merely to accommodate pre-migration rows.
   - Migration behavior requires focused tests.

#### Session-reported domain decisions, confirmed by current source

- One active `SaleItem` represents one customer-facing product line per sale.
- Inventory batches and bundle-component relief remain represented by `InventoryMovement`.
- Sale returns identify the sold line with `saleItemId`, including non-stock lines with no inventory record.
- `SaleItem.lineCost` is the exact sale-time COGS amount; weighted `unitCost` is only a summary and can round.
- Stock behavior is represented by `isStockItem`, `isBundle`, `manufacturable`, `sellable`, and `purchasable`.
- SERLP Mobile enforces mutually compatible stock/bundle/manufacturing flag combinations.

### Historical verification reported by the session

The following are historical session results, not fresh verification:

- LivelyCura Backend build reported passing.
- Three focused backend unit suites reported **16/16 tests passing**.
- Two focused backend integration suites reported **17/17 tests passing**.
- SERLP Mobile TypeScript checking and scoped formatting reported passing.
- Backend builds were repeatedly reported passing after the migration corrections, including after model-collection conversion.
- **No migration-test result or final post-`lineCost` verification was reported after the last user request.**

No secret values, environment values, or full command payloads are reproduced here.

## Current-Code Reconciliation

Both repositories were inspected statically and read-only.

### LivelyCura Backend

- Branch: `feature/stock-behavior`
- HEAD: `02656a8fb0bd`
- Working tree: clean

Current evidence:

- `scripts/migrations/index.ts`
  - Registers the stock-behavior, duplicate-sale-item merge, `lineCost` backfill, and return-item cleanup migrations.
- `scripts/migrations/migrateProductStockBehaviorAndSaleItemIndex.ts`
  - Uses imported models and model collections.
  - Backfills product stock defaults and reconciles indexes without opening a connection.
- `scripts/migrations/migrateBackfillSaleItemLineCost.ts`
  - Streams sale items and derives exact `lineCost` from original SALE movements, with historical `unitCost` fallback.
- `scripts/migrations/migrateMergeDuplicateSaleItemsPerProduct.ts`
  - Streams duplicate groups.
  - Uses imported sale, return, and movement models.
  - Executes each group in a transaction, repoints references before soft deletion, preserves idempotence, and builds the active unique product-line index.
- `src/models/selling/saleItems/index.ts`
  - Declares `lineCost` required.
  - Declares one active `{saleId, productId}` line through a unique partial index.
- `src/common/interfaces/accounting/autoPosting.ts`
  - Requires `lineCost` for sale and return COGS contracts.
- `src/services/accounting/autoPosting/postSale/addCogsLines.ts`
  - Sums exact `lineCost`; it no longer derives COGS from optional unit-cost fallbacks.
- `tests/integration/migrations/saleItemMergeAndBackfill.test.ts`
  - Covers merge totals, rerun idempotence, reference repointing, movement-based backfill, zero-quantity handling, and active-index enforcement.

Git history contains the session-era migration correction commit and later follow-up commits that added and hardened migration tests. Commit containment corroborates lineage but is not runtime proof.

### SERLP Mobile

- Branch: `feature/stock-behavior`
- HEAD: `646c0b016627`
- Working tree: clean

Current evidence:

- `src/catalog/createProduct/hooks/useCreateProductForm.ts`
  - Sends `isStockItem` and `isBundle` from the selected stock behavior.
- `src/catalog/productDetails/hooks/useProductSettingsFlow.ts`
  - Reads and writes all relevant commerce/stock flags and enforces bundle, stock, and manufacturing compatibility.
- `src/catalog/products/hooks/useProductsQuery.ts`
  - Fetches stock and bundle flags.
- `src/selling/processReturn/hooks/useSaleReturnFlow.ts`
  - Keys quantities and return inputs by `SaleItem.id` and submits `saleItemId`.
- `src/selling/saleDetail/hooks/useSaleQuery.ts`
  - Fetches the sale-item IDs required by the return flow.
- `src/interfaces/graphql/graphql.ts`
  - Contains the current `CreateSaleReturnItemInput.saleItemId` contract and product stock fields.

The current branch contains the session-era mobile stock/return changes, although their commits were recorded after this exact session ended.

## Contradictions and Open Questions

1. **Batching implementation drift**
   - The user explicitly demanded cursor plus explicit batch accumulation/flush.
   - Current merge code streams the aggregate cursor but handles one duplicate group transactionally at a time; it no longer has the exact explicit batch-array/flush structure.
   - It avoids materializing all duplicate groups, but it still materializes the items for one group with `.toArray()`. Static inspection cannot establish the maximum production group size.

2. **Connection wording versus current transaction support**
   - Current migrations do not call `connect` or `disconnect` and use imported models, satisfying the core connection-ownership correction.
   - The merge migration now imports `mongoose` solely for `mongoose.connection.startSession()`. This contradicts the session assistant’s broader claim that all `mongoose` usage was removed, but not necessarily the user’s core prohibition against opening a connection inside a migration.

3. **Exact-session completion boundary**
   - A direct successor, `20260629_193407_346702` (`Stock and Sales Review #2`), starts when this record ends and names this session as its parent.
   - It was outside the frozen scope and was not audited. Any centralized promotion should process it next and de-duplicate its replayed context before assigning final completion provenance.

4. **Verification boundary**
   - Current test files exist and later commits are contained in HEAD, but no builds, tests, migrations, services, databases, or deployments were run during this audit.
   - The historical manual generated-type update is statically consistent with current source, but this audit did not regenerate GraphQL artifacts.

### Reusable rule

This record adds a useful migration rule not presently captured in the searched vault pages:

> Application-startup migrations must use the runner-owned connection and imported models, stream production-sized datasets with bounded work, preserve dependency-safe write order, backfill before tightening required contracts, and include focused idempotence and reference-integrity tests.

## Recommended Promotion Targets

When writes are authorized, promote through a grouped LivelyCura Hermes supplement rather than a transcript page:

1. `wiki/projects/livelycura-backend.md`
2. `wiki/projects/serlp-mobile.md`
3. A new grouped LivelyCura Hermes source summary and sanitized raw manifest
4. `wiki/syntheses/software-development-operating-manual.md` for the reusable migration rule
5. `wiki/syntheses/new-project-bootstrap-operating-manual.md` only if schema-evolution/migration foundations belong there
6. `wiki/syntheses/project-knowledge-harvest-status.md`
7. `index.md` and exactly one `log.md` entry during authorized centralized promotion

Do not update unrelated LivelyCura project pages from this record.

## Completion

- **Exact IDs processed:** 1 — `20260629_173939_b6748a`
- **Classification count:** 1 substantive
- **Verification:** historical reports plus static current-source/Git reconciliation only
- **Repositories inspected:** LivelyCura Backend and SERLP Mobile, read-only
- **Secrets/full transcripts included:** none
- **Files created or modified:** **none**
- **Issues encountered:** the exact record ends mid-follow-up and has an unaudited direct successor; current migration implementation has also evolved beyond the session-era batching structure.