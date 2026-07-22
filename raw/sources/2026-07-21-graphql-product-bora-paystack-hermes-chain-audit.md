# Sanitized audit — GraphQL Product Nullable Field Error chain

## Scope and provenance

- **Exact records:** `20260627_113946_8a0b7e`, `20260627_153636_3d38e3`
- **Source:** `/Users/acazumah/.hermes/profiles/coder/state.db`, read-only
- **Logical locators:** `sessions.id` / `messages.session_id`
- **Frozen cutoff:** 2026-07-21 17:12:06 GMT
- **Post-cutoff rows:** none for either record
- **Full transcripts, secrets, environment values, account details, private payloads, screenshots, and tool chatter:** excluded
- **Files/repositories/databases modified:** none

## Metadata and classification

| ID | Metadata | Actual scope | Record quality | Promotion status | Coverage |
|---|---|---|---|---|---|
| `20260627_113946_8a0b7e` | Started 2026-06-27 11:51:22.780 UTC; ended 15:36:36.765; `cli`; cwd `/Users/acazumah/Documents`; title `GraphQL Product Nullable Field Error`; active; end reason `compression`; 10 user / 123 assistant / 199 tool rows | LivelyCura Backend, LivelyCura Pharmacy Portal, then Bora Capital Backend | **substantive**, multi-project | Mixed: `promote/current`, `historical/superseded`, and one component `incomplete` | Eligible **+1** |
| `20260627_153636_3d38e3` | Started 2026-06-27 15:36:36.766 UTC; last substantive row 19:23:15.530; session later reaped 2026-06-29; `cli`; parent is first ID; null cwd; title `#2`; active; end reason `ws_orphan_reap`; 11 user / 168 assistant / 229 tool rows | Unique work targets Bora Capital Backend; LivelyCura content is replay only | **substantive continuation**, not a whole-record duplicate | Mixed: `promote/current`, `historical/superseded`, and provider execution `incomplete` | Eligible **+1** |

**Classification totals:** 2 substantive; 0 whole-record duplicates; 0 interrupted; 0 unrelated; 0 process-control.

## Replay de-duplication

The child’s first **145 rows**, through message `5483`, are replay/compaction context:

- **131 exact parent-signature matches:** 55 assistant, 71 tool, 5 user.
- The remaining 14 prefix rows are compaction or rewritten replay forms.
- Only the subsequent **263-row child segment** and child-attributable completion of the parent’s last request were assessed as new evidence.
- The replayed GraphQL, sidebar, and initial Paystack work is **duplicate/reference-only in the child** and must not be promoted twice.

---

## Record 1 — `20260627_113946_8a0b7e`

### Actual repositories

1. `/Users/acazumah/Documents/LivelyCura/livelycura-backend`
2. `/Users/acazumah/Documents/LivelyCura/livelycura-pharmacy-portal`
3. `/Users/acazumah/Documents/Kusantec/bora-capital-backend`

The title describes only the first task. The record later switched to the Pharmacy Portal and then Bora Capital.

### User requests and corrections

- Repair a GraphQL failure caused by a legacy Product whose `isStockItem` did not satisfy the non-null schema contract.
- **Explicit correction:** repair legacy Product data through the migration; do **not** introduce field-level GraphQL fallback resolvers.
- Remove duplicated Manufacturing navigation in the Pharmacy Portal.
- Add Bora Paystack tooling to create and configure one subaccount per portfolio.
- **Financial correction:** every portfolio must have separate settlement details; shared settlement accounts defeat the design.
- Final request before compression: persist settlement bank/account details and simplify the over-engineered strategy/guard logic.

### Outcomes and historical verification

#### LivelyCura Backend — `promote/current`

- The agent initially added fallback Product field resolvers, but the user rejected that mechanism.
- The fallback resolvers and their new fallback tests were removed.
- The accepted implementation retained:
  - migration matching explicit null and missing `isStockItem`/`isBundle`;
  - create defaults `manufacturable=false`, `isStockItem=true`, `isBundle=false`;
  - update behavior preventing nullable inputs from rewriting those fields to null.
- A transient edit caused a resolver test failure; the session repaired it before completion.
- The session reported:
  - 3 focused suites / 7 tests passing after the correction;
  - TypeScript build passing.

#### LivelyCura Pharmacy Portal — `promote/current`

- Duplicate Manufacturing, Marketplace, and Courier registrations were removed from the menu registry.
- A regression test asserts unique top-level sidebar labels.
- The session reported one focused test file with 9 tests passing and type-check passing.

