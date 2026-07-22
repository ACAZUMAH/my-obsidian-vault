# Kusantec/Bora Hermes Conversation Harvest — Supplement 1

Source: sanitized read-only evidence report produced from coder/default Hermes SQLite stores and current static repository reconciliation on 2026-07-21. Full transcripts, tool chatter, secrets, credential values, and private identifiers are excluded.

# Sanitized Bora Capital Hermes Evidence Report

## Outcome

- Audited all **7 requested sessions** directly from the two Hermes SQLite databases in read-only mode.
- Classification: **6 substantive**, **1 interrupted**.
- Reconciled the evidence against the current Bora Capital backend repository without running builds, tests, migrations, or external services.
- No secrets, credential values, private identifiers, full transcripts, or unrelated tool output are reproduced.

### Read-only sources

- Coder: `/Users/acazumah/.hermes/profiles/coder/state.db`
- Default: `/Users/acazumah/.hermes/state.db`
- Current repository: `/Users/acazumah/Documents/Kusantec/bora-capital-backend`
- Vault: `/Users/acazumah/Documents/Work Space`

Timestamps below are local machine time. Default-profile sessions are untitled in database metadata.

---

## Per-Session Evidence

### 1. `20260713_173225_73e447` — interrupted duplicate precursor

- **Profile:** coder
- **Date:** 2026-07-13 17:32; ended 2026-07-18 02:27 by compression
- **Historical cwd:** `/Users/acazumah/Documents/Kusantec/bora-capital-backend`
- **Indexed title:** `Partner Mobile App Setup #2`
- **Parent:** `20260630_230125_403524`
- **Record quality:** `interrupted`
- **Promotion:** `incomplete`
- **Confidence:** high
- **Minimal quotation:** none
- **Direct evidence:** Message `15283` requests a production-fintech security investigation and remediation plan. Message `15299` records only `Operation interrupted`.
- **Overlap:** The same request was completed two minutes later in default session `20260713_191745_a48077`; this record adds no independent Bora outcome.
- **Exclusions:** Earlier inherited Altin Partner Mobile work and a later detached test-process notification are unrelated to Bora evidence.
- **Reusable rule:** none from this record.

### 2. `20260713_191745_a48077` — security audit and plan

- **Profile:** default
- **Date:** 2026-07-13 19:17–19:44
- **Historical cwd / target:** Bora Capital backend
- **Indexed title:** none
- **Record quality:** `substantive`
- **Promotion:** `historical/superseded`
- **Confidence:** high for the historical audit; medium for any present-risk statement
- **Direct evidence:** User request at message `95`; final audit at message `837`.
- **Durable evidence:**
  - Production fintech security required investigation across authorization, authentication, secrets, dependencies, CI/CD, infrastructure, monitoring, and incident response.
  - The session identified account/wallet/auto-top-up ownership gaps, authentication weaknesses, fail-open authorization, logging exposure, dependency debt, and potentially exposed historical configuration.
  - It recommended containment before broad remediation and prioritized authorization before authentication/session and infrastructure work.
- **Transcript-reported outcome:**
  - Created `.hermes/plans/2026-07-13_193619-fintech-backend-security-hardening.md`.
  - Reported **17 suites / 102 tests passing**.
  - Reported no application-source changes.
- **Current-code reconciliation:**
  - The plan remains in `HEAD` history but is currently deleted in the dirty working tree.
  - Many identified authorization findings were subsequently repaired, so the session’s “high risk” conclusion is a historical snapshot, not a current assessment.
- **Reusable rule:** security remediation should be risk-ranked, evidence-backed, and staged from containment through release verification.

### 3. `20260713_194431_64df24` — cash transaction authorization

- **Profile:** default
- **Date:** 2026-07-13 19:44–20:53
- **Parent:** `20260713_191745_a48077`
- **Record quality:** `substantive`
- **Promotion:** `promote/current`
- **Confidence:** high
- **Direct correction:** Message `936` directs the agent to:
  - leave migrations and cron placement unchanged;
  - address one issue at a time so each fix can be reviewed.
- **Transcript-reported outcome:** Message `1015` reports Fix 1 complete:
  - deposits and withdrawals bound to the authenticated user;
  - investment-account ownership checked before BCL calls;
  - withdrawal identity sourced from the authenticated user rather than caller input.
- **Historical verification:** build passed; **18 suites / 105 tests**, 3 focused security tests, Prettier, and `git diff --check` passed.
- **Current-code evidence:**
  - `src/graphql/transactions/resolvers.ts`
  - `src/services/transactions/bcl-transactions/transfer.ts`
  - `src/services/transactions/bcl-transactions/withdraw.ts`
  - `tests/unit/services/transactions/cashAuthorization.spec.ts`
- **Reusable rule:** bind financial operations to authenticated identity and owned accounts before any provider request; ignore caller-supplied identity fields.

