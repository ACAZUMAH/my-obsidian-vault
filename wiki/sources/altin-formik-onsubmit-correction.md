---
type: source
status: active
created: 2026-10-09
updated: 2026-10-09
tags: [altin, mobile, forms, formik, support, livelycura]
sources:
  - ../../raw/sources/2026-10-09-altin-formik-onsubmit-correction.md
confidence: high
---

# Altin Formik onSubmit Correction

## Source

- Raw file: [Altin Formik onSubmit correction](../../raw/sources/2026-10-09-altin-formik-onsubmit-correction.md)
- Date: 2026-10-09
- Author: user, through an Altin Partner Mobile Claude Code session
- Ingested: 2026-10-09

## Core Claims

- User correction: Formik's `onSubmit` never makes backend requests. Form hooks hold only state: a private Yup schema, `initialValues`, `validateOnMount: true`, `onSubmit: () => {}`, and `return form`.
- Edit form hooks take the loaded record, memoize `initialValues`, and set `enableReinitialize: true`. No seeded refs or effects.
- Requests live in a screen `handleSubmit` that reads `form.values`, calls the named mutation action, and navigates on a result. Multi-step screens keep that state and those handlers in a `use…Screen` hook. Buttons use the mutation's `loading` and `form.isValid`.
- References: the LivelyCura pharmacy portal, the admin portal, and the Check City app, not SERLP.
- User verdict: the Altin Profile and Support work was bad and will be redone, starting from Check City's Support UI.

## Useful Details

- Pharmacy portal: 166 of about 175 form `onSubmit` values are `() => {}`. Its handlers sit mostly in page components (139 files), a few in page hooks.
- Check City Support has 19 files and 1,370 lines. It is chat-first:
  - a topic sheet, then a welcome block, then a shared composer;
  - the first message creates the case, with the subject derived from the topic or order;
  - the case screen is the thread, with a centred context line, bubbles, scroll-to-end, and no success toasts.
- Altin Support has 52 files and 3,559 lines.
  - Ticket details stack five cards with the conversation last, and there is a toast on every reply.
  - Status is shown three times.
  - Attachments show as bare "Attachment" links, and every linked order runs its own query.
  - The list behaves like a records explorer.
- The 2026-10-09 Altin pass converted all 17 Formik hooks. Independent reviews checked behavior against saved originals, and type checks pass.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]].
- [[altin-profile-inline-edit-correction|Altin Profile Inline Edit Correction]].
- [[altin-orders-mobile-web-reference|Altin Orders mobile web reference]].
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]].

## Contradictions Or Tensions

- Supersedes the 2026-09-12 rules that form hooks call named mutations in `onSubmit`, use `isSubmitting`, and seed edit forms once.
- Supersedes the same-day claim in [[altin-profile-inline-edit-correction|the inline edit correction]] that the repository's committed hooks are the form reference.

## Open Questions

- Should Altin's Raise a ticket become chat-first with a derived subject, and should the order issue report open or reuse a ticket conversation? These are product decisions for the user.
