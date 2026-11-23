---
type: source
status: active
created: 2026-10-21
updated: 2026-10-21
tags: [altin, mobile, onboarding, kyc, navigation, livelycura]
sources:
  - ../../raw/sources/2026-10-21-altin-onboarding-gate.md
confidence: high
---

# Altin Onboarding and the Post-Sign-In Gate

## Source

- Raw file: [Altin Partner onboarding and gate](../../raw/sources/2026-10-21-altin-onboarding-gate.md)
- Date: 2026-10-20 to 2026-10-21
- Author: user, through an Altin Partner Mobile Claude Code session; repository `docs/onboarding.md` and `AGENTS.md`
- Ingested: 2026-10-21

## Core Claims

- Onboarding (the organization's KYC) is how an organization gets approved: members file the business profile and documents while it is pending, Altin reviews, and only then does it become active. The user's first ordering (pending → contact support, approved → onboarding) was corrected after research; the user chose "KYC first, then waiting".
- User decisions: no membership → a "no organization yet" notice with contact support and sign out; pending or rejected with KYC unfinished → onboarding; every required document submitted → "Pending approval"; active → the app, with KYC upkeep under More; paused or closed → a blocking notice. Members without `VIEW_KYC` get a "waiting on your admin" notice.
- The navigation gate reads only the organization status and `VIEW_KYC`, never KYC data, and its route group uses a composite navigation key so approval or a status change lands cleanly on the new entry screen.
- User decision (2026-10-21): onboarding is one screen with the status card on top and Profile, Documents and History tabs, opening on the next job; account actions before approval sit in a header menu; More gains a Compliance section. Moving it into an Apps "Compliance" module or splitting it into three More rows was rejected because pending members can't reach Apps or More.
- User instruction: the app talks to the production API, so KYC writes, uploads and support contacts are verified offline only; on the device editors are opened and cancelled.

## Useful Details

- System freshness: memberships are never persisted and are `null` until System loads; SystemProvider blocks only before the first load, with an in-flight load beating a redelivered error; System reloads on a real foreground return (at most once a minute) and on pull in gate screens; sign-out clears the Apollo cache.
- Uploads: photos or PDFs, 1–10 per document, uploaded one at a time with a fresh token per file; uploaded blob ids are kept so a retry skips them. Expiry dates come from a ported calendar sheet and must be after today; expired documents need a new date.
- Envelope exceptions: the profile query's `success:false` means "no profile yet" and the checklist's means "no tier yet"; both show the server message instead of an error.
- Live finding: one active organization had no profile and no documents, so approval without a verified profile happens in practice; the approved card says "approved", not "verified".
- The support WhatsApp, phone and email values were not supplied; they are placeholders and a release blocker, and the contact buttons stay hidden until set.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]]
- [[altin-permission-gating|Altin Permission Gating]]: the status gate is the one carve-out from "never gate a route by unregistering it".
- [[altin-profile-inline-edit-correction|Altin Profile Inline Edit Correction]]: the in-place editing precedent the KYC editors follow.
- [[altin-reports-mobile|Altin Reports Mobile]]: the preceding feature, built in the same session family.

## Contradictions Or Tensions

- The admin app's copy says approval requires a verified profile, but a live active organization had none. The mobile copy follows the observed state.
- The web app never blocks on status (banner plus a one-time redirect); the mobile app blocks by user decision.

## Open Questions

- What are the support WhatsApp, phone and email values?
- Should the auth link await the token refresh so an expired token on resume no longer unmounts navigation?
- Should approval prompt for a first outlet, and should status changes arrive by push?
