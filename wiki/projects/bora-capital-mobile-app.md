---
type: project
status: active
created: 2026-07-21
updated: 2026-11-23
tags: [project, bora-capital, mobile, expo, investment]
sources:
  - ../sources/kusantec-bora-project-knowledge-harvest-batch-1.md
  - ../sources/bora-canonical-identity-authorization-hermes-chain.md
  - ../sources/bora-push-device-binding.md
  - ../sources/bora-kyc-supervision-and-statement-update.md
  - ../sources/bora-accepted-risks-deposit-path-and-api-domain.md
  - ../sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md
  - ../../raw/sources/2026-11-22-bora-a1-customer-pays-paystack-fee-implementation.md
confidence: high
---

# Bora Capital Advisors Mobile App

## Summary

Expo customer application for Bora Capital onboarding, identity/KYC, investment portfolios, deposits, withdrawals, goals, reports, notifications, financial education, and Oye.

## Purpose

Provides the customer-facing investment experience backed by [[bora-capital-backend|Bora Capital Backend]], including authenticated portfolio operations and backend-verified Paystack funding.

## Stack

- Expo SDK 54, React Native 0.81, React 19, Expo Router 6.
- Apollo Client 3, GraphQL 16, Redux Toolkit/React Redux.
- SecureStore, AsyncStorage, biometrics, notifications, device/network/file/media modules.
- Firebase Analytics, Sentry, Lottie/Reanimated, SVG/charts, PDF/WebView.
- Jest/Testing Library, Expo ESLint, TypeScript 5.9.
- npm 10.9.4.

## Architecture

`app/` is the Expo Router boundary for public auth/onboarding/legal routes and protected tabs, portfolio, deposit, withdrawal, transaction, goal, KYC, profile, notification, report, and security routes.

`app/_layout.tsx` composes Redux, Apollo, auth/theme/balance providers, route gating, secure logging, privacy/screen-capture/integrity controls, offline/toast behavior, analytics, diagnostics, monitoring, and the global visual shell. `AuthGate` swaps the available route tree based on restored authentication, PIN, and biometric state.

The Paystack deposit hook initializes through GraphQL, opens only an allowed provider URL, verifies through the backend while/after checkout, polls boundedly, and refreshes balances only after successful backend/BCL completion.

## Folder Ownership

- `app`: route entry points and route-level composition.
- `src/features`: feature-owned UI, hooks, styles, and domain presentation.
- `src/api`: GraphQL operations/contracts.
- `src/hooks` and `src/services`: reusable orchestration, Paystack browser, notifications, analytics, auth, and device behavior.
- `src/store` and `src/context`: Redux and cross-route state/providers.
- `src/components`: shared presentation, navigation, privacy, security, and global status UI.
- `src/constants`, `src/theme`, `src/types`, `src/utils`: configuration, tokens, contracts, guards, redaction, and mappings.
- `scripts`: production configuration and OTA/runtime safety validation.
- `.agents/skills`: repository-local interface/design workflows.

## Commands

- `npm start`, `npm run android`, `npm run ios`, `npm run web`.
- `npm run lint`, `npm run typecheck`, `npm test`.
- `npm run validate:ota-runtime`, `npm run validate:production`.
- `npm run vercel-build` — Expo web export.
- EAS profiles: development, iOS simulator, preview, and production.

## Runtime/Deployment

EAS owns native builds and store submission. GitHub Actions use Node 22/npm for audit, OTA-runtime validation, lint, typecheck, Jest, preview updates, native build planning, optional update publication, and optional production submission. Runtime version follows app version.

Current app configuration disables Expo updates even though update hooks/workflow paths exist. The inspected `develop` branch was based at `393bac0ef0dc` with a pre-existing modified `package-lock.json`; this harvest did not change it.

Distribution (user statement, 2026-11-06): the app ships only through TestFlight, with no public store builds. Breaking backend GraphQL input changes can therefore ship with a new TestFlight build and no deprecate-then-remove phase; the first was the KYC ID image change (send `imgIDFrontString` and `imgIDBackString` only; `imgIDString` removed). Re-check once the app is publicly released. See [[../sources/bora-kyc-supervision-and-statement-update|Bora KYC Supervision And Statement Update]].

