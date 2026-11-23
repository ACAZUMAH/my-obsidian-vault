# Bora staging storage was already fixed; do not repeat third-party status claims

Date: 2026-10-26
Source: Direct user correction after the fund fact-sheet PDF work (paraphrased; the user was emphatic).

## What happened

Kusantec's 23 Oct fact-sheet handoff said staging banner uploads fail with 502 and asked for the staging `SPACES_*` settings to be checked. The agent repeated that claim as current fact in `docs/frontend-handoff-2026-10-24.md`: in the `BAD_GATEWAY` error note, in the admin acceptance tests ("once its storage works"), and as an open item. It also put it in the vault's fact-sheet Source Record and in the backend project page.

## User correction

The user had already updated the staging storage URL setting (an `http://` URL issue), so the 502 claim was stale. The user said they had told the agent this; it was not in that session's conversation or in the vault.

## Resolution

- The staging-storage claims were removed from `docs/frontend-handoff-2026-10-24.md` and from the vault pages.
- Rule going forward: a status claim taken from a third-party handoff or document (for example "staging X is broken") is not current fact. Confirm it with the user before writing it into a handoff, plan, or the vault.
