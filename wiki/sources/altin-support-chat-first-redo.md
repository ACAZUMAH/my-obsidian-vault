---
type: source
status: active
created: 2026-10-09
updated: 2026-10-09
tags: [altin, mobile, support, ux, livelycura]
sources:
  - ../../raw/sources/2026-10-09-altin-support-chat-first-redo.md
confidence: high
---

# Altin Support Chat-First Redo

## Source

- Raw file: [Altin support chat-first redo](../../raw/sources/2026-10-09-altin-support-chat-first-redo.md)
- Date: 2026-10-09
- Author: user, through an Altin Partner Mobile Claude Code session
- Ingested: 2026-10-09

## Core Claims

- User decision: a support ticket's subject is derived from the selected category; members don't type one.
- User decision: an order that already has an issue doesn't get another one. Report an issue opens that order's live conversation (open, in progress, resolved) instead.
- Altin Support follows Check City's chat-first model:
  - the thread is the screen;
  - one composer starts and continues conversations;
  - a topic sheet starts them;
  - there are no success toasts.

## Useful Details

- The order lookup only sees tickets the server shows the member. A colleague's ticket stays invisible without VIEW_SUPPORT_TICKETS, so only a backend create-time guard can fully enforce one ticket per order.
- `navigation.popTo` reuses an already-open conversation; `replace` would duplicate it.
- A chat composer needs the keyboard-avoiding offset reduced by the bottom safe-area inset, so it sits on the keyboard.
- Open choices for the user:
  - live updates (no WebSocket link yet);
  - photo-library attachments;
  - a new-conversation action on closed tickets.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]].
- [[altin-formik-onsubmit-correction|Altin Formik onSubmit Correction]].
- [[altin-profile-support|Altin Profile and Support]].

## Contradictions Or Tensions

- Supersedes the 2026-10-08 form-and-records Support (typed subject, order picker, details cards) and the separate Orders issue-report form.

## Open Questions

- Should the backend reject or redirect a second live ticket on the same order?
