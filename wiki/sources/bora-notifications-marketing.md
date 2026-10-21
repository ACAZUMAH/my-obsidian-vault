---
type: source
status: active
created: 2026-09-30
updated: 2026-10-21
tags: [bora-capital, backend, notifications, marketing, campaigns, uploads]
sources:
  - ../../raw/sources/2026-09-30-bora-notifications-campaigns-banners.md
  - ../../raw/sources/2026-10-01-bora-handoff-delta-permissions-inbox.md
  - ../../raw/sources/2026-10-01-bora-campaign-sms-hold.md
  - ../../raw/sources/2026-10-13-bora-push-sound-channel.md
  - ../../raw/sources/2026-10-21-bora-push-device-binding.md
confidence: high
---

# Bora Notifications, Campaigns, And Banners

## Source

- Raw file: [2026-09-30-bora-notifications-campaigns-banners.md](../../raw/sources/2026-09-30-bora-notifications-campaigns-banners.md)
- Follow-up raw file: [2026-10-01-bora-handoff-delta-permissions-inbox.md](../../raw/sources/2026-10-01-bora-handoff-delta-permissions-inbox.md)
- Follow-up raw file: [2026-10-01-bora-campaign-sms-hold.md](../../raw/sources/2026-10-01-bora-campaign-sms-hold.md)
- Follow-up raw file: [2026-10-13-bora-push-sound-channel.md](../../raw/sources/2026-10-13-bora-push-sound-channel.md)
- Follow-up raw file: [2026-10-21-bora-push-device-binding.md](../../raw/sources/2026-10-21-bora-push-device-binding.md)
- Date: 2026-09-30
- Author: direct user direction with Claude Code implementation
- Ingested: 2026-09-30

## Core Claims

- Every notification is an inbox row plus one delivery row per external channel, written in one transaction; a leased, retrying cron worker sends push (Expo), email (Resend batch), and SMS (Hubtel). User writes never wait on or fail because of a provider.
- The client key picks the inbox: the customer app reads the CUSTOMER audience and the admin portal the STAFF audience, even for the same person.
- Staff notifications are admin-inbox only. Customers get support replies and resolutions in the inbox and by push; notification text names only the case number.
- Signup welcome, KYC approval, deposit, and withdrawal events keep their own templated email, SMS, and push and also add an inbox-only item keyed by the event, so repeats never duplicate it. Since 2026-10-21 a customer-app sign-in sends a `NEW_SIGNIN` security alert to the account's other signed-in phones instead of the welcome-back push; it stays out of the inbox. Push devices are per install and session-bound; see [[bora-push-device-binding|Bora Push Notifications Bound To Device And Session]].
- Every push carries the Bora sound and Android channel (2026-10-13): `sound: "bora_signature_v1.wav"` for iOS and `channelId: "bora_updates_v1"` for Android. `sendPushNotification` applies them as overridable defaults. The app bundles the file and creates the channel; a sound change ships as a new `_v2` file and channel together, because Android channel sounds are fixed once created. Expo does not display an Android push whose channel is missing on the device, while iOS falls back to the default sound when the file is missing. Per-token capability gating (`capabilities`, `appVersion`, a feature switch), proposed by the mobile developer, was rejected because the app is not in production and every build is a fresh install. It becomes necessary for any channel change after launch.
- Marketing consent: customers are never asked, receive marketing by default, and can switch off push, email, or SMS. In-app marketing is never gated. Consent is checked again at send time for marketing deliveries because paced SMS can take hours.
- Campaigns always create inbox items and add consented channels per recipient; dispatch is resumable through a compare-and-swap cursor and cancel works mid-send.
- Campaign SMS is on hold until the user finishes investigating Hubtel: unless `CAMPAIGN_SMS_ENABLED` is exactly `true`, SMS campaigns cannot be scheduled, sent, or tested, and dispatch queues no SMS. OTP and transaction SMS are unaffected.
- Email unsubscribe uses the mail app's one-click button (RFC 8058) posting to the API itself; no website is involved.
- Banner images follow LivelyCura custom-app banners: upload inside create/update, store an `Upload` record, reference it by `imageId`, and build URLs from `UPLOADS_BASE_URL`.

## Useful Details

- Hubtel's 5 requests per minute are shared with OTPs, so the worker sends one SMS per 30 seconds; SMS campaigns are impractical at scale until Hubtel batch sending is confirmed.
- Customer audience filters must treat a missing `accessChannels` as CUSTOMER (matching sign-in) and a missing `kycStatus` as PENDING.
- Bora storage stays private by default; a public-folder list (only marketing banners) replaces LivelyCura's private-folder list. Banner fields are validated before the upload so invalid requests leave nothing in storage; LivelyCura's upload intents and reconciliation worker were not ported.
- Required configuration: `UPLOADS_BASE_URL`, `API_PUBLIC_URL`, `UNSUBSCRIBE_TOKEN_SECRET` (32+ characters), and cron jobs enabled. `.env.default` is ignored by git, so these variables are not recorded in the repository and must be set on the deployment directly.
- The existing storage helper was dead code whose upload API had been removed; its AWS SDK also failed to load from stale nested `node_modules`. A cached App Platform build may need its cache cleared on the first deploy.
- Frontend handoff: `docs/frontend-handoff-app.md` and `docs/frontend-handoff-admin.md`; the per-feature docs were retired on 2026-10-01.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[bora-realtime-support-subscriptions|Bora Realtime Support Subscriptions]]
- [[bora-customer-support-administration|Bora Customer Support Administration]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]

## Contradictions Or Tensions

- The user first chose opt-in-with-opt-out consent, then proposed removing consent, then kept opt-out after the legal, platform, and deliverability risks were explained.
- The plan assumed an existing upload service; it had no callers, private ACLs, and a broken SDK install, so banner uploads were rebuilt on the LivelyCura pattern.
- Staff support notifications were first built with email and then limited to the admin inbox at the user's direction.

## Open Questions

- Does Hubtel's `batch/simple/send` endpoint exist on `smsc.hubtel.com`, and what is the production rate limit?
- Should transactional SMS be prioritized over marketing SMS before any transactional SMS uses the queue? (Capping SMS campaigns was superseded by the hold.)
