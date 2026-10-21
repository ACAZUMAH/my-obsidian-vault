# Bora Notifications, Marketing Campaigns, And Banners — Decisions And Implementation

Date: 2026-09-30
Source: direct user direction in Claude Code during Bora backend notification and marketing work (2026-09-29 to 2026-09-30)

## User Direction

- The work is backend APIs only; a colleague builds the customer app and admin portal from handoff documentation.
- Scope: push notification when staff reply to support, one notification system for the admin portal and the app, scheduled push/email/SMS campaigns, and marketing. News is out of scope because the frontend scrapes it from Bora's website.
- Delivery design chosen: stored notifications plus a retry worker. Existing welcome, KYC, deposit, and withdrawal notifications move into the inbox only as a later step with explicit approval (deposit/withdrawal code is otherwise off limits).
- Marketing means in-app banners/promotions.
- Consent chosen: customers are opted in and can opt out. Later the user proposed removing consent entirely ("they are supposed to receive it if a marketing is sent"); after the risks were laid out, the user chose to keep per-channel opt-out. In-app marketing (inbox items, banners) must never be consent-gated.
- Staff support notifications go to the admin portal inbox only; no email.
- Resend and Hubtel both offer batch sending and must be used for deliveries and campaigns. Hubtel's documentation shows no bulk endpoint; the user will test `smsc.hubtel.com/v1/messages/batch/simple/send` themselves.
- Email unsubscribe must not depend on a website: use the mail app's own unsubscribe and point customers to the app settings. The user initially believed no public URL existed; the backend API's own public address is used.
- Banners appear on the home screen only. Call-to-action links are HTTPS only because app deep links are unconfirmed.
- Banner images must be uploaded the way LivelyCura custom-app banners are: the image is uploaded before the banner is saved, and the banner stores the returned upload record.
- End-to-end live testing is deferred until all the planned work is finished.
- The user asked where push, email, and SMS are actually sent, reading `notifyUsers` as only creating inbox items; the delivery worker was explained.

## Agent Evidence

- Hubtel allows 5 SMS requests per minute, shared with OTP delivery. The worker sends at most one SMS per 30 seconds; at that pace an SMS campaign to 1,000 recipients takes about 8 hours, and the SMS queue is first-in, first-out.
- Sign-in treats users without an `accessChannels` field as customers, and invited staff are created with an empty `accessChannels`; customer audience filters must match missing-or-CUSTOMER. Missing `kycStatus` means PENDING (model default).
- Apple guideline 4.5.4, Ghana's Data Protection Act 2012 (Act 843) section 40, and Gmail/Yahoo bulk-sender one-click unsubscribe rules were the reasons given for keeping opt-out; without it, customers' only escape (blocking the SMS sender, reporting spam, disabling notifications) also stops OTPs and transactional messages.
- RFC 8058 one-click unsubscribe works through `List-Unsubscribe` and `List-Unsubscribe-Post` headers that make the mail provider POST to the sender. A GET on the link must never change state because email security scanners open links.
- Bora's `uploadStreamToStorage` had no callers: the upload GraphQL module and services were removed in commit `1bb0cf2`, and the security-hardening commit `485e6b1` made uploads private. The removed `uploadPhoto` passed a string where a regex was intended, so data-URL uploads were never stripped of their prefix.
- `@aws-sdk/client-s3` failed to load (`Package subpath './retry' is not defined by "exports"`) from stale nested `@aws-sdk`/`@smithy` folders in local `node_modules` that were absent from `yarn.lock`; `yarn install --force` did not prune them. Rebuilding those scopes fixed it. A cached App Platform build could carry the same drift.
- LivelyCura custom-app banners take `imageFile` (base64) in create/update, upload through `uploadPhoto` → `persistUploadBuffer` (durable upload intents plus a reconciliation worker), store an `Upload` record (filename, directory, mimeType, size), reference it by `imageId`, expose `image: Upload!`, and build URLs from `UPLOADS_BASE_URL`; LivelyCura storage is public by default with a private-directory list.

## Implemented Scope

- Notification core: `Notification` (inbox item with audience, category, target, dedupe key) and `NotificationDelivery` (one row per channel) written in one transaction by `notifyUsers`; a cron worker every 5 seconds leases deliveries, sends push through Expo, email through Resend batch (100 per request, idempotency key), and SMS through Hubtel one at a time, retries with capped exponential backoff for 5 attempts, and never reclaims an SMS lease (marks it `SMS_OUTCOME_UNKNOWN`).
- Inbox APIs and `myNotificationReceived`; the client key selects the CUSTOMER or STAFF inbox.
- Support notifications: staff replies and resolutions notify the customer (inbox plus push); new cases and customer messages notify the eligible assignee or every active holder of `supportCases.respond` (admin inbox only). Text names only the case number.
- Marketing preferences (push, email, SMS; unset means opted in), a notification `category`, and a send-time consent check for marketing deliveries.
- Campaigns: admin CRUD, audience preview, DRAFT/SCHEDULED/SENDING/SENT/CANCELLED lifecycle, dispatch cron every 30 seconds in 200-user batches with a compare-and-swap cursor, per-recipient channel filtering, cancel mid-send, stats, audited lifecycle actions, and test sends to the acting admin through the worker's own senders with a one-minute cooldown.
- Email unsubscribe: HMAC-signed tokens, one-click headers on marketing emails only, a POST endpoint beside the Paystack webhook, a GET that only explains, and a plain-text footer pointing to app settings.
- Banners: draft-only editing, audited publish/unpublish, `getActiveMarketingBanners(placement: HOME)`, and LivelyCura-style uploads (`Upload` model, strict PNG/JPEG/WebP structure validation, public-folder list because Bora defaults private, field validation before upload, stored-file cleanup when the record fails, no upload-intent machinery).
- Frontend handoff: `docs/notifications-marketing-api.md`, with every GraphQL example validated against the schema and depth limit.
- Final verification on 2026-09-30: build, Prettier, and diff checks passed; 138 test suites and 835 tests passed; each step's guards were mutation-checked.
