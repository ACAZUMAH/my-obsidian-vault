---
type: source
status: active
created: 2026-10-01
updated: 2026-10-01
tags: [bora-capital, backend, authentication, biometrics, documentation]
sources:
  - ../../raw/sources/2026-10-01-bora-biometric-login-and-handoff-docs.md
  - ../../raw/sources/2026-10-01-bora-handoff-delta-permissions-inbox.md
  - ../../raw/sources/2026-10-01-bora-handoff-scope-correction.md
confidence: high
---

# Bora Biometric Login And Consolidated Frontend Handoff

## Source

- Raw file: [2026-10-01-bora-biometric-login-and-handoff-docs.md](../../raw/sources/2026-10-01-bora-biometric-login-and-handoff-docs.md)
- Follow-up raw file: [2026-10-01-bora-handoff-delta-permissions-inbox.md](../../raw/sources/2026-10-01-bora-handoff-delta-permissions-inbox.md)
- Correction raw file: [2026-10-01-bora-handoff-scope-correction.md](../../raw/sources/2026-10-01-bora-handoff-scope-correction.md)
- Date: 2026-10-01
- Author: direct user direction with Claude Code implementation
- Ingested: 2026-10-01

## Core Claims

- Frontend handoff for Bora is two files: `docs/frontend-handoff-app.md` and `docs/frontend-handoff-admin.md`, each covering everything that client must build. Per-feature handoff docs were retired.
- Each handoff covers only what changed since the previous one. Only features the user names as sent are left out: so far withdrawals, investment accounts, and goals and top-ups. Never infer from old documents which features were sent; ask instead.
- Biometric login is a server-side device credential, not stored metadata: a random per-device token, hashed on the server, kept by the app in biometric-protected secure storage, and exchanged by `loginWithBiometric` for a normal session.
- Enabling needs no password within 10 minutes of an OTP sign-in (the app prompts right after sign-up or sign-in) and the account password at any other time.
- Biometric login lapses after 90 days without use and is turned off by logout (the app calls `disableBiometricLogin`), password change or reset, or account disablement.

## Useful Details

- Sessions hard-expire 7 days after sign-in; refresh does not extend them, so biometric login creates a fresh session each time.
- Sessions carry assurance level `biometric`, which must stay in the refresh-claim, principal, and session-model allow-lists.
- `loginWithBiometric` and `enableBiometricLogin` are rate limited; a wrong enrolment password returns 400 so the app does not treat it as a logout.
- Schema validation of handoff examples caught stale Grow Wealth query names from the earlier handoff; validate every handoff GraphQL example against the live schema.
- `getMyPermissions` gives the admin portal the signed-in user's permissions, direct grants included, with wildcards expanded; menus use it instead of `me.platformRoles`.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[bora-notifications-marketing|Bora Notifications, Campaigns, And Banners]]

## Contradictions Or Tensions

- A password prompt was proposed for enabling biometrics and rejected by the user; the 10-minute post-OTP window keeps the user's flow while denying silent enrolment from an old or stolen session.
- Several docs outside the handoff scope (`SECURITY.md`, `auth-wallet-frontend-integration.md`, `architecture/`) were deleted outside the agent's commands; the user later committed the deletions, so they were intended.
- The first consolidated app handoff repeated features from the previous handoff; the user corrected it to cover only new changes.
- The trimmed handoff then also removed existing-customer onboarding, KYC, Grow Wealth, and statements on an unconfirmed agent inference; the user corrected that too, and those sections were restored.

## Open Questions

- None currently.