#### Bora Capital Backend — mixed

- Added Paystack helper/setup scripts and bulk portfolio provisioning logic.
- Existing payment initialization was confirmed to resolve configuration by portfolio and send the configured subaccount to Paystack.
- Bulk setup queried BCL portfolios and attempted to create one Paystack subaccount/configuration per portfolio.
- The session reported repeated builds and the focused six-test deposit suite passing.
- A read-only bank-list provider call succeeded; actual subaccount provisioning was not successfully completed in this parent.
- Generated dummy settlement details and shared/file strategy variants were intermediate designs later superseded in the child.
- The parent’s final schema/simplification request was **incomplete here** and completed only in the child.

### Current static reconciliation

#### LivelyCura Backend

Current branch pointer: `feature/stock-behavior` at `02656a8fb0bd740e970f00c6a30a0e77fb157f79`.

Current source supports the accepted correction:

- `src/graphql/catalog/products/typeDefs.ts` keeps `manufacturable`, `isStockItem`, and `isBundle` non-null on Product output.
- `src/graphql/catalog/products/resolvers.ts` has no fallback resolvers for those booleans.
- `src/models/catalog/products/index.ts` defines required defaults.
- `src/services/catalog/products/createProduct.ts` and `updateProduct.ts` normalize stock-behavior values.
- `scripts/migrations/migrateProductStockBehaviorAndSaleItemIndex.ts` backfills null/missing stock/bundle fields.
- The migration is registered as `MIGRATE_PRODUCT_STOCK_BEHAVIOR_AND_SALE_ITEM_INDEX_V2`.
- `tests/unit/scripts/migrations/stockSaleItemMigrations.test.ts` statically covers the backfill.

Current runner tension: LivelyCura’s migration runner catches failures without rethrowing, so a failed backfill can remain unapplied while startup continues.

#### Pharmacy Portal

Current branch pointer: `feature/stock-behavior` at `2a5e51d605a75b33d507174cbcdf2a9282aef03a`.

- `src/layouts/main/constants/menuItems/index.ts` contains each affected menu once.
- `src/layouts/main/hooks/useFilteredMenuItems.test.tsx` retains the uniqueness regression.

### Reusable-rule assessment

- **Supports an existing cross-project rule; do not duplicate it:** backfill persisted data before relying on a tightened/non-null contract, and do not mask invalid stored state with GraphQL fallbacks when migration is the selected correction.
- Adds project-specific evidence that menu registries must not emit duplicate top-level navigation entries.
- Reinforces the already-promoted financial-separation rule.

**Confidence:** high for historical intent/outcomes and current static ownership; no fresh runtime verification.

---

## Record 2 — `20260627_153636_3d38e3`

### Actual repository

- `/Users/acazumah/Documents/Kusantec/bora-capital-backend`

Current branch pointer: `feature/updates` at `49fe85765b8cbf893a0e9c845412876a5887530a`.

### Unique requests and corrections

- Complete the parent’s pending request by storing settlement bank code and account number in portfolio payment configuration and simplifying bulk setup.
- **Explicit decision:** use the migration registry’s one-time record rather than leave setup as only a manual script.
- After Paystack rejected generated account numbers, the user asked for a testable approach.
- The agent introduced local fake subaccount identifiers and then a payment-initialization bypass.
- **Explicit final correction:** fake/local subaccount behavior is unacceptable because the same code ships to production; restore real Paystack subaccounts and accept settlement accounts through an environment array.
- Communication correction: do not automatically agree with the user; state plainly when the user is technically wrong.

### Outcomes and historical verification

#### Current/promotable components

- Added `settlementBankCode` and `settlementAccountNumber` to the Mongoose schema and TypeScript interface.
- Added and registered one-shot migration `CREATE_PAYSTACK_PORTFOLIO_SUBACCOUNTS_V1`.
- Bulk creation now consumes a settlement-account array and persists the real provider subaccount code plus settlement metadata.
- Payment initialization was restored to always send a real Paystack subaccount with `bearer: 'subaccount'`.
- Final session verification reported:
  - TypeScript build passing;
  - focused deposit suite: 1 suite / 6 tests passing;
  - dry-run mapping completing;
  - no fake-subaccount logic remaining.

#### Superseded components

- Generated random settlement accounts.
- Shared/file/account-number strategy machinery.
- Local `ACCT_TEST_…` markers.
- Omitting subaccount data during staging payment initialization.
- Optional Paystack initialization input fields.

#### Incomplete component

