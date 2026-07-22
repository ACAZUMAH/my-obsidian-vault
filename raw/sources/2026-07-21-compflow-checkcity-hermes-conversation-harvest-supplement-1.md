# CompFlow And CheckCity Hermes Conversation Harvest — Supplement 1

Source: sanitized read-only evidence report produced from coder/default Hermes SQLite stores and current static repository reconciliation on 2026-07-21. Full transcripts, tool chatter, secrets, private payloads, screenshots, and environment values are excluded.

# Sanitized read-only evidence report

## Outcome

- Processed **3 exact coder-profile sessions** and **1 default-profile de-duplication control**.
- Classifications: **3 substantive**, **1 duplicate**.
- Promotion status: **3 promote/current**, **1 reference-only**.
- Inspected both SQLite databases read-only and reconciled claims against five clean repository checkouts.
- Verification scope was **historical session reports plus current static source inspection**. No builds, tests, services, databases, payments, emails, migrations, or deployments were executed.
- No secrets, private identifiers, raw payloads, screenshots, full transcripts, or environment values are included.

## Evidence reports

### `20260710_190402_e7ba9f`

- **Date:** 2026-07-10; substantive continuation on 2026-07-11.
- **Historical cwd:** `/Users/acazumah/Documents/compFlow`
- **Indexed title:** `Proper Project Stack Setup`
- **Target repositories:** CompFlow public, admin, client portal, and backend.
- **Minimal safe quotation:** none.
- **Record quality:** `substantive`
- **Promotion status:** `promote/current`
- **Durable evidence:**
  - “Spin up a project” means install the actual dependency stack, configure providers/runtime, establish the expected folder ownership, and prove the applications work—not produce minimal renderable stubs.
  - Existing projects and saved skill references are architectural contracts. Passing tests/builds is insufficient when file responsibilities and project conventions do not match.
  - Final accepted backend ownership separates process entry, startup orchestration, Express creation, Apollo HTTP, GraphQL subscriptions, error formatting, database ownership, JWT middleware, request context, and DataLoader creation.
  - JWT resolution belongs in middleware; GraphQL context spreads the request, loaders, and request IP.
  - The internal admin and business client portal are explicitly different product surfaces. The session ends immediately after the client-portal addition request, so it does **not** prove that addition was completed.
- **Transcript-reported outcome:**
  - Successive scaffold attempts were rejected and superseded.
  - The final backend report attributed three passing tests, TypeScript/alias build success, GraphQL HTTP health, invalid-JWT rejection, and a successful WebSocket acknowledgement.
  - Earlier reports attributed successful public/admin generation, tests, builds, browser rendering, and GraphQL smoke checks. These are historical 2026-07-10/11 results only.
- **Current-code evidence:**
  - Backend: `src/main.ts`, `src/app.ts`, `src/servers/createExpressApp.ts`, `createGraphqlServer.ts`, `createGraphqlSubscriptionServer.ts`, `formatGraphqlErrors.ts`, `src/middlewares/verify-token.ts`, `src/common/db/index.ts`, and `src/dataloaders/index.ts`.
  - `createGraphqlServer.ts` still returns `{ ...req, ...createDataLoaders(), ip }`; `verify-token.ts` still attaches user/token fields to the request.
  - Four independent repositories remain clean at the commits already recorded in the vault.
- **Current-code tensions:**
  - The session’s database-bypass smoke command is no longer implemented even though the README still documents it.
  - The session-era `schema.graphql` and backend `codegen.ts` are absent.
  - Current backend no longer exposes `adminOverview`, while admin still queries it with fallback.
  - `src/dataloaders/index.ts` preserves the context boundary but currently returns an empty loader set.
- **Confidence:** high for corrections and static current ownership; medium-high for historical runtime details because they were not rerun.
- **Reusable rule:** adds a bootstrap rule: use saved skills and their linked references as executable checklists; compilation does not prove architectural parity.

### `20260711_165753_68ff6f`

