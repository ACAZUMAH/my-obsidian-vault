---
type: source
status: active
created: 2026-10-21
updated: 2026-10-21
tags: [bora-capital, backend, notifications, push, expo, sessions, security]
sources:
  - ../../raw/sources/2026-10-21-bora-push-device-binding.md
source_date: 2026-10-21
ingested: 2026-10-21
confidence: high
---

# Bora Push Notifications Bound To Device And Session

## Source

- Raw file: [Push notifications bound to device and session](../../raw/sources/2026-10-21-bora-push-device-binding.md)
- Date: 2026-10-19 to 2026-10-21
- Author: User bug reports and decisions, implemented by the agent
- Ingested: 2026-10-21

## Core Claims

- A push registration belongs to one app install. `PushDevice` holds one row per install, with a unique token and a unique installation id, bound to the signed-in user and session. Registering moves the install and its token to that account; tokens are never kept per user.
- Server-side session ends unbind devices: revoking a session, all of a user's sessions, or a refresh-token family deletes the matching devices. Sends, campaign reach, and `me.expoPushTokens` use only devices whose session is active, unexpired, and owned by the same user.
- Registration requires the customer-app client, a session-bound access token, `installationId`, `buildType`, and `appId`. Production accepts only the store build and bundle id; staging accepts staging and development builds; Expo Go never registers outside local development.
- Sign-in and sign-up codes are bound to the client that requested them. Admin-portal sign-ins send no push.
- The "Welcome back" push is replaced by a `NEW_SIGNIN` security alert to the account's other signed-in phones. It is not added to the inbox.
- Any push Expo refuses counts as failed and is retried, up to the delivery attempt limit. Failures are tracked per message, so a partial failure never pushes twice. Only `DeviceNotRegistered`, from a ticket or a receipt, deletes a device.
- Knowing a token or installation id is accepted as enough to claim a phone. Each move between accounts writes a `PUSH_DEVICE_REASSIGNED` security audit event with user ids only.

## Useful Details

- Push tokens are credentials: failure lists are non-enumerable on the thrown error, and the shared redaction removes `ExpoPushToken[...]` from log and Sentry text.
- Expo tickets are stored for a day; a five-minute leased cron reads receipts about 15 minutes after sending.
- Migration `PURGE_USER_EXPO_PUSH_TOKENS_V1` removes the old per-user arrays through the raw collection, because a model update on a field no longer in the schema is a silent no-op.
- Release order: an app build sending the new fields goes on every test phone before the backend deploys; the deploy deletes all old tokens.
- Frontend contract: section 3 of `docs/frontend-handoff-2026-10-17.md`.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[../projects/bora-capital-mobile-app|Bora Capital Advisors Mobile App]]
- [[bora-notifications-marketing|Bora Notifications, Campaigns, And Banners]]
- [[bora-single-input-object-convention|Bora Service Functions Take One Input Object]]

## Contradictions Or Tensions

- Supersedes the per-user `expoPushTokens` array and the sign-in welcome-back push described in [[bora-notifications-marketing|Bora Notifications, Campaigns, And Banners]].
- A sign-out that never reaches the server leaves the phone receiving pushes until the session expires, up to 7 days.

## Open Questions

- Whether to add a backend way to end a session without the phone's tokens, closing the offline sign-out window.
