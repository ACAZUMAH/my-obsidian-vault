# Bora frontend handoffs are for the frontend developer only

Date: 2026-10-26
Source: Direct user correction after the fund fact-sheet handoff `docs/frontend-handoff-2026-10-24.md` (paraphrased; the user was emphatic).

## What happened

The agent copied the "Open items" section from the earlier handoff format and filled it with items meant for the user, the backend owner:

- a stale staging-storage claim;
- a deferred backend decision (stale-screen `expectedDraftUpdatedAt` check, deferred with versioning);
- a product question for the user ("no way to withdraw a published PDF; ask if Bora needs one");
- a repeat of the scope note already in the intro.

## User correction

The user writes handoffs to send to the frontend developer. Anything directed at the user does not belong there: backend open questions, deferred backend decisions, backend-owned operational issues, and questions for the user.

## Resolution

- Those items were removed from `docs/frontend-handoff-2026-10-24.md`. Only the frontend-relevant note remains: check file references against the latest `develop`.
- Rule: a frontend handoff contains only what the frontend developer must know or do. Backend open questions, decisions, and questions for the user go to the user in chat, never into the handoff. Do not copy a section from an earlier handoff without checking that each item is for the frontend.