Actual Paystack-backed provisioning did **not** succeed in the exact record. The provider rejected invalid settlement details, and the final verification used a dry run plus unit/build checks. No successful real subaccount creation, migration execution, redeploy, or payment initialization was established.

### Current static reconciliation

Current source confirms:

- `src/models/portfolioPaymentConfig/index.ts` and its interface contain settlement bank/account fields.
- `scripts/paystack/createPortfolioSubaccounts.ts` requires settlement-account numbers and creates only real provider subaccounts.
- `scripts/migrations/createPaystackPortfolioSubaccounts_V1.ts` requires bank code and settlement-account array and fails if any portfolio setup fails.
- `scripts/migrations/index.ts` registers the V1 migration and records it only after success.
- `src/services/transactions/payment/initializeDepositPayment.ts` always sends the real configured subaccount.
- Payment interfaces require `subaccount`.
- No fake-subaccount marker logic remains.

### Current contradictions and gaps

1. **Distinct settlement accounts are not enforced.**  
   The explicit business invariant is one separate settlement account per portfolio, but current code only checks array length. It does not reject duplicate account numbers, and the model has no uniqueness constraint on `settlementAccountNumber`.

2. **Order-based mapping is fragile.**  
   Settlement accounts are assigned by BCL portfolio result order. A changed or unstable ordering could associate a valid account with the wrong portfolio.

3. **“One-shot” is conditional on full success.**  
   The migration record prevents reruns only after success. Partial external side effects can occur before failure and retry. Existing local configurations are skipped, but there is no demonstrated provider-level idempotency for a subaccount created before a local write failed.

4. **Startup/provider side-effect boundary remains risky.**  
   The migration invokes BCL and Paystack during application startup. `src/app.ts` starts `runMigrations()` without awaiting it, although the current Bora runner now rethrows failures.

5. **Documented manual commands are orphaned.**  
   `scripts/paystack/README.md` documents `yarn paystack:*` commands, but current `package.json` contains no Paystack script aliases.

6. **Claimed cleanup migration is absent.**  
   The child’s final answer reported a V2 cleanup migration for possible fake configurations. Current source contains neither that file nor its registration. Because fake logic is also absent, this may be intentionally superseded, but whether any environment ever persisted fake configurations is unresolved.

7. **Sensitive-output exposure risk.**  
   Current setup/migration result structures include settlement account details, and the migration serializes full failure results to logs. This should be reconciled with the project rule not to expose sensitive financial data.

8. **No focused current migration tests found.**  
   The existing deposit unit test covers routing with a configured subaccount, not array uniqueness, portfolio/account association, partial provider failure, rerun behavior, or startup migration execution.

### Reusable-rule assessment

- The record strongly supports the existing rule that each portfolio’s funds must remain separated through a real provider subaccount and dedicated settlement details.
- New reusable caution: a migration registry gives **once-after-success**, not provider-level exactly-once behavior; external side effects require explicit idempotency and partial-failure handling.
- The communication correction belongs in the personal operating manual: disagree directly when warranted rather than reflexively affirming.

**Confidence:** high for transcript decisions and present static code; medium for operational safety because provider/runtime execution was not completed.

---

## Promotion targets

If centrally integrated:

1. One sanitized raw evidence report and one coherent source summary for this chain.
2. `wiki/projects/livelycura-backend.md`
   - Product non-null/backfill decision, no-resolver correction, current migration/test targets, and failure-swallowing tension.
3. `wiki/projects/livelycura-pharmacy-portal.md`
   - Unique top-level menu registration and regression evidence.
4. `wiki/projects/bora-capital-backend.md`
   - Settlement metadata, real-subaccount migration, provider verification boundary, and all current gaps above.
5. `wiki/syntheses/software-development-operating-manual.md`
   - Add provenance only for already-present backfill and financial-separation rules; avoid duplicate wording.
   - Consider adding the external-side-effect migration caution.
6. `wiki/syntheses/personal-operating-manual.md`
   - Preserve the correction to state technical disagreement plainly.
7. Checkpoint, index, and one log entry after authorized promotion.

## Coverage and successor

- Canonical checkpoint remains **29/130** because this audit was read-only.
- Both IDs are unique primary non-subagent records with independent classified evidence.
- After authorized promotion/checkpointing: **31/130 classified, 99 pending**.
- Replayed child prefix contributes **zero additional coverage** beyond the child record itself.
- **Direct successor of `20260627_153636_3d38e3`: none.**
- The next chronological primary record starts a separate Ride Ordering Backend chain and is not a successor or part of this audit.