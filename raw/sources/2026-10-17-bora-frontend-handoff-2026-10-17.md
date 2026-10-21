# Bora frontend handoff 2026-10-17 and the restored 2026-10-13 handoff

Date: 2026-10-17
Source: The user's request "now write a hand off", git push history, and the user's answer that the 2026-10-13 handoff had been sent.

## Facts

- `fc3fa4a`, which contained `docs/frontend-handoff-2026-10-13.md`, was pushed to `origin/feature/updates` on 2026-10-13 at 20:08 UTC. The user confirmed that this version was sent to the frontend developer.
- On 2026-10-16 the agent extended that same file with the rejected-KYC correction (`updateKyc`, `kycSubmission`) and the Grow Wealth cash movement statement. The user's push `3bea375` on 2026-10-17 published the extended file. This broke the frozen-once-sent rule.

## Resolution

- `docs/frontend-handoff-2026-10-13.md` was restored to its `fc3fa4a` (sent) content.
- `docs/frontend-handoff-2026-10-17.md` covers only what changed since then: a correction of the sent item that said not to show a correction form for rejected KYC; correcting a rejected KYC through `updateKyc` with `kycSubmission`, including the null-submission case for KYC sent before the release; and the cash movement statement.
- KYC `BAD_GATEWAY` errors reach the client as the generic "Internal server error", because 5xx messages are hidden. The app shows its own contact-support message, and the KYC stays `SUBMITTED`.
- All 3 GraphQL examples validated against the executable schema.

## Lesson

A pushed handoff file is probably sent. Check `git reflog show origin/<branch>` before extending a dated handoff, and if its commit was already pushed, start a new dated file.
