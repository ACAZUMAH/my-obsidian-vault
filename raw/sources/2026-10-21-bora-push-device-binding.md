# Bora push notifications bound to device and session

Date: 2026-10-19 to 2026-10-21
Source: The user's bug reports and decisions during the Bora push-notification fix, and the resulting backend change (uncommitted on `feature/updates` at the time of writing).

## User reports

1. With the app on two phones, signing in on phone A, signing out, then signing in on phone B left phone A receiving push notifications.
2. Sign-in, sign-up, and transaction pushes reached every device ever registered.
3. Signing in to the admin portal (web, staff) sent pushes to the mobile apps, including Expo Go.

## Root causes found

- Tokens were an unbounded array on the user document. Registration only added tokens, never removed them from other users, and was not tied to a device or a session.
- Nothing on the server removed a token at logout, session revocation, refresh-token reuse, or password reset. Removal depended on a best-effort app call that often did not run.
- OTP verification did not know which client was signing in, so an admin-portal sign-in sent the customer "Welcome back" push. Staff and customers share one user document.
- Expo Go and development builds registered against the same backend with no check.
- Expo receipts were never read, and ticket errors such as `InvalidCredentials` deleted tokens.

## User decisions

- Backend work only, plus a frontend handoff; the mobile developer implements the app side.
- `installationId`, `buildType`, and `appId` are required on registration, and the old per-user token arrays are purged by migration.
- Pushes that Expo refuses for any reason count as failed and are retried, not marked delivered.
- The "Welcome back" push becomes a new sign-in security alert to the account's other signed-in phones (`NEW_SIGNIN`); admin-portal sign-ins send no push.
- Holding a push token or installation id is accepted as enough to claim a phone, with a `PUSH_DEVICE_REASSIGNED` security audit event (user ids only) whenever a phone moves between accounts.

## Implemented

- `PushDevice` collection (`pushdevices`): one row per install, unique token and unique installation id, bound to user and session. Registration moves the install and token to the signed-in account inside a transaction; it requires a customer-app client, a session-bound access token, bounded input, and a per-user rate limit of 10 per minute per server instance. Production accepts only the store build and bundle id; staging accepts staging and development builds.
- Revoking a session, all sessions, or a refresh-token family deletes the matching devices. Every send uses only devices whose session is active, unexpired, and owned by the same user; `me.expoPushTokens` lists the same devices, to the owner only.
- Sign-in and sign-up codes record the issuing client; a code issued to one client cannot be completed by another, and only customer-app sign-ins send the alert.
- Expo tickets are stored and a five-minute receipt check deletes devices reported `DeviceNotRegistered`. Account-level errors no longer delete devices. Failures are tracked per message, so a partial failure never pushes twice, and failure lists never reach logs.
- Migration `PURGE_USER_EXPO_PUSH_TOKENS_V1` removes the old arrays through the raw collection.
- Handoff: section 3 of `docs/frontend-handoff-2026-10-17.md`. Backend deploys only after an app build that sends the new fields is on every test phone.
- Verification: 167 suites and 1124 tests passing, build green. Not run against a real MongoDB or Expo account.
