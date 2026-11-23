# Bora frontend handoff sent status is not shown by git

Date: 2026-10-22
Source: Direct user correction after the Bora push-notification work (paraphrased; the user's wording was emphatic).

## What happened

During the push-notification fix the agent added the new push-device contract as section 3 of `docs/frontend-handoff-2026-10-17.md`. The file was uncommitted, and the vault rule said unpushed updates extend one handoff "until the batch is pushed and sent", so the agent treated it as unsent. The change was committed in `3699212`.

## User correction

The user had already sent both the 2026-10-13 and the 2026-10-17 handoffs to the frontend developer. They had said several times that new frontend-affecting changes go in a new handoff. An uncommitted or unpushed handoff is not proof that it is unsent.

## Resolution

- `docs/frontend-handoff-2026-10-17.md` was restored to the version the user sent: only the agent's additions were removed, and its KYC and Grow Wealth sections are unchanged.
- The push-device contract, the `NEW_SIGNIN` alert, and a correction of the 2026-10-13 statement that `addUserExpoPushToken` is unchanged moved to a new `docs/frontend-handoff-2026-10-22.md`.
- Rule going forward: before adding to an existing dated handoff, ask the user whether it has been sent. If it has, or the answer is unknown, start a new dated handoff.
