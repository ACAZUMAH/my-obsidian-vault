---
type: source
status: active
created: 2026-10-08
updated: 2026-10-08
tags: [altin, mobile, profile, support, ui, verification]
sources:
  - ../../raw/sources/2026-10-08-altin-profile-support-ui-corrections.md
confidence: high
---

# Altin Profile and Support UI Corrections

## Source

- Raw file: [Altin profile and support UI corrections](../../raw/sources/2026-10-08-altin-profile-support-ui-corrections.md)
- Date: 2026-10-08
- Author: user, through an Altin Partner Mobile Claude Code session
- Ingested: 2026-10-08

## Core Claims

- User correction: UI work is not done until every new or changed screen has been viewed on the running simulator. Type-checks and code reviews do not establish acceptable UI.
- Mobile Profile is read-only; the header Edit is the single entry point for photo, alternate phone, phone-number change, and verification.
- No Altin web app actually saves profile edits: partner, admin, and ERP saves are stubs. The API can update only the photo and alternate phone, so name, email, city, and about stay read-only until the backend extends `updateProfile`.
- Support composes its reply bar like SERLP's composer: one bar with attach, a growing input, and a round send button.

## Useful Details

- On card surfaces, the shared secondary button (`surfaceMuted` fill) reads as disabled; Support uses dashed add tiles and Profile uses a flush text action instead.
- A ticket without an organization cannot load its linked orders' details; rows name the order by id with an explanatory note.
- Choices inside forms use the field-label variant of `FilterChoices`, matching other form labels.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]].
- [[altin-profile-support|Altin Profile and Support]].
- [[../syntheses/personal-operating-manual|Personal Operating Manual]].

## Contradictions Or Tensions

- Supersedes the earlier Profile view with Change number and Verify actions; those moved into Edit profile at the user's direction.

## Open Questions

- When will the backend add name, city, and about to `updateProfile`?
