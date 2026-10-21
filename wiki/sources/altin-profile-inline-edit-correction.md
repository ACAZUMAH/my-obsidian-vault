---
type: source
status: active
created: 2026-10-09
updated: 2026-10-09
tags: [altin, mobile, profile, forms, formik, ux]
sources:
  - ../../raw/sources/2026-10-09-altin-profile-inline-edit-correction.md
confidence: high
---

# Altin Profile Inline Edit Correction

## Source

- Raw file: [Altin profile inline edit correction](../../raw/sources/2026-10-09-altin-profile-inline-edit-correction.md)
- Date: 2026-10-09
- Author: user, through an Altin Partner Mobile Claude Code session
- Ingested: 2026-10-09

## Core Claims

- User correction: editing must not chain screens. The Profile header Edit makes the same screen editable; multi-step fields such as an SMS code appear inline, not on another screen.
- User correction: write Formik hooks the way this repository's committed form hooks are written. Do not go to SERLP or another reference project for form structure when the repository already has the pattern.
- The repository's form-hook shape: private `validationSchema`, parameterless `use…Form()` owning its resource, refresh, and named mutation hooks, typed `useFormik` with `validateOnMount` and a guarded `onSubmit`, and a `{ form, loading, resource, ... }` return bound directly by the screen.

## Useful Details

- Assistant-written files are untracked in the working tree; the user's own reference hooks are the committed ones.
- Extras that made the rejected hook messy: seeding refs, a hand-computed "changed" flag, picker state, upload-and-retry inside `onSubmit`, and navigation helpers.
- Profile saves the photo and alternate number first, then requests the code, and confirms the code last, so a failed confirmation never replays a used code.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]].
- [[altin-profile-support-ui-corrections|Altin Profile and Support UI Corrections]].
- [[altin-orders-mobile-web-reference|Altin Orders mobile web reference]].
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]].

## Contradictions Or Tensions

- Supersedes the 2026-10-08 Profile design in which Edit profile was a separate screen and phone change and verification opened further screens.

## Open Questions

- None from this correction.
