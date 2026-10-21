# Bora frontend handoffs frozen once sent

Date: 2026-10-12
Source: direct user correction.

During the 2026-10-11/12 rate-limiting and KYC work, the agent appended new sections (sign-in lock, token refresh, signup limit, KYC rejection reason) to the already-sent `docs/frontend-handoff-app.md` and `docs/frontend-handoff-admin.md`, following the earlier convention of updating those two files with every frontend-facing change.

The user objected strongly: whenever new updates are implemented, write a new handover markdown file to send to the frontend developer, and never update what has already been sent.

Resolution: the agent's edits to both sent handoffs were reverted (the admin file is back to its committed state; in the app file only the agent's own edits were removed, leaving another session's uncommitted currency, lookup-filter, and Grow Wealth additions untouched), and the changes were moved into a new `docs/frontend-handoff-2026-10-12.md`.
