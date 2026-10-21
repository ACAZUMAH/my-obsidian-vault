---
type: project
status: active
created: 2026-07-21
updated: 2026-10-21
tags: [project, bora-capital, mobile, expo, investment]
sources:
  - ../sources/kusantec-bora-project-knowledge-harvest-batch-1.md
  - ../sources/bora-canonical-identity-authorization-hermes-chain.md
  - ../sources/bora-push-device-binding.md
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

## Durable Conventions

- This project uses Expo Router; do not replace it with another navigation architecture based on unrelated family defaults.
- Route files should remain entry/composition points while reusable behavior lives under the owning `src` feature/hook/service.
- Secure tokens use SecureStore; Redux/provider state drives routing and shared UI.
- Financial actions require authenticated state, current KYC, and transaction authorization where configured.
- The production deposit UI uses Paystack initialization and backend verification only; do not fall back to the legacy direct-deposit mutation.
- Deposit initialization sends account, amount, and optional narration without `userId`; single investment-account lookup sends only account number because identity is backend-principal-owned.
- Treat push registration as optional/degraded: register by app/OS, handle token rotation, back off on provider failures, preserve local per-user history, and deep-link by notification type.
- From the 2026-10-21 backend change, registration must send a per-install `installationId` (kept across sign-out, device-only keychain class), `buildType`, and `appId`; register after every sign-in, on every launch, and on token change; never register from Expo Go or web; and send every sign-out through `logout`. Route `NEW_SIGNIN` pushes to security settings. Contract: section 3 of the backend's `docs/frontend-handoff-2026-10-17.md`; see [[../sources/bora-push-device-binding|Bora Push Notifications Bound To Device And Session]].
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