- **Date:** 2026-07-11.
- **Historical cwd:** `/Users/acazumah/Documents/compFlow`
- **Indexed title:** `Backend Authentication Setup`
- **Target repository:** `/Users/acazumah/Documents/compFlow/compflow-backend`
- **Minimal safe quotation:** none.
- **Record quality:** `substantive`
- **Promotion status:** `promote/current`
- **Durable evidence:**
  - The initial password/Bcrypt/Zod/Pino implementation was explicitly rejected.
  - Accepted authentication mirrors LivelyCura: one email/phone login flow, a stored OTP token, OTP verification through `completeLoginWithToken`, and JWT issuance only after successful verification.
  - Backend conventions require Winston logging and AJV validation.
  - Self-service business onboarding should initialize and verify subscription payment before provisioning the organization/owner relationship; the Bora Paystack implementation was the requested reference.
  - OTP email uses Resend with React Email templates. Tests may mock delivery/rendering, but production code must use the real template path.
- **Transcript-reported outcome:**
  - After correction, the session reported two passing suites/four tests and a passing build.
  - It reported OTP login → verification → JWT → authenticated `me` coverage with pending-organization state.
  - It later reported the same build/test result after adding Resend and independently rendering the React Email template.
  - No real external email was sent.
- **Current-code evidence:**
  - `src/graphql/auth/typeDefs.ts` exposes `login`, `loginWithEmail`, `loginWithPhoneNumber`, and `completeLoginWithToken`.
  - `src/services/auth/login.ts` creates a six-digit token and sends OTP by available channel.
  - `src/services/auth/completeLoginWithToken.ts` consumes OTP state before signing JWT.
  - `src/logger/logger.ts`, AJV dependencies, `src/services/notifications/otp.ts`, Resend sender, and React Email templates remain present.
  - `applySuccessfulBusinessSubscription.ts` validates payment reference, amount, and success status before organization creation and owner assignment.
  - Focused current test files exist for auth, authorization, subscriptions, payroll, migrations, and transport; they were not executed.
- **Current-code tensions/open questions:**
  - The wrong password implementation is historical and fully superseded.
  - The final request to continue with other APIs has no supported outcome in this session.
  - Static source confirms integration structure, not current Resend delivery, Paystack behavior, database state, or runtime authorization.
- **Confidence:** high.
- **Reusable rule:** mainly adds direct project provenance to existing OTP, verified-payment provisioning, and notification-boundary rules rather than a new cross-project rule.

### `20260707_234259_178721`

- **Date:** 2026-07-07; relevant continuations on 2026-07-08 and 2026-07-09.
- **Historical cwd:** `/Users/acazumah/Documents/LivelyCura/livelycura-check-city-app`
- **Indexed title:** `Coding Task Assistance`
- **Target repository:** LivelyCura CheckCity App.
- **Minimal safe quotation:** none.
- **Record quality:** `substantive`
- **Promotion status:** `promote/current`
- **Durable evidence:**
  - The final bottom-tab design has Menu, Search, and Orders in one track with Cart as a detached action.
  - The inactive cart must not use the active color. Active items expand, reveal labels, and fill their complete surface without an inset gap.
  - Badge placement must remain visible outside the detached cart surface.
  - Profile/More was tried as a tab and explicitly removed. Profile access belongs only in Menu, Cart, and Orders headers.
  - The generic floating header defaults to no profile action; screens opt in deliberately.
  - The menu branch selector remains floating and transparent at the top; only its selector surface regains a background/elevation while scrolling.
  - Interfaces, constants, components, and navigation concerns must remain in their owning files rather than being combined.
- **Transcript-reported outcome:**
  - Each completed iteration reported Prettier and `git diff --check` success plus successful iOS Metro bundle generation.
  - Full type-check was repeatedly reported as blocked by pre-existing generated GraphQL errors.
  - Intermediate More-tab and notification-bell implementations were later superseded within the same session.
