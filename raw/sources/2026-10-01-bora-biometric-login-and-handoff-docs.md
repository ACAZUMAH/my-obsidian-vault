# Bora Biometric Login And Consolidated Frontend Handoff — Decisions And Implementation

Date: 2026-10-01
Source: direct user direction in Claude Code during Bora backend work (2026-09-30 to 2026-10-01)

## User Direction

- The frontend handoff must be two Markdown files, one for the customer app and one for the admin portal, each containing everything that frontend must build and the API changes, instead of separate per-feature documents. The per-feature documents are to be deleted after merging, and the files cover everything on `feature/updates` not yet on `develop`.
- Before the handoff, biometric login must be added: the app had been storing biometric login state locally and it expired early. Returning users must be able to log in with biometrics. Device fields requested: `deviceId` (stable per install), `deviceName`, `platform` (ios/android), `osVersion`, `appVersion`, `biometricType` (face/fingerprint), and `biometricEnabled`.
- The user rejected a password prompt when enabling biometrics: the app shows the enable prompt immediately after sign-up or sign-in, other apps work that way, and logout clears everything so the next sign-in shows the same prompt.
- Biometric login should lapse after 90 days without use.

## Agent Evidence

- Sessions hard-expire 7 days after sign-in and refresh does not extend them, which explains the early expiry of locally stored login state.
- Device metadata cannot authenticate: a device ID is not secret. The design adds a random per-device token whose SHA-256 hash is stored server-side; the app keeps the token in biometric-protected secure storage.
- Refresh tokens are validated against an assurance-level allow-list, which also exists in the principal builder and the session model; a new `biometric` level had to be added to all three or biometric sessions could not refresh.
- An authenticated enrolment path that accepts a password could be used to guess passwords with a stolen access token, so it is rate limited; a wrong password returns 400, not 401, so the app does not treat it as a logout.
- The admin portal can read a staff member's role permissions through `me.platformRoles` but not their direct grants; this gap was flagged, not fixed.
- The per-feature docs (`customer-support-api.md`, `fund-admin-api.md`, `investment-account-frontend.md`, `frontend-handoff-post-withdrawal-verification.md`) plus `SECURITY.md`, `auth-wallet-frontend-integration.md`, the untracked `architecture/` folder, and the uncommitted notifications doc were deleted from disk outside the agent's commands (around a Finder `.DS_Store` change). Content was recovered from git history for the merge.
- Validating every GraphQL example against the live schema showed that the 28 September handoff still named `getMyGrowWealth` and `getMyGrowWealthAsset`, which were renamed to `getMyGrowWealthPortfolios` and `getMyGrowWealthPortfolioById` in commit `2abde13`.

## Implemented Scope

- `enableBiometricLogin` stores the device fields and a token hash per user and device; it needs no password within 10 minutes of an OTP sign-in and requires the account password otherwise. It returns the token once.
- `loginWithBiometric` (customer app only, rate limited) starts a normal 7-day session with assurance level `biometric` and extends the device's 90-day window; `getMyBiometricDevices` and `disableBiometricLogin` manage devices; password change and reset turn biometric login off on every device; lapsed devices are turned off on use.
- `docs/frontend-handoff-app.md` and `docs/frontend-handoff-admin.md` replace the per-feature docs; all 31 GraphQL operation examples validate against the schema and depth limit, and all JSON examples parse.
- Verification: build passed; 140 test suites and 857 tests passed; 17 biometric guards were mutation-checked.
