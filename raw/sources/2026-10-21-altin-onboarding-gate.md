# Altin Partner Mobile: onboarding (KYC) and the post-sign-in gate

- Date: 2026-10-20 to 2026-10-21
- Author: the user (Caleb), through an Altin Partner Mobile Claude Code session
- Repository: `altin-partner-mobile`, branch `feature/apps`, uncommitted when recorded
- Repository records: `docs/onboarding.md`, the `AGENTS.md` "Onboarding and the post-sign-in gate" section

## The user's request (verbatim, 2026-10-20)

> we coming to work on the final part of the app. the kyc and onboarding, so attached is an implement plan but it's not that clear and it doesn't follow our architecture, the one who built the web apps sent it to me. So I got some small fear idea of how the flow will. so if the employee logs in and they don't have an org we show a screen with the they don't a have an org yet so the should contact support, if the have an org and it's not been approved yet same show screen with org pending approval with contact support. then if the org is approved but the have been onboarded yet we show them the onboarding screen. let's do some planning

The attached plan is the web developer's `docs/partner-onboarding-flow.md` in the repository.

## What research established (web partner app, admin app, generated schema)

- A super admin creates every organization and names an existing user its first admin; there is no self-signup.
- Organizations start `PENDING_APPROVAL`. Only the partner app creates the KYC profile, uploads and resubmits documents, and resubmits for approval; the admin app has no call site for those mutations.
- Admin approves documents, verifies the profile (enabled only when every REQUIRED checklist entry has enough approved documents; SOFT_GATE only warns), then approves the organization. Its copy says approval requires a verified profile. Rejection needs a reason (`REJECTED`); the partner resubmits for approval.
- Invalidating a document or changing the tier moves an approved organization back to pending. Suspend sets `PAUSED`, Close sets the terminal `CLOSED`.
- There is no "onboarded" flag and no push notification for status changes.
- So the user's first ordering (pending → contact support, approved → onboarding) would deadlock: onboarding is how an organization becomes approved.

## The user's decisions (answers to the planning questions, 2026-10-20)

- Pending flow: "KYC first, then waiting" — pending or rejected with KYC unfinished opens onboarding; once every required document is submitted, a "Pending approval, contact support" state; rejected shows the reason and Resubmit.
- After approval: "Nothing more, open app" — KYC upkeep lives under More.
- Contact support: "WhatsApp + phone + email" — the values were not supplied; they are placeholders and a release blocker.
- Paused and closed: "Blocking screen".
- Plan approved with defaults: auto-select a single membership; resubmit for approval waits until flagged documents are fixed; no polling for approval.

## Later instructions and corrections

- 2026-10-21: "continue and take note the app talks to the production api so thread lightly". Earlier the same day: "open Edit/create, then cancel, never submit" and "Uploads and the mutations stay offline-only; on the device just open the editor and cancel."
- Adversarial review (2026-10-21): the user chose "Fix findings 1, 3, 4, 5 and 6 together in one pass, verify them, then report. Leave #2 as a follow-up." Finding 1 was a regression in the new System error rule; finding 2 (an expired token on resume still remounts navigation) predates this work.
- Layout (2026-10-21), verbatim:

> before we move to the next step. please let's do some thing about the ui on the things you change the onboarding is so long don't you think it makes sense to use tabs because they will have to scroll a lot to get it done, and I want to do research on either to move it to the apps section and naming it compliance and under compliance we have onboarding and under onboarding we have profile, documents, and status history or have it still on the more screen but separated into a section called compliance then we have three stuff there under it profile, documents and status history or we still have only onboarding then when they tab open a screen containing the three rather

  The assistant recommended against an Apps "Compliance" module and against three separate More rows, because members of a pending organization never see Apps or More (onboarding is their root screen), so either would duplicate the gate screen. The user chose:

> Go with tabs: one Onboarding screen, status card on top, Profile / Documents / History tabs (port serlp DetailTabs), default tab = next job, gate actions in a header menu, and a Compliance section header on More.

## Live findings (read-only, production)

- An ACTIVE fleet organization had no business profile and 0 of 9 required documents, so the backend did not enforce "approval requires a verified profile" for it. The approved-stage card therefore says "Organization approved", not "verified".
- A pending shipper organization opened onboarding as the gate root with three required entries; switching organization from the gate returned to Home.
- After sign-out, Keycloak showed its login form, so a different account can sign in (no `prompt=login` change needed).

## Implementation summary

- `stack.tsx` gates on status and `VIEW_KYC` only; `gateRoutes` uses the composite navigation key `${org}:${gate}`, proven against the real React Navigation router (without it, approval strands the member on onboarding).
- System freshness: memberships are not persisted and are `null` until loaded; SystemProvider blocks only before the first load; System reloads on a real foreground return (60 s minimum) and on pull in gate screens; `signOut` clears the Apollo cache.
- `src/onboarding`: status card, tabs, in-place profile create/edit, document upload and resubmit (photos/PDFs, 1–10, sequential upload with a fresh token per file), resubmit for approval, history. `src/organizations` owns the status notices.
- Shared additions: `Notice`, `ContactSupport`, `DatePickerSheet` and `DetailTabs` (both ported from serlp-mobile), a neutral `ModuleHeader` right action, `DetailAction.immediate`.
- Verification: 118 offline checks with mocks; read-only simulator checks; no KYC mutation, upload or support contact was exercised against production.

## Follow-ups

- Supply the support WhatsApp, phone and email values.
- An expired token on resume still unmounts navigation (the auth link should await the refresh).
- Low review findings: forced logouts skip the cache clear; date-format helper reuse; a neutral label for transitions without an actor; iOS call-prompt cancel toast.
- Not built: first-outlet step after approval, push notifications for status changes, camera capture.
