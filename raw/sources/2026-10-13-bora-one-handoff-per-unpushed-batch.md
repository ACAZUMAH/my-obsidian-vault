# Bora one handoff per unpushed batch

Date: 2026-10-13
Source: direct user correction.

After the 2026-10-12 rule (never edit a sent handoff; write a new one), the agent split the current unpushed work across `docs/frontend-handoff-2026-10-12.md` and `docs/frontend-handoff-2026-10-12-errors-and-accounts.md`, and asked whether to write yet another note for the removed refresh limit. The user said none of these updates had been committed or pushed, so they all belong in one handover, not separate ones.

Resolution: one `docs/frontend-handoff-2026-10-13.md` covers the whole unpushed batch in its final state (no refresh rate limit). It includes another session's uncommitted currency, rate, lookup-filter, and Grow Wealth error notes, which had been sitting inside the sent `frontend-handoff-app.md`. The two split files were deleted, and `frontend-handoff-app.md` was restored to its committed (sent) version. All GraphQL examples in the combined file were validated against the live schema.