- **Current-code evidence:**
  - `BottomTabNavigator.tsx` currently registers Menu, Search, Orders, and Cart only.
  - `constants/tabs.ts` keeps three track tabs and a separate cart configuration.
  - `AnimatedTabItem.tsx` retains Reanimated active transitions and reduced-motion handling.
  - Bottom-tab styles retain active/inactive flex differentiation, complete track clipping, detached cart sizing, and external badge positioning.
  - `FloatingHeader.tsx` defaults `showProfileAction` to false.
  - Only `OrdersHeader`, `CartHeader`, and `BranchSelectorHeader` opt into or directly render the profile action.
  - `BranchSelectorHeader.tsx` animates only the branch selector surface from transparent to the themed card color as scrolling advances.
- **Current-code tensions/open questions:**
  - Notification registration/handling now exists elsewhere in current source, so the historical statement that its backend API was unavailable should not be promoted as current fact. The header still correctly uses profile rather than a notification bell.
  - Current type-check status is unknown; the historical generated-file blocker was not rerun.
- **Confidence:** high for current static behavior; medium-high for historical verification.
- **Reusable rule:** supports existing responsive-tab, reduced-motion, feature-ownership, and explicit opt-in header conventions; it does not require a duplicate generalized rule.

### Default-profile de-duplication control: `20260710_173537_54b264`

- **Database role:** existing processed control only.
- **Date/cwd:** 2026-07-10, `/Users/acazumah/Documents/compFlow`
- **Indexed title:** none.
- **Record quality:** `duplicate`
- **Promotion status:** `reference-only`
- **Result:** the existing CompFlow Hermes Supplement 1 accurately captures the root-monorepo correction, separate application folders, Yarn ownership, initial historical tests/builds/services, and current `adminOverview` drift. It should **not** be promoted again.
- **New relationship:** it is predecessor provenance for `20260710_190402_e7ba9f`, whose later corrections add full-stack and exact file-responsibility expectations.
- **Confidence:** high.
- **Reusable rule:** supports the already-promoted “shared parent folder is not monorepo authorization” rule only.

## Suggested vault updates

No changes were made, but a future authorized promotion should:

1. Add **CompFlow Hermes Supplement 2** for coder sessions:
   - `20260710_190402_e7ba9f`
   - `20260711_165753_68ff6f`
   - Link the default session only as de-duplicated predecessor provenance.
2. Add a **LivelyCura CheckCity Hermes Supplement 1** for `20260707_234259_178721`.
3. Update project provenance:
   - CompFlow Backend: corrected startup ownership, OTP/Winston/AJV, Resend, and payment-before-provisioning evidence.
   - CompFlow Admin/Client Portal: explicit internal-versus-business surface decision, without claiming the final client-portal request was implemented by that session.
   - CheckCity: direct Hermes provenance for the final tabs, profile placement, branch-header behavior, and historical verification blocker.
4. Update the checkpoint without combining archive types:
   - CompFlow: **3 directly classified Hermes sessions total**—one already processed default session plus two new coder sessions.
   - LivelyCura: retain the **37 Codex classifications** separately and add **1 directly classified Hermes session**.
5. Promote only one new bootstrap rule: linked skill references must be followed as file-level execution checklists; build/test success alone is not proof of convention parity.
6. Preserve the current tensions around stale DB-bypass documentation, absent Codegen/schema artifacts, removed `adminOverview`, unexecuted external integrations, and unknown current type-check status.

## Provenance and completion

- **Coder DB:** `/Users/acazumah/.hermes/profiles/coder/state.db`
- **Default DB:** `/Users/acazumah/.hermes/state.db`
- The canonical records are SQLite `sessions` rows and their keyed `messages` rows; no separate transcript file was substituted.
- All four records are active/non-archived.
- Repository checkouts inspected read-only:
  - CompFlow public: `develop` at `03421056ea70`
  - CompFlow admin: `main` at `832109de1042`
  - CompFlow client portal: `develop` at `55e4e4d16087`
  - CompFlow backend: `main` at `b512a40b7b9e`
  - CheckCity: `feature/address` at `b8213cfba580`
- All checkouts were clean.
- **Files created or modified:** none.
- **Issues encountered:** none blocking; current runtime confidence remains limited because the audit intentionally performed no fresh execution.