### 4. `20260713_205301_72152d` — statements and wallet-by-ID authorization

- **Profile:** default
- **Date:** 2026-07-13 20:53–21:35
- **Parent:** `20260713_194431_64df24`
- **Record quality:** `substantive`
- **Promotion:** `promote/current`
- **Confidence:** high
- **Transcript-reported outcomes:**
  - **Fix 2**, message `1186`: both mini and date-range statements now reject unowned accounts before contacting BCL.
  - **Fix 3**, message `1245`: wallet lookup now uses wallet ID plus authenticated owner ID and returns a non-enumerating not-found result.
- **Historical verification:**
  - Fix 2: build, Prettier, and diff check passed; **19 suites / 107 tests**.
  - Fix 3: build, Prettier, and diff check passed; **20 suites / 109 tests**.
- **Current-code evidence:**
  - `src/services/transactions/bcl-transactions/getTransactions.ts`
  - `src/services/transactions/bcl-transactions/getTransactionsWithRanges.ts`
  - `tests/unit/services/transactions/statementAuthorization.spec.ts`
  - `src/graphql/wallet/resolvers.ts`
  - `src/services/wallets/getWalletById.ts`
  - `tests/unit/graphql/walletAuthorization.spec.ts`
- **Reusable rule:** provider-backed reads require the same authenticated ownership validation as financial writes; use owner-scoped queries that avoid object-existence disclosure.

### 5. `20260713_213541_c58421` — wallet list and creation authorization

- **Profile:** default
- **Date:** 2026-07-13 21:35–2026-07-14 00:47
- **Parent:** `20260713_205301_72152d`
- **Record quality:** `substantive`
- **Promotion:** `promote/current`
- **Confidence:** high
- **Transcript-reported outcomes:**
  - **Fix 4**, message `1472`: wallet lists overwrite client-selected `userId` with authenticated identity while preserving other filters.
  - **Fix 5**, message `1498`: wallet creation similarly overwrites client-selected identity.
- **Historical verification:**
  - Fix 4: build, Prettier, and diff check passed; **20 suites / 110 tests**.
  - Fix 5: build, Prettier, and diff check passed; **20 suites / 111 tests**.
- **Current-code evidence:**
  - `src/graphql/wallet/resolvers.ts` applies `principal.userId` after caller input for list and create operations.
  - `tests/unit/graphql/walletAuthorization.spec.ts` covers lookup, list, creation, update, and deletion identity binding.
- **Open tail:** Message `1499` requests the next fix, but no further result belongs to this exact session.
- **Reusable rule:** when retaining a compatibility input shape, apply canonical principal identity after spreading caller-controlled data so it cannot be overridden.

### 6. `20260714_133535_83849e` — auto-top-up authorization and execution correction

- **Profile:** coder
- **Date:** 2026-07-14 13:35–18:35
- **Historical cwd / target:** Bora Capital backend
- **Indexed title:** `Why the Hermes Chat Disappeared`
- **Record quality:** `substantive`
- **Promotion:** `promote/current`
- **Confidence:** high for Fixes 13–15; medium-high for the broad final ID-normalization rule
- **User corrections:**
  - Message `15378`: asking whether work can continue does not authorize editing. The agent reported reverting its premature test and waiting for explicit `next`.
  - Message `15562`: incoming IDs should first resolve their documents; downstream queries/writes should then use the fetched documents’ canonical IDs.
- **Transcript-reported outcomes:**
  - Message `15411`: Fix 13, owner-scoped `getAutoTopUp`; **23 suites / 121 tests**.
  - Message `15498`: Fix 14, owner-scoped `pauseAutoTopUp`; **23 suites / 124 tests**.
  - Message `15561`: Fix 15, owner-scoped `resumeAutoTopUp`; **23 suites / 127 tests**.
  - Each reported focused authorization tests, build, scoped Prettier, and diff check passing.
- **Current-code evidence:**
  - `src/graphql/goals/autoTopUp/resolvers.ts`
  - `src/services/goals/autoTopUps/getAutoTopUpById.ts`
  - `pauseAutoTopUp.ts`, `resumeAutoTopUp.ts`, `cancelAutoTopUp.ts`
  - `tests/unit/graphql/autoTopUpAuthorization.spec.ts`
  - Current transition services fetch the user and owner-scoped auto-top-up, then pass the fetched auto-top-up `_id` downstream.
- **Current-code tension:** `getAutoTopUpById` still supports an internal ownerless `findById` path when no `userId` is supplied. Public GraphQL paths are scoped, but the helper is not universally fail-closed.
- **Reusable rules:**
  - A question is not authorization to edit.
  - Resolve externally supplied IDs and use canonical document identity for downstream mutations.

### 7. `20260720_193333_054b33` — Sentry and deployment-compatible wallet encryption