API host (user statements, 2026-11-19): production uses `api-production-bora-x7evx.ondigitalocean.app`, and the app pins its `ondigitalocean.app` certificate, so moving to the recommended `api.boradvisors.com` custom domain needs a new mobile build. Never point the app at `boracapital.com`, which Bora does not control. See [[../sources/bora-accepted-risks-deposit-path-and-api-domain|Bora Accepted Risks, Deposit Path, And API Domain]].

## Durable Conventions

- This project uses Expo Router; do not replace it with another navigation architecture based on unrelated family defaults.
- Route files should remain entry/composition points while reusable behavior lives under the owning `src` feature/hook/service.
- Secure tokens use SecureStore; Redux/provider state drives routing and shared UI.
- Financial actions require authenticated state, current KYC, and transaction authorization where configured.
- The production deposit UI uses Paystack initialization and backend verification only; do not fall back to the legacy direct-deposit mutation. The backend removed that mutation (`depositCash`) on 2026-11-19, pending deploy.
- Deposit initialization sends account, amount, and optional narration without `userId`; single investment-account lookup sends only account number because identity is backend-principal-owned.
- Treat push registration as optional/degraded: register by app/OS, handle token rotation, back off on provider failures, preserve local per-user history, and deep-link by notification type.
- From the 2026-10-21 backend change, registration must send a per-install `installationId` (kept across sign-out, device-only keychain class), `buildType`, and `appId`; register after every sign-in, on every launch, and on token change; never register from Expo Go or web; and send every sign-out through `logout`. Route `NEW_SIGNIN` pushes to security settings. Contract: section 1 of the backend's `docs/frontend-handoff-2026-10-22.md`; see [[../sources/bora-push-device-binding|Bora Push Notifications Bound To Device And Session]].
- Production configuration must reject local/non-HTTPS endpoints, public secret-like variables, KYC bypass, and invalid TLS-pinning ownership.

## Constraints

- The frontend cannot bypass a missing portfolio Paystack subaccount and must not claim payment success before backend/BCL verification.
- Deposit confirmation is guarded against duplicate presses and unsafe authorization URLs.
- Native dependency/fingerprint changes require a compatible app-version/runtime change and a new binary rather than an unsafe OTA-only release.
- Push service or credential failure must degrade without crashing the app.
- Public environment variables are not secret storage.
- Existing security/privacy controls and accurate store permission declarations are release requirements.

## Decisions And Rationale

