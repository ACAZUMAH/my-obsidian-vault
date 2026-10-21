---
type: source
status: active
created: 2026-10-09
updated: 2026-10-09
tags: [altin, mobile, profile, forms, phone-numbers, livelycura]
sources:
  - ../../raw/sources/2026-10-09-altin-profile-separate-editors-correction.md
confidence: high
---

# Altin Profile Separate Editors Correction

## Source

- Raw file: [Altin profile separate editors correction](../../raw/sources/2026-10-09-altin-profile-separate-editors-correction.md)
- Date: 2026-10-09
- Author: user, through an Altin Partner Mobile Claude Code session
- Ingested: 2026-10-09

## Core Claims

- User correction: values saved by different APIs are edited and saved separately, never through one combined form or Save. Altin Profile's photo, phone number and alternate phone each have their own in-place editor.
- User correction: phone inputs take local numbers and convert them with `awesome-phonenumber`; members never type the country code.
- The editors follow the admin portal's section editors. A view/edit toggle sits in each section, and the edit component owns its form hook and handler.

## Useful Details

- Shared helpers in Check City and the admin portal: `validatePhoneNumber` (region GH), `getPhoneNumberWithCode` (E.164), and `getPhoneNumberWithZero` (local form for prefill). Altin now has the same helpers in `src/helpers/phoneNumbers.ts`.
- `user.updateProfile` requires `profilePictureId`. Saving the photo alone resends the current alternate number, and saving the alternate alone resends the current photo id.
- Order creation still validates recipient phones with the old +233 pattern.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]].
- [[altin-formik-onsubmit-correction|Altin Formik onSubmit Correction]].
- [[altin-profile-inline-edit-correction|Altin Profile Inline Edit Correction]].
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]].

## Contradictions Or Tensions

- Supersedes the inline-edit correction's single edit mode, in which one Save handled the photo, the alternate number and a phone change.

## Open Questions

- Should order creation and other phone inputs move to local entry with `awesome-phonenumber` too?