- **Profile:** default
- **Date:** started 2026-07-20 19:33; session remains open in metadata
- **Historical cwd / target:** Bora Capital backend
- **Indexed title:** none
- **Record quality:** `substantive`
- **Promotion:** `promote/current`
- **Confidence:** medium-high because the implementation is present only in a dirty working tree
- **Direct decisions and corrections:**
  - Message `3129`: replace Rollbar with Sentry; the Sentry package had already been added.
  - Messages `3268`, `3308`, `3316`, and `3317`: DigitalOcean rejects the JSON-shaped encryption environment value. Use exactly:
    - `WALLET_CREDENTIAL_ENCRYPTION_KEY`
    - `WALLET_CREDENTIAL_ACTIVE_KEY_VERSION`
    - Remove the extra key-ring/fingerprint-variable design.
- **Transcript-reported outcomes:**
  - Sentry migration, message `3236`: **60 suites / 305 tests**, build and production dependency audit passed; scoped formatting passed. A pre-existing generated-file formatting issue blocked repository-wide formatting.
  - Final wallet configuration, message `3381`: **60 suites / 303 tests**, build, and changed-file formatting passed.
- **Current-code evidence:**
  - `package.json` contains `@sentry/node` and no Rollbar dependency.
  - `src/loggers/sentry.ts` disables sending without a DSN, sets environment, disables default PII, and redacts event data.
  - Current call sites use `src/loggers/sentry`; no live Rollbar references were found.
  - `src/security/walletCredentials.ts` reads exactly the two corrected environment names.
  - It derives separate encryption and fingerprint subkeys through HKDF.
  - `docs/security/wallet-credential-encryption.md` documents scalar DigitalOcean values with no JSON braces or quotes.
  - `tests/unit/security/walletCredentials.spec.ts` covers encryption/decryption, randomized ciphertext, deterministic contextual fingerprints, missing configuration, and tamper rejection.
- **Current-code tensions:**
  - Sentry and wallet-encryption changes are uncommitted; the current branch is `feature/updates` at `49fe85765b8c`.
  - `.env.example` is deleted in the working tree.
  - The single-key design requires coordinated re-encryption for rotation; it is not a multi-key online rotation system.
- **Reusable rule:** deployment-platform configuration constraints outrank an agent’s preferred abstraction; follow the explicit platform-compatible contract and verify the simplified design.

---

## Current Repository Reconciliation

The repository was inspected statically at:

- Branch: `feature/updates`
- HEAD: `49fe85765b8c`
- Latest commit: `feat(updates): security hardens fixes`

Current source supports the transaction, wallet, and auto-top-up authorization outcomes. The July 20 Sentry and wallet-encryption work is present but uncommitted. The historical security plan exists in `HEAD` but is deleted from the working tree.

No current tests or builds were run during this audit. All test/build counts above are explicitly session-reported historical results.

---

## Suggested Vault Updates

When writes are authorized:

1. **Create a dedicated Hermes supplement source**
   - Suggested title: `Kusantec/Bora Hermes Conversation Harvest — Supplement 1`.
   - Keep it separate from the existing Codex batch so archive provenance is not conflated.
   - Record all seven exact database/session locators and the **6 substantive / 1 interrupted** classification.

2. **Update `bora-capital-backend.md`**
   - Add direct Hermes provenance for the staged security remediation.
   - Add current transaction, wallet, and auto-top-up ownership boundaries.
   - Add the Sentry migration and redaction boundary.
   - Document the exact two-variable wallet-encryption contract.
   - Preserve the dirty-tree/uncommitted-state caveat and the ownerless internal auto-top-up helper tension.

3. **Update `project-knowledge-harvest-status.md`**
   - Mark this exact seven-session Bora Hermes set as processed.
   - Do **not** claim complete global Hermes coverage without a separate exhaustive discovery pass.

4. **Update `software-development-operating-manual.md` provenance**
   - These sessions directly support existing rules for:
     - one-security-issue-at-a-time remediation;
     - leaving Bora migrations/crons outside the remediation scope;
     - resolving incoming IDs to canonical document identity;
     - principal-derived authorization.
   - Avoid duplicating those rules; add the Hermes source as evidence.
   - Add Sentry redaction and deployment-platform-compatible secret configuration only if intended as cross-project rules.

5. **No mobile project update**
   - These exact sessions provide no independent mobile-app implementation outcome.

## Completion

- **Exact IDs processed:** 7 of 7
- **Classifications:** 6 substantive, 1 interrupted
- **Files created or modified:** none
- **Verification:** historical transcript reports plus static current-code inspection only
- **Issues encountered:** linked compression duplicated earlier messages; default sessions lacked titles; current repository is dirty; the historical plan is deleted in the working tree; no fresh runtime verification was authorized or performed.