- Expo Router file ownership matches the current application and its route-heavy financial flows.
- AuthGate removes protected routes when unauthenticated or locked rather than relying only on screen-level checks.
- Paystack verification remains server-owned so a browser redirect or client state cannot credit investments.
- Local notification history improves offline continuity while the backend/Expo delivery path remains authoritative for push transport.
- OTA fingerprint validation prevents JavaScript updates from crossing an incompatible native runtime boundary.
- Written 2026-11-22 as the backend's `docs/frontend-handoff-2026-11-22.md` (uncommitted, not sent; [evidence](../../raw/sources/2026-11-22-bora-frontend-handoff-2026-11-22.md)). Its app items:
  - the fee (A1);
  - deposit result wording (A4, the agent's copy, approved by the owner 2026-11-23: [evidence](../../raw/sources/2026-11-23-bora-a4-wording-approved-bcl-email-case-deferred.md));
  - withdrawal refusals (C23);
  - Oye limits: current builds send up to 6,000 characters of history in the prompt and the backend now refuses over 2,000;
  - the side note.

  The payout step is not in it. The owner's item list it was written from (decisions, 2026-11-21):
  - Deposit result copy. BCL accepting the deposit means it went through, and BCL has already alerted the customer, so drop "your investment account has been credited". Proposed: "Deposit successful. You'll get a confirmation message when it reflects on your portfolio." When the server returns `PROCESSING`, show "Payment received, awaiting confirmation". Keep the neutral "checking your payment, do not pay again" wording for the `PROCESSING` the app sets itself after client errors. The exact wording is the owner's.
  - "That verification code is incorrect" only for the server's own code errors (wrong, expired, too many attempts). Today `mapVerificationError` matches any message containing "invalid", so BCL's "Invalid Account Number" refusal shows as a code error. Show BCL's refusal text instead.
  - Show amount, Paystack fee and total on the deposit, goal top-up and auto top-up screens. The customer bears the fee. The backend fee change is built (A1, 2026-11-22, uncommitted) and is on at deploy, so builds without it show only the deposit while Paystack asks for the total. Read the quote from `getDepositFeeQuote(amount)` before confirming, or from `amount`/`fee`/`total` on the checkout reply; payment results carry the same fields; `AutoTopUp` has `fee` and `total` per run. Keep "Total Investment" meaning the deposit. Evidence: [A1](../../raw/sources/2026-11-22-bora-a1-customer-pays-paystack-fee-implementation.md).
  - Later, a "pay to" step (bank or Mobile Money) for withdrawals, once BCL adds payout fields.
  - App-only side note, the developer's call (owner decision, 2026-11-21): on a phone keyboard that uses a decimal comma, typing "500,50" in the withdrawal amount becomes "50050". The confirm screen shows 50,050 before the customer confirms, so the customer can see it, but it is an older input issue in `sanitizeAmountInput` (`app/withdrawals/amount.tsx`).

  See [[../sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog|Bora Deposit And Withdrawal Flow Decisions And Fix Backlog]].

## Verification Expectations

Preserve the dirty lockfile unless dependency work is explicitly in scope. Run production/OTA validators, lint, typecheck, Jest, and Expo startup on iOS/Android. Exercise cold auth restoration, PIN/biometric gates, KYC protection, deposit success/failure/abandonment/missing-subaccount paths, duplicate confirmation, safe-link rejection, push permission/rotation/deep links, offline degradation, and native privacy controls. Validate the real EAS profile and store artifact; a web export or Expo Go smoke test is insufficient for native security and push behavior.

## Evidence

- Current package/README, app/EAS configuration, route/provider/auth/Apollo/store, deposit/push/security source, validation scripts, workflow, and live Git state at base commit `393bac0ef0dc` plus the pre-existing lockfile modification.
- Repository inventory and backend session reconciliation in [[../sources/kusantec-bora-project-knowledge-harvest-batch-1|Kusantec/Bora Project Knowledge Harvest — Batch 1]]. No historical mobile-working-directory Codex session was discovered.
- [[../sources/bora-canonical-identity-authorization-hermes-chain|Bora Canonical Identity And Authorization Hermes Chain]] confirms that current mobile deposit/account operations correctly omit `userId`; those records changed backend contracts rather than mobile files, and one utility comment remains stale.

## Contradictions

- README describes an older/simpler route tree and Node 18 prerequisite; current package/config/workflow use Expo 54 and Node 22 CI with substantially broader financial/security infrastructure.
- OTA update code and workflow options exist while current app configuration disables updates; do not report OTA publishing as active without reconciliation.
- A historical backend correction required frontend-passed `userId` for deposits. Current mobile input intentionally omits it and uses authenticated-principal identity.
- One deposit utility comment still describes the superseded explicit-user-ID contract despite current generated types and operations omitting it.
- The working tree already had a modified lockfile, so the base commit alone does not reproduce the inspected dependency state.
- No mobile session explains all current design/security choices; those are observed implementation, not inferred user preference.

## Confidence

High for current static route/provider/deposit/push/release architecture; medium for live native and deployment behavior because no build, device flow, or EAS job was executed.

## Open Questions

- Is Expo Updates intentionally disabled for every profile, or only pending release-policy completion?
- Which README sections should be rewritten to match the current Expo 54 route and security architecture?
- Should deposit identity remain principal-derived across backend and mobile?
- When will the modified lockfile be stabilized and validated in CI?
