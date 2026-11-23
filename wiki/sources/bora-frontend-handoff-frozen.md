---
type: source
status: active
created: 2026-10-12
updated: 2026-11-22
tags: [bora-capital, backend, frontend-handoff, workflow]
sources:
  - ../../raw/sources/2026-10-12-bora-frontend-handoff-frozen.md
  - ../../raw/sources/2026-10-13-bora-one-handoff-per-unpushed-batch.md
  - ../../raw/sources/2026-10-17-bora-frontend-handoff-2026-10-17.md
  - ../../raw/sources/2026-10-22-bora-handoff-sent-status-correction.md
  - ../../raw/sources/2026-10-25-bora-fund-fact-sheet-pdfs.md
  - ../../raw/sources/2026-10-26-bora-handoff-audience-frontend-only.md
  - ../../raw/sources/2026-10-28-bora-new-handoff-per-update-and-portal-ownership.md
  - ../../raw/sources/2026-11-22-bora-frontend-handoff-2026-11-22.md
  - ../../raw/sources/2026-11-22-bora-email-case-insensitive-matching.md
source_date: 2026-10-12
ingested: 2026-10-12
confidence: high
---

# Bora Frontend Handoffs Frozen Once Sent

## Source

- Raw file: [Direct user correction](../../raw/sources/2026-10-12-bora-frontend-handoff-frozen.md)
- Raw file: [Restored sent handoff and 2026-10-17 handoff](../../raw/sources/2026-10-17-bora-frontend-handoff-2026-10-17.md)
- Date: 2026-10-12
- Author: Direct user correction
- Ingested: 2026-10-12
- Refinement: [One handoff per unpushed batch](../../raw/sources/2026-10-13-bora-one-handoff-per-unpushed-batch.md), direct user correction on 2026-10-13.
- Correction: [Sent status is not shown by git](../../raw/sources/2026-10-22-bora-handoff-sent-status-correction.md), direct user correction on 2026-10-22.

## Core Claims

- A frontend handoff the user has sent to the frontend developer must never be edited.
- Each new backend update gets a new dated handoff, `docs/frontend-handoff-YYYY-MM-DD.md`, that states what it adds since the previous one (user correction, 2026-10-28, repeated). Add to an existing dated file only when the user says so for that update; an earlier "not sent" answer expires once the file is committed, pushed or a new update starts. Items are marked for the customer app or the admin portal ([raw evidence](../../raw/sources/2026-10-28-bora-new-handoff-per-update-and-portal-ownership.md)).
- The admin portal (`Kusantec/bora-admin-portal`) is the frontend developer's work, not the user's or the agent's. Its docs, CSVs, JSON and scripts are unverified and have put wrong data into the fund database; never use them as data. A handoff may state plainly, with file references, where portal code writes wrong data, and set rules for writing fund data (user correction, 2026-10-28).
- Git state does not show whether a handoff was sent (user correction, 2026-10-22). An uncommitted or unpushed handoff may already be with the frontend developer. Before adding to an existing dated handoff, ask the user whether it has been sent; if it has, or the answer is unknown, start a new dated handoff.
- Corrections to sent items are stated in the next handoff, not patched into the old one.
- A handoff is for the frontend developer only (user correction, 2026-10-26). Backend open questions, deferred backend decisions, backend-owned issues, and questions for the user go to the user in chat, never into the handoff ([raw evidence](../../raw/sources/2026-10-26-bora-handoff-audience-frontend-only.md)).

## Useful Details

- This replaces the 2026-10-01 convention of keeping two living handoff files (`frontend-handoff-app.md`, `frontend-handoff-admin.md`) and updating them with every change.
- `docs/frontend-handoff-2026-10-13.md` was pushed in `fc3fa4a` and sent; it is frozen at that content. It covers KYC rejection reason, error format, malformed-request messages, expired codes, sign-in lock, one-at-a-time refresh, signup limit, existing-customer accounts, currencies and rates, lookup filters, Grow Wealth provider errors, and notification sound.
- On 2026-10-16 the agent extended the sent 2026-10-13 file, and the extension was pushed in `3bea375`. On 2026-10-17 the file was restored to its sent content, and the additions moved to `docs/frontend-handoff-2026-10-17.md`: a correction of the sent "no correction form" item, rejected-KYC correction through `updateKyc`/`kycSubmission`, and the Grow Wealth cash movement statement. Check `git reflog show origin/<branch>` before extending any dated handoff.
- On 2026-10-21 the agent added the push-device contract to `docs/frontend-handoff-2026-10-17.md` because the file was uncommitted, but the user had already sent it. On 2026-10-22 the file was restored to its sent version, and the push contract, the `NEW_SIGNIN` alert, and a correction of the 2026-10-13 "`addUserExpoPushToken` is unchanged" statement moved to `docs/frontend-handoff-2026-10-22.md`. The 2026-10-13 and 2026-10-17 handoffs are both sent and frozen.
- On 2026-10-24 the user confirmed `docs/frontend-handoff-2026-10-22.md` was sent, so the fund fact-sheet contract and the `SetFundVisibilityInput` rename went to a new `docs/frontend-handoff-2026-10-24.md` ([raw evidence](../../raw/sources/2026-10-25-bora-fund-fact-sheet-pdfs.md)).
- On 2026-10-28 the agent extended `docs/frontend-handoff-2026-10-24.md` with the `sinceInceptionJourney` change on an earlier "unsent" answer, but the user had sent it. It was restored to its `47d0850` content, and the change, rules for writing fund data, and audited portal and app fixes went to `docs/frontend-handoff-2026-10-28.md`.
- On 2026-11-22 a new `docs/frontend-handoff-2026-11-22.md` was written for everything since the 2026-11-12 handoff, with the 2026-11-12 file left untouched ([evidence](../../raw/sources/2026-11-22-bora-frontend-handoff-2026-11-22.md)). The client checkouts were stale, so its line numbers refer to the remote `develop` commits it names. Read a client's latest code with `git show origin/develop:<path>`, never from a stale working tree.
- The owner confirmed `docs/frontend-handoff-2026-11-22.md` was sent, so the same-day correction to its section 5 (emails matched ignoring letter case; the app's no-lowercase build after this backend; the portal's forgot-password lowercasing) went to a new `docs/frontend-handoff-2026-11-22-emails.md`. A second handoff on the same date takes a short descriptive suffix ([evidence](../../raw/sources/2026-11-22-bora-email-case-insensitive-matching.md)).

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[bora-biometric-login-and-handoff-docs|Bora Biometric Login And Consolidated Frontend Handoff]]

## Contradictions Or Tensions

- Supersedes the 2026-10-01 instruction to update the two handoff files in place.
- On 2026-10-12 one unpushed batch was split across two dated files; the user corrected that on 2026-10-13, and they were merged.
- The 2026-10-13 rule "extend until the batch is pushed and sent" was read as "unpushed means unsent". The 2026-10-22 correction overrides that reading: sent status comes from the user, not from git.

## Open Questions

- None.
