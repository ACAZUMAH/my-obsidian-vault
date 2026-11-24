# LLM Wiki Log

Append-only chronological record of wiki operations. New entries go directly under this note.

## [2026-11-24] ingest | Bora Withdrawal Payouts Built

What changed:

- Preserved the owner's answers and the build instruction for withdrawal payouts.
- Recorded the production check: BCL's `fetchbanks` returns `{}` in production and has no `BankCode` in staging, so banks go by `BankID`.
- Recorded the owner's decision against name checks, and the build and push of `4310bb5`.

Files touched:

- `raw/sources/2026-11-24-bora-withdrawal-payouts-built.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/projects/bora-capital-mobile-app.md`
- `log.md`

Key result:

- Agents know the payout field contract, that bank numbers are stored only encrypted, and that payout accounts are never name-checked.

Follow-ups:

- BCL must load its production bank list, add the payout fields, and confirm `BankID` is enough.
- The frontend implements the 2026-11-24 handoff.

## [2026-11-24] ingest | BCL Production Live, Payout Field Names Requested

What changed:

- Recorded that BCL enabled production deposits and withdrawals, and that BCL agreed to add payout fields to `addcicashwithdrawal_bcl` and asked what Bora calls them.
- Captured the agent's mapping of payout data:
  - bank wallets keep only the last 4 digits and a nickname as `accountName`;
  - the app drops `BankID`;
  - `mobileNetwork` is free text.
- Captured the proposed field names (pending the owner).

Files touched:

- `raw/sources/2026-11-24-bora-bcl-production-live-and-payout-fields-request.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `log.md`

Key result:

- Agents know BCL is live and that the payout fields are being agreed. Bank payouts need Bora-side storage changes before any field can be filled.

Follow-ups:

- Owner approves or changes the field names and sends them to BCL.
- Get BCL's answers on branch codes, network codes, investor-name rule and number format.

## [2026-11-23] ingest | Bora Email Matching And BCL Fix Pushed

What changed:

- Recorded the owner-instructed commits and pushes on `feature/updates`:
  - `1ab2559`: case-insensitive email matching;
  - `6f053be`: the BCL sign-in 403 fix.
- The first push also carried `ca3cfa1`, the backlog.
- Replaced the stale "Uncommitted" and "Not pushed" statuses.

Files touched:

- `raw/sources/2026-11-23-bora-email-matching-and-bcl-fix-committed-and-pushed.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `log.md`

Key result:

- Agents know `feature/updates` matches origin at `6f053be`, with no PR and no deploy.

Follow-ups:

- A PR or deploy happens only when the owner asks.

## [2026-11-23] ingest | Bora BCL Sign-In 403 Hang Fixed

What changed:

- Preserved the owner's approval ("Yes, fix it") and the uncommitted fix.
  - The BCL client's 403 retry skips the sign-in request, so a refused sign-in fails at once instead of hanging every BCL call until a restart.

Files touched:

- `raw/sources/2026-11-23-bora-bcl-sign-in-403-hang-fix.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `log.md`

Key result:

- Agents know the sign-in 403 hang is fixed, not open. Verification: 217 suites, 2,026 tests; 3 mutation checks caught.

Follow-ups:

- Commit when the owner asks.

## [2026-11-23] maintenance | Capture-First Auto-Publish Rule

What changed:

- Recorded the user's directive: add vault-worthy knowledge straight away and tell the user afterward, and push every vault change right away.
- Added `scripts/publish_vault.py`, exposed as `python3 scripts/wiki_tool.py publish -m "<message>" -- <paths>`. It commits exactly the named files from a private index under an exclusive lock, scans added lines for secrets and personal emails, validates the exact committed tree, commits with compare-and-swap, and pushes without force.
- Added a Capture And Publish section to `AGENTS.md`. Rewrote the ingest, query, lint, and default-behavior rules, the workflow guide, the lint checklist, the scripts README, and the ingest, query, lint, and vault-maintenance skills. Schema contract v6 registers the publisher.
- Replaced "never push unless asked" in `~/.claude/CLAUDE.md` and added the same rule to `~/.codex/AGENTS.md`. Neither file is versioned. Hermes profile memories defer to `AGENTS.md` and needed no change.

Files touched: `AGENTS.md`, `schema/{workflows.md,lint-checklist.md,README.md,vault-structure.json}`, `scripts/{publish_vault.py,wiki_tool.py,README.md}`, four skill files, `raw/sources/2026-11-23-vault-capture-first-auto-publish-directive.md`, `wiki/sources/vault-capture-first-auto-publish-directive.md`, `wiki/syntheses/personal-operating-manual.md`, `index.md`, `log.md`.

Key result: the publisher was tested in a throwaway clone with a bare remote. Covered: push, isolation from other agents' staged and untracked work, secret and email blocks, validation blocks, refusals, no-op, deletion, diverged remote, offline recovery, and lock serialization. Each publish takes about 0.4 s.

Follow-ups: decide whether to publish the uncommitted backlog from earlier sessions, and whether a Claude Code hook should enforce publishing.

## [2026-11-23] ingest | Bora A4 Wording Approved, BCL Email Case Deferred

What changed:

- Preserved the owner's 2026-11-23 answers:
  - the A4 deposit result wording in the sent 2026-11-22 handoff is approved;
  - the BCL email letter-case check is deferred until production raises it;
  - the production email audit is done and the emails handoff is sent.
- Recorded the agent's reproduction of the BCL sign-in 403 hang and of the proposed fix. The fix is still undecided.

Files touched:

- `raw/sources/2026-11-23-bora-a4-wording-approved-bcl-email-case-deferred.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/projects/bora-capital-mobile-app.md`
- `log.md`

Key result:

- Agents stop treating A4 as an open question and stop listing the BCL email case check.

Follow-ups:

- The owner decides whether to apply the one-line BCL sign-in 403 fix in `src/services/bcl/client.ts`.

## [2026-11-23] maintenance | Agent Context SessionStart Hook

What changed:

- Added an `agent_context.py hook` subcommand and registered it as a Claude Code SessionStart hook (`startup|resume|clear`, 15-second timeout) in `~/.claude/settings.json`. Open handoffs for the session's repository now surface automatically.
- Preserved the user's go-ahead as raw evidence and folded it into the existing Source Record.

Files touched:

- `.agents/skills/agent-context/scripts/agent_context.py`
- `.agents/skills/agent-context/SKILL.md`
- `raw/sources/2026-11-23-agent-context-session-start-hook.md`
- `wiki/sources/agent-context-handoffs-directive.md`
- `wiki/concepts/hermes-obsidian-memory-architecture.md`
- `index.md`
- `log.md`
- Outside the vault: `~/.claude/settings.json`, `~/.claude/CLAUDE.md`

Key result:

- The hook prints nothing when no handoff is open and exits 0 on any error, so it cannot block a session. It was pipe-tested on real, worktree, empty, malformed, and missing-directory payloads.

Follow-ups:

- Confirm the hook fires in a fresh session.
- Hermes profile memories are still not wired.

## [2026-11-23] maintenance | Agent Context Handoffs

What changed:

- Added `raw/agent-contexts/` as a local-only, append-only handoff layer so agents can continue work after the user switches accounts. Everything except its README is gitignored.
- Added the `agent-context` skill with a standard-library helper (`new`, `status`, `transcripts`, `digest`) for save, resume, and recover-from-native-transcript.
- Registered the path and skill in `schema/vault-structure.json` (version 5), the schema docs, and the skills catalog. Documented the layer in `AGENTS.md`.
- Preserved the user's directive as raw evidence with a Source Record, and updated the shared-brain architecture concept and the personal operating manual.
- Outside the vault: symlinked `~/.claude/skills/agent-context`, and added a Session Handoffs section to `~/.claude/CLAUDE.md` and `~/.codex/AGENTS.md`.

Files touched:

- `.gitignore`
- `raw/agent-contexts/README.md`
- `.agents/skills/agent-context/SKILL.md`
- `.agents/skills/agent-context/scripts/agent_context.py`
- `.agents/skills/README.md`
- `schema/vault-structure.json`
- `schema/README.md`
- `schema/local-skills.md`
- `AGENTS.md`
- `raw/sources/2026-11-23-agent-context-handoffs-directive.md`
- `wiki/sources/agent-context-handoffs-directive.md`
- `wiki/concepts/hermes-obsidian-memory-architecture.md`
- `wiki/syntheses/personal-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Snapshots are curated rather than copied transcripts. Recovery orders native transcripts by the last record's timestamp because file mtimes on this machine were rewritten in bulk.

Follow-ups:

- Hermes profile memories are not wired to the skill yet.
- A Claude Code SessionStart hook could surface open handoffs automatically.
- No snapshot pruning policy yet.

## [2026-11-22] ingest | Bora Remaining Fixes Done, Handoff Ready

What changed:

- Preserved the owner's instruction to do every remaining fix at once, and the fixes themselves:
  - customer wording for refunded goal top-ups;
  - `limit: null` giving the default;
  - the restored `NEW_SIGNIN` description;
  - wallet paging fetching one extra row.
- Preserved the final four-agent review: 7 of 8 findings confirmed and applied.
- Marked the handoff check's findings settled on the backlog record and the backend page.

Files touched:

- `raw/sources/2026-11-22-bora-remaining-fixes-and-handoff-ready.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- `docs/frontend-handoff-2026-11-22.md` is ready for the owner to send. Everything is uncommitted; the BCL client's 403 sign-in retry is still undecided.

## [2026-11-22] update | Bora Email Lowercasing Reverted

What changed:

- Preserved the owner's decision to keep email lookups exact, with the reasoning: staging users came from the app, production is TestFlight only, and those users linked successfully.
- Recorded the revert of the agent's lowercasing, the tests now guarding emails kept as typed, and the new handoff section telling the app to stop lowercasing.

Files touched:

- `raw/sources/2026-11-22-bora-email-as-typed-revert-and-handoff.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Emails stay as typed end to end; the frontend handoff carries the app change.

## [2026-11-22] update | Bora Emails Kept Exactly As Typed

What changed:

- Preserved the owner's correction: BCL keeps an email exactly as the customer typed it, neither Bora nor the app may change its letter case, and the app's lowercasing goes to the frontend handoff.
- Replaced the agent's "store emails lowercased" rule on the backend page and reopened the finding on the backlog record.

Files touched:

- `raw/sources/2026-11-22-bora-email-kept-as-typed-owner-correction.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Agents never lowercase or reformat a stored email. The owner has not yet said whether email lookups should ignore letter case.

## [2026-11-22] ingest | Bora Linked-Account Email Case Fixed

What changed:

- Preserved the fix for password recovery failing for linked investors whose BCL email has capitals: linked accounts now store the email lowercased. Also preserved its tests, three mutation checks and the independent review.
- Marked the finding resolved on the backlog record and the backend page, with the rule that account emails are stored trimmed and lowercased.

Files touched:

- `raw/sources/2026-11-22-bora-linked-account-email-case-fix.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Three findings from the handoff check remain for the owner: the Oye cap, the refund reason shown to customers, and `limit: null`.

## [2026-11-22] ingest | Bora 2026-11-22 Frontend Handoff Written

What changed:

- Preserved what the new dated frontend handoff covers, how it was checked (306 claims, 20 upheld findings fixed), and four undecided owner findings: the Oye cap breaking current app builds, password recovery failing for linked investors whose BCL email has capitals, the refund reason shown to customers, and `limit: null`.
- Recorded the handoff on the backlog record, the handoff-rules record (read client code from the remote `develop`, not stale checkouts), and the backend and mobile app pages.

Files touched:

- `raw/sources/2026-11-22-bora-frontend-handoff-2026-11-22.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/sources/bora-frontend-handoff-frozen.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/projects/bora-capital-mobile-app.md`
- `index.md`
- `log.md`

Key result:

- `docs/frontend-handoff-2026-11-22.md` is written, verified and unsent; the owner sends it and decides the four findings.

## [2026-11-22] ingest | Bora A1 Customer Pays The Paystack Fee Built

What changed:

- Preserved the A1 evidence and the owner's choices: the fee is on at deploy, and card auto top-ups add it too.
- Recorded A1 as built and uncommitted on the backlog record and the backend page, with the fee-charging convention; updated the mobile app handoff item with the new fields.

Files touched:

- `raw/sources/2026-11-22-bora-a1-customer-pays-paystack-fee-implementation.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/projects/bora-capital-mobile-app.md`
- `index.md`
- `log.md`

Key result:

- Every approved backend item (A2, A3, A6, B7, B8, B10, B11, B12, B14, B15 and A1) is built and uncommitted; what remains is the frontend handoffs and the owner's live settlement check.

Follow-ups:

- The owner commits and deploys, then confirms settlement with one small live deposit.
- Write the dated frontend handoff (mobile app and admin portal) when the owner asks.

## [2026-11-22] update | Bora B11 Look-Back Back To 72 Hours

What changed:

- Preserved the owner's statement that the 16 Nov GH¢1.00 production deposit was a test, and his instruction to set the B11 look-back back to 72 hours.
- Updated the backlog record and the backend page from 30 days to 72 hours.

Files touched:

- `raw/sources/2026-11-22-bora-b11-lookback-back-to-72-hours.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The vault matches the code: the hourly re-check looks back 72 hours.

Follow-ups:

- None.

## [2026-11-22] ingest | Bora B11 Hourly Paystack Re-Check Built

What changed:

- Preserved the B11 evidence and the owner's choice of a 30-day look-back, which reaches deposits paid before the live webhook existed.
- Recorded B11 as built and uncommitted on the backlog record and the backend page, with the re-check convention; removed it from the not-yet-built lists.

Files touched:

- `raw/sources/2026-11-22-bora-b11-hourly-paystack-recheck-implementation.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The next session sees that B7, A2, A3, A6, B14, B15, B12, B10, B8 and B11 are built and uncommitted, and that A1 (customer pays the fee) remains, plus the frontend handoffs.

Follow-ups:

- The owner commits these fixes.
- A1 next, only on the owner's go-ahead.

## [2026-11-22] ingest | Bora B8 Auto Top-Up Never Charges A Period Twice

What changed:

- Preserved the B8 evidence: unknown charge outcomes wait and are settled with Paystack before any new charge; the review's older duplicate-period bug (a write error swallowed inside a MongoDB transaction) is fixed.
- Recorded B8 as built and uncommitted on the backlog record and the backend page, with the waiting-charge and transaction-error conventions.
- Recorded an incident: a deadlocked mutation run left one file mutated; it was restored and checked.

Files touched:

- `raw/sources/2026-11-22-bora-b8-auto-top-up-unknown-charge-implementation.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The next session sees that B7, A2, A3, A6, B14, B15, B12, B10 and B8 are built and uncommitted, and that B11 and A1 remain.

Follow-ups:

- The owner commits these fixes.
- B11 covers auto top-up deposits whose webhook never arrives.

## [2026-11-21] ingest | Bora B10 Staff Transactions And Deposit Reconciliation Built

What changed:

- Preserved the owner's close-action choices (send to BCL again or mark refunded; refunds made in the Paystack dashboard and recorded in Bora; per-deposit Sentry alert removed) and the B10 build evidence.
- Recorded B10 as built and uncommitted on the backlog record and the backend page, with the staff close-action convention, and added the admin portal work to the next handoff list.
- Recorded an incident: an overwritten test file was restored the same session.

Files touched:

- `raw/sources/2026-11-21-bora-b10-staff-transactions-and-reconciliation-implementation.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The next session sees that B7, A2, A3, A6, B14, B15, B12 and B10 are built and uncommitted, and that B8, B11 and A1 remain.

Follow-ups:

- The owner commits these fixes; the admin portal needs a dated handoff when the owner asks.
- The owner decides what to do with `scripts/deposits_production`, whose README still names the removed alert.

## [2026-11-21] ingest | Bora Reconciliation Is Staff Work In The Admin Portal

What changed:

- Preserved the owner's correction: staff reconcile deposits in the admin portal, not the owner. Sentry is not a reconciliation channel, and `scripts/deposits_production/inspectDeposit.ts` is a diagnostic script, not a reconciliation tool.
- Added the decision to the backlog record, with B10 marked as being for staff in the admin portal, and added it as a convention on the backend page.

Files touched:

- `raw/sources/2026-11-21-bora-reconciliation-is-staff-work-in-admin-portal.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Agents design reconciliation for staff in the admin portal and stop treating Sentry or the diagnostic script as the way cases get handled.

Follow-ups:

- Whether to undo the agent's B7 and B12 README edits, and what Sentry should keep, wait on the owner.

## [2026-11-21] ingest | Bora B12 BCL Reply And Unsent Deposit Retry Built

What changed:

- Preserved the evidence for B12, built in the backend working tree and uncommitted.
  - Every BCL deposit failure stores BCL's reply on the deposit; a finalize failure after BCL accepted also stores BCL's ERP reference.
  - A deposit BCL certainly never received waits in the new `RETRY_PENDING` status and the hourly reconciliation job sends it again, after a fresh Paystack check, up to 25 posts in all; timeouts and every other BCL answer stay manual cases.
  - One hourly summary alert names deposits still waiting after 3 posts; they must never be posted by hand.
- Recorded the verification: full suite, build, eleven mutation checks, and an independent review whose 3 confirmed findings were fixed.
- Moved B12 to "built" on the backlog record and the backend page, added the `RETRY_PENDING` convention, and noted what the B10 admin view must show for waiting deposits.

Files touched:

- `raw/sources/2026-11-21-bora-b12-bcl-reply-and-unsent-deposit-retry-implementation.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The next session sees that B7, A2, A3, A6, B14, B15 and B12 are built and uncommitted, and that B8, B10, B11 and A1 remain.

Follow-ups:

- The owner commits these fixes with the other uncommitted backend work.
- Next backlog item only after the owner's go-ahead.

## [2026-11-21] ingest | Record LivelyCura HRM Shift Management Scope Decision

What changed:

- Preserved the product owner's 2026-11-21 shift-management concern and his answer "B: roles decide" verbatim, with the investigation findings and the two options, as conversation evidence.
- Added a Source Record, plus a "Shift Management Scope (Decided, Not Yet Built)" subsection and an Evidence entry on the backend page.
- Added one decision line to the Pharmacy Portal and SERLP Mobile pages, the source to all three pages' sources, and refreshed their index entries.

Files touched:

- `raw/sources/2026-11-21-livelycura-hrm-shift-management-scope-decision.md`
- `wiki/sources/livelycura-hrm-shift-management-scope-decision.md`
- `wiki/projects/livelycura-backend.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/projects/serlp-mobile.md`
- `index.md`
- `log.md`

Key result:

- Shift work is HR-led through roles: every shift action counts roles at the shift's own branch on every screen and in SERLP AI, HR's organization-wide role covers every branch, a branch manager needs a branch role with shift rights, and nothing is locked to organization level. Open-shift publishing and pickup approvals keep counting roles at the branch; the rest of Employees decision 5 stays organization-level.

Follow-ups:

- Nothing is built yet; verify the pages against the implementation once it lands.
- The Employees decisions, including decision 5, have no Source Record yet.

## [2026-11-21] ingest | Bora Decimal-Comma Note For The Frontend Handoff

What changed:

- Preserved the owner's decision, in their words, to tell the frontend developer in the next dated handoff that a decimal-comma keyboard turns the withdrawal amount "500,50" into 50050, which the confirm screen shows before the customer confirms.
- Added the item to the handoff lists on the backlog record and the mobile app page.

Files touched:

- `raw/sources/2026-11-21-bora-handoff-decimal-comma-note.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-mobile-app.md`
- `log.md`

Key result:

- Whoever writes the next frontend handoff sees this app-only note along with the other items.

Follow-ups:

- Include the note when the owner asks for the next dated frontend handoff.

## [2026-11-21] ingest | Bora B15 Withdrawal Amount Format Built

What changed:

- Preserved the evidence for B15, built in the backend working tree and uncommitted.
  - `requestWithdrawal` now refuses any amount that is not a plain number greater than zero with up to two decimal places (a 400), before saving or sending anything.
  - It checks the format only; the limits stay with BCL.
- Recorded the verification: full suite, build, five mutation checks, and one independent check. That check confirmed every amount the app can send still passes, and that no other path sends withdrawal amounts to BCL.
- Moved B15 to "built" on the backlog record and the backend page.

Files touched:

- `raw/sources/2026-11-21-bora-b15-withdrawal-amount-format-implementation.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The next session sees that B7, A2, A3, A6, B14 and B15 are built and uncommitted.

Follow-ups:

- The owner commits these fixes with the other uncommitted backend work.
- Next backlog item only after the owner's go-ahead.

## [2026-11-21] ingest | Bora B14 Withdrawal Refusal Messages Built

What changed:

- Preserved the evidence for B14, built in the backend working tree and uncommitted.
  - BCL's own refusal text (`Status[0].Description`, then `Message`, whatever the HTTP status) now reaches the customer as a 400.
  - BCL refusing our own sign-in or access token, unreadable replies and network failures stay a hidden 502.
  - New pure helpers in `src/services/bcl/replies.ts` are used only by the withdrawal code.
- Recorded what was tried and reverted: a shared BCL client change that would have stranded KYC submissions, and an "any 403" rule that would have hidden real BCL refusals.
- Added the withdrawal rule to the backend's BCL-error convention. Moved B14 to "built". Recorded the BCL client 403 hang as an open item raised with the owner, and how B14 interacts with the C23 app item.

Files touched:

- `raw/sources/2026-11-21-bora-b14-withdrawal-refusal-messages-implementation.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The next session sees that B7, A2, A3, A6 and B14 are built and uncommitted, how withdrawal failures are reported, and which BCL client issue awaits the owner's decision.

Follow-ups:

- The owner decides whether to fix the BCL client 403 hang.
- The owner commits these fixes with the other uncommitted backend work.
- Ship C23 (app) with or after B14.
- Next backlog item only after the owner's go-ahead.

## [2026-11-21] ingest | Bora A6 Withdrawal Date Format Built

What changed:

- Preserved the evidence for A6, built in the backend working tree and uncommitted. The withdrawal `TransactionDate` is now sent to BCL, and stored on the withdrawal record, as `DD MMM YYYY` (English month), the format deposits already use.
- Recorded the verification: full suite, build, a revert check that fails six tests, and one independent review. The review found no reader of the stored date and no other BCL withdrawal path.
- Moved A6 to "built". Resolved the stale "not yet implemented" notes on the backlog record and the backend page. Added to the B10 design note that withdrawal lists must sort on `createdAt` or `submittedAt`, never on the date text.

Files touched:

- `raw/sources/2026-11-21-bora-a6-withdrawal-date-implementation.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The next session sees that B7, A2, A3 and A6 are built and uncommitted, and that the withdrawal date matches BCL's format.

Follow-ups:

- The owner commits these fixes with the other uncommitted backend work.
- Next backlog item only after the owner's go-ahead.

## [2026-11-21] ingest | Bora A2 And A3 Deposit Alerts Built

What changed:

- Preserved the evidence for A2 and A3, built in the backend working tree and uncommitted.
  - Bora's only deposit alert is now the existing `DEPOSIT_PENDING` type, worded "Payment received, awaiting confirmation". It is sent alongside the BCL post only when the caller wins the deposit's claim.
  - "Deposit completed" is no longer sent, and `DEPOSIT_SUCCESSFUL` is deprecated in the schema.
  - `transferCash`'s dead after-BCL alert option is removed.
- Recorded the verification: full suite, build, a rendered-email check, seven mutation checks on the alert's timing and count, and a three-lens review. The review's one confirmed test gap was covered.
- Moved A2 and A3 to "built" on the backlog record and the backend page. Added a possible frontend handoff line for the owner to decide on.

Files touched:

- `raw/sources/2026-11-21-bora-a2-a3-deposit-alerts-implementation.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The next session sees that B7, A2 and A3 are built, how the deposit alert now behaves, and how it was verified.

Follow-ups:

- The owner may change the alert's wording.
- The owner commits B7, A2 and A3 with the other uncommitted backend work.
- Next backlog item only after the owner's go-ahead.

## [2026-11-21] ingest | Bora B7 Deposit Double-Post Guard Built

What changed:

- Preserved the evidence for B7, the first item of the approved Bora backlog. It was built in the backend working tree and is uncommitted.
  - Only a deposit with no `bclSync.status` may be claimed or take a non-success write.
  - Finalize requires the caller's own claim.
  - The auto top-up failure path leaves claimed deposits and their contributions alone.
  - One shared deposit read replaces four identical queries.
- Recorded the verification: the full suite, the build, seven mutation checks, a sift-backed race spec that fails on the pre-change code, and a three-lens review in which a skeptic checked each finding.
- Added the deposit claim rule to the backend's durable conventions. Moved B7 from "approved" to "built". Widened the B10 reconciliation view to cover any deposit left with `bclSync.status IN_PROGRESS`.
- Corrected the stale "unconfigured Paystack live webhook" in the backend index entry, and removed "Docker smoke checks" from the backend verification expectations, following the owner's 2026-11-21 no-Docker decision.

Files touched:

- `raw/sources/2026-11-21-bora-b7-deposit-double-post-guard-implementation.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The next session sees that B7 is built, what rule it enforces, and how it was verified. The backlog continues from the next item.

Follow-ups:

- The owner reviews and commits B7 together with the other uncommitted backend work.
- Next backlog items, one at a time, after the owner's go-ahead.

## [2026-11-21] ingest | Bora Deposit And Withdrawal Flow Decisions And Fix Backlog

What changed:

- Preserved the owner's 2026-11-19 to 2026-11-21 Bora decisions:
  - go-live audit fixes (one shared signup code, linking only after the emailed code, GraphQL operation limits, Oye and WebSocket caps, cooldown buckets), all uncommitted;
  - the deposit and withdrawal flow sent to BCL: the customer bears the Paystack fee, Bora's "payment received, awaiting confirmation" alert, BCL's confirmation alerts, payout fields waiting on BCL;
  - the owner's answers to a double-checked open-issue list.
- Recorded the approved fix backlog, the next frontend-handoff items, findings never to re-raise, and the Paystack live webhook now configured.
- Marked as superseded the subaccount-as-fee-bearer decision, the withdrawal `YYYY-MM-DD` date, and the separate-signup-codes rationale.
- Added three working preferences: plain explanations, never re-raise decided findings, and partner documents covering only what was asked.

Files touched:

- `raw/sources/2026-11-21-bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/projects/bora-capital-mobile-app.md`
- `wiki/syntheses/personal-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- The next session can resume the Bora backlog from one record: what is approved, what waits on BCL, what goes in the frontend handoff, and what must not be raised again.

Follow-ups:

- Build the approved backlog one item at a time, starting with the double-post guard.
- Get the owner's deposit result wording.
- Write the dated frontend handoff.
- Commit the uncommitted audit fixes.
- Wait for BCL to enable production deposits and withdrawals and to add the payout fields.

## [2026-11-19] ingest | Bora Accepted Risks, Deposit Path, And API Domain

What changed:

- Preserved the owner's 2026-11-19 Bora backend statements: the signup cap stays at 200 per IP per hour (raised from 20 in `8da3912`, 2026-10-30); four accepted risks never to re-flag in audits; `depositCash` removed from schema, resolver and shield (uncommitted, not deployed), leaving Paystack as the only deposit path; production App Platform host, `boracapital.com` not Bora's, `api.boradvisors.com` as the recommended API domain with a new app build for the pinned certificate; and the open item that the Paystack live webhook is not configured.
- Marked the 20-per-hour signup cap and the "legacy direct-deposit mutation remains" note as superseded, and resolved the open `depositCash` concern pending deploy.

Files touched:

- `raw/sources/2026-11-19-bora-accepted-risks-deposit-path-and-api-domain.md`
- `wiki/sources/bora-accepted-risks-deposit-path-and-api-domain.md`
- `wiki/sources/bora-client-ip-app-platform.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/projects/bora-capital-mobile-app.md`
- `index.md`
- `log.md`

Key result:

- Audits have one place listing the accepted Bora risks and the current signup cap; the cap, commit, CORS origins and uncommitted `depositCash` removal were checked in the local checkout.

Follow-ups:

- Configure the Paystack live webhook URL; commit and deploy the `depositCash` removal; move the app to `api.boradvisors.com` with its next build.

## [2026-11-13] ingest | LivelyCura Customer Mobile iOS 27 Cart, Glass And Scene Startup

What changed:

- Preserved the owner's decisions on the iOS 27 cart tab, the Reduce Transparency glass fallback and the UIScene life cycle adoption, all committed on `feature/ui-updates`.
- Marked the earlier iOS 27 "prominent" cart role as superseded.

Files touched:

- `raw/sources/2026-11-13-livelycura-customer-mobile-ios27-cart-glass-scenes.md`
- `wiki/sources/livelycura-customer-mobile-ios27-cart-glass-scenes.md`
- `wiki/sources/livelycura-customer-mobile-glass-home-direction.md`
- `wiki/projects/livelycura-customer-mobile.md`
- `index.md`
- `log.md`

Key result:

- Xcode 27 builds of the customer app launch on iOS 27, and the cart follows each iOS version's tab bar.

## [2026-11-13] ingest | LivelyCura Customer Portal Cancel Reason And Redesign Commit

What changed:

- Preserved the owner's decision to add an optional shopper cancel reason (web, mobile app and backend), the header-doubling fix, and the commit of the portal redesign.
- Replaced the stale "uncommitted" and "no shopper cancel note" statements.

Files touched:

- `raw/sources/2026-11-13-livelycura-customer-portal-cancel-reason-and-commit.md`
- `wiki/sources/livelycura-customer-portal-redesign-direction.md`
- `wiki/projects/livelycura-customer-portal.md`
- `index.md`
- `log.md`

Key result:

- The portal redesign is committed on `feature/portal-ui` (`fe03c61`); the backend cancel change on `feature/hrm` must go live first.

## [2026-11-12] ingest | No Project Copies Direction

What changed:

- Preserved the owner's direction that agents never make a copy of a project folder (git worktree) to do work, after a second unexpected copy.
- Added the rule to the Personal Operating Manual's change-work preferences.

Files touched:

- `raw/sources/2026-11-12-no-project-copies-direction.md`
- `wiki/sources/no-project-copies-direction.md`
- `wiki/syntheses/personal-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Branch work stays in the existing folder; blockers are raised plainly with in-place choices.

## [2026-11-12] update | Bora Live NIA Matches A JPEG Selfie

What changed:

- Preserved the user's live run with `--format jpg`: their own selfie as a 129 KB JPEG with `dataType` `JPG` returned HTTP 200, code `00`, "Verified Successfully". Closed the JPEG open question, and recorded that earlier `.jpg` runs were converted to PNG by the script.

Files touched:

- `raw/sources/2026-11-12-bora-nia-live-jpeg-match.md`
- `wiki/sources/bora-kyc-supervision-and-statement-update.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- NIA accepts JPEG selfies with `dataType` `JPG`; the backend change and the 2026-11-12 handoff are confirmed.

## [2026-11-12] update | Bora KYC Selfie Can Be A JPEG

What changed:

- Preserved the user's request to accept JPEG selfies as well as PNG: the backend reads the format from the bytes and sends NIA `dataType` `PNG` or `JPG`. Recorded that NIA's document shows only PNG, so a live JPEG check through `scripts/nia_staging/testNiaSelfie.ts --format jpg` comes before release, and the new `docs/frontend-handoff-2026-11-12.md`.

Files touched:

- `raw/sources/2026-11-12-bora-kyc-jpeg-selfie.md`
- `wiki/sources/bora-kyc-supervision-and-statement-update.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- PNG and JPEG selfies reach NIA; whether live NIA accepts `JPG` as the `dataType` is the open check.

## [2026-11-12] ingest | LivelyCura Customer Portal Privacy And Terms Approved

What changed:

- Preserved the owner's approval of the redesigned Privacy and Terms pages and their two additions ("On this page" for Privacy, the reading marker on both).
- Recorded the Privacy Policy text review and the pending commit as open questions.

Files touched:

- `raw/sources/2026-11-12-livelycura-customer-portal-policy-pages-approved.md`
- `wiki/sources/livelycura-customer-portal-redesign-direction.md`
- `wiki/projects/livelycura-customer-portal.md`
- `index.md`
- `log.md`

Key result:

- Every page in the customer portal redesign is built and approved; all of it is uncommitted on `feature/portal-ui`.

## [2026-11-12] ingest | LivelyCura Customer Portal Login Frame Approved

What changed:

- Preserved the owner's approval of the redesigned Login page frame and the move of sign-in messages to the forest toast.

Files touched:

- `raw/sources/2026-11-12-livelycura-customer-portal-login-approved.md`
- `wiki/sources/livelycura-customer-portal-redesign-direction.md`
- `index.md`
- `log.md`

Key result:

- Only Privacy and Terms remain in the old design.

## [2026-11-12] ingest | LivelyCura Customer Portal Get Care Approved

What changed:

- Preserved the owner's approval of the redesigned Get Care page, its two additions (phone number shown, WhatsApp wording) and the dial-directly fix.

Files touched:

- `raw/sources/2026-11-12-livelycura-customer-portal-get-care-approved.md`
- `wiki/sources/livelycura-customer-portal-redesign-direction.md`
- `index.md`
- `log.md`

Key result:

- Only the Login page frame and the Privacy and Terms pages remain in the old design.

## [2026-11-12] ingest | LivelyCura Customer Portal Account Pages Approved

What changed:

- Preserved the owner's approval of the redesigned account area (frame, Dashboard, Orders, Prescriptions, Notifications, Support, Settings), the bugs fixed on the way, and the owner's calls: no note on the shopper's cancel, no side-stripe borders.
- Updated the support rendering convention: inbox rows keep the latest-chat preview and also show the case number and status.
- Recorded backend follow-ups (refill orders, prescription edit permissions, cancel note).

Files touched:

- `raw/sources/2026-11-12-livelycura-customer-portal-account-pages-approved.md`
- `wiki/sources/livelycura-customer-portal-redesign-direction.md`
- `wiki/sources/customer-portal-support-rendering-conventions.md`
- `wiki/projects/livelycura-customer-portal.md`
- `index.md`
- `log.md`

Key result:

- Home, Products, the product page, the checkout flow and the whole account area are approved; Get Care, the Login frame and the policy pages remain.

## [2026-11-11] ingest | LivelyCura Customer Portal Checkout Flow Approved

What changed:

- Preserved the owner's acceptance of the redesigned checkout flow and its five additions, plus the preference for spinners (not bar loaders) on busy buttons. Added the spinner convention to the project page.

Files touched:

- `raw/sources/2026-11-11-livelycura-customer-portal-checkout-flow-approved.md`
- `wiki/sources/livelycura-customer-portal-redesign-direction.md`
- `wiki/projects/livelycura-customer-portal.md`
- `index.md`
- `log.md`

Key result:

- Home, Products, the product page and the checkout flow are built and approved; the account orders pages are next.

## [2026-11-11] ingest | LivelyCura Customer Portal Product Page Approved

What changed:

- Preserved the owner's approval of the redesigned single product page and its five additions, the lean build approach, and the dark-mode footer-corner fix. Recorded the cache-first arrival, the scroll-snap gallery and the footer-band overlap convention in the redesign Source Record.

Files touched:

- `raw/sources/2026-11-11-livelycura-customer-portal-product-page-approved.md`
- `wiki/sources/livelycura-customer-portal-redesign-direction.md`
- `index.md`
- `log.md`

Key result:

- Home, Products and the product page are approved, still uncommitted on `feature/portal-ui` at the owner's request.

## [2026-11-11] ingest | LivelyCura Customer Portal Products Page Approved

What changed:

- Preserved the owner's approval of the redesigned Products list and category pages, the four approved additions, the cost question and the "keep full run" choice, and the SSR head-tag fix that affects every page. Recorded the Products conventions (history-state search, 24 per page, view-transition naming safe under the SSR router, the whole-document crawler render) on the project page and in the redesign Source Record.

Files touched:

- `raw/sources/2026-11-11-livelycura-customer-portal-products-page-approved.md`
- `wiki/sources/livelycura-customer-portal-redesign-direction.md`
- `wiki/projects/livelycura-customer-portal.md`
- `index.md`
- `log.md`

Key result:

- Home and Products are built and approved, still uncommitted on `feature/portal-ui` at the owner's request. Crawlers now get head tags in `<head>` once the branch ships.

## [2026-11-10] update | LivelyCura HRM Review Screen Items Belong To Their Module

What changed:

- Preserved the user's 2026-11-10 correction during the Roles review: a "boxes that do nothing, and misleading names" decision mixed other modules' permission boxes (Products, Accounting, CRM, Leaves, Shifts) into Roles. Added the rule that an item merely shown on the current feature's screen belongs to its own module, and that briefs are filtered before presenting, to the feature-by-feature Source Record and the operating manual.

Files touched:

- `raw/sources/2026-11-10-livelycura-hrm-review-screen-items-belong-to-their-module.md`
- `wiki/sources/livelycura-hrm-feature-by-feature-review.md`
- `wiki/syntheses/personal-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- The feature-by-feature scope rule now covers items that appear on the current screen but belong to other modules.

## [2026-11-10] update | LivelyCura Customer Portal Home Scroll Motion Approved

What changed:

- Preserved the owner's approval ("Looks right") of the customer portal Home's scroll layer after scrolling the built page, with no changes asked, including the hero plus's turn that briefly reads as an "×". Marked it approved in the redesign Source Record (core claim and open question) and in the project page's motion convention.

Files touched:

- `raw/sources/2026-11-10-livelycura-customer-portal-home-scroll-motion-approved.md`
- `wiki/sources/livelycura-customer-portal-redesign-direction.md`
- `wiki/projects/livelycura-customer-portal.md`
- `index.md`
- `log.md`

Key result:

- Home's per-section scroll moments are approved; the work is still uncommitted on `feature/portal-ui`, and whether later pages get their own scroll moments stays open.

## [2026-11-10] update | Bora Live NIA Match And Non-Match

What changed:

- Preserved the user's two live NIA runs through `scripts/nia_staging/testNiaSelfie.ts`: a photo of someone else returned HTTP 200, code `01`, "Not Matched Found", `verified` "FALSE" (backend 400 "Your selfie did not match…"); their own selfie returned HTTP 200, code `00`, "Verified Successfully", `verified` "TRUE" (on to BCL). `success` is true for both. Code `11` was not reproduced.

Files touched:

- `raw/sources/2026-11-10-bora-nia-live-selfie-results.md`
- `wiki/sources/bora-kyc-supervision-and-statement-update.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The live NIA contract matches the backend's reading: only `code` and `verified` decide, and the customer gets verified or not verified.

## [2026-11-09] update | Bora NIA Unrecognised Answers Return 400

What changed:

- Preserved the user's decision that an NIA answer the backend does not recognise is a 400 "NIA could not verify this Ghana Card and selfie", not a 502, after staging got code `11` with `code`, `success` and `msg` beside `data`; recorded the code-11 open question and the `scripts/nia_staging` test script.

Files touched:

- `raw/sources/2026-11-09-bora-nia-unrecognised-answer-400.md`
- `wiki/sources/bora-kyc-supervision-and-statement-update.md`
- `wiki/projects/bora-capital-backend.md`
- `log.md`

Key result:

- Only an NIA outage or a reply with no code is a 502; every other non-match is a 400 and never reaches BCL.

## [2026-11-09] ingest | LivelyCura Customer Portal Home Scroll Motion

What changed:

- Preserved the owner's 2026-11-09 follow-up on the customer portal redesign: after reviewing the rebuilt Home they asked to keep its animations and add scroll animations before moving to the next page. Recorded what was built (uncommitted on `feature/portal-ui`, owner review pending): one CSS scroll-scrubbed moment fitted to each Home section, with the Shop tiles' rolling forest doors as the signature, behind an `@supports` test and a reduced-motion gate so Firefox, reduced motion and print show the finished page.
- Extended the redesign Source Record with the new raw file, the refined motion claim, the mechanics, a load-time lesson (a scrubbed reveal freezes part-way at the bottom edge on load, so ranges must keep common window heights from loading cut text), a tension note reconciling it with "not scroll-reveal on every section", and an open question about later pages.
- Updated the project page's motion convention and rationale.

Files touched:

- `raw/sources/2026-11-09-livelycura-customer-portal-home-scroll-motion.md`
- `wiki/sources/livelycura-customer-portal-redesign-direction.md`
- `wiki/projects/livelycura-customer-portal.md`
- `index.md`
- `log.md`

Key result:

- Future portal pages treat scroll motion as part of Green Room: one fitted moment per section, never a repeated fade-up, CSS only, gated, and text never moving on its own.

Follow-ups:

- The owner reviews Home's scroll layer; Safari 26, Firefox and real Android phones were not run at recording.

## [2026-11-09] ingest | Bora Fund NAV History From BCL

What changed:

- Preserved the user's 2026-11-09 decision, after Bora told the client presentation that BCL keeps each fund's NAV history and updates it daily: customer fund NAV history loads from BCL's `CIPortfolioPrices` (through `fetchBclData`, cached 30 minutes with a 7-day last-known fallback, `[]` with a warning when BCL fails and nothing is cached), and the stored `navHistory` is removed from the facts, types, model, validation, seeds and production fund scripts and unset on deploy by `REMOVE_FUND_NAV_HISTORY_V1`. The customer GraphQL contract is unchanged; the admin portal must ship with the backend release.
- Marked the superseded claims rather than deleting them: local facts owning NAV history, the seed's `navHistory` as the 1 Year Price Trend shown to customers, and the 2026-10-27 no-silent-shrink rule, now noted as lapsed with the field. Added Contradictions Or Tensions notes with sources on each side and a confidence split (high for code, medium for BCL data depth), plus an open question on how far back BCL's history goes.
- Left the mobile app page alone: it does not describe the fund chart's data source, and the app needs no change.

Files touched:

- `raw/sources/2026-11-09-bora-fund-nav-history-from-bcl.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Future Bora fund work treats BCL as the only customer NAV-history source and does not reintroduce a stored series; `sinceInceptionJourney` and `factSheetNav` stay local.

Follow-ups:

- Verify BCL's history depth with a live `CIPortfolioPrices` call; the user runs credentialed calls.
- The backend change was uncommitted at recording; `docs/frontend-handoff-2026-11-09.md` goes to the admin-portal developer.

## [2026-11-09] ingest | LivelyCura Customer Portal Redesign Direction

What changed:

- Preserved the owner's 2026-11-09 decisions for the customer web portal: a page-by-page restyle, Home first, on `feature/portal-ui` (cut from `develop` at `72b656b`), merged only when the owner says so; the same colours as the customer app but a web style of its own; the "Green Room" direction picked from three probes; a few signature motion moments with CSS and View Transitions instead of scroll-reveal everywhere; Unsplash stock checked for foreign signage until real photos; and the approved Home plan with its additions, bundled fixes and the create-the-router-once prerequisite.
- Added the redesign, motion and imagery conventions, the rationale, the router constraint, an open question on real photos, and a tension note to the project page. The older "extend the existing theme" convention stays, marked with the redesign as its exception.
- Left the software development manual alone: its LivelyCura section holds family-wide rules and already links the project page, and this direction is portal-specific.

Files touched:

- `raw/sources/2026-11-09-livelycura-customer-portal-redesign-direction.md`
- `wiki/sources/livelycura-customer-portal-redesign-direction.md`
- `wiki/projects/livelycura-customer-portal.md`
- `index.md`
- `log.md`

Key result:

- Future customer-portal UI work on `feature/portal-ui` follows Green Room and its motion rules and does not copy the mobile app's look.

Follow-ups:

- Replace the Unsplash stock with real photos, ideally from Kumasi, when they exist.

## [2026-11-08] ingest | LivelyCura Customer Mobile Dark Mode And Drawn Tab Bar

What changed:

- Preserved the user's request that Android and pre-iOS 26 devices keep the same tab bar design as iOS 26, drawn on solid surfaces like Telegram, and the built dark mode (iOS-style, following the phone by default, with a Light/Dark/System choice).
- Removed the open question about how dark mode is chosen, now settled, and the superseded "light first" convention. Visual approval is pending.

Files touched:

- `raw/sources/2026-11-08-livelycura-customer-mobile-dark-mode-and-drawn-tab-bar.md`
- `wiki/sources/livelycura-customer-mobile-glass-home-direction.md`
- `wiki/projects/livelycura-customer-mobile.md`
- `log.md`

Key result:

- Future customer-mobile work keeps one tab bar design on every platform and builds every screen for both light and dark mode.

## [2026-11-08] ingest | LivelyCura Customer Mobile Cart Button Cover

What changed:

- Preserved the user's approved cart design: the tab bar's separate round button with a full count badge, which grows a full-screen cart cover out of itself (tab bar included) and shrinks it back on close, like Telegram's iOS 26 search. The floating cart bubble is gone.
- Recorded the correction that the first version, a normal Cart tab, was not what the user meant.
- Updated the glass Home Source Record, the project page's conventions and the index line.

Files touched:

- `raw/sources/2026-11-08-livelycura-customer-mobile-cart-button-cover.md`
- `wiki/sources/livelycura-customer-mobile-glass-home-direction.md`
- `wiki/projects/livelycura-customer-mobile.md`
- `index.md`
- `log.md`

Key result:

- Future customer-mobile work keeps the cart as a cover opened from the tab bar's round button, not a tab or a floating bubble.

## [2026-11-08] update | LivelyCura Customer Mobile Profile Title

What changed:

- Preserved the user's instruction that Profile also gets a title centred on its back-button row. This replaces the earlier note that Profile has none.

Files touched:

- `raw/sources/2026-11-08-livelycura-customer-mobile-profile-title.md`
- `wiki/sources/livelycura-customer-mobile-glass-home-direction.md`
- `wiki/projects/livelycura-customer-mobile.md`
- `log.md`

Key result:

- Pushed customer-mobile screens with a back button carry their title centred on that row, Profile included.

## [2026-11-08] ingest | LivelyCura Customer Mobile Pushed-Screen Headers

What changed:

- Preserved the user's correction that customer-mobile pushed screens never put a title under the back button. A title, if any, sits centred on the same row as the glass back button, and Profile has none.
- Preserved the correction that inspo images are style references, not templates: Sign out and Delete Account get their own group, and settings tiles are brand green.
- Added both to the glass Home Source Record and the project page's conventions, and updated the index line.

Files touched:

- `raw/sources/2026-11-08-livelycura-customer-mobile-pushed-screen-headers.md`
- `wiki/sources/livelycura-customer-mobile-glass-home-direction.md`
- `wiki/projects/livelycura-customer-mobile.md`
- `index.md`
- `log.md`

Key result:

- Future customer-mobile screens use the shared back-and-title row instead of stacking titles under the back button.

## [2026-11-07] ingest | LivelyCura Customer Mobile Native Glass Approved

What changed:

- Preserved the user's approved customer-mobile design. The tab bar is the platform's native one (Liquid Glass with the sliding selection on iOS 26, Material on Android), header controls use clear glass, and the Home top row floats with no bar behind it. Tab screens run edge to edge, and the hero green runs from `primary`, fading from the search bar to the banner.
- Rewrote the glass Home Source Record to the approved state, which drops the superseded custom tab bar and strip-colouring details. Updated the project page's visual-direction convention.

Files touched:

- `raw/sources/2026-11-07-livelycura-customer-mobile-native-glass-approved.md`
- `wiki/sources/livelycura-customer-mobile-glass-home-direction.md`
- `wiki/projects/livelycura-customer-mobile.md`
- `index.md`
- `log.md`

Key result:

- Future customer-mobile work keeps the native tab bar and the approved Home top instead of rebuilding them.

Follow-ups:

- Record how dark mode is chosen once the user decides.

## [2026-11-07] ingest | LivelyCura Customer Mobile Hero Fade Clarification

What changed:

- Preserved the user's clarification that the Home hero green fades softly into the page behind the banner, not ending with a hard edge above it. That reverses the agent's reading recorded in the previous entry.
- Updated the glass Home Source Record's sources and Core Claims, and its index line.

Files touched:

- `raw/sources/2026-11-07-livelycura-customer-mobile-hero-fade-clarification.md`
- `wiki/sources/livelycura-customer-mobile-glass-home-direction.md`
- `index.md`
- `log.md`

Key result:

- The Source Record describes the shipped hero: solid green behind the controls, fading behind the banner.

Follow-ups:

- None.

## [2026-11-07] ingest | LivelyCura Customer Mobile Home Header Correction

What changed:

- Preserved the user's correction that the Home header must follow the inspo: green ends below the search bar, location picker left, Favourites and Profile right, no greeting, banner on the page as a solid green card.
- Updated the glass Home Source Record's sources and Core Claims (the banner is no longer glass).

Files touched:

- `raw/sources/2026-11-07-livelycura-customer-mobile-home-header-correction.md`
- `wiki/sources/livelycura-customer-mobile-glass-home-direction.md`
- `log.md`

Key result:

- The Source Record now matches the shipped Home layout.

Follow-ups:

- None.

## [2026-11-07] ingest | LivelyCura Customer Mobile Glass Home Direction

What changed:

- Preserved the user's design decisions for the customer app: iOS Liquid Glass on the controls layer only with solid content cards, no blur on Android, light mode first then dark, and the support card holding the Home banner slot until marketing banners exist.
- Updated the project page's Stack (Expo SDK 57), Durable Conventions, Evidence and Open Questions.

Files touched:

- `raw/sources/2026-11-07-livelycura-customer-mobile-glass-home-direction.md`
- `wiki/sources/livelycura-customer-mobile-glass-home-direction.md`
- `wiki/projects/livelycura-customer-mobile.md`
- `index.md`
- `log.md`

Key result:

- Future customer-mobile work reads the glass direction from the vault and the repo `PRODUCT.md`, which no longer lists glassmorphism as an anti-reference.

Follow-ups:

- Record how dark mode is chosen once the user decides.

## [2026-11-06] update | Bora Refused KYC Form Saved In One Transaction

What changed:

- Preserved the user's same-day decision to move the refused-form save into one `withTransaction` with the claim release, which removed the best-effort exception to the 2026-10-16 `withTransaction` rule recorded in the previous entry.
- Updated the KYC Source Record's Core Claims and Contradictions, and the backend project page's KYC and Evidence bullets.

Files touched:

- `raw/sources/2026-11-06-bora-refused-form-one-transaction.md`
- `wiki/sources/bora-kyc-supervision-and-statement-update.md`
- `wiki/projects/bora-capital-backend.md`
- `log.md`

Key result:

- A refused KYC form and its claim release now commit or roll back together; if either fails, the claim stays `SUBMITTED` for reconciliation.

## [2026-11-06] ingest | Record Bora KYC NIA Gate, ID Image, And Refused Forms

What changed:

- Preserved the user's 2026-11-06 Bora backend decisions after a production `413 PayloadTooLargeError` on a KYC submission: the NIA selfie check gates the BCL post and returns any NIA error to the customer; the Express JSON body limit stays at 5 MB for security (shrink payloads, never raise it); the app sends the ID front image once as `imgIDFrontString` (`imgIDString` removed from both KYC inputs, sent to BCL by `formatPayload`); refused KYC forms are saved while the claim is held so `updateKyc` serves refused `PENDING` users as well as `REJECTED` ones.
- Recorded the user's statement that the customer app ships only through TestFlight as of 2026-11-06, which allowed the breaking input change without a deprecation phase.
- Extended the existing KYC Source Record instead of creating a near-duplicate; added KYC, Constraints, and Evidence bullets on the backend project page and a distribution note on the mobile app page.
- Flagged the best-effort refused-form save as a narrow exception to the 2026-10-16 `withTransaction` rule, and the 413 cause as likely rather than confirmed.

Files touched:

- `raw/sources/2026-11-06-bora-kyc-id-image-and-refused-form.md`
- `wiki/sources/bora-kyc-supervision-and-statement-update.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/projects/bora-capital-mobile-app.md`
- `index.md`
- `log.md`

Key result:

- KYC submissions stop at NIA before BCL, refused forms survive for correction, and 413s are fixed by smaller payloads, not a larger body limit.

Follow-ups:

- Re-check the TestFlight-only status before the next breaking GraphQL input change.
- The backend change was uncommitted at recording, with no live NIA or BCL call.

## [2026-11-05] ingest | Record LivelyCura SERLP Mobile Portal Parity

What changed:

- Preserved the user's 2026-11-05 rule from the HRM Employees work: serlp-mobile is the mobile version of the ERP, so anything the SERLP portal (`livelycura-pharmacy-portal`) does, serlp-mobile must also do, adapted to mobile. Agents never offer "portal-only" or ask how much of a feature belongs on serlp-mobile; gaps are parity work.
- Added a Source Record, a Durable Conventions bullet on the serlp-mobile and pharmacy portal project pages, and a LivelyCura Family bullet in the development manual.
- Updated the development manual's index source count to match its frontmatter (62).

Files touched:

- `raw/sources/2026-11-05-livelycura-serlp-mobile-portal-parity.md`
- `wiki/sources/livelycura-serlp-mobile-portal-parity.md`
- `wiki/projects/serlp-mobile.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Portal features are in scope for serlp-mobile by default; how much belongs on mobile is not offered as a choice.

Follow-ups:

- None.

## [2026-11-02] ingest | Record LivelyCura Refetch Queries After Mutation

What changed:

- Preserved the user's 2026-11-02 rule from the HRM Employees review: LivelyCura client apps (SERLP portal, serlp-mobile, Loop) refresh screen data after a mutation with Apollo `refetchQueries` project-wide; the brief old value after Save (about 2–3 seconds on the Employees page) is accepted; don't propose `awaitRefetchQueries`, extra returned fields for cache writes, or `cache.modify` to change it.
- Added a Source Record with a repository usage check, a Durable Conventions bullet on the portal, serlp-mobile and Loop project pages, and a LivelyCura Family bullet in the development manual.
- Corrected the development manual's index source count to match its frontmatter (61).

Files touched:

- `raw/sources/2026-11-02-livelycura-refetch-queries-after-mutation.md`
- `wiki/sources/livelycura-refetch-queries-after-mutation.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/projects/serlp-mobile.md`
- `wiki/projects/livelycura-loop-app.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Post-mutation refresh stays on `refetchQueries`; the save delay is not offered as a fix.

Follow-ups:

- None.

## [2026-11-01] ingest | Record LivelyCura HRM Feature-By-Feature Review Scope

What changed:

- Preserved the user's 2026-11-01 correction from the HRM Employees review: report and decide only the current feature's items, keep finished features closed even for findings the current change caused, park later-feature items silently until that feature is reached, and don't call a message vague when it already tells the user what happened. Earlier consistent statements (Payroll 2026-10-19, Admin Portal 2026-10-25) are kept as context.
- Added a Source Record, one bullet under the Personal Operating Manual's Change And Remediation Work, and a Durable Conventions bullet on the portal, serlp-mobile and Loop project pages.

Files touched:

- `raw/sources/2026-11-01-livelycura-hrm-feature-by-feature-review.md`
- `wiki/sources/livelycura-hrm-feature-by-feature-review.md`
- `wiki/syntheses/personal-operating-manual.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/projects/serlp-mobile.md`
- `wiki/projects/livelycura-loop-app.md`
- `index.md`
- `log.md`

Key result:

- HRM review reports stay inside the current feature; closed and later features are not raised.

Follow-ups:

- None.

## [2026-10-31] ingest | C.E.Q.A React Hook Form Migration

What changed:

- Recorded the user's decision to move Call Center Web App and Keks Admin Portal from Formik to React Hook Form with the Yup resolver, and the correction to keep the existing form structure ("follow how I do things already").
- Replaced the Formik form rules in the development manual with the React Hook Form convention, keeping the structural rules (private schema, named form hook, screen-owned submission, no form controllers) and noting that unmigrated repositories stay on Formik.
- Updated both project pages: stack, form conventions, verification expectations, evidence, and the production Keks CORS ports.

Files touched:

- `raw/sources/2026-10-31-ceqa-react-hook-form-migration.md`
- `wiki/sources/ceqa-react-hook-form-migration.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/projects/call-center-web-app.md`
- `wiki/projects/keks-admin-portal.md`
- `index.md`

Key result:

- React Hook Form is the current form convention; verified pitfalls (stale `isValid` after `reset()`, `setValue` without validation, schema-inferred form types) are recorded with the fixes used.

Follow-ups:

- Decide whether and in what order the remaining Formik repositories migrate.

## [2026-10-29] correction | Bora Production Scripts Follow paystack_production

What changed:

- Recorded the user's correction that production scripts must follow the `scripts/paystack_production` pattern: `PROD_` env values and pasted production data in `constants`, never the local runtime, which is staging, and never fetching what the constants hold.
- Replaced the production seed and admin bootstrap description on the project page.

Files touched:

- `raw/sources/2026-10-29-bora-production-scripts-follow-paystack-production.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The project page names the production-script pattern and the two corrected scripts.

## [2026-10-28] update | Bora Production Admin Bootstrap And Fund Seed

What changed:

- Recorded the production fund seed for `BBF1100`, from the printed sheet and created hidden, and the bootstrap path that invites a missing first administrator.

Files touched:

- `raw/sources/2026-10-28-bora-production-admin-and-fund-seed.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `log.md`

Key result:

- The project page says how production gets its first administrator and its funds.

## [2026-10-28] decision | Bora Journey Since Inception Cannot Be Cleared

What changed:

- Recorded the user's decision that `updateFund` refuses an explicit `null` or `[]` for `sinceInceptionJourney` once a fund has a journey.

Files touched:

- `raw/sources/2026-10-28-bora-journey-cannot-be-cleared.md`
- `wiki/projects/bora-capital-backend.md`
- `log.md`

Key result:

- The Bora fund convention states how a stored journey is protected from clearing.

## [2026-10-28] correction | Bora New Handoff Per Update And Admin Portal Ownership

What changed:

- Recorded the user's repeated correction that each new backend update gets a new dated handoff, and that the sent 2026-10-24 handoff was restored and the journey change moved to 2026-10-28.
- Recorded that the admin portal is the frontend developer's work, its data is unverified, and Bora's PDFs are the only fund data source.

Files touched:

- `raw/sources/2026-10-28-bora-new-handoff-per-update-and-portal-ownership.md`
- `wiki/sources/bora-frontend-handoff-frozen.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Handoff and data-source rules now name the per-update file and the portal's ownership.

## [2026-10-28] correction | Bora Fund Chart Series Are The Printed Points

What changed:

- Recorded the user's correction that each chart series holds the values printed on that chart. `navHistory` holds the trend's NAV prices. The new `sinceInceptionJourney` holds the journey's GH¢ amounts.
- Recorded that the earlier seed data came from the portal's chart-line-reconstructed CSVs.

Files touched:

- `raw/sources/2026-10-28-bora-fund-charts-are-printed-points.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The fund convention names both series, their units, and their source.

## [2026-10-27] correction | Bora Funds Keep Two NAV Series

What changed:

- Recorded the user's correction that the 1 Year Price Trend (customers) and the Journey since inception (admin) are separate. `navHistory` is now the year only, and a new admin-only `sinceInceptionNavHistory` holds the journey. The seed writes both inline, with no CSV.

Files touched:

- `raw/sources/2026-10-27-bora-two-nav-series.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `log.md`

Key result:

- The fund convention names both series and who sees each.

## [2026-10-27] correction | Bora Seed Restored And NAV History Is The 1 Year Price Trend

What changed:

- Recorded that `navHistory` is the sheet's 1 Year Price Trend.
- Recorded that the 30 Sep seed is the user's original file restored and updated in place, keeping its original wording.

Files touched:

- `raw/sources/2026-10-27-bora-seed-restored-with-price-trend.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `log.md`

Key result:

- The seed convention names the price trend and the update-in-place rule.

## [2026-10-27] correction | Bora Fund Seed Keeps The Full NAV History

What changed:

- Recorded the user's correction that the 30 Sep seed must keep each fund's full daily NAV series. Its single printed point had wiped the dev history.
- The seed rule now includes the portal's 30 Sep NAV CSVs and forbids shrinking `navHistory` without confirmation.

Files touched:

- `raw/sources/2026-10-27-bora-seed-keeps-full-nav-history.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The seed convention no longer says single printed point.

## [2026-10-26] decision | Bora Fund Facts In One Stored Format

What changed:

- Preserved the user's decisions and the audit behind them. Fund facts are now stored in one format: known sheet wording is normalized and unknown wording rejected. A benchmark figure is required on every performance row. NAV series are allowed with range checks. The seed uses the 30 Sep 2026 sheets with the printed text verbatim.
- Recorded that the sheets' '1H' is calendar H1, not trailing 6M, and the open Bora sheet questions.

Files touched:

- `raw/sources/2026-10-26-bora-fund-fact-formats-and-sep-seed.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The fund-administration record carries the stored-format rules and the seed's 30 Sep basis.

## [2026-10-26] decision | Empty Bora Exit-Fee List Means Nil

What changed:

- Recorded that the dev fund values are the 30 Sep sheets, republished through the portal on 2026-10-23, not seed errors.
- Recorded that the portal saves a "Nil" redemption fee as an empty list, and the user's decision that an empty list shows "No exit fee".
- Added an open question about the Balanced 30 Sep sheet's NAV label.

Files touched:

- `raw/sources/2026-10-26-bora-empty-exit-fees-mean-nil.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `log.md`

Key result:

- The customer exit-fee contract defines what an empty list means.

## [2026-10-26] decision | Show Bora Customers Holding Period And Exit Fees

What changed:

- Preserved the user's requirement that customers see each fund's recommended holding period and redemption (exit) fee tiers before investing. Both were already stored; `CISFundDetails` now exposes them.
- Recorded that `totalAum` is the fact sheet's "Fund Size".

Files touched:

- `raw/sources/2026-10-26-bora-customer-holding-period-exit-fees.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The customer fund contract carries the two disclosures customers need before investing.

## [2026-10-26] correction | Bora Handoffs Carry Only Frontend Items

What changed:

- Recorded the user's correction that a frontend handoff is written for the frontend developer: backend open questions, deferred backend decisions, backend-owned issues, and questions for the user go to the user in chat, never into the handoff.
- Recorded that the staging 502 was the 2026-10-23 `SPACES_ENDPOINT` fix (missing `https://`), and that earlier session transcripts are searched before a status claim is repeated.

Files touched:

- `raw/sources/2026-10-26-bora-handoff-audience-frontend-only.md`
- `wiki/sources/bora-frontend-handoff-frozen.md`
- `wiki/sources/bora-fund-fact-sheet-pdfs.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The handoff convention states its audience and what stays out of it.

## [2026-10-26] correction | Remove Stale Bora Staging Storage Claim

What changed:

- Recorded the user's correction that staging storage was already fixed. The "staging banner uploads return 502" claim came from Kusantec's 23 Oct handoff and was stale; it was removed from the fact-sheet Source Record and the backend page.
- Added the rule that status claims from third-party documents are confirmed with the user before they go into a handoff.

Files touched:

- `raw/sources/2026-10-26-bora-staging-storage-already-fixed.md`
- `wiki/sources/bora-fund-fact-sheet-pdfs.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- No vault page says staging storage is broken.

## [2026-10-25] ingest | Record LivelyCura HRM Employee Record Design

What changed:

- Preserved the user's 2026-10-25 employee-record redesign request, the "ERP is general-purpose" correction and their four plan answers.
- Added a Source Record and a backend Durable Conventions bullet.

Files touched:

- `raw/sources/2026-10-25-livelycura-hrm-employee-record-design.md`
- `wiki/sources/livelycura-hrm-employee-record-design.md`
- `wiki/projects/livelycura-backend.md`
- `index.md`
- `log.md`

Key result:

- Employee work starts from industry-neutral built-in fields plus organization-defined questions.

## [2026-10-25] ingest | Record LivelyCura User Account Versus Employee Rule

What changed:

- Preserved the user's 2026-10-25 rule that the shared login account and an organization's employee record stay separate, with no syncing of HR edits.
- Added a Source Record, a backend Durable Conventions bullet and a Loop App note.

Files touched:

- `raw/sources/2026-10-25-livelycura-user-account-vs-employee.md`
- `wiki/sources/livelycura-user-account-vs-employee.md`
- `wiki/projects/livelycura-backend.md`
- `wiki/projects/livelycura-loop-app.md`
- `index.md`
- `log.md`

Key result:

- Employee fixes and account fixes stay separate; Loop shows employee details.

## [2026-10-25] ingest | Record Think-Like-A-User Direction

What changed:

- Preserved the user's 2026-10-25 direction to judge fixes by real user behaviour, skip guards against unlikely actions, and avoid internal jargon.
- Added a Source Record and one bullet under the Personal Operating Manual's Change And Remediation Work.

Files touched:

- `raw/sources/2026-10-25-think-like-a-user-direction.md`
- `wiki/sources/think-like-a-user-direction.md`
- `wiki/syntheses/personal-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Future proposals are weighed by what real users would plausibly do.

## [2026-10-25] decision | Record Bora Fund Fact-Sheet PDF Storage

What changed:

- Preserved the user's 2026-10-24 decisions on official fund fact-sheet PDFs: no versioning, extraction stays in the portal, a 3 MiB cap, a publish date guard, a new dated handoff, and the `SetFundVisibilityInput` rename.
- Added a Source Record and updated the Bora backend page (fund model, private signed URLs and reference-checked deletes, current handoff, offline codegen) and the frozen-handoff record.

Files touched:

- `raw/sources/2026-10-25-bora-fund-fact-sheet-pdfs.md`
- `wiki/sources/bora-fund-fact-sheet-pdfs.md`
- `wiki/sources/bora-frontend-handoff-frozen.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The backend page carries the fact-sheet slot model, the private-upload serving rule, and `docs/frontend-handoff-2026-10-24.md` as the current handoff.

## [2026-10-24] update | Drop the Holidays "Still to be announced" Card

What changed:

- Preserved the product owner's 2026-10-24 decision to remove the Eid "still to be announced" card: HR adds announced holidays itself, and a day HR doesn't add was not a holiday for that organization.
- Updated the holidays Source Record, the backend and Pharmacy Portal pages, and the index entry.

Files touched:

- `raw/sources/2026-10-24-livelycura-hrm-holidays-no-expected-card.md`
- `wiki/sources/livelycura-hrm-holidays-decisions.md`
- `wiki/projects/livelycura-backend.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `index.md`
- `log.md`

Key result:

- No holiday reminder card on any screen; Eid and other announced days are created with New Holiday.

## [2026-10-24] update | Record LivelyCura HRM Holidays Build-Spec Answers

What changed:

- Preserved the product owner's two answers to the Holidays build spec as conversation evidence.
- Added them to the holidays Source Record and the backend page's Holidays subsection.

Files touched:

- `raw/sources/2026-10-24-livelycura-hrm-holidays-spec-answers.md`
- `wiki/sources/livelycura-hrm-holidays-decisions.md`
- `wiki/projects/livelycura-backend.md`
- `index.md`
- `log.md`

Key result:

- Holiday open-shift pickups count only for the picked-up shift, and unmarked holiday clock-ins are allowed but flagged for the manager.

## [2026-10-23] ingest | Record LivelyCura HRM Holidays Decisions

What changed:

- Preserved the product owner's nine 2026-10-23 holiday decisions verbatim, with the research findings that prompted them, as conversation evidence.
- Added a Source Record and a "Holidays (Decided, Not Yet Built)" subsection under the backend page's Decisions And Rationale.
- Linked the Pharmacy Portal, Loop App, SERLP Mobile and Admin Portal pages to the backend rules.

Files touched:

- `raw/sources/2026-10-23-livelycura-hrm-holidays-decisions.md`
- `wiki/sources/livelycura-hrm-holidays-decisions.md`
- `wiki/projects/livelycura-backend.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/projects/livelycura-loop-app.md`
- `wiki/projects/serlp-mobile.md`
- `wiki/projects/livelycura-admin-portal.md`
- `index.md`
- `log.md`

Key result:

- Future HRM holiday work starts from the decided rules: everyone off by default with a per-holiday working list, one entry per year with a type, and attendance that corrects itself without overwriting clock-ins or manual corrections.

Follow-ups:

- Nothing is built yet; verify the pages against the implementation once it lands. Holiday pay waits for the Payroll feature.

## [2026-10-23] ingest | Record LivelyCura HRM Leave Balances Decisions

What changed:

- Preserved the product owner's 2026-10-22/23 leave-balance decisions, the Labour Act 2003 (Act 651) sections they rely on, and the adopted review safeguards as conversation evidence.
- Added a Source Record and a "Leave Balances (Decided, Not Yet Built)" subsection under the backend page's Decisions And Rationale.
- Linked the Pharmacy Portal, Loop App, and SERLP Mobile pages to the backend rules.

Files touched:

- `raw/sources/2026-10-23-livelycura-hrm-leave-balances-decisions.md`
- `wiki/sources/livelycura-hrm-leave-balances-decisions.md`
- `wiki/projects/livelycura-backend.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/projects/livelycura-loop-app.md`
- `wiki/projects/serlp-mobile.md`
- `index.md`
- `log.md`

Key result:

- Future HRM leave work starts from the decided rules: hard annual balance in working days, reasoned append-only HR adjustments as the only override, full carry-over, and warn-only limits for other leave types.

Follow-ups:

- Nothing is built yet; verify the pages against the implementation once it lands. Payroll links (unpaid deductions, exit payout) wait for the Payroll feature.

## [2026-10-22] update | Record Bora Handoff Sent-Status Correction

What changed:

- Recorded the user's correction that git state does not show whether a frontend handoff was sent: ask before adding to an existing dated handoff, and start a new one if it was sent or the answer is unknown.
- Recorded that `docs/frontend-handoff-2026-10-17.md` was already sent and restored to that version, and that the push-device contract moved to `docs/frontend-handoff-2026-10-22.md`.
- Pointed the backend, mobile, and push-device pages at the 2026-10-22 handoff.

Files touched:

- `raw/sources/2026-10-22-bora-handoff-sent-status-correction.md`
- `wiki/sources/bora-frontend-handoff-frozen.md`
- `wiki/sources/bora-push-device-binding.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/projects/bora-capital-mobile-app.md`
- `index.md`
- `log.md`

Key result:

- Future Bora work asks before extending a dated handoff instead of inferring sent status from git.

## [2026-10-21] update | Record Nalo Recipient Format For Bora

What changed:

- Recorded the user's correction that Nalo rejects a number with a leading `+`, and that the adapter must remove it itself, as LivelyCura's does.
- Recorded the user's own adapter rewrite, which is not matched to LivelyCura: any failure now returns false instead of throwing, and Hubtel always sends from `BoraCapital`.

Files touched:

- `raw/sources/2026-10-21-bora-nalo-msisdn-plus.md`
- `wiki/sources/bora-notifications-marketing.md`
- `wiki/projects/bora-capital-backend.md`
- `log.md`

Key result:

- The Bora SMS records match the current adapter: numbers are sent without the plus, and failures return false.

## [2026-10-21] update | Correct Bora Nalo SMS Record To The Simplified Build

What changed:

- Recorded the user's correction that the first Nalo build was over-engineered, given that LivelyCura had been named as the reference, and the simplified build that replaced it: a LivelyCura-shaped Nalo adapter, `SMS_PROVIDER=hubtel` as the only switch, bulk sending of identical texts, and every failure retried.
- Removed the outcome classification, batch fallback, send budget, and startup credential check claims from the Bora pages.
- Added a Change Control rule: build to a named reference implementation's scope, and propose any extra layers separately.

Files touched:

- `raw/sources/2026-10-21-bora-nalo-sms-simplification.md`
- `wiki/sources/bora-notifications-marketing.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- The Bora SMS records now match the simplified Nalo build, and the manual records how to build from a named reference.

## [2026-10-21] ingest | Record Bora Nalo SMS Provider And Hubtel Switch

What changed:

- Recorded the user's requirement that Nalo becomes Bora's SMS provider while Hubtel stays switchable, and the five approved decisions: `SMS_PROVIDER` defaulting to `nalo`, a staging/production credential check at startup, unknown-outcome-no-resend for Nalo only, Nalo pacing of 100 SMS per 30 seconds with up to 100 recipients per request, and the campaign SMS hold unchanged.
- Recorded the Nalo API facts (JSON send-message, a comma-separated recipient list with one job ID, documented status codes, no published rate limit) and the LivelyCura conventions followed.
- Replaced the stale Hubtel-only pacing and hold wording, corrected the claim that Bora's `.env.default` is untracked, and replaced the Hubtel batch open question with the Nalo live checks.

Files touched:

- `raw/sources/2026-10-21-bora-nalo-sms-provider.md`
- `wiki/sources/bora-notifications-marketing.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Bora SMS conventions now name Nalo as the default provider, Hubtel as the switchable alternative, the per-provider pacing, and the live checks still required before campaign SMS can be enabled.

## [2026-10-21] ingest | Record Altin Onboarding And Post-Sign-In Gate

What changed:

- Recorded the user's onboarding request and decisions: onboarding (KYC) is how an organization gets approved, so pending or rejected organizations open it as the root screen; members with no organization, or a paused or closed one, see a blocking notice with contact support; approved organizations reach onboarding from More → Compliance.
- Recorded the gate design (status and VIEW_KYC only, composite navigation key), the System freshness rules, the one-screen tabs layout the user chose over an Apps module or separate More rows, and the instruction to verify KYC writes and uploads offline only.
- Noted the live finding that an active organization had no profile, and the open support-contact values and token-expiry remount.

Files touched:

- `raw/sources/2026-10-21-altin-onboarding-gate.md`
- `wiki/sources/altin-onboarding-gate.md`
- `wiki/projects/altin-partner-mobile.md`
- `index.md`
- `log.md`

Key result:

- Future Altin work treats onboarding as the pre-approval root screen and keeps the gate keyed on status alone.

Follow-ups:

- Record the support contact values when the user supplies them.

## [2026-10-21] ingest | Record Bora Push Device Binding And Input-Object Convention

What changed:

- Recorded the user's bug reports and decisions for the Bora push-notification fix: per-install, session-bound push devices; unbinding on session revocation; client-bound sign-in codes; the `NEW_SIGNIN` alert replacing the welcome-back push; Expo receipt pruning and per-message retries; token redaction; `PUSH_DEVICE_REASSIGNED` audit events; and the old token purge.
- Recorded the user's correction that Bora functions take one input object typed by an interface.
- Replaced the "welcome-back push" wording in the backend conventions and the notifications Source Record, and added the new registration contract to the mobile project page.

Files touched:

- `raw/sources/2026-10-21-bora-push-device-binding.md`
- `raw/sources/2026-10-21-bora-single-input-object-convention.md`
- `wiki/sources/bora-push-device-binding.md`
- `wiki/sources/bora-single-input-object-convention.md`
- `wiki/sources/bora-notifications-marketing.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/projects/bora-capital-mobile-app.md`
- `index.md`
- `log.md`

Key result:

- Future Bora work treats push registrations as per install and session-bound, and writes functions with one input object.

## [2026-10-20] ingest | Altin Reports Fixes

What changed:

- Recorded the user-approved 2026-10-20 Altin Partner Mobile Reports fixes:
  - web date-preset day ranges;
  - one date range computed per Generate, stored in `useReportFilters`, and shared by the query, the scope line and every export, rolling forward after midnight;
  - A4 landscape for Order funnel, Payment attempts and Assignment efficiency, with Print passing the matching orientation to the print sheet;
  - a 297 × 210 mm sheet for landscape reports, a deliberate difference from the web because iOS clipped the web's 210 mm sheet and cut off Payment attempts' last columns;
  - Receivables aging, which has no date filter, always just refetching on refresh;
  - per-report loading skeletons;
  - courier print lines with the web `CourierCell` wording;
  - deletion of the unused `ComingSoon` component.
- Replaced the stale claim that the repository docs keep "the web's backend values". They now say exports print the web's values except rates, which are scaled.
- Removed backend-data observations from the wiki pages, because the user put the backend out of scope. Raw evidence is unchanged.
- Recorded the 2026-10-20 device check: presets, landscape PDFs and Print, all 14 Payment attempts columns, three skeletons, and Dispatch backlog's exports.

Files touched:

- `raw/sources/2026-10-20-altin-reports-fixes.md`
- `raw/sources/2026-10-20-altin-reports-print-orientation-refresh.md`
- `raw/sources/2026-10-20-altin-reports-landscape-sheet-device-check.md`
- `wiki/sources/altin-reports-mobile.md`
- `wiki/projects/altin-partner-mobile.md`
- `index.md`
- `log.md`

Key result:

- The existing Reports Source Record and project page reflect the 2026-10-20 state, with no duplicate pages.

Follow-ups:

- A device pass for dark mode, Android, and the remaining unchecked PDF and Print exports.

## [2026-10-19] ingest | Bora Admin Portal CI/CD Convention

What changed:

- Recorded the user's correction that web portal CI/CD copies the `livelycura-pharmacy-portal` workflows: environment-named repository variables for API URLs, environment-named repository secrets for Netlify, and self-contained staging/production build → artifact → deploy jobs. API URLs never go in workflow YAML and values are not scoped per GitHub environment.

Files touched:

- `raw/sources/2026-10-19-bora-admin-portal-ci-cd-convention.md`
- `wiki/sources/bora-admin-portal-ci-cd-convention.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- The development manual's Change Control section carries the CI/CD convention.

## [2026-10-18] ingest | Altin Reports Rate Scaling

What changed:

- Recorded the user's decision that Altin Partner Mobile report exports scale the backend's rate fractions to percentages (`fractionToPercent`, decimal shift in the Decimal string) for Assignment efficiency, Payment attempts, and Revenue & commission. The web prints them unscaled, so this is a documented deliberate difference.
- Refreshed the Reports live-check state: every report screen was checked, COD reconciliation and Receivables aging were disabled server-side, and Order funnel returns zeros. This replaces the earlier "Courier earnings only" claim.
- Flagged that the repository's "exports keep the web's backend values" wording now means scaled backend values.

Files touched:

- `raw/sources/2026-10-18-altin-reports-rate-scaling.md`
- `wiki/sources/altin-reports-mobile.md`
- `wiki/projects/altin-partner-mobile.md`
- `index.md`
- `log.md`

Key result:

- The existing Reports Source Record and project page carry the rate-scaling decision and the current verification boundary, without a duplicate record.

Follow-ups:

- Dark mode, Dispatch backlog's exports, and the COD reconciliation and Receivables aging data once those reports are re-enabled.

## [2026-10-18] ingest | Altin Reports Mobile

What changed:

- Recorded the 2026-10-18 Altin Partner Mobile Reports build and the user's decisions: Reports in the web page order with per-report permission rules, one mobile card per record (no sideways tables, no separate status tables, no Summary label), Print/PDF/CSV identical to the web exports apart from documented deliberate fixes, and Revenue & commission kept with a deprecation caveat.
- Replaced the project page's "Reports tab remains a placeholder" statements.
- Added the lesson that `pod install` fails silently without a UTF-8 locale, so native rebuilds must be confirmed.

Files touched:

- `raw/sources/2026-10-18-altin-reports-mobile.md`
- `wiki/sources/altin-reports-mobile.md`
- `wiki/projects/altin-partner-mobile.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- The project page reflects the built Reports tab, its screen and export rules, and the native-rebuild check. Evidence is the repository's `docs/reports.md` and `AGENTS.md` Reports section.

Follow-ups:

- A live pass of the nine unchecked reports and dark mode.
- The project Summary still describes the pre-redo Support (Raise a ticket with order links); it predates the 2026-10-09 chat-first redo.

## [2026-10-17] update | Restore Sent Bora Handoff And Add 2026-10-17 Handoff

What changed:

- Recorded that the sent 2026-10-13 frontend handoff had been extended after it was pushed. It was restored to the sent content, and the additions moved to a new 2026-10-17 handoff.
- Added the rule to check the remote push history before extending a dated handoff.

Files touched:

- `raw/sources/2026-10-17-bora-frontend-handoff-2026-10-17.md`
- `wiki/sources/bora-frontend-handoff-frozen.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Sent handoffs stay frozen, and the frontend developer receives only the delta in the 2026-10-17 handoff.

Follow-ups:

- None.

## [2026-10-17] decision | Record Bora Local-Only Scripts

What changed:

- Recorded that the bootstrap, Paystack setup, and seed scripts, plus their two specs, are gitignored and never pushed. Committed tests use a synthetic fund-facts fixture.

Files touched:

- `raw/sources/2026-10-17-bora-local-only-scripts.md`
- `wiki/sources/bora-local-only-scripts.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Committed code must not depend on local-only scripts; a fresh-checkout simulation passes CI checks.

Follow-ups:

- None.

## [2026-10-16] update | Split Bora User Updates By Transaction

What changed:

- Recorded the user's correction: `updateUserInSession` is for transactions only, with the session as a required parameter, and other user writes use a generic `updateUser`. The profile service became `updateUserProfile`.

Files touched:

- `raw/sources/2026-10-16-bora-user-update-transaction-split.md`
- `wiki/sources/bora-single-user-update-path.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- The same-day single-function record is superseded by two typed paths that share one helper.

Follow-ups:

- None.

## [2026-10-16] ingest | Record Bora Single User-Update Path

What changed:

- Recorded the user's correction that repeated operations are written once and imported. In Bora, every single-user write now goes through `updateUserInSession`.

Files touched:

- `raw/sources/2026-10-16-bora-single-user-update-path.md`
- `wiki/sources/bora-single-user-update-path.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- One user-update path with a fixed credential projection and optional transaction session; the write-once rule is in the development manual.

Follow-ups:

- None.

## [2026-10-16] update | Correct Bora KYC Storage And Cash Movement Detection

What changed:

- Recorded the restructure of the KYC saved form after the user's correction. Images now live in the `kycSubmissions` document, the supervision reference and the form commit in one transaction, approval deletes the form transactionally, and best-effort try/catch was removed.
- Recorded that cash movement balance rows are found by position rather than wording, and that single-digit days are accepted.

Files touched:

- `raw/sources/2026-10-16-bora-kyc-repost-and-cash-movement.md`
- `wiki/sources/bora-kyc-supervision-and-statement-update.md`
- `wiki/projects/bora-capital-backend.md`
- `log.md`

Key result:

- The saved KYC form is atomic with KYC state, and the statement parser no longer depends on BCL's wording.

Follow-ups:

- None.

## [2026-10-16] ingest | Record Bora KYC Re-post And Grow Wealth Cash Movements

What changed:

- Recorded BCL's answer: partners re-post a rejected KYC through `addindividualidentity_bcl` with amended fields, with no duplicate flag; IMS data is never edited. This supersedes the 2026-10-13 wait for an update endpoint.
- Recorded the implementation: the saved `kycSubmissions` form with private reused images, `updateKyc` for `REJECTED` users, the shared `submitKycToBcl`, the owner-only `User.kycSubmission`, and deletion after approval.
- Recorded the Grow Wealth cash movement statement (`LinkedPortfolioCMS`) and its structured GraphQL query.

Files touched:

- `raw/sources/2026-10-16-bora-kyc-repost-and-cash-movement.md`
- `wiki/sources/bora-kyc-supervision-and-statement-update.md`
- `wiki/sources/bora-grow-wealth-existing-customer-valuations.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Rejected customers correct only what is wrong and re-post, and linked Grow Wealth customers can view cash movements.

Follow-ups:

- Verify a rejected-KYC re-post and a cash movement statement against staging BCL.

## [2026-10-13] ingest | Record Bora createKyc Without Resubmission

What changed:

- Recorded the user's correction: BCL's add endpoint only creates an individual and is never used to resubmit or update a rejected KYC. BCL will provide an update endpoint.
- Recorded the rename of `updateKyc`/`UpdateKycInput` to `createKyc`/`CreateKycInput`, which now accepts only `PENDING` users, and the removal of the 2026-09-06 resubmission design.

Files touched:

- `raw/sources/2026-10-13-bora-createkyc-no-resubmission.md`
- `wiki/sources/bora-kyc-supervision-and-statement-update.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Rejected customers see BCL's reason and cannot create a duplicate BCL individual by resubmitting.

Follow-ups:

- Build rejected-KYC updates on BCL's update endpoint when it is delivered.

## [2026-10-13] ingest | Record Bora Push Capability Gating Rejected

What changed:

- Recorded that Expo drops an Android push whose channel is missing on the device, and that iOS falls back to the default sound when the file is missing.
- Recorded the user's decision to skip the mobile developer's per-token capability gating, `appVersion`, and feature switch while the app is pre-production with reinstall-only builds.

Files touched:

- `raw/sources/2026-10-13-bora-push-sound-channel.md`
- `wiki/sources/bora-notifications-marketing.md`
- `log.md`

Key result:

- The backend keeps sending the Bora sound and channel on every push; testers reinstall the new build.

Follow-ups:

- Add per-device gating before any channel or sound change after the app is in production.

## [2026-10-13] ingest | Record Bora Push Sound And Channel

What changed:

- Recorded the user's choice of `bora_signature_v1.wav` (iOS sound) and `bora_updates_v1` (Android channel), applied to every push in `sendPushNotification` as overridable defaults.
- Recorded why the backend must send the iOS sound, and that a channel sound change ships as a new versioned file and channel.

Files touched:

- `raw/sources/2026-10-13-bora-push-sound-channel.md`
- `wiki/sources/bora-notifications-marketing.md`
- `index.md`
- `log.md`

Key result:

- Every Bora push plays the Bora sound once the app bundles the file and creates the channel.

Follow-ups:

- None.

## [2026-10-13] ingest | Record Bora One Handoff Per Unpushed Batch

What changed:

- Refined the handoff rule after a user correction: all uncommitted and unpushed updates go in one dated handoff, extended in place until pushed and sent, rather than several dated files.
- Recorded the merge into `docs/frontend-handoff-2026-10-13.md`, including another session's currency, lookup, and Grow Wealth notes, and the restoration of the sent app handoff.

Files touched:

- `raw/sources/2026-10-13-bora-one-handoff-per-unpushed-batch.md`
- `wiki/sources/bora-frontend-handoff-frozen.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- One handoff file covers the current unpushed batch in its final state, and the sent handoffs are back to their committed versions.

Follow-ups:

- None.

## [2026-10-13] ingest | Record Bora refreshToken Rate Limit Removed

What changed:

- Recorded the user-approved removal of all `refreshToken` rate limits (the per-IP limit, and the per-session limit from 2026-10-12) and of the `rateLimitRule` `getKey` option; `refreshToken` now has an explicit `allow` policy.
- Kept the frontend requirement to refresh one at a time per device.

Files touched:

- `raw/sources/2026-10-13-bora-refresh-token-limit-removed.md`
- `wiki/sources/bora-client-ip-app-platform.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Token refresh can no longer be blocked by a rate limit; signed single-use tokens and reuse detection remain the protection.

Follow-ups:

- Tell the frontend that the 10-per-minute refresh limit in `frontend-handoff-2026-10-12.md` no longer applies.

## [2026-10-12] ingest | Record Bora Error Format Consistency

What changed:

- Recorded the reproduced problems: Apollo request errors were shown as "Internal server error" and reported to Sentry; Express and REST errors lacked the error array and code; an expired OTP returned `INTERNAL_SERVER_ERROR`.
- Recorded the fixes: Apollo client codes map to `BAD_REQUEST`, a shared `getErrorCode` with a 4xx fallback, `constructHTTPResponse` in the GraphQL error shape, and schema hints hidden outside development.

Files touched:

- `raw/sources/2026-10-12-bora-error-format-consistency.md`
- `wiki/sources/bora-error-format-consistency.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Every error the frontend receives has the documented array shape and a code, and malformed requests no longer read as server crashes.

Follow-ups:

- None.

## [2026-10-12] ingest | Record Bora Existing-Customer Account Ownership

What changed:

- Recorded the confirmed CAL-05 problem: existing clients could list their BCL accounts but were blocked from transacting, because ownership was checked against a list only app-opened accounts filled.
- Recorded the approved fix: save BCL-confirmed account numbers at existing-customer onboarding and on every BCL account read, keeping the transaction check local.

Files touched:

- `raw/sources/2026-10-12-bora-existing-customer-account-ownership.md`
- `wiki/sources/bora-existing-customer-account-ownership.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Existing clients can transact on their BCL accounts once onboarded or once the accounts screen loads.

Follow-ups:

- Decide whether accounts BCL stops returning should ever be removed from the cache.

## [2026-10-12] ingest | Record Bora Frontend Handoffs Frozen Once Sent

What changed:

- Recorded the user's correction: never edit a frontend handoff that has been sent; each new batch of frontend-facing changes gets a new dated `docs/frontend-handoff-YYYY-MM-DD.md`.
- Replaced the 2026-10-01 convention of updating two living handoff files in place.

Files touched:

- `raw/sources/2026-10-12-bora-frontend-handoff-frozen.md`
- `wiki/sources/bora-frontend-handoff-frozen.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The 2026-10-12 changes live in `docs/frontend-handoff-2026-10-12.md`, and the sent handoffs no longer contain the agent's edits.

Follow-ups:

- The user decides whether another session's currency, lookup-filter, and Grow Wealth additions in the sent app handoff move to a dated file.

## [2026-10-12] ingest | Record Bora KYC ApprovalStatus Contract

What changed:

- Recorded BCL's ApprovalStatus samples (credentials and cookies omitted): `P` pending, `A` approved, `R` rejected with `Remarks`, and `0`+`Invalid` for an unrecognized reference. These supersede the 2026-09-18 uncertainty and the 2026-10-11 interim identity-lookup rule.
- Recorded the implementation: map by code, keep the IdentityID lookup only after approval, and store the rejection reason as `User.kycRejectionReason`.
- Recorded that the previous code required `Status: "0"` and would have kept every real submission pending.

Files touched:

- `raw/sources/2026-10-12-bora-kyc-approval-status-contract.md`
- `wiki/sources/bora-kyc-supervision-and-statement-update.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Approved and rejected KYC now reach the app, and rejected customers see BCL's reason.

Follow-ups:

- Ask BCL to include the IdentityID in the approved response.

## [2026-10-12] ingest | Record Bora Signup Flat IP Cap

What changed:

- Recorded the shared durable limiter `createRateLimitWindow` (`rateLimitWindows`, unique `{ scope, keyHash }`), now used by the sign-in password lock and signup.
- Recorded the flat signup cap of 20 per IP per hour, which replaces the escalating per-IP cooldown and the `ipHash` path on `authRequestThrottles`.
- Recorded the open questions: tuning the cap, SMS abuse spread across many IPs, and the leftover production `ipHash` index.

Files touched:

- `raw/sources/2026-10-12-bora-signup-flat-ip-cap.md`
- `wiki/sources/bora-client-ip-app-platform.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- A busy carrier or office IP waits at most an hour for signups instead of being locked out for a day.

Follow-ups:

- Decide on SMS fraud controls or country restrictions for signup numbers; optionally drop `ipHash_1_action_1`.

## [2026-10-12] ingest | Record Bora refreshToken Session Limit

What changed:

- Recorded the `refreshToken` limits: 120 per minute per IP as a flood guard, then 10 per minute per session keyed on the verified refresh JWT (`sid`, or the user for legacy tokens). `rateLimitRule` gained an optional `getKey`.
- Recorded that clients must refresh one at a time, because a reused refresh token revokes the whole session family.

Files touched:

- `raw/sources/2026-10-12-bora-refresh-token-session-limit.md`
- `wiki/sources/bora-client-ip-app-platform.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Customers behind a shared carrier IP no longer block each other's token refresh.

Follow-ups:

- Replace the escalating per-IP signup cooldown with a flat per-IP cap.

## [2026-10-11] ingest | Record Bora Sign-In Password Lock

What changed:

- Recorded that per-IP limits are only a flood guard and that OTP sends and guesses were already limited per customer.
- Recorded the new sign-in password lock: 5 attempts per phone number per 15 minutes, spent before the password check, unknown numbers counted alike, cleared by a correct password or any password reset or change.
- Withdrew the earlier idea of keying signup on email; the remaining follow-ups are `refreshToken` per session and a flat per-IP signup cap.

Files touched:

- `raw/sources/2026-10-11-bora-signin-password-lock.md`
- `wiki/sources/bora-client-ip-app-platform.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- An attacker rotating IPs can no longer guess passwords for one phone number without limit.

Follow-ups:

- Key `refreshToken` on the session; replace the escalating per-IP signup cooldown with a flat cap.

## [2026-10-11] ingest | Record Bora Client IP Behind App Platform

What changed:

- Recorded that App Platform puts the caller IP in `do-connecting-ip` and its own ingress address in `X-Forwarded-For`, so `trust proxy` cannot fix shared rate limits.
- Recorded the fix: `getClientIp` keys every shield rate limit and the signup cooldown on `do-connecting-ip` in both the HTTP and WebSocket contexts.
- Recorded the user's plan to put their own Cloudflare zone in front later, and the required switch to range-checked `CF-Connecting-IP` when that happens.

Files touched:

- `raw/sources/2026-10-11-bora-client-ip-app-platform.md`
- `wiki/sources/bora-client-ip-app-platform.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Rate limits apply per caller IP instead of to all customers combined.

Follow-ups:

- Key signup, sign-in and OTP limits on the email or phone, and `refreshToken` on the session.
- Update `getClientIp` before enabling the user's own Cloudflare proxy.

## [2026-10-11] ingest | Record Bora KYC BCL Agreed Outcome Rule

What changed:

- Recorded BCL's interim KYC rule: ApprovalStatus only detects pending; after that, the identity lookup decides (identity returned = approved, confirmed miss = rejected with a generic message).
- Recorded Bora's safeguards: provider failures never reject, a stated approval followed by a miss stays pending, and a stated rejection skips the lookup. Only an HTTP 400 with a message counts as a confirmed miss, which deliberately departs from the general `fetchBclData` passthrough rule.
- Recorded the open requests to BCL: explicit outcomes, IdentityID on approval, a rejection reason, and resubmission rules.

Files touched:

- `raw/sources/2026-10-11-bora-kyc-bcl-agreed-outcome-rule.md`
- `wiki/sources/bora-kyc-supervision-and-statement-update.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Customers who receive BCL's approval email see approved on the next app open, and an outage can no longer mark anyone rejected.

Follow-ups:

- Replace the interim rule when BCL returns explicit outcomes with an IdentityID and a rejection reason.

## [2026-10-11] ingest | Record Bora BCL Error Passthrough And Secret-File Rule

What changed:

- Recorded the user's cross-project rule: never read `.env` or other secret-bearing files, even for a live provider call; the user runs credentialed calls.
- Recorded the Bora convention that BCL `fetchdata` status codes are unreliable, so BCL's `Description`/`Message` goes to the frontend as a 400 through the shared `fetchBclData`. A 502 is used only for unreachable or unreadable responses. The same rule now covers Grow Wealth.
- Recorded the new authenticated `getCurrencies` and `getCurrencyRates` lookups and the open BCL questions on rate direction and KYC currency.

Files touched:

- `raw/sources/2026-10-11-bora-bcl-error-passthrough-and-secret-files.md`
- `wiki/sources/bora-bcl-error-passthrough-and-secret-files.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/personal-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Agents leave secret files unread in every project, and Bora surfaces BCL's own error text instead of modelling BCL error shapes.

Follow-ups:

- Record BCL's answers on `CurrencyRate` direction and KYC-currency matching when the user has them.

## [2026-10-10] ingest | Record LivelyCura Fleet Jobs Naming Decision

What changed:

- Recorded the user's decision to name the Fleet job entity `FleetJob`/`fleetJobs` across backend, Pharmacy Portal and SERLP Mobile code. It is an exception to the drop-the-Fleet-prefix rule and applies only to jobs.
- Recorded the clarified scope: stored `jobId` becomes `fleetJobId` and the audit entity becomes `FleetJob`, with no migration; URLs, deep links, route constants and visible labels stay.

Files touched:

- `raw/sources/2026-10-10-livelycura-fleet-jobs-naming-decision.md`
- `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`
- `wiki/projects/livelycura-backend.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/projects/serlp-mobile.md`
- `index.md`
- `log.md`

Key result:

- Fleet jobs carry the `Fleet` prefix in code; every other Fleet entity keeps the no-prefix rule.

Follow-ups:

- None.

## [2026-10-09] ingest | Record Call Center Wider Search Hook And Action Correction

What changed:

- Recorded the user's correction that new request hooks follow the sibling location-hook shape, with no inline response interfaces or custom error classes.
- Recorded that dropdown actions must look clickable, and the `searchLocationWider` integration rules.

Files touched:

- `raw/sources/2026-10-09-call-center-wider-search-hook-and-action-correction.md`
- `wiki/sources/call-center-wider-search-hook-and-action-correction.md`
- `wiki/projects/call-center-web-app.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Agents copy the nearest sibling's structure instead of introducing new patterns.

Follow-ups:

- Admin-dashboard "Wider Search" usage type awaits the admin repository location.

## [2026-10-09] correction | Record Altin Profile Separate Editors Correction

What changed:

- Recorded the user's correction that the profile photo, phone number and alternate phone use different APIs and must not be saved through one form.
- Recorded the rule that phone inputs take local numbers converted with awesome-phonenumber, as in Check City and the admin portal.

Files touched:

- `raw/sources/2026-10-09-altin-profile-separate-editors-correction.md`
- `wiki/sources/altin-profile-separate-editors-correction.md`
- `wiki/projects/altin-partner-mobile.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Agents give separately saved values their own editors and never make users type a country code.

Follow-ups:

- Decide whether order creation's recipient phone moves to local entry too.

## [2026-10-09] decision | Record Altin Support Chat-First Redo

What changed:

- Recorded the user's decisions: a support subject is derived from the selected category, and an order with an existing live ticket reopens it instead of raising another.
- Recorded Altin Support's chat-first redesign after Check City, the removed order-issue form, and the review findings left for the user.

Files touched:

- `raw/sources/2026-10-09-altin-support-chat-first-redo.md`
- `wiki/sources/altin-support-chat-first-redo.md`
- `wiki/projects/altin-partner-mobile.md`
- `index.md`
- `log.md`

Key result:

- Agents keep Altin Support chat-first and know the one-ticket-per-order rule is visibility-limited until the backend guards it.

Follow-ups:

- User choices pending: live updates, photo-library attachments, closed-ticket new conversation, and a backend duplicate guard. Profile redo is still to come.

## [2026-10-09] correction | Record Altin Formik onSubmit Correction

What changed:

- Recorded the user's correction that Formik `onSubmit` never makes backend requests: form hooks hold state only and screens own submission, following the LivelyCura pharmacy portal, admin portal and Check City.
- Superseded the earlier SERLP onSubmit rules and the same-day "repository committed hooks" rule in the Altin project page and the development manual.
- Recorded the Check City vs Altin Support comparison that the user asked for, ahead of redoing Profile and Support.

Files touched:

- `raw/sources/2026-10-09-altin-formik-onsubmit-correction.md`
- `wiki/sources/altin-formik-onsubmit-correction.md`
- `wiki/projects/altin-partner-mobile.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Agents writing forms in Altin or sibling LivelyCura apps keep requests out of Formik and read the named LivelyCura references first.

Follow-ups:

- Redo Altin Support chat-first and Profile, with the user's decisions on derived subjects and order-issue flow.

## [2026-10-09] correction | Record Altin Profile Inline Edit Correction

What changed:

- Recorded the user's rejection of the Profile → Edit profile → Change phone number route; Profile now edits in place with the SMS code step inline.
- Recorded the correction that form hooks follow the repository's own committed Formik hooks, not SERLP, and the shape those hooks share.

Files touched:

- `raw/sources/2026-10-09-altin-profile-inline-edit-correction.md`
- `wiki/sources/altin-profile-inline-edit-correction.md`
- `wiki/projects/altin-partner-mobile.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Agents check the repository's committed form hooks before any reference project, and keep multi-step edits on one screen.

Follow-ups:

- None.

## [2026-10-08] correction | Record Altin Profile And Support UI Corrections

What changed:

- Recorded the user's correction that UI work is not done until every new or changed screen has been viewed on the running device, after Profile and Support were reported done without device checks.
- Recorded the fixed Support and Profile UI: a SERLP-style reply composer, readable linked-order rows with unlink confirmation, dashed add tiles, and a read-only Profile whose header Edit covers the photo, alternate phone, phone change, and verification.
- Recorded that no Altin web app saves profile edits and the API updates only the photo and alternate phone, plus the proposed backend change.

Files touched:

- `raw/sources/2026-10-08-altin-profile-support-ui-corrections.md`
- `wiki/sources/altin-profile-support-ui-corrections.md`
- `wiki/projects/altin-partner-mobile.md`
- `wiki/syntheses/personal-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Agents across projects verify UI on the device before reporting it done, and the Altin page records why profile names and details are read-only.

Follow-ups:

- Backend: add first name, last name, city, and about to `UpdateUserProfileInput` and make `profilePictureId` optional.

## [2026-10-08] ingest | Record Altin Profile And Support

What changed:

- Recorded the Profile and Support build in Altin Partner Mobile from the web contracts: ungated routes like the web, `VIEW_ORDERS` for order linking, no ticket triage, and no in-app password change.
- Recorded the user's choice of `expo-image-picker`, the shared REST blob upload with its unverified path, and the `no-cache` rule for the profile's `currentUser` query.
- Added two cross-project lessons to the development manual: check `requireOptionalNativeModule` before importing a native package, give mutation-running modals their own toast host, and keep secondary readers of an app-gating root field out of the cache.

Files touched:

- `raw/sources/2026-10-08-altin-profile-support.md`
- `wiki/sources/altin-profile-support.md`
- `wiki/projects/altin-partner-mobile.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- The project page describes Profile and Support as built, with their contracts and the rebuild requirement.

Follow-ups:

- Confirm the blob upload path and whether `updateProfile` accepts partner members during the user's live testing.

## [2026-10-08] ingest | Record Altin Module Builds And Scope Corrections

What changed:

- Recorded the Team, Accounting, Billing, API keys, Webhooks, Notifications, and support-ticket builds in Altin Partner Mobile, with the user's scope answers, and rewrote the stale project summary that called Team, Accounting, and Billing placeholders.
- Recorded the Orders history accordion, arrival tones, sliding bottom sheets, the backdrop and pressed-style fixes, one-time secrets with `expo-clipboard`, and the notification and ticket-reply rules.
- Recorded the Apollo lesson that objects shared with the System query must select `id`, and corrected the Commands claim now that `tests/` was deleted in commit `e4c14fa`.
- Added the user's scope corrections to the personal manual: change only what was asked, treat unanswered proposals as declined, and finish the whole of an update instruction instead of doing part and asking.

Files touched:

- `raw/sources/2026-10-08-altin-module-builds-and-scope-corrections.md`
- `wiki/sources/altin-module-builds-and-scope-corrections.md`
- `wiki/projects/altin-partner-mobile.md`
- `wiki/syntheses/personal-operating-manual.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- The Altin project page describes the app as it is, and agents across projects carry the two scope corrections.

Follow-ups:

- Push notifications, `useSystemQuery` first-load hardening, and Android keyboard avoidance for the ticket reply composer remain open.

## [2026-10-08] ingest | Record Altin Permission Gating

What changed:

- Recorded the SERLP-style permission model the user asked for in Altin Partner Mobile: every route stays registered, `withPermission` shows a No access screen, `usePermissions().can` takes inline permissions or named `permissionRules`, and `PermissionGate` hides in-screen controls.
- Recorded the user's correction that mutation hooks do not check permissions because their triggers are already gated, while query skips and organization-context guards remain.
- Recorded per-report Home analytics gating and the Apollo Client 3 lesson that `refetch()` still sends a skipped query.
- Added the cross-project gating rule to the development manual and marked route-registration availability and the deleted `getAppAccess` flags as superseded.

Files touched:

- `raw/sources/2026-10-08-altin-permission-gating.md`
- `wiki/sources/altin-permission-gating.md`
- `wiki/projects/altin-partner-mobile.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Vault guidance matches the repository `AGENTS.md`, `docs/fleet.md`, and `docs/outlets.md`, so future agents gate screens with wrappers rather than unregistered routes and leave permission checks out of mutation hooks.

Follow-ups:

- Decide whether opening a support ticket from a notification should also require `VIEW_SUPPORT_TICKETS` for non-reporters.

## [2026-10-07] ingest | Record Altin Theme, Navigation, And Runtime Corrections

What changed:

- Recorded the user's rejection of the brand-book palette and Plus Jakarta Sans / IBM Plex fonts as the Altin Partner app theme; `docs/app-theme-guide.md`, the user's token tuning, and system typography now govern, while brand lockups and icons remain.
- Recorded identical primary icon wells in both appearances, neutral notification/back controls, 0.3 card borders, the Reports tab replacing Notifications, development-build-only OAuth, and the no-stray-Metro rule.
- Updated the project summary for Fleet's first pass and the Home, Search, organization, More, and Reports state, and marked older Notifications-tab claims as superseded.

Files touched:

- `raw/sources/2026-10-07-altin-theme-navigation-runtime-corrections.md`
- `wiki/sources/altin-theme-navigation-runtime-corrections.md`
- `wiki/sources/altin-mobile-brand-system.md`
- `wiki/sources/altin-orders-mobile-web-reference.md`
- `wiki/sources/ceqa-altin-hermes-conversation-harvest-supplement-1.md`
- `wiki/projects/altin-partner-mobile.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Vault guidance now matches the repository `AGENTS.md`, `DESIGN.md`, and `PRODUCT.md`, so future agents will not restore the rejected theme or the Notifications tab.

Follow-ups:

- Confirm whether other Altin mobile apps also follow `app-theme-guide.md` over the brand-book palette and fonts.

## [2026-09-29] implementation | Record Bora Live Support Subscription Contract

What changed:

- Recorded the `customerSupportCaseUpdated` contract, client-based audiences, post-commit identifier-only publishing, and silent replays/no-ops.
- Recorded that graphql-middleware authorizes custom-resolve subscription fields per event and that graphql-shield only surfaces returned rule errors.
- Recorded the verified Bora defect where Shield denials surface as `INTERNAL_SERVER_ERROR`, and marked the Phase 2 subscription deferral as superseded.

Files touched:

- `raw/sources/2026-09-29-bora-support-subscription-contract.md`
- `wiki/sources/bora-realtime-support-subscriptions.md`
- `wiki/sources/bora-customer-support-administration.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Frontend and future agents share one live support contract, and GraphQL Shield subscription work guards both stream setup and per-event delivery.

## [2026-09-29] correction | Record Bora Realtime Transport And Functional Code Style

What changed:

- Recorded that Bora support conversations must update live through GraphQL subscriptions, with WebSocket authentication equal to HTTP and per-operation/per-event session revalidation.
- Recorded the user's correction that the single App Platform instance uses LivelyCura's in-memory PubSub; the MongoDB change-stream fan-out stays unwired as a functional factory.
- Generalized the payments-only no-class convention into a user-wide functional code-style rule and added a topology-before-infrastructure lesson.

Files touched:

- `raw/sources/2026-09-29-bora-realtime-support-subscriptions.md`
- `wiki/sources/bora-realtime-support-subscriptions.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Future agents write functional code without classes and confirm deployment topology before adding cross-process infrastructure.

## [2026-09-29] ingest | Connect Claude Code To The Shared Brain

What changed:

- Recorded the user directive to install the Obsidian skills in Claude Code and connect it to the vault.
- Added Claude Code as a third integration layer alongside Hermes and Codex: global `~/.claude/CLAUDE.md` pointer, `OBSIDIAN_VAULT_PATH`, and `~/.claude/skills/` symlinks into `.agents/skills/`.
- Recorded that the Obsidian CLI needs `vault="Work Space"` when invoked outside the vault directory.

Files touched:

- `raw/sources/2026-09-29-claude-code-shared-brain-integration.md`
- `wiki/sources/claude-code-shared-brain-integration.md`
- `wiki/entities/claude-code.md`
- `wiki/concepts/hermes-obsidian-memory-architecture.md`
- `index.md`
- `log.md`

Key result:

- Claude Code now retrieves from and promotes into the same canonical vault, and the vault's skills remain the single skill source.

Follow-ups:

- Decide whether Claude Code transcripts and per-repository auto-memory enter the harvest checkpoint process.

## [2026-09-29] ingest | Add Bora Customer Support Administration

What changed:

- Recorded the customer-owned support case and public conversation contract.
- Added the permission-controlled admin queue, internal notes, assignment, priority, and explicit lifecycle actions.
- Preserved idempotent writes, internal-note isolation, service-owned logic, and the deferral of attachments, subscriptions, and automatic support notifications.

Files touched:

- `raw/sources/2026-09-29-bora-customer-support-administration.md`
- `wiki/sources/bora-customer-support-administration.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Bora's second administration phase now has a durable customer-support API contract, while marketing/news and outbound campaign administration remain later work.

## [2026-09-28] correction | Keep Bora Resolvers Transport-Only

What changed:

- Recorded that resolver functions only extract transport values and delegate to owning services.
- Moved mapping, filtering, calculation, normalization, and response construction into documented services.
- Required generated GraphQL argument types and enums instead of handwritten resolver shapes or string unions.

Files touched:

- `raw/sources/2026-09-28-bora-resolver-domain-logic-and-generated-enum-correction.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Future Bora GraphQL work keeps application logic in services and reuses generated schema types at the resolver boundary.

## [2026-09-28] correction | Restore Bora Resolver And Service Documentation Style

What changed:

- Preserved the correction that resolver functions belong above resolver maps as named, documented constants.
- Required every new or rewritten service function to retain or add repository-style JSDoc.
- Recorded that function rewrites must update existing documentation rather than remove it.

Files touched:

- `raw/sources/2026-09-28-bora-resolver-and-service-documentation-correction.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Future Bora backend work keeps resolver maps declarative and preserves reviewable function documentation throughout service changes.

## [2026-09-28] correction | Align Bora RBAC With Live LivelyCura

What changed:

- Preserved the direct correction that the initial `AccessRole` structure and naming were wrong.
- Made live LivelyCura the authority for Bora role and permission naming and folder ownership.
- Recorded `Role`, `RoleModel`, `platformRoles`, `permissions`, role operations, the separated permission layer, and the staff domain as the durable contract.

Files touched:

- `raw/sources/2026-09-28-bora-rbac-livelycura-naming-correction.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Future Bora RBAC work follows the current live LivelyCura structure and does not reintroduce the rejected `AccessRole`, `accessRoleIds`, `directPermissions`, or `access.*` contract.

## [2026-09-28] ingest | Add Existing Customer Grow Wealth Valuations

What changed:

- Recorded the BCL linked-portfolio and linked-portfolio-valuation sequence for existing customers.
- Added separate typed GraphQL contracts for the grouped Grow Wealth dashboard and detailed valuation report.
- Preserved authenticated principal ownership and the hold on new-customer Grow Wealth creation.

Files touched:

- `raw/sources/2026-09-28-bora-grow-wealth-existing-customer-valuations.md`
- `wiki/sources/bora-grow-wealth-existing-customer-valuations.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Grow Wealth is no longer wholly deferred: existing linked customers have typed summary and report reads, while new-customer creation remains an explicit open scope.

## [2026-09-27] correction | Remove Preproduction Courier Legacy Compatibility

What changed:

- Recorded that the retired company-facing Courier feature was never used in production.
- Removed the assumption that its history, balances, obligations, migrations, cutover materializers, reconciliation, or Portal UI need preservation.
- Kept current merchant/order requestor references with the active workflows that own them.

Files touched:

- `raw/sources/2026-09-27-livelycura-preproduction-courier-no-legacy-compatibility.md`
- `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/projects/livelycura-backend.md`
- `index.md`
- `log.md`

Key result:

- Future Courier cleanup removes the preproduction company feature directly and does not recreate it under Billing or backend compatibility code.

## [2026-09-26] ingest | Correct Admin Notification Folder Ownership

What changed:

- Recorded direct `src/notifications` ownership for the Admin notification feature.
- Rejected the redundant `src/notifications/inbox` layer.
- Required structural moves to preserve all operation hooks and update imports together.

Files touched:

- `raw/sources/2026-09-26-livelycura-admin-notification-folder-ownership-correction.md`
- `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`
- `wiki/projects/livelycura-admin-portal.md`
- `index.md`
- `log.md`

Key result:

- Future Admin notification work uses the established domain-root folder structure and avoids partial moves that break module loading.

## [2026-09-26] ingest | Separate Admin Inbox From Courier Configuration

What changed:

- Recorded that the Admin notification inbox belongs behind the main-header notification icon.
- Restored Courier Configuration as a separate Courier navigation surface for rider delivery notification settings.
- Marked the earlier settings-removal inference as superseded while preserving its raw evidence and log entry.

Files touched:

- `raw/sources/2026-09-26-livelycura-admin-notification-inbox-and-courier-configuration-correction.md`
- `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`
- `wiki/projects/livelycura-admin-portal.md`
- `index.md`
- `log.md`

Key result:

- Admin has two explicit surfaces with separate responsibilities: the header inbox and Courier Configuration.

## [2026-09-26] correction | Remove Admin Courier Notification Settings

What changed:

- Recorded removal of the redundant Admin Courier notification settings page, route, and sidebar item.
- Preserved rider notification delivery as system behavior.
- Required any future Admin notification surface to provide a coherent operational workflow and complete controls.

Files touched:

- `raw/sources/2026-09-26-livelycura-admin-courier-notification-settings-removal.md`
- `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`
- `wiki/projects/livelycura-admin-portal.md`
- `index.md`
- `log.md`

Key result:

- Admin Courier no longer exposes two redundant switches as a standalone feature.

## [2026-09-26] correction | Preserve Courier Requestor Identity

What changed:

- Recorded that Customer, Facility, and Organization are all valid delivery requestors.
- Clarified that requestor references support delivery, order, billing, and remittance workflows without restoring organization/facility ownership of riders or providers.
- Prohibited coercing Facility requestors to Organization at the GraphQL boundary.

Files touched:

- `raw/sources/2026-09-26-livelycura-courier-requestor-identity-correction.md`
- `wiki/sources/livelycura-graphql-contract-compatibility.md`
- `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`
- `wiki/projects/livelycura-backend.md`
- `wiki/projects/livelycura-admin-portal.md`
- `index.md`
- `log.md`

Key result:

- Future Courier cleanup preserves merchant requestor identity while keeping Fleet and platform rider ownership separate.

## [2026-09-25] correction | LivelyCura Fleet Filter URL Parsing

- What changed: preserved the user's pagination and status parsing correction; refined the Fleet source, Pharmacy Portal project convention, and index.
- Files touched: `raw/sources/2026-09-25-livelycura-fleet-filter-url-parsing-correction.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-pharmacy-portal.md`, `index.md`, and `log.md`.
- Key result: Fleet list hooks use the Portal's numeric pagination defaults and nullable enum filters, without custom clamping or `ALL` sentinels.
- Follow-ups: none.

## [2026-09-25] ingest | LivelyCura Fleet Filters And Icons

- What changed: preserved the user's Fleet filter-hook and icon correction; updated the Fleet source, Pharmacy Portal project page, and index.
- Files touched: `raw/sources/2026-09-25-livelycura-fleet-filter-hooks-and-tab-icons.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-pharmacy-portal.md`, `index.md`, and `log.md`.
- Key result: Fleet list hooks follow Portal URL-filter conventions and visible Fleet navigation/detail tabs have icons.
- Follow-ups: none.

## [2026-09-25] ingest | LivelyCura Fleet Contract And Filter Naming

- What changed: preserved the user's correction and updated Fleet source and project conventions plus the index.
- Files touched: `raw/sources/2026-09-25-livelycura-fleet-graphql-and-filter-naming-correction.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-backend.md`, `wiki/projects/livelycura-pharmacy-portal.md`, `index.md`, and `log.md`.
- Key result: Fleet naming covers services, GraphQL, and interfaces together; list filters use the established date-bound patterns.
- Follow-ups: none.

## [2026-09-24] ingest | LivelyCura Fleet Internal Naming

- What changed: preserved the direct naming correction and updated the Fleet source, Backend and Pharmacy Portal project conventions, and index.
- Files touched: `raw/sources/2026-09-24-livelycura-fleet-internal-naming-correction.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-backend.md`, `wiki/projects/livelycura-pharmacy-portal.md`, `index.md`, and `log.md`.
- Key result: Fleet-owned internal functions and file basenames omit redundant `Fleet`; public GraphQL and model contracts keep their established names.
- Follow-ups: none.

## [2026-09-24] ingest | LivelyCura Fleet Error Scope

- What changed: preserved the direct error-copy correction and updated the Fleet source, Backend project, and index.
- Files touched: `raw/sources/2026-09-24-livelycura-fleet-error-scope-and-maintenance-slice.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-backend.md`, `index.md`, and `log.md`.
- Key result: Fleet errors name the missing record and say facility when `facilityId` is present, otherwise organization; feature work continues one slice at a time.
- Follow-ups: none.

## [2026-09-24] ingest | LivelyCura Fleet Input Prompts

- What changed: preserved the direct Fleet input-prompt correction and updated the Fleet source, Pharmacy Portal project, and index.
- Files touched: `raw/sources/2026-09-24-livelycura-fleet-input-prompts.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-pharmacy-portal.md`, `index.md`, and `log.md`.
- Key result: create-page fields show useful placeholders; list-header filter inputs use placeholders without visible labels.
- Follow-ups: none.

## [2026-09-24] ingest | LivelyCura Fleet Date Picker Convention

- What changed: preserved the direct Fleet date-input correction and updated the Fleet source, Pharmacy Portal project, and index.
- Files touched: `raw/sources/2026-09-24-livelycura-fleet-date-picker-correction.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-pharmacy-portal.md`, `index.md`, and `log.md`.
- Key result: Fleet date-only and date-time controls follow the Portal’s Mantine pickers while retaining form and filter value contracts.
- Follow-ups: none.

## [2026-09-24] ingest | Altin Search Browse Restoration

- What changed: preserved the direct Browse correction and reconciled the Search Source Record, Altin project, and index.
- Files touched: `raw/sources/2026-09-24-altin-search-browse-restoration.md`, `wiki/sources/altin-search-browse-grouping.md`, `wiki/projects/altin-partner-mobile.md`, `index.md`, and `log.md`.
- Key result: empty-query Search shows Browse, Actions, and Suggestions; typing and results remain scoped to their existing sections.
- Follow-ups: none.

## [2026-09-24] ingest | Altin Search Empty Query Scope

- What changed: preserved the scope correction and updated the existing Search Source Record, Altin project, and index.
- Files touched: `raw/sources/2026-09-24-altin-search-empty-query-correction.md`, `wiki/sources/altin-search-browse-grouping.md`, `wiki/projects/altin-partner-mobile.md`, `index.md`, and `log.md`.
- Key result: only the empty-query landing view is simplified to Actions and Suggestions; typing and results retain their existing sections.
- Follow-ups: none.

## [2026-09-24] ingest | Altin Search Isolation and Sections

- What changed: preserved the direct Search presentation correction and updated the existing Search Source Record, Altin project, and index.
- Files touched: `raw/sources/2026-09-24-altin-search-isolation-sections.md`, `wiki/sources/altin-search-browse-grouping.md`, `wiki/projects/altin-partner-mobile.md`, `index.md`, and `log.md`.
- Key result: Search owns its styles and rows; the idle sections are Browse, Actions, and Suggestions.
- Follow-ups: none.

## [2026-09-24] ingest | Altin Search Browse Grouping

- What changed: preserved the direct Search grouping correction and updated the Altin project and index.
- Files touched: `raw/sources/2026-09-24-altin-search-browse-grouping.md`, `wiki/sources/altin-search-browse-grouping.md`, `wiki/projects/altin-partner-mobile.md`, `index.md`, and `log.md`.
- Key result: available apps appear in one Search Browse card with feature previews; the Apps directory keeps its own grouping.
- Follow-ups: none.

## [2026-09-23] ingest | Altin Mobile Brand System

- What changed: preserved the supplied brand book and direct correction, then updated Altin project and cross-project mobile brand guidance.
- Files touched: `raw/assets/altin-brand-book-v1.0.pdf`, `raw/sources/2026-09-23-altin-mobile-brand-decision.md`, `wiki/sources/altin-mobile-brand-system.md`, `wiki/projects/altin-partner-mobile.md`, `wiki/syntheses/software-development-operating-manual.md`, `index.md`, and `log.md`.
- Key result: Paper `#F8F6F3` and the three supplied font families supersede the earlier web-era mobile colors and type.
- Follow-ups: check adoption in other Altin app repositories when those apps are next edited.

## [2026-09-21] ingest | CheckCity TypeScript Test Convention

- What changed: preserved the explicit TypeScript test correction and linked it from the CheckCity project and index.
- Files touched: `raw/sources/2026-09-21-checkcity-typescript-tests.md`, `wiki/sources/checkcity-typescript-tests.md`, `wiki/projects/livelycura-check-city-app.md`, `index.md`, and `log.md`.
- Key result: Cart tests use TypeScript with typed mocks and fixtures.
- Follow-ups: none for the requested Cart scope.

## [2026-09-21] ingest | CheckCity Delivery Warning Threshold Correction

- What changed: preserved the direct threshold correction and superseded the independent 10 km trigger in the delivery Source Record, project, and index.
- Files touched: `raw/sources/2026-09-21-checkcity-delivery-warning-threshold-correction.md`, `wiki/sources/checkcity-delivery-location-confirmation.md`, `wiki/projects/livelycura-check-city-app.md`, `index.md`, and `log.md`.
- Key result: warning requires both GH₵60+ and at least 15 km; the reported 10.2 km / GH₵41 case does not warn.
- Follow-ups: preserve the distinction between the user’s 15–20 km range and the assistant’s chosen 15 km lower boundary.

## [2026-09-21] ingest | Fleet Operator Details Page

- What changed: preserved the routed complete-detail correction; updated the Fleet Source Record, Pharmacy Portal ownership conventions, and index.
- Files touched: `raw/sources/2026-09-21-fleet-operator-details-page.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-pharmacy-portal.md`, `index.md`, and `log.md`.
- Key result: operator viewing is a protected page owned by `src/fleet/operatorDetails`, backed by the by-ID query and complete profile, compliance, work-state, location, audit, document, and timestamp presentation.
- Follow-ups: continue the Fleet frontend one rebuilt feature at a time; unrelated unfinished Fleet and Billing drafts still block the repository-wide TypeScript check.

## [2026-09-21] ingest | Fleet Operator Document Previews And Upload State

- What changed: preserved the document-preview and upload-loading correction; updated the Fleet Source Record, Pharmacy Portal project convention, cross-project development manual, and index.
- Files touched: `raw/sources/2026-09-21-fleet-operator-document-previews-and-upload-state.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-pharmacy-portal.md`, `wiki/syntheses/software-development-operating-manual.md`, `index.md`, and `log.md`.
- Key result: operator image/PDF uploads render inline previews, saved update-form documents resolve through temporary URLs, and each upload button owns its loading state.
- Follow-ups: continue the Fleet frontend one rebuilt feature at a time; unrelated unfinished Fleet and Billing drafts still block the repository-wide TypeScript check.

## [2026-09-21] ingest | Fleet Operator Profile Image Preview

- What changed: preserved the profile-image preview correction and updated the Fleet Source Record, Pharmacy Portal project convention, and index.
- Files touched: `raw/sources/2026-09-21-fleet-operator-profile-image-preview.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-pharmacy-portal.md`, `index.md`, and `log.md`.
- Key result: operator create and update forms show the selected image itself, while update forms also resolve the saved private image through the existing temporary URL query.
- Follow-ups: continue the Fleet frontend one rebuilt feature at a time; unrelated unfinished Fleet and Billing drafts still block the repository-wide TypeScript check.

## [2026-09-21] ingest | Fleet Operator Accordion And Component-File Correction

- What changed: preserved the operator-form presentation and component-file correction; updated the Fleet Source Record, Pharmacy Portal project convention, cross-project development manual, and index.
- Files touched: `raw/sources/2026-09-21-fleet-operator-accordion-and-component-files.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-pharmacy-portal.md`, `wiki/syntheses/software-development-operating-manual.md`, `index.md`, and `log.md`.
- Key result: repeatable Fleet operator person/compliance sections use accordions with their add actions inside, and independent editor components remain in separate owned files.
- Follow-ups: continue the Fleet frontend one rebuilt feature at a time; unrelated unfinished Fleet and Billing drafts still block the repository-wide TypeScript check.

## [2026-09-21] ingest | Fleet Create Folder Ownership Correction

- What changed: preserved the create-folder ownership correction and updated the Fleet Source Record, Pharmacy Portal project convention, and index.
- Files touched: `raw/sources/2026-09-21-fleet-create-folder-ownership-correction.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-pharmacy-portal.md`, `index.md`, and `log.md`.
- Key result: `src/fleet/createOperator` owns all creation-specific page, component, interface, and mutation code; `src/fleet/operators` owns roster and update behavior only.
- Follow-ups: continue the Fleet frontend one feature at a time; unrelated unfinished Fleet drafts and Billing contract mismatches still block a clean full TypeScript check.

## [2026-09-21] ingest | Fleet Operator Create Page And Courier Route Removal

- What changed: preserved the routed operator-registration and complete Courier-route cleanup corrections; updated the Fleet Source Record, Pharmacy Portal project conventions, and index.
- Files touched: `raw/sources/2026-09-21-fleet-operator-create-page-and-courier-route-removal.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-pharmacy-portal.md`, `index.md`, and `log.md`.
- Key result: operator creation is a protected page with page-owned mutation behavior and shared form fields, while Pharmacy Portal no longer contains Courier routes, redirects, notices, or route constants.
- Follow-ups: unfinished Fleet draft screens and existing Billing contract mismatches still prevent a clean full TypeScript check; continue rebuilding Fleet one feature at a time.

## [2026-09-21] ingest | Pharmacy Portal Fleet Route Endpoint Correction

- What changed: preserved the direct route-architecture correction and updated the existing Fleet Source Record, Pharmacy Portal project conventions, and index.
- Files touched: `raw/sources/2026-09-21-pharmacy-portal-fleet-route-endpoints.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-pharmacy-portal.md`, `index.md`, and `log.md`.
- Key result: Fleet paths are declared once in `routeEndpoints` and reused by the app registry, menu, router, redirects, and tests; module and operator permission guards retain the established parent/child route ownership.
- Follow-ups: continue the Fleet frontend one rebuilt feature at a time; no deployment or broader Fleet-screen completion claim.

## [2026-09-21] ingest | Fleet Operator Frontend And Retired Module Login

- What changed: preserved the frontend sequencing and login-failure request; updated the Fleet Source Record, Backend and Pharmacy Portal project conventions, and index.
- Files touched: `raw/sources/2026-09-21-fleet-operator-frontend-and-retired-module-login.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-backend.md`, `wiki/projects/livelycura-pharmacy-portal.md`, `index.md`, and `log.md`.
- Key result: Pharmacy Portal Fleet people use the operator contract, established feature structure, focused command hooks, complete person profiles, and separate live work state; stale stored `COURIER` module values are filtered at GraphQL serialization without restoring Courier as an organization module.
- Follow-ups: continue rebuilding the remaining Fleet frontend areas one at a time; no migration, deployment, or production-login verification claim.

## [2026-09-20] ingest | Fleet GraphQL Architecture Correction

- What changed: preserved the direct Fleet resolver, type-definition composition, and Shield ownership correction; updated the Fleet Source Record, backend project conventions, cross-project development manual, and index.
- Files touched: `raw/sources/2026-09-20-fleet-graphql-architecture-correction.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-backend.md`, `wiki/syntheses/software-development-operating-manual.md`, `index.md`, and `log.md`.
- Key result: Fleet GraphQL follows the HRM module shape; resolvers call services directly, Shield owns endpoint permission/context checks, SDL and resolver maps use explicit repository composition patterns, and the rejected Fleet principal/module/facility validation layer must not return.
- Follow-ups: continue reviewing the remaining Fleet features one at a time; shared-principal removal does not establish that their service architectures are accepted.

## [2026-09-19] ingest | Fleet Model Update-Method Correction

- What changed: preserved the direct Mongoose persistence correction and updated the existing Fleet Source Record, backend conventions, and index.
- Files touched: `raw/sources/2026-09-19-fleet-model-update-method-correction.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-backend.md`, `index.md`, and `log.md`.
- Key result: Fleet update services use owning-model update methods with deliberate atomic operators, updated return values, audit-visible writes, and preserved transaction sessions; document `.save()` must not return.
- Follow-ups: no migration, client rollout, or production deployment claim.

## [2026-09-19] ingest | Fleet Operator Work-State Correction

- What changed: preserved the direct operator-state correction and updated the existing Fleet Source Record, backend conventions, and index.
- Files touched: `raw/sources/2026-09-19-fleet-operator-work-state-correction.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-backend.md`, `index.md`, and `log.md`.
- Key result: Fleet operator profile, lifecycle, and live dispatch state are separate; online presence, accepting work, capacity, heartbeat expiry, current coordinates, derived load, and actual availability use purpose-specific operations.
- Follow-ups: no migration, client rollout, or production deployment claim.

## [2026-09-18] ingest | Bora Oye Website Grounding

- What changed: preserved the user report of incorrect Oye answers and recorded the official website grounding and customer-query privacy boundaries.
- Files touched: `raw/sources/2026-09-18-bora-oye-website-grounding.md`, `wiki/sources/bora-oye-website-grounding.md`, `wiki/projects/bora-capital-backend.md`, `index.md`, and `log.md`.
- Key result: Bora-specific answers require current `boradvisors.com` evidence, exact citations, and fail-closed behavior; public-site search receives allowlisted topic terms only.
- Follow-ups: evaluate the deployed model with anonymized real meeting questions when available.

## [2026-09-18] ingest | Bora Production CI Audit Scope

- What changed: preserved the user correction and recorded production-only CI audit placement.
- Files touched: `raw/sources/2026-09-18-bora-production-ci-audit-scope.md`, `wiki/sources/bora-production-ci-audit-scope.md`, `wiki/projects/bora-capital-backend.md`, `index.md`, and `log.md`.
- Key result: reusable PR/staging verification excludes the audit; production deployment remains gated by it.
- Follow-ups: no live GitHub Actions run claimed.

## [2026-09-18] ingest | Bora KYC Provider Description Uncertainty

- What changed: preserved the direct user correction and qualified existing KYC supervision claims.
- Files touched: `raw/sources/2026-09-18-bora-kyc-supervision-description-uncertainty.md`, `wiki/sources/bora-kyc-supervision-and-statement-update.md`, `wiki/projects/bora-capital-backend.md`, `index.md`, and `log.md`.
- Key result: only pending supervision is provider-confirmed; approved/rejected mappings are provisional implementation assumptions. Grow Wealth remains unfinished.
- Follow-ups: obtain sanitized BCL approved/rejected responses or an authoritative contract before claiming end-to-end final-outcome support.

## [2026-09-18] ingest | Fleet Service Architecture Correction

- What changed: preserved the direct service-layer correction and updated the Fleet Source Record, backend conventions, cross-project development manual, and index.
- Files touched: `raw/sources/2026-09-18-fleet-service-architecture-correction.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-backend.md`, `wiki/syntheses/software-development-operating-manual.md`, `index.md`, and `log.md`.
- Key result: Fleet feature services own database operations; helpers stay pure; transactions belong only to the concrete multi-document workflows that need them. The rejected global transaction/idempotency and generic persistence/query layers must not return.
- Follow-ups: no Fleet migration, deployment, or client rollout claim.

## [2026-09-18] ingest | Fleet Deletion And Revision Fields

- What changed: preserved the direct field-removal correction and updated the existing Fleet Source Record, backend conventions, and index.
- Files touched: `raw/sources/2026-09-18-fleet-deletion-and-version-fields.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-backend.md`, `index.md`, and `log.md`.
- Key result: Fleet omits deletion timestamps and custom revision contracts while retaining established archive metadata and transactional operation checks.
- Follow-ups: no migration or deployment claim; unrelated domains retain their own conventions.

## [2026-09-17] ingest | Fleet Validation And Archiving Conventions

- What changed: preserved the direct model-validation and archive-pattern corrections; updated the existing Fleet Source Record, backend conventions, and index.
- Files touched: `raw/sources/2026-09-17-fleet-model-validation-and-archiving-correction.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-backend.md`, `index.md`, and `log.md`.
- Key result: validation belongs in services; model constraints must follow reference code. Archiving reuses Departments/MLS metadata and ARCHIVED status, distinct from INACTIVE and deletedAt.
- Follow-ups: no deployment or migration completion claim.

## [2026-09-17] ingest | Fleet People Naming And Registration

- What changed: preserved the direct naming/profile and revision-counter corrections; updated the existing Fleet Source Record, backend conventions, and index.
- Files touched: `raw/sources/2026-09-17-fleet-person-profile-correction.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-backend.md`, `index.md`, and `log.md`.
- Key result: company Fleet people records must accommodate both riders and drivers, capture fuller registration information, and omit the rejected custom revision counter.
- Follow-ups: exact replacement naming and field choices remain implementation decisions; no rollout or migration claim recorded.

## [2026-09-17] ingest | Courier Backend Ownership Correction

- What changed: preserved the direct correction and merchant/order clarification, updated the existing architecture Source Record, backend conventions, and index.
- Files touched: `raw/sources/2026-09-17-courier-backend-boundary-correction.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, `wiki/projects/livelycura-backend.md`, `index.md`, and `log.md`.
- Key result: Courier has no company ownership; merchant/order links serve billing and cash remittance only. Backend architecture and cleanup precede Fleet migrations and client work.
- Follow-ups: historical financial handling remains separate; no implementation completion claim recorded.

## [2026-09-17] ingest | Independent Fleet And Platform Dispatch

- What changed: preserved the direct product decision, added its Source Record, and updated five affected project notes plus the index.
- Files touched: `raw/sources/2026-09-17-livelycura-independent-fleet-decision.md`, `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`, project notes for Backend, Pharmacy Portal, Admin Portal, SERLP Mobile, and Courier Mobile, `index.md`, and `log.md`.
- Key result: company Fleet and LivelyCura network dispatch have separate product ownership; optional network enrollment remains explicit.
- Follow-ups: define optional company network participation terms; no production rollout claim recorded.

## [2026-09-16] ingest | Keks Single Employee PUT Correction

- What changed: preserved the explicit endpoint correction, updated the existing Source Record and Keks conventions, and synchronized the index.
- Files touched: `raw/sources/2026-09-16-keks-single-employee-put-correction.md`, `wiki/sources/keks-backend-errors-and-bulk-time-punches.md`, `wiki/projects/keks-admin-portal.md`, `index.md`, and `log.md`.
- Key result: individual edits use PUT /users with internal id and editable employee_id; bulk imports retain PATCH /users/bulk. The earlier read-only-ID conclusion is rejected.
- Follow-ups: none.

## [2026-09-16] ingest | Keks Step Validation Correction

- What changed: preserved the explicit rejection of submit-time step jumping, expanded the existing Keks Source Record, and updated the project convention and index.
- Files touched: `raw/sources/2026-09-16-keks-step-validation-correction.md`, `wiki/sources/keks-backend-errors-and-bulk-time-punches.md`, `wiki/projects/keks-admin-portal.md`, `index.md`, and `log.md`.
- Key result: use existing Formik blur/touched errors and disable Next for invalid current steps; do not invent a different validation interaction.
- Follow-ups: none.

## [2026-09-16] ingest | Keks Backend Errors And Bulk Time Punches

- What changed: preserved the user correction and relevant API contract evidence, added a Source Record, and updated Keks conventions and index.
- Files touched: `raw/sources/2026-09-16-keks-backend-errors-and-bulk-time-punches.md`, `wiki/sources/keks-backend-errors-and-bulk-time-punches.md`, `wiki/projects/keks-admin-portal.md`, `index.md`, and `log.md`.
- Key result: backend error details take precedence over generic notifications; required-field choices carry through labels and serialization; bulk manual overrides run sequentially for unique employee IDs with progress.
- Follow-ups: verify current backend contracts before future changes; selected shifts do not override pending-request semantics.

## [2026-09-14] ingest | LivelyCura Result PDF And OTP Contract

- What changed: preserved the sanitized user correction, expanded the existing result-delivery Source Record, updated backend/customer-portal constraints, and synchronized the index.
- Files touched: `raw/sources/2026-09-14-livelycura-result-pdf-and-otp-correction.md`, `wiki/sources/livelycura-result-link-environments.md`, `wiki/projects/livelycura-backend.md`, `wiki/projects/livelycura-customer-portal.md`, `index.md`, and `log.md`.
- Key result: result emails require actual PDF attachments; LivelyCura SMS identity remains separate from the serlp.com email sender; generic OTP acceptance is not proof of sending and recipients need the newest link.
- Follow-ups: verify deployed delivery separately from local rendering and provider-payload checks.

## [2026-09-14] ingest | doorDrop Expo Image Native ABI Alignment

- What changed: preserved the sanitized crash evidence, recorded the installed-package mismatch and verified remediation, updated the doorDrop runtime convention, and synchronized the index.
- Files touched: `raw/sources/2026-09-14-doordrop-expo-image-native-abi-crash.md`, `wiki/sources/doordrop-expo-image-native-abi-alignment.md`, `wiki/projects/livelycura-choproute-app.md`, `index.md`, and `log.md`.
- Key result: SDK 57 Expo native packages must stay on one compatible patch graph; Expo Image upgrades require dependency alignment plus a clean native rebuild and simulator launch verification.
- Follow-ups: none for this incident.

## [2026-09-14] ingest | doorDrop Rebrand And Flat Assets

- What changed: preserved the direct rebrand and asset-structure instructions, updated the existing consumer-marketplace project record, and synchronized the index.
- Files touched: `raw/sources/2026-09-14-doordrop-rebrand-and-asset-structure.md`, `wiki/sources/doordrop-rebrand-and-asset-structure.md`, `wiki/projects/livelycura-choproute-app.md`, `index.md`, and `log.md`.
- Key result: the public app and repository are now doorDrop; static images remain flat under `assets` and runtime imports go through `assets/images.js`; the ChopRoute backend client key remains a compatibility boundary.
- Follow-ups: decide separately whether to migrate the backend marketplace record and `CHOPROUTE_MARKETPLACE` identifier.

## [2026-09-14] ingest | CheckCity Warning-Only Delivery Correction

- What changed: preserved the user correction, updated the delivery Source Record and project convention, and synchronized the index.
- Files touched: `raw/sources/2026-09-14-checkcity-delivery-warning-correction.md`, `wiki/sources/checkcity-delivery-location-confirmation.md`, `wiki/projects/livelycura-check-city-app.md`, `index.md`, and `log.md`.
- Key result: warning at GH₵60 or above (or beyond 10 km); customer may review location or confirm and continue. Latest direction supersedes the earlier 20 km hard cap.
- Follow-ups: distance warning remains tunable.

## [2026-09-14] ingest | CheckCity Delivery Location Confirmation

- What changed: preserved the duplicate-place-name concern and explicit 20 km hard-cap instruction; recorded the assistant-selected initial warning thresholds separately from user decisions.
- Files touched: `raw/sources/2026-09-14-checkcity-delivery-location-confirmation.md`, `wiki/sources/checkcity-delivery-location-confirmation.md`, `wiki/projects/livelycura-check-city-app.md`, `index.md`, and `log.md`.
- Key result: verify destination and willingness to pay after estimating; initial warnings above 10 km or GH₵50, with no override beyond 20 km.
- Follow-ups: adjust warning values after user evaluation.

## [2026-09-14] ingest | CheckCity Support Conditional Rendering

- What changed: preserved the direct rejection of nested support-screen rendering and linked it to the existing support Source Record, CheckCity conventions, and index.
- Files touched: `raw/sources/2026-09-14-checkcity-support-conditional-rendering.md`, `wiki/sources/checkcity-order-support-card-layout.md`, `wiki/projects/livelycura-check-city-app.md`, `index.md`, and `log.md`.
- Key result: support-screen branches use the shared Conditional component with safe nullable data access.
- Follow-ups: none.

## [2026-09-14] ingest | CheckCity Single Order Chat

- What changed: preserved the direct single-chat requirement and updated the existing support Source Record, CheckCity project convention, and index.
- Files touched: `raw/sources/2026-09-14-checkcity-single-order-chat.md`, `wiki/sources/checkcity-order-support-card-layout.md`, `wiki/projects/livelycura-check-city-app.md`, `index.md`, and `log.md`.
- Key result: one conversation per order; opened and closed chats remain visible inside the Help card, with reopening available.
- Follow-ups: none.

## [2026-09-12] ingest | Mutation Toast Errors and Submission State

- What changed: preserved the direct rejection of mutation error-return/throwing layers and the saving-ref question; verified SERLP's caught-error Toast and null-result mutation pattern.
- Files touched: `raw/sources/2026-09-12-altin-toast-mutation-errors.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/projects/altin-partner-mobile.md`, `wiki/syntheses/software-development-operating-manual.md`, `index.md`, and `log.md`.
- Key result: actual API validation messages belong in mutation-owned toasts; forms retain client validation/drafts, advance on success only, and use Formik/Apollo submission state without saving refs. Earlier conflicting assistant rules are superseded.
- Follow-ups: preserve the user's live-testing boundary; offline tests do not establish user acceptance.

## [2026-09-12] ingest | Rejected Form Layers and Schema Controller

- What changed: preserved the user's explicit outletForm rejection and the full rejected code attachment; checked SERLP direct form bindings and numeric/seeding examples.
- Files touched: `raw/sources/2026-09-12-altin-form-layer-rejection.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/projects/altin-partner-mobile.md`, `wiki/syntheses/software-development-operating-manual.md`, `index.md`, and `log.md`.
- Key result: unnecessary form features, wrappers and relocated abstractions are not accepted consistency; preserve the user's createOrder folder rename and consult actual source.
- Follow-ups: review replacement code against reference ownership and simplicity. Tests and assistant completion claims are not user acceptance.

## [2026-09-12] ingest | Cross-project Form Code Consistency

- What changed: preserved the user's rejection of the first Formik/Yup migration and verified the actual SERLP hook/component structure.
- Files touched: `raw/sources/2026-09-12-altin-cross-project-form-structure.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/projects/altin-partner-mobile.md`, `wiki/syntheses/software-development-operating-manual.md`, `index.md`, and `log.md`.
- Key result: consistency includes schema placement, form-hook ownership, direct mutation calls, returned state and component bindings. Library installation and passing tests do not establish architectural conformity or user acceptance.
- Follow-ups: compare actual source before implementing; retain workflow requirements without inventing alternate form controllers.

## [2026-09-12] ingest | Required Formik and Yup Forms

- What changed: preserved the user's explicit Formik/Yup correction and verified the SERLP form-hook pattern.
- Files touched: `raw/sources/2026-09-12-altin-formik-yup-correction.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/projects/altin-partner-mobile.md`, `wiki/syntheses/software-development-operating-manual.md`, `index.md`, and `log.md`.
- Key result: Formik and Yup are required; custom form state/validation and duplicated field gates are rejected. Feature ownership and workflow guards remain compatible with that convention.
- Follow-ups: consult actual reference form hooks before implementation; verification does not imply user acceptance.

## [2026-09-12] ingest | Exact Apollo Hook Examples and Project-wide Correction

- What changed: preserved the user's supplied query/mutation examples and explicit instruction to update every mismatching hook and remove combined aliased overview requests.
- Files touched: `raw/sources/2026-09-12-altin-exact-apollo-hook-pattern.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/projects/altin-partner-mobile.md`, `wiki/syntheses/software-development-operating-manual.md`, `index.md`, and `log.md`.
- Key result: query data/pageInfo/display flags and full Apollo results, named typed mutation actions with refetch/error-feedback flow, one operation per hook, and reference-project/vault consultation are now explicit. Prior assistant interpretations remain marked superseded.
- Follow-ups: use these examples before implementing; do not treat a refactor or passing tests as user acceptance.

## [2026-09-12] ingest | Altin Mobile Query Architecture Correction

- What changed: preserved the user's second rejection and corrected the earlier assistant-authored function-body-only gql interpretation against actual mobile query examples.
- Files touched: `raw/sources/2026-09-12-altin-mobile-query-architecture-correction.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/projects/altin-partner-mobile.md`, `index.md`, and `log.md`.
- Key result: direct Apollo query hooks follow local Home/SERLP architecture; the web clone supplies product/API contracts. Earlier raw evidence remains intact and its interpretation is explicitly superseded.
- Follow-ups: inspect real mobile hooks before implementing another feature; do not promote an inferred fix as user acceptance.

## [2026-09-12] ingest | Altin Fleet Query Ownership Correction

- What changed: preserved the user's renewed rejection of the exported aliased Fleet overview document and linked it into existing project guidance.
- Files touched: `raw/sources/2026-09-12-altin-fleet-query-ownership-correction.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/projects/altin-partner-mobile.md`, `index.md`, and `log.md`.
- Key result: operation ownership remains explicit; the source distinguishes the assistant's inlining/separate-read remediation from user acceptance.
- Follow-ups: apply the established hook ownership convention before adding further Fleet operations.

## [2026-09-12] ingest | CheckCity Order Support Card Layout

- What changed: preserved the user correction and linked the card-layout convention to CheckCity.
- Files touched: `raw/sources/2026-09-12-checkcity-order-support-card-layout.md`, `wiki/sources/checkcity-order-support-card-layout.md`, `wiki/projects/livelycura-check-city-app.md`, `index.md`, and `log.md`.
- Key result: Help and order chats share one card with divider-separated rows.
- Follow-ups: none.

## [2026-09-11] maintenance | Courier Appearance Controls And Dark Surfaces

- What changed: recorded the explicit rejection of segmented theme selection and the semantic-token requirement for delivery-detail utility cards.
- Files touched: `wiki/projects/livelycura-courier-mobile.md`, `index.md`, and `log.md`.
- Key result: Courier account appearance uses accessible descriptive choice rows, while task-detail cards preserve surface/text contrast in dark mode.
- Follow-ups: native visual acceptance remains pending on a running simulator or device.

## [2026-09-11] ingest | Altin Input Placeholders

- What changed: recorded the explicit placeholder requirement and updated the existing Orders/Outlets Source Records, project conventions, and index.
- Files touched: `raw/sources/2026-09-11-altin-input-placeholders.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/sources/altin-outlets-mobile.md`, `wiki/projects/altin-partner-mobile.md`, `index.md`, and `log.md`.
- Key result: all form inputs include useful placeholders, with omissions caught by the shared component type.
- Follow-ups: preserve visible labels and keep guidance separate from submitted values.

## [2026-09-11] ingest | Altin Create Forms And Inputs

- What changed: recorded the clarification that SERLP references apply to visible create/edit forms and inputs, not only mutation architecture.
- Files touched: `raw/sources/2026-09-11-altin-create-form-input-patterns.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/sources/altin-outlets-mobile.md`, `wiki/projects/altin-partner-mobile.md`, `index.md`, and `log.md`.
- Key result: form panels, bordered fields, compact labels, selection triggers and Screen footer composition are shared with Altin tokens and feature-owned behavior.
- Follow-ups: preserve user edits and the prohibition on production mutation testing.

## [2026-09-11] ingest | Altin Detail Headers And Direct Mutations

- What changed: preserved the explicit detail-header and mutation-simplicity correction, updated existing Orders/Outlets Source Records, the Altin project, and index.
- Files touched: `raw/sources/2026-09-11-altin-detail-headers-direct-mutations.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/sources/altin-outlets-mobile.md`, `wiki/projects/altin-partner-mobile.md`, `index.md`, and `log.md`.
- Key result: details have no drawer; Order details report from the right header action; feature mutations use Apollo directly with local form ownership, superseding the generic wrapper guidance.
- Follow-ups: maintain the production testing restriction and preserve user edits.

## [2026-09-11] ingest | Altin Outlet Bulk Import

- What changed: preserved the explicit bulk-import scope addition and updated the Outlets Source Record, Altin project, and index.
- Files touched: `raw/sources/2026-09-11-altin-outlet-bulk-import.md`, `wiki/sources/altin-outlets-mobile.md`, `wiki/projects/altin-partner-mobile.md`, `index.md`, and `log.md`.
- Key result: CSV bulk import belongs in both Outlets Quick actions and drawer, with combined create/update permission gates and a 500-row atomic API contract.
- Follow-ups: production imports remain excluded from development verification; the user owns live testing after changing the endpoint.

## [2026-09-11] ingest | Altin Module Actions And Consistency

- What changed: preserved the direct overview/drawer/action correction and the instruction to consult the cloned web project; updated existing Orders/Outlets Source Records, the Altin project, and index.
- Files touched: `raw/sources/2026-09-11-altin-module-actions-consistency.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/sources/altin-outlets-mobile.md`, `wiki/projects/altin-partner-mobile.md`, `index.md`, and `log.md`.
- Key result: supported actions belong in both Quick actions and module drawers; omit redundant organization headers and share View all. Create order and issue reporting supersede their earlier deferral. Resource-hook questions are not treated as deletion authorization.
- Follow-ups: no production writes for validation; source-contract checks do not establish the cause of missing organization-scoped records or user acceptance of the UI.

## [2026-09-11] ingest | Altin Outlets Scope And Rounded Statuses

- What changed: preserved the direct Outlets/create-edit/testing instruction and shared rounded-status rule; added the focused Source Record and updated existing Altin project/Orders links and index.
- Files touched: `raw/sources/2026-09-11-altin-outlets-scope.md`, `wiki/sources/altin-outlets-mobile.md`, `wiki/projects/altin-partner-mobile.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `index.md`, and `log.md`.
- Key result: Outlets includes API-integrated create/edit, but production testing is explicitly excluded; the user owns endpoint switching and live testing. Shared resources/presentation preserve module ownership.
- Follow-ups: native UI and live API validation remain unverified; source review is not visual acceptance.

## [2026-09-11] ingest | Altin Refresh And Tip Text

- What changed: captured the tip-text and endless-refresh report, and promoted the verified state/text ownership lessons into the existing Altin source/project notes and index.
- Files touched: `raw/sources/2026-09-11-altin-refresh-and-tip-text.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/projects/altin-partner-mobile.md`, `index.md`, and `log.md`.
- Key result: background focus loads and explicit refresh need distinct state; custom title typography must not inherit a smaller fixed line box. Production verification remains read-only.
- Follow-ups: local state tests and the iOS Back-navigation check do not prove every native gesture or platform.

## [2026-09-11] ingest | Altin Apps Stack Navigation

- What changed: preserved the direct Apps navigation instruction and updated the existing Orders Source Record, Altin project, and index; recorded shared detail presentation ownership without claiming visual acceptance.
- Files touched: `raw/sources/2026-09-11-altin-apps-stack-navigation.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/projects/altin-partner-mobile.md`, `index.md`, and `log.md`.
- Key result: the center Apps control opens a root-stack directory with Back while the other four controls remain tabs. The earlier five-route contract is explicitly superseded.
- Follow-ups: source and native checks do not establish user acceptance or untested platform readiness.

## [2026-09-10] maintenance | Altin Command Reference Cleanup

- What changed: removed the obsolete standalone Orders GraphQL validator command from the Altin project command reference after its repository script/package entry were removed.
- Files touched: `wiki/projects/altin-partner-mobile.md` and `log.md`. The existing project index date remains current.
- Key result: project guidance no longer directs agents to a nonexistent command; no broader restriction on validation tools is inferred.

## [2026-09-10] ingest | Altin Compact Cards And Production Verification

- What changed: preserved the compact-card/reusable-screen correction and the explicit production-API warning; updated the existing Orders Source Record, Altin project, development manual, and index.
- Files touched: `raw/sources/2026-09-10-altin-compact-cards-production-api.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/projects/altin-partner-mobile.md`, `wiki/syntheses/software-development-operating-manual.md`, `index.md`, and `log.md`.
- Key result: show a few scan fields and reveal detail on tap; use actual SERLP shared composition while preserving feature ownership. Treat the running backend as production and keep verification read-only with local tests for artificial scenarios.
- Follow-ups: runtime environment changes need fresh confirmation; implementation/review does not establish user visual acceptance.

## [2026-09-10] ingest | LivelyCura SMS-Only Sender Scope

- What changed: preserved the user's email-domain correction and updated the existing result-link Source Record, backend project, and index.
- Files touched: `raw/sources/2026-09-10-livelycura-result-email-sender-correction.md`, `wiki/sources/livelycura-result-link-environments.md`, `wiki/projects/livelycura-backend.md`, `index.md`, and `log.md`.
- Key result: SMS sender, email address, and portal URL are separate contracts; result email reuses central serlp.com email branding rather than a result-only livelycura.com sender.
- Follow-ups: establish any later email-domain change through explicit scope and provider verification; unit tests do not prove live delivery.

## [2026-09-10] ingest | LivelyCura Result Link Environments

- What changed: preserved the direct routing instruction, added a concise Source Record, and updated the existing backend project and index.
- Files touched: `raw/sources/2026-09-10-livelycura-result-link-environments.md`, `wiki/sources/livelycura-result-link-environments.md`, `wiki/projects/livelycura-backend.md`, `index.md`, and `log.md`.
- Key result: laboratory result links use the customer portal for local, staging, or production; unrelated URLs and private delivery data remain outside this decision.
- Follow-ups: verify deployments separately; the convention is not evidence of a live rollout.

## [2026-09-09] ingest | Restore LivelyCura Sale POS Lab Contract

- What changed: preserved the later reversal as new raw evidence and updated the existing Source Record, both project pages, and the index without rewriting earlier evidence or log entries.
- Files touched: `raw/sources/2026-09-09-livelycura-lab-sale-non-stock-correction.md`, `wiki/sources/livelycura-lab-order-agent-environment-correction.md`, `wiki/projects/livelycura-backend.md`, `wiki/projects/livelycura-pharmacy-portal.md`, `index.md`, and `log.md`.
- Key result: Sale POS creates lab requests; ordinary non-stock services require no inventory, and lab sync must not inherit the catalog's stock default. The order trigger is withdrawn while the Agent environment rule remains.
- Follow-ups: verify existing environment flags and deployment separately; do not infer live writes or clinical lifecycle changes.

## [2026-09-09] ingest | LivelyCura Lab Order And Agent Environment Correction

- What changed: preserved direct user evidence, added its Source Record, and corrected both existing project pages and the index.
- Files touched: `raw/sources/2026-09-09-livelycura-lab-order-agent-environment-correction.md`, `wiki/sources/livelycura-lab-order-agent-environment-correction.md`, `wiki/projects/livelycura-backend.md`, `wiki/projects/livelycura-pharmacy-portal.md`, `index.md`, and `log.md`.
- Key result: Order POS supersedes the earlier automatic sale trigger for non-stock lab tests; Agent environment visibility is separate from build optimization and retains permissions. Historical behavior remains explicit.
- Follow-ups: verify deployment separately and define later order-edit/cancellation effects on clinical work; do not infer permission to change existing staging records.

## [2026-09-09] ingest | Altin React.FC Component Convention

- What changed: preserved the user's direct component-typing correction and extended existing Altin and development guidance.
- Files touched: `raw/sources/2026-09-09-altin-react-fc-convention.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/projects/altin-partner-mobile.md`, `wiki/syntheses/software-development-operating-manual.md`, `index.md`, and `log.md`.
- Key result: use React.FC<Props> with separately owned interfaces instead of parameter annotations; preserve typed value boundaries and intervening edits.
- Follow-ups: none for this convention.

## [2026-09-09] ingest | Altin Orders Implementation Corrections

- What changed: preserved the user's technical corrections and updated existing Altin and development guidance without promoting private screenshot data.
- Files touched: `raw/sources/2026-09-09-altin-orders-implementation-corrections.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/projects/altin-partner-mobile.md`, `wiki/syntheses/software-development-operating-manual.md`, `index.md`, and `log.md`.
- Key result: Conditional, skeletons, sibling detail ownership, inline hook operations, separate cards, plain list headers, reuse of the existing runtime, and preservation of intervening edits are explicit. Later corrections supersede conflicting plan text and prior visual approval.
- Follow-ups: user visual acceptance remains distinct from source or simulator verification.

## [2026-09-09] ingest | Altin Orders Mobile Reference and Ownership

- What changed: preserved the approved Orders decisions and updated the existing Altin project guidance.
- Files touched: `raw/sources/2026-09-09-altin-orders-mobile-web-reference.md`, `wiki/sources/altin-orders-mobile-web-reference.md`, `wiki/projects/altin-partner-mobile.md`, `index.md`, and `log.md`.
- Key result: the web clone supplies product/API contracts while mobile ownership remains authoritative; organization access, reset behavior, and Tips' broader scope are explicit.
- Follow-ups: select the next remaining module; keep deferred write/realtime features separate.

## [2026-09-08] ingest | Keks Conditional Rendering Convention

- What changed: preserved the user's direct correction about ternary rendering and extended the existing Keks analytics source record and project conventions.
- Files touched: `raw/sources/2026-09-08-keks-conditional-rendering-correction.md`, `wiki/sources/keks-analytics-ui-scope-correction.md`, `wiki/projects/keks-admin-portal.md`, `index.md`, and `log.md`.
- Key result: use the existing shared Conditional component for conditional JSX while retaining state exclusivity and the requested UI scope.
- Follow-ups: none for this scoped convention.

## [2026-09-08] ingest | Keks Analytics UI Scope Correction

- What changed: preserved the user's rejection of page-wide redesign and deletion of a disliked addition; recorded restyling-only scope and existing feature architecture.
- Files touched: `raw/sources/2026-09-08-keks-analytics-ui-scope-correction.md`, `wiki/sources/keks-analytics-ui-scope-correction.md`, `wiki/projects/keks-admin-portal.md`, `index.md`, and `log.md`.
- Key result: retain both Workforce Attendance and Needs Attention and preserve unrelated analytics components when improving the new sections.
- Follow-ups: none for this scoped correction.

## [2026-09-07] ingest | Call Center Customer Detail Navigation Correction

- What changed: preserved the user's acceptance of customer styling and rejection of inline profile navigation; recorded separate list/detail route and folder ownership plus the tenant-theme total contrast lesson.
- Files touched: `raw/sources/2026-09-07-call-center-customer-detail-navigation-correction.md`, `wiki/sources/call-center-customer-detail-navigation-correction.md`, `wiki/projects/call-center-web-app.md`, `index.md`, and `log.md`.
- Key result: future customer work must follow the application's existing list-to-detail navigation and plural/singular feature structure.
- Follow-ups: none for this scoped correction.

## [2026-09-07] ingest | Call Center Customer UI Consistency Correction

- What changed: preserved direct user rejection of the initial Customers UI and recorded existing-page comparison plus in-shell visual verification as project guidance.
- Files touched: `raw/sources/2026-09-07-call-center-customer-ui-consistency-correction.md`, `wiki/sources/call-center-customer-ui-consistency-correction.md`, `wiki/projects/call-center-web-app.md`, `index.md`, and `log.md`.
- Key result: future customer-service UI changes must fit the existing call-center application rather than rely on generic component previews.
- Follow-ups: none for this scoped durable correction.

## [2026-09-06] ingest | Bora KYC Supervision And Statement Update

- What changed: preserved direct user clarification and recorded supervised KYC, profile-refresh approval, corrected resubmission, the date-range statement endpoint update, and continued linked-portfolio deferral.
- Files touched: `raw/sources/2026-09-06-bora-kyc-supervision-and-statement-update.md`, `wiki/sources/bora-kyc-supervision-and-statement-update.md`, `wiki/projects/bora-capital-backend.md`, `index.md`, and `log.md`.
- Key result: future Bora changes distinguish submission from approval and retain the user's explicit linked-account scope boundary.
- Follow-ups: clarify the linked-portfolio product requirements; live BCL verification remains a separate provider check.

## [2026-09-04] ingest | Customer Portal Support Rendering Conventions

- What changed: preserved the direct user correction and recorded existing conditional-component reuse, feature-owned support styles, accepted-layout preservation, and latest-chat history previews.
- Files touched: `raw/sources/2026-09-04-customer-portal-support-rendering-conventions.md`, `wiki/sources/customer-portal-support-rendering-conventions.md`, `wiki/projects/livelycura-customer-portal.md`, `index.md`, and `log.md`.
- Key result: future Customer Portal support edits have an explicit, source-backed implementation convention.
- Follow-ups: none for this scoped correction.

## [2026-09-01] maintenance | Rename Marketplace Business Product Listing

What changed:

- Replaced the ambiguous `MarketplaceBusinessProductConfiguration` term with `MarketplaceBusinessProductListing` across the durable marketplace architecture.
- Recorded that a listing owns canonical marketplace categories and publication state for an ordinary ERP product without copying product data.
- Preserved the deployed MongoDB collection name as a compatibility-only implementation detail.

Files touched:

- `index.md`
- `log.md`
- `raw/sources/2026-09-01-marketplace-business-product-listing-rename.md`
- `wiki/sources/marketplace-scoped-admin-catalog-order-restructure.md`
- `wiki/projects/livelycura-backend.md`
- `wiki/projects/livelycura-admin-portal.md`
- `wiki/projects/livelycura-choproute-app.md`

Key result:

- Future backend and Admin work must use “business product listing,” not “business product configuration,” for this marketplace-owned relationship.

Follow-ups:

- Rename the physical collection only if a separate data migration is later justified; do not silently create a second collection.

## [2026-09-01] maintenance | Require Fresh CheckCity Location And Branch

What changed:

- Recorded device location and nearest-branch selection as app-lifecycle state that refreshes on cold launch and every foreground return.
- Prohibited persisted delivery locations, persisted branches, and arbitrary first-branch fallback from remaining orderable when GPS refresh fails.
- Added the checkout rule that ordering remains blocked until current GPS coordinates and their nearest branch are resolved.

Files touched:

- `index.md`
- `log.md`
- `wiki/projects/livelycura-check-city-app.md`

Key result:

- Future CheckCity changes must never allow customers to submit orders using a stale delivery location or branch after relaunching or returning to the app.

Follow-ups:

- Verify cold-launch, background/foreground, permission-denied, and changed-physical-location behavior in Expo Go on a device or simulator with controlled location updates.

## [2026-08-30] maintenance | Record Shared Customer Support Architecture

What changed:

- Added the cross-application customer-support ownership and routing architecture.
- Linked the backend, Admin, Pharmacy Portal, Customer Portal, Customer Mobile, CheckCity, and ChopRoute project pages to the shared contract.
- Recorded verified-client ownership, channel isolation, responder boundaries, private notes/attachments, lifecycle/idempotency, CRM-module exception, and notification privacy/deep links.

Files touched:

- `index.md`
- `log.md`
- `wiki/concepts/livelycura-customer-support-architecture.md`
- Seven linked LivelyCura project pages.

Key result:

- Future customer channels, including the reserved organization storefront, must reuse the same support domain and derive ownership only from verified backend context.

Follow-ups:

- Add SLA, transfer, automation, guest intake, chatbot, and configurable-retention rules only as explicit later versions.

## [2026-08-30] maintenance | Correct CheckCity App-Rating Trigger

What changed:

- Updated the CheckCity project rule so native app-rating eligibility starts after any successful order creation, including pickup.
- Superseded the earlier delivery-completion and completed-delivery-count gate.
- Preserved the distinction between checkout-created order navigation and ordinary historical order-detail views, plus the Expo Go native-action guard and persisted per-user attempt state.

Files touched:

- `index.md`
- `log.md`
- `wiki/projects/livelycura-check-city-app.md`

Key result:

- Future CheckCity work must not exclude pickup customers from app-rating eligibility or reattach review prompts to delivery completion.

Follow-ups:

- Verify the native prompt in a standalone development build; Expo Go must exercise eligibility without rating the Expo Go host application.

## [2026-08-29] maintenance | Remove Parallel CheckCity Feedback Domain

What changed:

- Recorded the product decision that customer feedback and customer support overlap and should not remain separate features.
- Removed the dedicated feedback route, profile/order entry points, GraphQL contract, persistence model, permissions, and generated types from the current project boundary.
- Preserved delivery activity, app ratings, and the mandatory Expo Go acceptance convention.

Files touched:

- `wiki/projects/livelycura-check-city-app.md`
- `index.md`
- `log.md`

Key result:

- Future customer-contact work should be designed under customer support rather than rebuilding a parallel feedback domain.

Follow-ups:

- Define the customer-support scope before implementing its mobile and backend intake flow.

## [2026-08-29] maintenance | Require Expo Go Acceptance For CheckCity

What changed:

- Updated the CheckCity project stack to Expo SDK 57.
- Recorded the user's correction that Expo-compatible customer-app work is incomplete until it launches through Expo Go with a cleared Metro cache and no optional-native-module crash.
- Recorded the boundary that native eligibility logic should still execute in Expo Go while host-app-native actions such as store review remain suppressed and unrecorded.

Files touched:

- `wiki/projects/livelycura-check-city-app.md`
- `index.md`
- `log.md`

Key result:

- Future CheckCity work now treats real Expo Go startup and affected-flow verification as an explicit acceptance criterion rather than relying on a custom development build alone.

Follow-ups:

- Continue using standalone builds for capabilities that genuinely require native binaries while preserving graceful Expo Go behavior for the rest of the app.

## [2026-08-28] maintenance | Persist Withdrawal Instructions Before OTP Completion

What changed:

- Replaced repeated account, amount, and comment submission with a dedicated pending-withdrawal resource.
- Recorded OTP `resourceId` binding and completion using only `otpRequestId` plus `otp`.
- Recorded atomic request claiming, server-owned BCL date generation, and `PENDING_VERIFICATION`/`PROCESSING`/`SUBMITTED`/`FAILED` lifecycle tracking.

Files touched:

- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The client submits the financial instruction once; OTP verification retrieves and executes the immutable stored request.

Follow-ups:

- Decide a retention/cleanup policy for expired pending-withdrawal records if operational volume requires it.

## [2026-08-28] maintenance | Make Withdrawal Date Server-Owned

What changed:

- Recorded that public withdrawal OTP and completion inputs must not accept `transactionDate`.
- Bound withdrawal OTPs only to customer-controlled account, amount, and comment fields.
- Recorded backend generation of the current `YYYY-MM-DD` date immediately before the verified BCL withdrawal request.

Files touched:

- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Clients no longer control BCL withdrawal transaction dates; the execution service owns the timestamp boundary.

Follow-ups:

- Keep deposit date ownership unchanged unless that separate contract is explicitly reviewed.

## [2026-08-28] maintenance | Restore GrowWealth Deferral And Canonical Phone Lookup

What changed:

- Corrected the portfolio boundary: GrowWealth remains service-only until BCL supplies response fields; only SIC is exposed through explicitly named GraphQL operations.
- Removed the recorded Ghana phone-format variants and restored exact lookup of the frontend-supplied canonical `+233…` number.
- Preserved email/phone-first existing-client linking, optional identity ID, and OTP-bound password creation without automatic login.

Files touched:

- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The durable project record now matches the reviewed implementation and no longer treats a raw `JSON` field as an acceptable placeholder GraphQL contract.

Follow-ups:

- Add GrowWealth GraphQL types and resolvers only after BCL provides the linked-portfolio response shape.

## [2026-08-28] maintenance | Complete Existing-Client Onboarding And Portfolio GraphQL Split

What changed:

- Recorded email/phone-first existing-client linking with optional BCL identity ID.
- Separated OTP verification/password creation from login-token issuance and preserved the normal login-screen transition.
- Recorded equivalent Ghana phone lookup after password recovery and separate typed SIC/raw-JSON GrowWealth GraphQL operations.

Files touched:

- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Existing clients now have an explicit non-login onboarding completion contract, while portfolio GraphQL distinguishes SIC from GrowWealth without guessing GrowWealth response fields.

Follow-ups:

- Replace the GrowWealth raw `JSON` result with typed fields after BCL supplies the response envelope and field definitions.

## [2026-08-28] maintenance | Separate SIC And GrowWealth Portfolio Contracts

What changed:

- Recorded SIC and GrowWealth as separate BCL-backed portfolio service families.
- Preserved GrowWealth as service-only with a raw provider response until BCL supplies its response fields.
- Recorded the bidirectional app/BCL translation for proof of address and ID front/back KYC images.

Files touched:

- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Future portfolio and KYC work has an explicit provider-boundary contract without prematurely publishing GrowWealth GraphQL fields.

Follow-ups:

- Add GrowWealth interfaces, normalization, and GraphQL schema only after BCL provides the linked-portfolio response shape.

## [2026-08-21] correction | Keep Paystack Provisioning Manual And Explicit

What changed:

- Recorded the user's rejection of bulk result-order Paystack setup and startup provider migrations.
- Established small, manually invoked, one-portfolio staging and production scripts as the Bora provisioning convention.
- Kept production credentials and settlement account identifiers out of the vault.

Files touched:

- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Future Paystack provisioning work should favor visible operator-controlled steps over generalized bulk orchestration.

Follow-ups:

- Execute live production setup only after explicit authorization and confirmation of the current Paystack Ghana bank code.

## [2026-08-08] correction | Use Shared Conditional In Marketplace Tables

What changed:

- Recorded the shared `Conditional` component as the required loading/data branch structure inside Admin table bodies.
- Applied the convention to Organization Access, Business Products, and Direct Orders.

Files touched:

- `raw/sources/2026-08-08-marketplace-admin-conditional-table-rendering-correction.md`
- `wiki/sources/marketplace-scoped-admin-catalog-order-restructure.md`
- `wiki/projects/livelycura-admin-portal.md`
- `index.md`
- `log.md`

Key result:

- Marketplace table rendering now follows the same component structure as the existing Admin tables instead of using one-off ternary branches.

Follow-ups:

- Use `Conditional` for later marketplace table loading/data branches from the start.

## [2026-08-08] correction | Restore Marketplace Admin Table Conventions

What changed:

- Recorded mandatory leading row numbers and labeled trailing Actions columns for marketplace tables.
- Added URL-backed organization, category, publication, and status filters according to each GraphQL list contract.
- Preserved feature-owned components, hooks, interfaces, and constants instead of moving list logic into shared or service files.

Files touched:

- `raw/sources/2026-08-08-marketplace-admin-table-filter-action-convention.md`
- `wiki/sources/marketplace-scoped-admin-catalog-order-restructure.md`
- `wiki/projects/livelycura-admin-portal.md`
- `index.md`
- `log.md`

Key result:

- Marketplace administration tables now inherit the existing Admin architecture and interaction model rather than using reduced one-off tables.

Follow-ups:

- Apply this convention to every later marketplace-scoped table before considering the screen complete.

## [2026-08-08] correction | Enforce Marketplace Admin Capability And Table UX

What changed:

- Recorded that disabled marketplace catalog/order capabilities must not appear in the selected-marketplace sidebar.
- Made organization access a searchable table with an explicit Add Organization selection modal.
- Recorded one refresh action per list header and layout-matched skeletons for marketplace loading states.

Files touched:

- `raw/sources/2026-08-08-marketplace-admin-capability-controls-loading-correction.md`
- `wiki/sources/marketplace-scoped-admin-catalog-order-restructure.md`
- `wiki/projects/livelycura-admin-portal.md`
- `index.md`
- `log.md`

Key result:

- Marketplace Admin navigation and table controls now derive from the selected marketplace's enabled capabilities and preserve the normal Admin list-page interaction model.

Follow-ups:

- Retain capability-filtered navigation and skeleton loading as later marketplace admin pages evolve.

## [2026-08-08] maintenance | Correct Marketplace Admin Navigation Ownership

What changed:

- Recorded launchpad-style marketplace cards as the selection experience.
- Superseded the single details page with in-content tabs; selected marketplace sections now belong to the main sidebar and render normal full list/table pages.
- Added live verification evidence for Organizations, Business Products, Direct Orders, route-scoped sidebar links, and a clean browser console.

Files touched:

- `raw/sources/2026-08-08-marketplace-admin-launchpad-sidebar-correction.md`
- `wiki/sources/marketplace-scoped-admin-catalog-order-restructure.md`
- `wiki/projects/livelycura-admin-portal.md`
- `index.md`
- `log.md`

Key result:

- Marketplace selection and navigation now follow the existing Admin shell instead of creating a separate in-page workspace pattern.

Follow-ups:

- Preserve this route/sidebar ownership while implementing later marketplace administration screens.

## [2026-08-08] maintenance | Replace Marketplace Category Projection With Admin Scope

What changed:

- Recorded selected-marketplace Admin ownership for organization access, catalog classification, canonical categories, bidding demand, direct fulfillment Orders, and capability settings.
- Superseded the organization-category projection and ERP marketplace-assignment contract while preserving the historical source record.
- Updated the Backend, Admin Portal, Pharmacy Portal, SERLP Mobile, and ChopRoute project boundaries plus implementation verification evidence.

Files touched:

- `raw/sources/2026-08-08-marketplace-scoped-admin-catalog-order-restructure.md`
- `wiki/sources/marketplace-scoped-admin-catalog-order-restructure.md`
- `wiki/sources/choproute-marketplace-owned-category-taxonomy.md`
- `wiki/projects/livelycura-backend.md`
- `wiki/projects/livelycura-admin-portal.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/projects/serlp-mobile.md`
- `wiki/projects/livelycura-choproute-app.md`
- `index.md`
- `log.md`

Key result:

- Admin now owns marketplace publication and canonical classification directly against ordinary products; ERP product/category behavior remains unchanged, existing Marketplace Product/bidding modes remain valid, and the ChopRoute consumer switch stays deferred.

Follow-ups:

- Deploy and run the registered migration after review, then migrate the ChopRoute consumer catalog and later design direct checkout/allocation/payment.

## [2026-08-07] implementation | Establish ChopRoute Canonical Category Taxonomy

What changed:

- Recorded `MarketplaceCategory` as ChopRoute's canonical customer-facing taxonomy and protected organization categories as its adapter into ordinary ERP product relationships.
- Superseded direct ERP-category discovery, same-name merging, and uncategorized product-name fallback.
- Recorded the completed backend, ChopRoute, SERLP, ERP, explicit migration, live-query, and focused-test verification boundaries.

Files touched:

- `raw/sources/2026-08-07-choproute-marketplace-owned-category-taxonomy.md`
- `wiki/sources/choproute-marketplace-owned-category-taxonomy.md`
- `wiki/projects/livelycura-choproute-app.md`
- `index.md`
- `log.md`

Key result:

- ChopRoute now uses stable canonical category IDs across organizations without duplicating ERP products or consulting procurement product-linking models.

Follow-ups:

- Approve and migrate additional canonical taxonomy entries beyond Fried Rice, Jollof, and Pizza; remove deprecated consumer `categoryIds` after all clients migrate.

## [2026-08-07] remediation | Migrate ChopRoute Navigation Actions To App Hooks

What changed:

- Recorded the authorized whole-source migration from direct feature navigation actions to the two app navigation hooks.
- Updated the earlier convention record from a known violation to a completed remediation.
- Preserved direct `useRoute`/`useNavigationState` as read-only concerns and removed obsolete feature navigation aliases.

Files touched:

- `raw/sources/2026-08-07-choproute-navigation-hook-migration.md`
- `wiki/sources/choproute-navigation-hook-migration.md`
- `wiki/sources/choproute-navigation-hook-convention.md`
- `wiki/projects/livelycura-choproute-app.md`
- `index.md`
- `log.md`

Key result:

- All ChopRoute navigation actions now cross the established app abstraction boundary, including the custom bottom tab bar and legacy screens.

Follow-ups:

- Consider centrally typing route names and parameters in the app navigation hooks.

## [2026-08-07] correction | Enforce ChopRoute Navigation Hooks

What changed:

- Preserved the correction that all navigation actions must use `useAppNavigation` or `useAppNavigationWithRef`.
- Recorded direct `useNavigation` usage in the newly worked feature surfaces as a known violation, not a competing convention.
- Clarified that `useRoute` remains appropriate for route reads and that typing gaps should be fixed centrally in the wrappers.

Files touched:

- `raw/sources/2026-08-07-choproute-navigation-hook-convention.md`
- `wiki/sources/choproute-navigation-hook-convention.md`
- `wiki/projects/livelycura-choproute-app.md`
- `index.md`
- `log.md`

Key result:

- Future ChopRoute navigation work must preserve the app-level abstraction instead of importing direct screen navigation actions.

Follow-ups:

- Replace the identified direct navigation actions in a separately authorized remediation step and decide whether to type the wrappers centrally.

## [2026-08-07] correction | Move ChopRoute Catalog Queries Into Owning Features

What changed:

- Preserved the correction that relocating the combined catalog query into global hooks was still wrong.
- Recorded separate Home product/category operations and corresponding feature-owned operations for Explore, Restaurants, Category Products, and Restaurant Details.
- Recorded Redux organization IDs as the required access input for every feature query and removed the global combined hook/filter contract.

Files touched:

- `raw/sources/2026-08-07-choproute-feature-owned-catalog-queries.md`
- `wiki/sources/choproute-feature-owned-catalog-queries.md`
- `wiki/sources/choproute-marketplace-feature-folder-removal.md`
- `wiki/projects/livelycura-choproute-app.md`
- `index.md`
- `log.md`

Key result:

- `src/hooks/useMarketPlace.ts` is the only general marketplace hook; product/category data operations now belong to their consuming feature folders.

Follow-ups:

- Remove the bounded category-name fallback once ERP product-category relationships are complete.

## [2026-08-07] correction | Remove ChopRoute Marketplace Feature Folder

What changed:

- Preserved the correction that no top-level `src/marketplace` client feature should remain after system and Redux ownership were established.
- Recorded relocation of shared catalog components, hook, interface, helper, and stage UI into the repository's established main folders.
- Superseded the immediately prior allowance for marketplace-owned catalog files without changing the visible catalog behavior.

Files touched:

- `raw/sources/2026-08-07-choproute-marketplace-feature-folder-removal.md`
- `wiki/sources/choproute-marketplace-feature-folder-removal.md`
- `wiki/projects/livelycura-choproute-app.md`
- `index.md`
- `log.md`

Key result:

- Future ChopRoute work must not recreate `src/marketplace`; system startup, Redux state, shared main-folder utilities, and feature-owned behavior are the client ownership boundaries.

Follow-ups:

- Split Home product and category queries during the next requested data-loading stage.

## [2026-08-07] correction | Align ChopRoute Marketplace Loading With System Structure

What changed:

- Preserved the direct correction that marketplace and access-organization loading belongs in `src/system` beside user startup.
- Recorded `src/hooks/useMarketPlace.ts` as the single general Redux access hook and removed marketplace-owned bootstrap/provider ownership.
- Recorded removal of the obsolete ChopRoute custom-app client feature while distinguishing generated shared-schema CustomApp types.

Files touched:

- `raw/sources/2026-08-07-choproute-system-marketplace-ownership-custom-app-removal.md`
- `wiki/sources/choproute-system-marketplace-ownership-custom-app-removal.md`
- `wiki/projects/livelycura-choproute-app.md`
- `index.md`
- `log.md`

Key result:

- Future ChopRoute work must load app-wide marketplace identity through the system startup layer and consume it through the one top-level Redux hook; `src/marketplace` remains domain/catalog code only.

Follow-ups:

- Move Home products and categories into separate Home-owned queries in the next integration stage.

## [2026-08-07] correction | Remove ChopRoute Client Branch Feature

What changed:

- Preserved the direct instruction to remove the unused client branch feature and files.
- Superseded the earlier decision to retain dormant branch and checkout code.
- Recorded that delivery location stays customer-facing while facility selection and allocation remain future server responsibilities.

Files touched:

- `raw/sources/2026-08-07-choproute-client-branch-removal.md`
- `wiki/sources/choproute-client-branch-removal.md`
- `wiki/projects/livelycura-choproute-app.md`
- `index.md`
- `log.md`

Key result:

- Future ChopRoute work must not restore global branch Redux state, hooks, selector routes, or UI; checkout and reorder remain gated until server-side marketplace allocation is implemented.

Follow-ups:

- Define marketplace order allocation separately when the ordering stage begins.

## [2026-08-07] correction | Move ChopRoute Marketplace State To Redux

What changed:

- Preserved the direct correction that the current marketplace and its access-granted organizations are Redux-owned application state, not React context.
- Recorded the staged sequence: complete Redux ownership first, then move Home product and category loading into separate Home-owned query files.
- Updated the ChopRoute project architecture, folder ownership, conventions, rationale, and verification evidence to match the live Redux bootstrap.

Files touched:

- `raw/sources/2026-08-07-choproute-redux-marketplace-state-correction.md`
- `wiki/sources/choproute-redux-marketplace-state-correction.md`
- `wiki/projects/livelycura-choproute-app.md`
- `index.md`
- `log.md`

Key result:

- Future work will treat Redux as the single client-side source for ChopRoute marketplace identity and accessible organizations, with Home query separation explicitly queued as the next integration stage.

Follow-ups:

- Split Home product and category loading into separate Home-owned query files without mixing in unrelated redesign work.

## [2026-08-06] ingest | Correct ChopRoute Shelf Shape And Home Category Groups

What changed:

- Preserved the failed straight-divider screenshot and the user's exact continuous-shelf correction as raw evidence.
- Clarified that the tab-bar border itself curves around the raised Restaurants action and that a circle over a straight divider is not acceptable.
- Recorded the shared category-group behavior across Home, Explore, and category detail, with ERP relationships authoritative and a bounded fallback only for the current uncategorized, clearly named test products.

Files touched:

- `raw/assets/2026-08-06-choproute-straight-divider-failed-implementation.png`
- `raw/sources/2026-08-06-choproute-shaped-tab-shelf-category-group-correction.md`
- `wiki/sources/choproute-raised-restaurants-navigation-category-correction.md`
- `wiki/sources/choproute-home-restaurants-navigation-direction.md`
- `wiki/projects/livelycura-choproute-app.md`
- `index.md`
- `log.md`

Key result:

- ChopRoute now has a durable exact shelf-shape contract and internally consistent category-group rendering for the current live test catalog without introducing marketplace product links.

Follow-ups:

- Populate ERP product-category relationships so future catalog growth no longer needs the bounded uncategorized-name fallback.

## [2026-08-06] ingest | Correct ChopRoute Center Navigation And Category Discovery

What changed:

- Preserved the newest navigation references and direct correction as raw evidence.
- Replaced the obsolete five-tab Restaurants contract with four true tabs around a raised center Restaurants stack action.
- Recorded access-scoped ERP category discovery independent of product-category assignments, with same-name category merging at the customer-facing filter layer.
- Reinforced the existing cross-project rule to reread and preserve newer live user edits.

Files touched:

- `raw/assets/2026-08-06-choproute-raised-center-navigation-dark.jpeg`
- `raw/assets/2026-08-06-choproute-raised-center-navigation-light.jpeg`
- `raw/sources/2026-08-06-choproute-raised-restaurants-navigation-category-correction.md`
- `wiki/sources/choproute-raised-restaurants-navigation-category-correction.md`
- `wiki/projects/livelycura-choproute-app.md`
- `index.md`
- `log.md`

Key result:

- ChopRoute now has a durable four-tab navigation contract with a standalone raised Restaurants action and an access-safe category list sourced directly from ordinary ERP categories.

Follow-ups:

- Decide how marketplace category order is configured once more organizations join.

## [2026-08-06] correction | Restore ChopRoute Feature Structure

What changed:

- Corrected the earlier mistaken flat-feature interpretation of “remove unnecessary folders.”
- Reorganized Explore, categoryProducts, and restaurants around the established components, hooks, interfaces, helpers, and constants subfolder structure.
- Kept obsolete competing top-level Menu, Search, and standalone Categories browse features removed without collapsing Explore's internal ownership.

Files touched:

- `raw/sources/2026-08-06-choproute-explore-feature-structure-correction.md`
- `wiki/sources/choproute-explore-naming-ownership-correction.md`
- `wiki/projects/livelycura-choproute-app.md`
- `index.md`
- `log.md`

Key result:

- ChopRoute's new browse features now follow the repository's established ownership structure instead of flattening concerns or inventing parallel top-level domains.

Follow-ups:

- Apply the same ownership check before implementing each later-stage feature.

## [2026-08-06] ingest | Consolidate ChopRoute Browse Ownership Under Explore

What changed:

- Preserved Explore as the canonical full-catalog tab and route instead of maintaining a parallel Menu identity.
- Recorded flat `src/explore` ownership for search and filters, plus removal of obsolete top-level Menu, Search, and standalone Categories browse features.
- Updated the ChopRoute project and earlier Home-navigation source to use Explore while retaining shared catalog and product-detail ownership outside the route feature.

Files touched:

- `raw/sources/2026-08-06-choproute-explore-naming-ownership-correction.md`
- `wiki/sources/choproute-explore-naming-ownership-correction.md`
- `wiki/sources/choproute-home-restaurants-navigation-direction.md`
- `wiki/projects/livelycura-choproute-app.md`
- `index.md`
- `log.md`

Key result:

- ChopRoute now has one durable browse contract: Explore owns its adjacent search/filter experience without unnecessary feature nesting, while cross-entry catalog and product infrastructure stays shared.

Follow-ups:

- Decide which additional Explore filters are needed after backend product-category relationships are populated.

## [2026-08-06] ingest | Separate ChopRoute Home From Restaurant Discovery

What changed:

- Preserved the correction that Home is product-led and must not display restaurant cards.
- Recorded category-specific Home routing, Popular-only Menu routing, and the dedicated Restaurants tab/detail interaction.
- Updated the ChopRoute project contract with access-checked organization filtering and shared product-card ownership.

Files touched:

- `raw/sources/2026-08-06-choproute-home-restaurants-navigation-direction.md`
- `wiki/sources/choproute-home-restaurants-navigation-direction.md`
- `wiki/projects/livelycura-choproute-app.md`
- `index.md`
- `log.md`

Key result:

- ChopRoute now has one durable discovery split: Home browses meals by popularity and category, while Restaurants browses access-granted organizations and their ordinary ERP products.

Follow-ups:

- Define Popular ranking and the selection policy for the four Home category sections after product-category data is populated.

## [2026-08-06] maintenance | Resolve ChopRoute Marketplace Client 401

What changed:

- Diagnosed the HTTP 401 as client-context rejection rather than a customer token failure.
- Confirmed the active ChopRoute marketplace existed without an `appIdentifier`, verified `CHOPROUTE_MARKETPLACE` had no marketplace or custom-app collision, and assigned it to that record.
- Updated the ChopRoute project contract with the confirmed runtime identifier and resolver verification.

Files touched:

- `wiki/projects/livelycura-choproute-app.md`
- `index.md`
- `log.md`

Key result:

- `resolveMarketplaceRequestContext("CHOPROUTE_MARKETPLACE")` now resolves the active ChopRoute marketplace and matches the app's `client` header.

Follow-ups:

- Restart the local backend and reload Metro, then visually confirm Check City and Pice Restaurant catalog data.

## [2026-08-06] ingest | Pivot The Existing Pice Scaffold To ChopRoute Stage One

What changed:

- Preserved the correction that the established marketplace plan continues stage by stage rather than being replaced.
- Renamed the active project knowledge from Pice to ChopRoute and retained the Pice material as historical UI evidence for a prospective separate engagement.
- Recorded active marketplace organization access and ordinary ERP products as the stage-one discovery path, with no bidding, MarketplaceProduct linking, duplicate food models, or app-owned delivery branch.

Files touched:

- `raw/sources/2026-08-06-choproute-marketplace-stage-one-correction.md`
- `wiki/sources/choproute-marketplace-stage-one-correction.md`
- `wiki/sources/pice-home-ui-direction.md`
- `wiki/sources/pice-project-bootstrap-directive.md`
- `wiki/projects/livelycura-choproute-app.md`
- `wiki/projects/livelycura-pice-app.md` (renamed/superseded)
- `index.md`
- `log.md`

Key result:

- ChopRoute stage one now has one durable contract: redesign the app and display ordinary products from dynamically access-granted organizations; leave ordering, facility allocation, pickup, payments, and payouts to later stages.

Follow-ups:

- Confirm the live ChopRoute marketplace `appIdentifier`, then visually verify Check City and Pice Restaurant data in the app before starting the next stage.

## [2026-08-05] maintenance | Separate Pice Delivery Address From Branch Selection

What changed:

- Preserved the direct correction that selecting a delivery location must not open the branch modal.
- Established that the Home `Deliver to` control owns address search/GPS while the branch header owns explicit branch selection.
- Recorded that nearest-branch resolution may occur silently after address selection without replacing the address flow.

Files touched:

- `raw/sources/2026-08-05-pice-delivery-address-branch-separation.md`
- `wiki/sources/pice-home-ui-direction.md`
- `wiki/projects/livelycura-pice-app.md`
- `index.md`
- `log.md`

Key result:

- Delivery-address selection and visible branch selection are now separate Pice interaction contracts.

Follow-ups:

- Recheck silent nearest-branch resolution with real backend branches and delivery addresses.

## [2026-08-05] maintenance | Make Pice Cart Emphasis Active-Only

What changed:

- Preserved the supplied active-Cart reference and direct correction.
- Superseded the incorrect rule that item count could trigger Cart's filled treatment.
- Established that selection alone controls tab fill, filled icons, and labels; Cart quantity controls only the badge.

Files touched:

- `raw/sources/2026-08-05-pice-cart-active-state-correction.md`
- `raw/assets/2026-08-05-pice-active-cart-tab-reference.png`
- `wiki/sources/pice-home-ui-direction.md`
- `wiki/projects/livelycura-pice-app.md`
- `index.md`
- `log.md`

Key result:

- An inactive Cart with items is outline-only with a badge and no label; an active Cart is filled and displays `Cart`.

Follow-ups:

- Recheck the same active-only contract if additional tab variants are introduced.

## [2026-08-05] maintenance | Preserve And Share The Approved Pice Menu Item

What changed:

- Preserved the direct correction that the approved Home product card must become the shared `MenuItem` without being redesigned.
- Established that Home and backend-loaded Menu products use the same vertical component, while favourites and recent/order-again use a separate horizontal variant.
- Recorded that generalization means ownership refactoring and never implies permission to restyle approved UI.

Files touched:

- `raw/sources/2026-08-05-pice-shared-menu-item-correction.md`
- `wiki/sources/pice-home-ui-direction.md`
- `wiki/projects/livelycura-pice-app.md`
- `index.md`
- `log.md`

Key result:

- Future Pice product-card work has one canonical vertical `MenuItem`; approved visuals remain unchanged unless the user explicitly requests redesign.

Follow-ups:

- Capture the populated Menu grid after backend test items are added.

## [2026-08-05] maintenance | Align Pice Home And Menu Naming

What changed:

- Preserved the direct correction that Home and Menu names must not be interchanged.
- Established matching route, screen, folder, and deep-link ownership for Home and Menu while keeping Search as an internal Menu capability and `/search` as a compatibility alias.
- Updated the Pice source, project, and index contracts with the naming boundary and implementation verification.

Files touched:

- `raw/sources/2026-08-05-pice-home-menu-naming-correction.md`
- `wiki/sources/pice-home-ui-direction.md`
- `wiki/projects/livelycura-pice-app.md`
- `index.md`
- `log.md`

Key result:

- Future Pice navigation work must use `HomeScreen`/`routes.home` for Home and `MenuScreen`/`routes.menu` for Menu; Search cannot replace Menu as a tab identity.

Follow-ups:

- Continue with the next Pice task after the code and vault checks pass.

## [2026-08-05] correction | Hide Labels On Inactive Pice Tabs

What changed:

- Preserved the direct correction that inactive bottom tabs are icon-only.
- Established that only the selected tab displays its label; Cart badges remain independent of label visibility.
- Updated the Pice source, project, and index contracts to prevent inactive labels from returning.

Files touched:

- `raw/sources/2026-08-05-pice-inactive-tab-label-correction.md`
- `wiki/sources/pice-home-ui-direction.md`
- `wiki/projects/livelycura-pice-app.md`
- `index.md`
- `log.md`

Verification:

- The iOS Simulator shows the Orders label only while Home, Menu, and Cart remain icon-only.
- TypeScript, Prettier, `git diff --check`, and the canonical vault validator passed.

## [2026-08-05] correction | Make Pice Components Match Their Reference States

What changed:

- Preserved the direct correction and three focused reference crops for bottom tabs, delivery, and categories.
- Superseded the permanently raised Cart interpretation with an in-bar state model: empty inactive Cart matches other tabs; Cart with items uses a filled circle and badge without protruding.
- Established the compact delivery card and unheaded six-photo category strip as durable Pice conventions.

Files touched:

- `raw/sources/2026-08-05-pice-component-state-correction.md`
- `raw/assets/2026-08-05-pice-bottom-tab-state-reference.png`
- `raw/assets/2026-08-05-pice-delivery-bar-reference.png`
- `raw/assets/2026-08-05-pice-category-strip-reference.png`
- `wiki/sources/pice-home-ui-direction.md`
- `wiki/projects/livelycura-pice-app.md`
- `index.md`
- `log.md`

Verification:

- Empty and two-item Cart states were captured in the iOS Simulator; the two-item circle and badge stay inside the bar.
- Focused reference and implementation crops were placed in one comparison artifact.
- TypeScript, Prettier, `git diff --check`, Expo web export, and the canonical vault validator passed.

## [2026-08-05] verification | Correct And Visually Verify The Pice Home Composition

What changed:

- Replaced the overlapping floating header with a safe-area header followed by the delivery/search row.
- Recorded the development-only Pice preview menu that preserves the complete home hierarchy when branch data is empty.
- Replaced the unstable animated hero with one stable full-width promotion and verified the corrected screen against both supplied references.

Files touched:

- `wiki/projects/livelycura-pice-app.md`
- `log.md`

Verification:

- A live iOS Simulator capture was placed beside both supplied reference images in one comparison artifact.
- TypeScript, Prettier, and `git diff --check` passed after the correction.

## [2026-08-05] correction | Match Pice Tabs To The References And Remove Background Decor

What changed:

- Preserved the direct correction that the uploaded UI—not the inherited code—controls Pice bottom-navigation composition.
- Superseded the detached-right Cart interpretation with Home, Menu, raised center Cart, and Orders in one full-width rounded bar.
- Established the app-wide prohibition on global patterns and screen/modal background-decoration layers.

Files touched:

- `raw/sources/2026-08-05-pice-ui-correction-bottom-tabs-background.md`
- `wiki/sources/pice-home-ui-direction.md`
- `wiki/projects/livelycura-pice-app.md`
- `index.md`
- `log.md`

Verification:

- Prettier, TypeScript, `git diff --check`, and a fresh Expo web export passed.
- Source search found no remaining runtime imports or renders of `BackgroundDecoration` or `PatternBackground`.
- The canonical vault validator was run after this correction.

## [2026-08-05] design | Establish The Pice Home UI Contract

What changed:

- Preserved the direct Pice home-screen direction and both supplied visual references as raw evidence.
- Recorded the CheckCity-independent home hierarchy, the Home/Menu/Orders plus detached-Cart navigation contract, header-only profile access, and provisional color status.
- Updated the Pice project page and vault index with the implemented design boundary and current verification state.

Files touched:

- `raw/sources/2026-08-05-pice-home-ui-direction.md`
- `raw/assets/2026-08-05-pice-home-ui-reference-1.jpg`
- `raw/assets/2026-08-05-pice-home-ui-reference-2.jpg`
- `wiki/sources/pice-home-ui-direction.md`
- `wiki/projects/livelycura-pice-app.md`
- `index.md`
- `log.md`

Verification:

- The Pice repository passed Prettier, TypeScript, and Expo web export; the export included all five generated food assets.
- The in-app browser blocked the local preview URL, so visual comparison remains pending rather than being reported as passed.
- The canonical vault validator was run after this focused update.

## [2026-08-04] setup | Bootstrap The LivelyCura Pice Food-Ordering App

What changed:

- Preserved the direct request to create Pice as a food-ordering brand distinct from CheckCity.
- Created the Pice project record with its Expo 57 stack, feature ownership, client identity, deployment boundaries, provisional brand state, and verification evidence.
- Indexed the directive Source Record and the new project page.

Files touched:

- `raw/sources/2026-08-04-pice-project-bootstrap-directive.md`
- `wiki/sources/pice-project-bootstrap-directive.md`
- `wiki/projects/livelycura-pice-app.md`
- `index.md`
- `log.md`

Verification:

- The Pice repository passed dependency installation, TypeScript, Prettier, Expo public-config evaluation, locally mapped dependency compatibility, web export, and a local HTTP 200 startup check.
- The independent Git repository is clean on `main` at root commit `56c4f7e` with no remote configured.
- The vault canonical validator was run after the focused update.

## [2026-08-02] correction | Make Call Center Root Category Filters Descendant-Aware

What changed:

- Corrected the selector convention: exact category matching uses `categoryIds`, while the root-category browser uses slug-backed `categoryPaths` so products assigned to children are included.
- Recorded the failed intermediate state where a root `_id` was valid but too narrow for root browsing.
- Updated the Call Center project page and vault index to reflect the corrected request semantics.

Files touched:

- `wiki/sources/call-center-product-category-filter-contract.md`
- `wiki/projects/call-center-web-app.md`
- `index.md`
- `log.md`

Verification:

- The focused category-filter regression and all 32 frontend tests passed.
- Frontend lint, TypeScript compilation, and the Vite production build passed.

## [2026-08-01] maintenance | Make Call Center Product Grid Panel-Responsive

What changed:

- Preserved the requested `base: 1`, `sm: 3`, `md: 3`, `lg: 4`, and `xl: 5` product-grid progression.
- Recorded that these breakpoints are evaluated against the draggable Products panel rather than the browser viewport.
- Linked the source evidence into the Call Center project page and vault index.

Files touched:

- `raw/sources/2026-08-01-call-center-product-grid-container-responsiveness.md`
- `wiki/sources/call-center-product-grid-container-responsiveness.md`
- `wiki/projects/call-center-web-app.md`
- `index.md`
- `log.md`

Verification:

- The focused container-query regression passed.
- Frontend lint and the Vite production bundle passed; the repository-wide TypeScript step remains blocked by the existing product-family test/export mismatch.

## [2026-08-01] maintenance | Record Call Center Category Filter Contract

What changed:

- Preserved the backend distinction between ID-backed `categoryIds` and slug-backed `categoryPaths` product filters.
- Recorded that the Call Center category selector uses category `_id` values and must clear the alternate path field.
- Linked the new source evidence into the Call Center project page and vault index.

Files touched:

- `raw/sources/2026-08-01-call-center-product-category-filter-contract.md`
- `wiki/sources/call-center-product-category-filter-contract.md`
- `wiki/projects/call-center-web-app.md`
- `index.md`
- `log.md`

Verification:

- The focused frontend category-filter regression passed.
- Frontend lint and the Vite production bundle passed; the repository-wide TypeScript step remains blocked by an unrelated existing product-family test/export mismatch.

## [2026-08-01] correction | Keep TypeScript Service Control Flow Explicit

What changed:

- Recorded that chained or nested conditional expressions must not orchestrate backend service workflows.
- Recorded that loading, validation, calculation, and document construction belong in documented, domain-owned helpers.
- Reinforced the existing typed data-object parameter convention.

Files touched:

- `raw/sources/2026-08-01-typescript-service-conditional-flow-decision.md`
- `wiki/sources/typescript-service-conditional-flow-decision.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Verification:

- Direct delivery-task creation-helper coverage passed 12 of 12 tests; the focused courier agreement, creation, and order-link set passed 74 of 74.
- The full backend command passed 615 unit files/3,110 tests and 50 integration files/344 tests.
- Backend TypeScript build and lint passed after the final test changes.

## [2026-07-31] correction | Group And Isolate Backend GraphQL Tests

What changed:

- Recorded that GraphQL tests live under their owning domain folder rather than as feature-specific files at the GraphQL test root.
- Recorded that backend unit tests must not read sibling frontend/mobile repositories that happen to exist in the local workspace.
- Recorded executable-schema and Shield-map contracts as the backend-owned courier and order-dispatch coverage boundary.

Files touched:

- `raw/sources/2026-07-31-livelycura-backend-graphql-test-organization-decision.md`
- `wiki/sources/livelycura-backend-graphql-test-organization-decision.md`
- `wiki/projects/livelycura-backend.md`
- `index.md`
- `log.md`

Verification:

- Focused courier and order-dispatch GraphQL tests passed 96 of 96.
- The formerly failing CI unit shard 2/4 passed 152 files and 696 tests.
- Backend lint and build passed.
- Vault validation was run after this update.

## [2026-07-31] maintenance | Record Bora Authentication And Wallet Security Redesign

What changed:

- Recorded canonical unique email/phone persistence, dual-channel signup ownership verification, phone/password plus email-OTP sign-in, and challenge-ID verification/resend.
- Recorded shared adaptive cooldowns, hashed signup-IP throttling, immutable wallet destinations, and resource-bound SMS verification for pending mobile-money wallets.
- Superseded stale claims about process-local-only throttling and unawaited post-readiness migrations; startup now fails closed before index creation, listening, and crons.

Files touched:

- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Verification:

- Fresh Bora `yarn run check` passed formatting, TypeScript, 83 test suites/396 tests, and the production dependency-audit gate.
- Repository `git diff --check` passed; live email/SMS delivery and deployment against legacy production data remain external checks.

## [2026-07-31] decision | Keep Missing-Price POS Products Visible But Unsellable

What changed:

- Recorded that the POS displays a missing facility price as zero instead of replacing it with an instructional message.
- Recorded that the cart action remains disabled until a persisted facility price exists.
- Preserved configured zero-price products as valid sellable products by distinguishing them through facility-price identity rather than numeric value.

Files touched:

- `raw/sources/2026-07-31-livelycura-pos-missing-price-decision.md`
- `wiki/sources/livelycura-pos-missing-price-decision.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `index.md`
- `log.md`

Verification:

- Confirmed `PosProductCard` displays zero, disables its cart action without a facility-price ID, and does not invoke the add callback from the disabled card.
- The focused `PosProductCard` suite passed 2 of 2 tests.

## [2026-07-31] repair | Preserve Bora Brand Text In Gmail iOS Dark Mode

What changed:

- Recorded that Gmail iOS full inversion changed light header/footer text to dark while the navy gradient remained fixed, producing unreadable dark-on-navy branding.
- Added the durable compatibility contract: the email body marker, Gmail-targeted selectors, navy gradient, and nested `screen`/`difference` blend wrappers must stay together.
- Limited the workaround to header/footer light text so existing light mode and the otherwise coherent dark content design remain unchanged.

Files touched:

- `wiki/projects/bora-capital-backend.md`
- `log.md`

Verification:

- Compared both user-supplied Gmail iOS screenshots with the compiled React Email output and confirmed the failure was full-invert text behavior, not responsive layout.
- Verified the Gmail compatibility regression red before implementation and green afterward.
- Confirmed compiled HTML retained two blend-wrapper pairs and the Gmail selector, and browser rendering introduced no black fallback blocks.
- Bora passed `yarn run check` with formatting, build, 70 suites/349 tests, and the production audit gate.
- Vault validation was run after this update.

## [2026-07-31] repair | Correct Bora Hubtel Gateway Mismatch

What changed:

- Corrected the durable Hubtel contract from `sms.hubtel.com` to the user-verified `smsc.hubtel.com` simple-message GET endpoint.
- Recorded that the failing and known-working requests differed in both hostname and Client ID even though their path and query-field shapes matched.
- Recorded that both gateways exist but produce distinct status-`100` responses, so they must not be treated as interchangeable.
- Preserved allowlisted provider diagnostics and removed temporary raw Axios console serialization that exposed credentials, recipient, and OTP content.

Files touched:

- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Verification:

- Used deliberately invalid probe credentials rather than replaying exposed live values or sending another SMS.
- Verified both endpoint and no-console-log regressions red before their fixes and green afterward.
- Bora passed the focused Hubtel test and `yarn run check` with formatting, build, 70 suites/348 tests, and the production audit gate.
- Vault validation was run after this update.

## [2026-07-31] repair | Preserve Legacy Order Reads After Remittance Field Addition

What changed:

- Recorded the failure cause: old delivery tasks returned `null` for the new non-null `cashRemittanceAmount`, which nulled the linked task and prevented ERP order reads.
- Recorded the no-migration compatibility rule: use the persisted amount when present, otherwise derive order-owned remittance from COD less delivery fee or default a manual task to full COD.

Files touched:

- `wiki/projects/livelycura-backend.md`
- `log.md`

Verification:

- Confirmed the exact GraphQL nullability error in the live backend log rather than attributing the page failure to the adjacent transient cron timeout.
- Added focused service and GraphQL field-resolver coverage and reran the backend build.
- Vault validation was run after this update.

## [2026-07-30] decision | Make Courier Remittance Receiver-Confirmed

What changed:

- Recorded that the rider never confirms their own cash handover: the courier provider confirms rider receipt, and the requesting business confirms direct or final receipt.
- Recorded separate `cashOnDeliveryAmount` and `cashRemittanceAmount` contracts; order-owned COD remits `order.total - order.deliveryFee`, leaving the delivery price with the rider.
- Recorded that Orders-only businesses confirm through entity-scoped `orders.update`, while Courier Mobile presents remittance as read-only pending/confirmed history.

Files touched:

- `wiki/projects/livelycura-backend.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/projects/livelycura-courier-mobile.md`
- `index.md`
- `log.md`

Verification:

- Reread the live project pages, index, and log immediately before the focused edits.
- Current backend, portal, and Courier Mobile implementations and focused tests were checked against the recorded boundary.
- Vault validation was run after this update.

## [2026-07-30] decision | Keep Courier Pickup Codes In Authorized ERP Views

What changed:

- Recorded that pickup verification codes are generated idempotently when an assigned route becomes ready and are not sent by SMS.
- Recorded that only authorized ERP order/task viewers can read the code, while rider and other clients receive no code.
- Recorded the presentation boundary: existing full-order details, the order pipeline drawer, and per-stop courier task routes show pending codes; Courier Mobile has no pickup resend action, while drop-off delivery remains separate.

Files touched:

- `wiki/projects/livelycura-backend.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/projects/livelycura-courier-mobile.md`
- `index.md`
- `log.md`

Verification:

- Reread the live project pages, index, and log immediately before the focused edits.
- Current backend, portal, and Courier Mobile implementations were checked against the recorded boundary.
- Vault validation was run after this update.

## [2026-07-30] maintenance | Record Hubtel Credential Rejection And Log Containment

What changed:

- Recorded that Hubtel HTTP 400/provider status `100` proves the simple-message request reached the provider but the supplied Messaging/SMS Client ID was not recognized.
- Recorded the required incident response: rotate the exposed pair, replace both staging values together, purge or restrict external log copies, redeploy, and run one controlled delivery without reusing leaked values.
- Recorded the code containment boundary: retain the current LivelyCura transport while logging only allowlisted error type/code, HTTP status, and provider status metadata—never the raw Axios error, credential-bearing URL, recipient, OTP, or message.

Files touched:

- `wiki/projects/bora-capital-backend.md`
- `log.md`

Verification:

- Reread the live Bora project page, index, and log immediately before the focused edits.
- Bora passed 17 focused notification tests and `yarn run check` with formatting, build, 70 suites/348 tests, and the production audit gate.
- Vault validation was run after this update.

## [2026-07-30] maintenance | Record Call Center Product Picker Fallback

What changed:

- Recorded that the opened catalog product, not any configured family sibling, determines whether the modal shows family-dimension options.
- Recorded the empty-`familyConfig` fallback to local size/preferences and the mixed-family regression case reported for Jollof Mini Bucket products.
- Corrected stale test-suite status: the focused product regression, lint, and build pass, but the current app-router test emits cross-realm `AbortSignal` rejections and keeps the full run nonzero despite passing assertions.

Files touched:

- `wiki/projects/call-center-web-app.md`
- `index.md`
- `log.md`

Verification:

- Reread the live project page, index, and log immediately before the focused edits.
- Repository verification passed the focused product test, lint, production build, and `git diff --check`; the isolated app test reproduced the unrelated full-suite blocker.
- Vault validation was run after this update.

## [2026-07-30] maintenance | Preserve Live References And Record Bora Notification Contracts

What changed:

- Strengthened the cross-project rule that a named live sibling implementation and newer user edits outrank earlier agent-authored code; agents must reread and compare the exact current reference before editing.
- Recorded Bora's shared React Email Tailwind layout, explicit dark-mode palette and navy anti-inversion fallback for email headers/footers.
- Recorded the LivelyCura-compatible Hubtel simple-SMS GET/query contract and the requirement to keep credential-bearing URLs and raw request errors out of logs.

Files touched:

- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Verification:

- Reread the live manual, Bora project page, index, and log immediately before the focused edits.
- Bora verification passed 14 focused notification tests, compiled HTML dark-mode inspection, build, formatting, 70 full suites/348 tests, and the production audit gate; live Hubtel staging delivery remains unexercised locally.
- Vault validation was run after this update.

## [2026-07-29] maintenance | Record Call Center Account And Product UI Boundaries

What changed:

- Recorded separate feature ownership for agent-account UI and active-brand switching, plus the protected `/account` route and user-menu hierarchy.
- Recorded bounded scrolling for growing product choices, the accessible grid/list segmented control, and resilient active-brand logo rendering.
- Added authenticated mock-backed browser evidence for the account menu/page, logo fallback, twelve-size picker, and unauthenticated account redirect.

Files touched:

- `wiki/projects/call-center-web-app.md`
- `log.md`

Verification:

- Reread both live notes immediately before the focused edits.
- Repository verification passed with 22 tests, lint, production build, and `git diff --check`; browser smoke checks exercised the changed UI without JavaScript errors.
- Vault validation was run after this update.

## [2026-07-29] maintenance | Record Call Center Multi-Brand Account Boundary

What changed:

- Recorded the self-scoped account query, suspended-brand limbo gate, same-token tenant switching, and local/server logout behavior.
- Established explicit tenant arguments and tenant-isolated query keys for shared catalog reads including family variants, plus cart/filter/query-cache invalidation and authenticated-layout remounting after a switch.
- Recorded fail-closed reconciliation for ambiguous switch responses, fail-soft suspended-login preservation, complete error-screen logout cleanup, transport-level 401 propagation, and blocking unsuccessful self-read envelopes without recursive 403 refetch.
- Superseded the historical nonzero full-test result with current lint, 22-test, production-build, and unauthenticated browser verification evidence while retaining the unexercised authenticated staging boundary.

Files touched:

- `wiki/projects/call-center-web-app.md`
- `index.md`
- `log.md`

Verification:

- Reread the live project page, index, and log before the focused edits.
- Repository checks passed with `yarn lint`, `yarn test --run`, and `yarn build`; the local login route rendered without JavaScript errors.
- `python3 scripts/wiki_tool.py check` was run after the vault update.

## [2026-07-29] convention | Enforce One GraphQL Operation Per Hook

What changed:

- Established that each GraphQL operation hook owns exactly one query, mutation, or subscription.
- Required separate hook files for separate operations, with composition at the screen or component boundary.
- Rejected hooks that combine queries, mutations, or subscriptions even when one feature consumes them together.

Files touched:

- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Verification:

- Reread the live manual, index, and log before the focused edits.
- `python3 scripts/wiki_tool.py check` passed after the update.

## [2026-07-29] convention | Replace Courier Task Polling With Lifecycle Events

What changed:

- Replaced the temporary polling guidance with an authorized, task-scoped GraphQL lifecycle subscription.
- Established one silent screen-focus refetch as the recovery path for missed events.
- Required task-detail loading skeletons to remain initial-load-only so OTP, proof, payment, and handover state stays mounted.

Files touched:

- `wiki/projects/livelycura-courier-mobile.md`
- `index.md`
- `log.md`

Verification:

- Reread the live project, index, and log before the focused edits.
- `python3 scripts/wiki_tool.py check` passed after the update.

## [2026-07-28] convention | Keep Courier Verification Stable During Synchronization

What changed:

- Recorded that task polling and refetching must preserve populated task content instead of showing the initial-loading skeleton.
- Established that OTP, proof, payment, and handover workflows remain mounted while task data synchronizes.
- Required nonessential task polling to pause while those rider inputs are active.

Files touched:

- `wiki/projects/livelycura-courier-mobile.md`
- `index.md`
- `log.md`

Verification:

- Reread the live project, index, and log before the focused edits.
- `python3 scripts/wiki_tool.py check` passed after the update.

## [2026-07-28] convention | Make System Provider Own Courier Rider Refresh

What changed:

- Recorded that authenticated rider mutations refetch and await the active `System` query.
- Established the System provider’s Redux user snapshot as the canonical rider state for Station status and task-action guards.
- Rejected feature-local availability state that can contradict the authenticated delivery agent.

Files touched:

- `wiki/projects/livelycura-courier-mobile.md`
- `index.md`
- `log.md`

Verification:

- Reread the live project, index, and log before the focused edits.
- `python3 scripts/wiki_tool.py check` passed after the update.

## [2026-07-28] convention | Tighten TypeScript And GraphQL Function Boundaries

What changed:

- Added the durable rule that related function parameters travel through one domain-owned typed data object rather than positional arguments.
- Added the GraphQL rule that root operations needing multiple client values expose one generated input-object argument and use generated resolver argument types.
- Added the boundary rule that domain services never receive `GraphqlContext`; GraphQL adapters extract and pass only the specific actor and scope values each service requires.
- Kept authorization and business logic in services behind thin resolvers.

Files touched:

- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Verification:

- Reread the live files before the focused edits and preserved existing entries.
- `python3 scripts/wiki_tool.py check` passed after the update.

## [2026-07-22] maintenance | Add Vault Command And Audit Tooling

What changed:

- Added `scripts/wiki_tool.py` as the unified entry point for canonical validation, advisory audit, and combined checks.
- Added a standard-library-only, read-only semantic/provenance audit with text, JSON, and explicit strict modes.
- Added an executable but inactive `.githooks/pre-commit` hook that runs the non-strict combined check when a user opts into `core.hooksPath`.
- Registered five automation files in schema v4 and connected command usage to the vault authority, workflows, lint checklist, local skills, index, and welcome page.

Files touched:

- `scripts/wiki_tool.py`, `scripts/audit_vault.py`, `scripts/validate_vault.py`, and `scripts/README.md`
- `.githooks/pre-commit`
- `AGENTS.md`, `welcome.md`, `index.md`, and `log.md`
- `schema/README.md`, `schema/workflows.md`, `schema/lint-checklist.md`, and `schema/vault-structure.json`
- `.agents/skills/vault-maintenance/SKILL.md` and `.agents/skills/llm-wiki-lint/SKILL.md`

Verification:

- `python3 scripts/wiki_tool.py check` passed canonical validation with five registered automation files and reported 11 advisory audit findings separately without modifying the vault.
- JSON output parsed, strict audit and strict combined modes exited 1 as documented, and the wrapper passed when invoked outside the vault root.
- The optional hook was executable and passed while `core.hooksPath` remained inactive.
- The read-only hash was unchanged across an audit run; `git diff --check` passed and no raw evidence changed.

## [2026-07-22] maintenance | Add Obsidian Graph Color Groups

What changed:

- Replaced the single schema-only graph group with nine folder-based color groups for projects, concepts, entities, questions, syntheses, Source Records, raw evidence, schema, and templates.
- Preserved the live graph's existing filter, display, force, zoom, orphan, and attachment settings.
- Linked the graph configuration from the maintenance section of `index.md` so the visual taxonomy is discoverable.

Files touched:

- `.obsidian/graph.json`
- `index.md`
- `log.md`

Verification:

- `jq` parsed the configuration and confirmed all nine expected group queries in order.
- `python3 scripts/validate_vault.py` passed with nine local skills, 63 of 63 raw sources covered, 56 of 56 Source Records indexed, and 885 checked wikilinks.
- `git diff --check` passed and no raw evidence changed.

## [2026-07-22] maintenance | Add LLM Wiki Operation Skills

What changed:

- Added repository-owned `llm-wiki-ingest`, `llm-wiki-query`, and `llm-wiki-lint` skills with generated `agents/openai.yaml` metadata.
- Kept `vault-maintenance` as the sole shared mutation and validation foundation; no competing maintenance skill was added.
- Registered all nine required local skills and documented the selection boundaries between ingest, query, lint, and maintenance.
- Linked each canonical operating workflow to its matching skill without moving authority out of `AGENTS.md` or `schema/`.

Files touched:

- `.agents/skills/llm-wiki-ingest/`, `.agents/skills/llm-wiki-query/`, and `.agents/skills/llm-wiki-lint/`
- `.agents/skills/README.md`, `AGENTS.md`, `index.md`, `welcome.md`, and `log.md`
- `schema/local-skills.md`, `schema/vault-structure.json`, and `schema/workflows.md`

Verification:

- The skill creator's `quick_validate.py` passed for all three skills; each generated `agents/openai.yaml` parsed and exposed the intended `$skill-name` default prompt.
- `python3 scripts/validate_vault.py` passed with nine validated local skills, 63 of 63 raw sources covered, 56 of 56 Source Records indexed, 96 wiki pages, and 885 checked wikilinks.
- Separate disposable-vault forward tests confirmed the ingest evidence/record/index/log chain, a read-only query, and a read-only lint report that separated structural validation from semantic findings.
- Local Markdown links resolved, the focused secret scan returned no findings, `git diff --check` passed, and no raw evidence changed.
- The unrelated `.obsidian/graph.json` change was preserved and excluded from this scoped commit; no push was performed.

## [2026-07-22] maintenance | Tighten Raw Evidence And Source Record Model

What changed:

- Kept `raw/sources/` as immutable evidence and retained `wiki/sources/` as the stable curated layer, now named Source Records throughout active navigation and operating guidance.
- Defined Source Records as concise provenance and retrieval nodes containing decision-relevant claims, connections, tensions, and questions rather than copies of exhaustive raw evidence.
- Applied the concision rule prospectively and to records when otherwise touched; no existing Source Record was bulk-rewritten.
- Added schema-v3 policy for required raw references, complete raw coverage, index connections, aggregation, shared evidence, and permitted direct raw citations.
- Extended the canonical validator to enforce the policy and report raw/source coverage counters.

Files touched:

- `AGENTS.md`, `welcome.md`, `index.md`, and `log.md`
- `_template/source-summary-template.md` and `.agents/skills/vault-maintenance/SKILL.md`
- Source-model documentation and policy under `schema/`
- `scripts/README.md` and `scripts/validate_vault.py`
- The source architecture, ingest/query/lint, Codex harvest, and first-ingest guidance pages

Verification:

- `python3 scripts/validate_vault.py` passed with 63 of 63 raw files covered, 56 of 56 Source Records indexed, 64 record-to-raw relationships, five aggregated records, one shared-evidence case, 96 wiki pages, and 885 checked wikilinks.
- Isolated temporary-vault tests correctly rejected an orphan raw file, a missing raw target, and an unindexed Source Record; a positive case also resolved a raw filename containing spaces. The temporary copies were removed afterward.
- Local Markdown links resolved, the focused secret-assignment scan returned no findings, and `git diff --check` passed.
- No file under `raw/sources/` changed; the concurrent `.obsidian/graph.json` change was preserved and excluded from this maintenance commit.

## [2026-07-22] maintenance | Correct Vault Operations Documentation Ownership

What changed:

- Moved the schema reference, workflow guidance, naming conventions, lint checklist, and local-skill documentation out of `wiki/concepts/` and into their canonical `schema/` ownership layer.
- Kept the six actual skill implementations under `.agents/skills/` and linked the schema-layer skill catalog directly to them.
- Registered all five schema documents in `schema/vault-structure.json` and extended the canonical validator to require both their files and exact `index.md` connections.
- Removed the five duplicate concept pages and updated the architecture, workflow overview, personal operating manual, scripts guide, skills catalog, and index to point to the canonical schema documents.
- Corrected the durable rule: vault additions belong in their canonical layer and must be indexed; being tracked in the wrong layer is insufficient.

Files touched:

- `AGENTS.md`, `index.md`, and `log.md`
- `schema/README.md`, `schema/workflows.md`, `schema/naming-conventions.md`, `schema/lint-checklist.md`, `schema/local-skills.md`, and `schema/vault-structure.json`
- `scripts/README.md` and `scripts/validate_vault.py`
- `.agents/skills/README.md`
- `wiki/concepts/raw-source-wiki-schema-architecture.md`, `wiki/concepts/ingest-query-lint-workflows.md`, and `wiki/syntheses/personal-operating-manual.md`
- Removed the five superseded `wiki/concepts/` operations-reference pages.

Verification:

- `python3 scripts/validate_vault.py` passed with 96 wiki pages, 885 checked wikilinks, five registered schema documents, five schema-document index links, six configured templates, and six validated local skills.
- All local Markdown links in the changed documentation resolved, the focused secret-assignment pattern scan returned no findings, and `git diff --check` passed.
- The concurrent `.obsidian/graph.json` change was preserved and excluded from this correction commit.

## [2026-07-22] maintenance | Add Vault Operations Reference Pages

What changed:

- Corrected the distinction between tracked repository infrastructure and first-class vault knowledge.
- Added five linked concept pages covering the vault schema, maintenance workflow, naming conventions, lint checklist, and project-local Agent Skills.
- Connected the detailed pages to the existing architecture and ingest/query/lint overview notes instead of creating competing ownership.
- Added all five pages to `index.md`, with schema and workflow guidance also exposed under Start Here and every requested topic exposed under Maintenance.
- Recorded the durable preference that “add to the vault” requires linked, indexed wiki content; tracked infrastructure files alone are insufficient.

Files touched:

- `wiki/concepts/vault-schema-reference.md`
- `wiki/concepts/vault-workflow-guide.md`
- `wiki/concepts/vault-naming-conventions.md`
- `wiki/concepts/vault-lint-checklist.md`
- `wiki/concepts/project-local-agent-skills.md`
- `wiki/concepts/raw-source-wiki-schema-architecture.md`
- `wiki/concepts/ingest-query-lint-workflows.md`
- `wiki/syntheses/personal-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Schema documentation, workflow guidance, naming rules, lint completion checks, and local-skill guidance are now visible and navigable as durable Obsidian knowledge, not only as repository implementation files.

Verification:

- `python3 scripts/validate_vault.py` passed with 101 wiki pages, 934 checked wikilinks, six configured templates, and six validated local skills.
- Git whitespace checks passed before commit review.
- A concurrent `.obsidian/graph.json` change was preserved but excluded from this maintenance commit.

Follow-ups:

- Consider automating orphan and duplicate-stem reporting only after the semantic rules are agreed.

## [2026-07-21] ingest | Frozen Non-Subagent Hermes Ledger Complete — 130/130

What changed:

- Classified the final ten populated non-subagent exact IDs: six default-profile Bora wallet/auto-top-up continuations, two misleadingly titled Bora backend records, and two generic-titled Altin Partner Mobile records.
- Closed the frozen non-subagent exact-ID ledger at 130/130; no direct exact IDs remain pending.
- Preserved three concise reports and created three schema-v2 source summaries with corrected project attribution.
- Promoted owner-scoped wallet/provider boundaries, canonical lookup and auto-top-up eligibility, Bora session/release closure, Altin Apps/module ownership, and shared-list-versus-feature ownership.
- Recorded remaining current tensions: ownerless internal auto-top-up fallback, Bora logger/deposit/email defects, deleted historical hardening plan, Altin empty-data shells, and inactive rejected generic module files.
- Kept the separate 90-record `source='subagent'` population explicitly unreconciled and did not start it automatically.

Files touched:

- Three immutable raw reports and three schema-v2 source summaries
- Bora backend and Altin Partner Mobile project pages
- Software-development manual, harvest-status synthesis, `index.md`, and `log.md`

Verification:

- Manual privacy review passed for all three preserved reports and three source summaries; no credentials, private payloads, transcript dumps, system prompts, environment values, or secret values were retained.
- An automated privacy-pattern script was blocked by execution consent and was not retried or bypassed.
- `python3 scripts/validate_vault.py` passed with 96 wiki pages, 885 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- No current project command, build, test, service, database mutation, migration, provider call, deployment, repository mutation, commit, push, or vault publication was performed centrally.

Follow-up:

- Reconcile the 90 frozen `source='subagent'` records against their parents only when explicitly resumed.

## [2026-07-21] ingest | Bora Quality And Deployment Closure 51–52

What changed:

- Classified the final two substantive coder-profile Bora continuations, advancing the frozen exact-ID ledger from 118 to 120 of 130 and leaving 10.
- Promoted exact closure for common-domain ownership, uppercase persisted enums plus migration, complete JSDoc/AST-backed checks, deliberate catch outcomes, and layered deployment evidence.
- Preserved the startup/migration race, current unchanged-rethrow violations, and exact-record boundary that #52 did not implement Sentry despite later dirty-tree Sentry source.
- Independently reconciled the final ten pending exact IDs twice; both methods returned the same three families.

Files touched:

- One immutable raw report and one schema-v2 source summary
- Bora backend project page
- Harvest-status synthesis, `index.md`, and `log.md`

Verification:

- `python3 scripts/validate_vault.py` passed with 93 wiki pages, 863 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- No current project command, build, test, service, database mutation, migration, provider call, deployment, repository mutation, commit, push, or vault publication was performed centrally.

Follow-up:

- Audit the final six default Bora, two Partner Mobile Setup, and two Casual Greeting/Altin continuations.

## [2026-07-21] ingest | Bora Runtime And Payment Safety 36–50 — Fast Mode

What changed:

- Classified fifteen consecutive substantive Bora records, advancing the frozen exact-ID ledger from 103 to 118 of 130 and leaving 12.
- Merged three concise reports into one source covering runtime restoration, scoped filter sanitization, BCL/Paystack transaction boundaries, webhook inboxes, reconciliation, session families, and enum/interface ownership.
- Preserved reversed control-removal work, rejected GO claims, the current successful-finalization state-guard regression, and the missing BCL idempotency/status-lookup dependency.
- Added one reusable scoped-filter-sanitization rule.
- Continued in fast durable-knowledge mode without replay arithmetic or exhaustive intermediate-test timelines.

Files touched:

- Three immutable raw reports and one schema-v2 source summary
- Bora backend project page and software-development manual
- Harvest-status synthesis, `index.md`, and `log.md`

Verification:

- `python3 scripts/validate_vault.py` passed with 92 wiki pages, 855 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- No current project command, build, test, service, database mutation, migration, provider call, deployment, repository mutation, commit, push, or vault publication was performed centrally.

Follow-up:

- Audit final Bora continuations `20260718_035439_fd6fd5` and `20260718_042843_74753d`, then regenerate the remaining ten candidates.

## [2026-07-21] ingest | Bora Authentication And Session Hardening 21–35 — Fast Mode

What changed:

- Classified fifteen consecutive substantive Bora records, advancing the frozen exact-ID ledger from 88 to 103 of 130 and leaving 27.
- Merged three concise reports into one source covering hash-only OTPs, atomic attempts, transactional login, rejected challenge IDs, refresh rotation, JWT constraints, secret hygiene, and structured redaction.
- Preserved unresolved operator obligations for likely historical credentials and the non-transactional password-reset/session-family revocation boundary.
- Added one reusable rule requiring every transport for one security operation to delegate to one owning service with transport-level regression coverage.
- Continued in fast durable-knowledge mode without replay arithmetic or exhaustive intermediate-test timelines.

Files touched:

- Three immutable raw reports and one schema-v2 source summary
- Bora backend project page and software-development manual
- Harvest-status synthesis, `index.md`, and `log.md`

Verification:

- `python3 scripts/validate_vault.py` passed with 91 wiki pages, 846 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- No current project command, build, test, service, database mutation, migration, provider call, deployment, repository mutation, commit, push, or vault publication was performed centrally.

Follow-up:

- Continue the verified Bora lineage from `20260717_160904_8adba5` in grouped fast mode.

## [2026-07-21] ingest | Bora Security Hardening Continuations 6–20 — Fast Mode

What changed:

- Classified fifteen consecutive substantive Bora records, advancing the frozen exact-ID ledger from 73 to 88 of 130 and leaving 42.
- Merged three concise audit reports into one source covering principal-bound GraphQL contracts, wallet/provider credential isolation, resolver/service ownership, financial notification isolation, and purpose-aware recovery.
- Preserved historical/current contradictions around wallet key rotation, plaintext credential migration, challenge-index rollout, challenge identity, and process-local rate limiting.
- Added one non-duplicate general communication rule: define necessary abbreviations and project-local shorthand at first use.
- Continued in fast durable-knowledge mode without replay arithmetic or exhaustive intermediate-test timelines.

Files touched:

- Three immutable raw reports and one schema-v2 source summary
- Bora backend project page and software-development manual
- Harvest-status synthesis, `index.md`, and `log.md`

Verification:

- `python3 scripts/validate_vault.py` passed with 90 wiki pages, 837 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- No current project command, build, test, service, database mutation, migration, provider call, deployment, repository mutation, commit, push, or vault publication was performed centrally.

Follow-up:

- Continue the verified Bora lineage from `20260716_171024_ddce8b` in grouped fast mode.

## [2026-07-21] ingest | Bora Canonical Identity And Authorization Chain

What changed:

- Classified four replay-heavy substantive Bora continuations, advancing the frozen exact-ID ledger from 69 to 73 of 130 and leaving 57.
- Attributed canonical-ID completion, owner-scoped auto-top-up cancellation, principal-bound deposit initialization, public/internal wallet contract separation, and principal-bound investment-account lookup to their exact records.
- Preserved that deposit Fix 17 closes only in the fourth record and that all test/build/codegen counts are historical session outcomes rather than current verification.
- Updated Bora backend/mobile provenance without duplicating operating-manual rules already present.
- Paused further full-message forensic harvesting after user feedback about duration; no successor batch was started.

Files touched:

- One immutable raw report and one schema-v2 source summary
- Bora backend and mobile project pages
- Harvest-status synthesis, `index.md`, and `log.md`

Verification:

- `python3 scripts/validate_vault.py` passed with 89 wiki pages, 828 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- No project command, build, test, service, database mutation, migration, provider call, deployment, repository mutation, commit, push, or vault publication was performed centrally.

Follow-up:

- Await explicit direction to stop permanently or resume in faster durable-knowledge-only mode.

## [2026-07-21] ingest | Standalone Scope Correction Ownership And ID-Collision Fix

What changed:

- Classified default records `20260721_155121_9e9cc3` and `20260721_162605_759657`, advancing the frozen exact-ID ledger from 67 to 69 of 130 and leaving 61.
- Classified the default cleanup body of `20260721_164555_84be3a` inside a store-qualified composite with +0 exact-ID increment because a different populated coder body under the same ID was already classified.
- Attributed unsupported Standalone writes and the correction request to `155121`, corrective writes and explicitly approved deletions to `162605`, and final log/validation closure to the default `164555` body.
- Corrected active sources so MovieFlix and GoAPI remain placeholders while Let’s Ride is active from later direct Hermes evidence.
- Reframed the 130 denominator as a frozen exact-ID ledger rather than a guaranteed physical-conversation count.
- Preserved all immutable raw manifests and superseded log evidence; restored no deleted page or repository-only rule.

Files touched:

- One immutable raw report and one schema-v2 source summary
- Coverage, scope-correction, Standalone, no-cwd, and Portfolio source summaries
- Harvest-status synthesis, `index.md`, and `log.md`

Verification:

- Direct read-only SQLite checks confirmed coder/default `20260721_164555_84be3a` are different populated bodies with 137 and 103 messages respectively.
- `python3 scripts/validate_vault.py` passed with 88 wiki pages, 818 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- No project command, build, test, service, database mutation, migration, provider call, deployment, repository mutation, commit, push, or vault publication was performed centrally.

Follow-ups:

- Regenerate the pending candidate list from the frozen manifest using store-qualified collision checks.
- Design a future composite-identity recount without silently changing the frozen denominator.

## [2026-07-21] ingest | Portfolio Integration And CompFlow Auth/Payroll/RBAC

What changed:

- Classified seven verified records and advanced coverage from 60 to 67 of 130, leaving 63.
- Resolved Portfolio Batch 1 integration ownership to `20260721_113041_3f113d`; classified `20260721_150209_773080` as interrupted unrelated Standalone reconnaissance with no write/validation closure.
- Classified five CompFlow Backend Authentication continuations, including #6 as a human-intent shell carrying meaningful execution/verification for #5.
- Promoted customer-driven onboarding, Moolre/Paystack provider separation, dual-channel OTP success semantics, mocked-versus-live evidence boundaries, payroll/minor-unit/lifecycle architecture, modular correction, service ownership, RBAC/Shield, and organization lifecycle.
- Preserved unresolved Moolre default, allow-fallback Shield dependency, four retained legacy payroll files, stale Admin contract, and missing final #6 rerun.
- Added reusable provider-test, multi-channel notification, and authorization-map coverage rules to both operating manuals.

Files touched:

- Two immutable raw reports and two schema-v2 source summaries
- Portfolio and CompFlow source/project pages
- Software and bootstrap operating manuals
- Harvest-status synthesis, `index.md`, and `log.md`

Verification:

- `python3 scripts/validate_vault.py` passed with 87 wiki pages, 800 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- No project command, build, test, service, database mutation, migration, provider call, deployment, application-repository mutation, commit, push, or vault publication was performed centrally.

Follow-ups:

- Audit Standalone correction chain `20260721_155121_9e9cc3` → `20260721_162605_759657` → `20260721_164555_84be3a`.
- Regenerate the remaining candidate list from the frozen manifest with exact session/message verification.

## [2026-07-21] ingest | Reconciliation Closure And Invalid Locator Correction

What changed:

- Classified two valid default-profile records and advanced coverage from 58 to 60 of 130, leaving 70.
- Attributed successful focused C.E.Q.A reconciliation closure to `20260721_032543_0fdcc0` without assigning schema/template or underlying Codex ownership.
- Recorded `20260721_112003_2f277e` as interrupted Portfolio reconnaissance with no integration; its direct successor is the Portfolio write-ownership candidate.
- Directly verified seven selector-supplied IDs against coder and default stores. All had zero session and message rows, are outside the denominator, and contribute +0 coverage.
- Replaced the invalid Backend Auth targets with the verified CompFlow Backend Authentication Setup continuations #2–#6.
- Confirmed no live title match for “Hermes Workspace Memory Setup”; no memory/bootstrap ownership was reassigned.

Files touched:

- Three immutable raw audit reports and two schema-v2 source summaries
- Prior vault-reconciliation source summary
- Harvest-status synthesis
- `index.md` and `log.md`

Verification:

- Direct read-only SQLite checks confirmed all seven selector-supplied locators had zero session and message rows in both coder and default stores.
- Direct title and exact-ID queries confirmed the corrected CompFlow chain and both default Portfolio successors are populated and lineaged.
- `python3 scripts/validate_vault.py` passed with 85 wiki pages, 777 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- No project build, test, service, database mutation, migration, provider, deployment, or native runtime was executed centrally.

Follow-ups:

- Audit default Portfolio successors `20260721_113041_3f113d` and `20260721_150209_773080`.
- Audit verified CompFlow auth continuations `20260711_221940_e79205` through `20260712_155404_4a08ff`.

## [2026-07-21] ingest | Harvest Vault Reconciliation, Product/MLS, And CompFlow Stack

What changed:

- Classified ten unique non-subagent records: one interrupted process-control continuation, five substantive Product/MLS/stock records, and four substantive CompFlow continuations.
- Advanced coverage from 48 to 58 of 130, leaving 72.
- Resolved the unanswered Product lab badge request while preserving current Products-table supersession and missing browser acceptance.
- Promoted item-driven stock/non-stock behavior, BOM-backed bundles, derived purpose, UOM-aware relief, and exact return identity as earlier provenance under the later movement-ledger contract.
- Added the apparent pure-bundle BOM creation guard conflict as an explicit current static tension.
- Promoted CompFlow Client Portal creation, database-managed plans, Apollo feature ownership, fake-contract removal, record-derived tenant scoping, and the registered developer-role migration.
- Preserved current CompFlow contradictions: migrations are not awaited/fail-closed, Admin still queries removed `adminOverview`, plan management is absent, and Atlas health is unknown.
- Recorded that `20260721_031558_72a825` did not integrate C.E.Q.A/Altin or author schema v2; its direct successor remains pending classification.

Files touched:

- Three immutable raw reports and three focused source summaries
- LivelyCura Backend and Pharmacy Portal project pages
- All four CompFlow project pages
- Prior Portfolio/LivelyCura and vault-continuation source summaries
- Software-development, new-project-bootstrap, and harvest-status syntheses
- `index.md` and `log.md`

Verification:

- `python3 scripts/validate_vault.py` passed with 83 wiki pages, 762 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- The first validation correctly rejected three nonconforming source-summary heading sets; all three were aligned to schema v2 and validation was rerun successfully.
- Repository reconciliation remained static/read-only; no project build, test, service, database, provider, migration, deployment, or native runtime was executed centrally.

Follow-ups:

- Audit default records `20260721_032543_0fdcc0` and `20260721_112003_2f277e`, then Backend Auth Flow chain `20260713_201517_37251f` onward.

## [2026-07-21] ingest | Harvest Vault Reconnaissance, Courier, Portfolio Skills, And MLS Tail

What changed:

- Classified seven unique non-subagent records: one interrupted process-control reconnaissance, two substantive Courier records, and four substantive mixed Portfolio/LivelyCura records.
- Advanced coverage from 41 to 48 of 130, leaving 82.
- Promoted exact sibling implementation transfer, Courier-owned OTP adaptation, restored flat navigation, mounted-layer color normalization, and rounded-border overlays.
- Attributed the accepted equal-card Swiper baseline, six-group Skills foundation, current Skills motion, Featured Projects hover interaction, and background polish to their exact Portfolio records.
- Promoted only the replay-heavy child’s unique LivelyCura MLS-sale fallback and test closure; replayed Portfolio context was not promoted twice.
- Recorded that the default-profile continuation performed reconnaissance only and did not integrate C.E.Q.A Batch 3 or own the six-template/direct-project schema.
- Corrected the stale software-manual statement that Let’s Ride remained only a provenance placeholder.

Files touched:

- Three immutable raw reports and three focused source summaries
- Courier Mobile, Portfolio Client Portal, LivelyCura Backend, and Pharmacy Portal project pages
- Prior Portfolio and vault-continuation source summaries
- Software-development and harvest-status syntheses
- `index.md` and `log.md`

Verification:

- `python3 scripts/validate_vault.py` passed with 80 wiki pages, 731 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- Repository reconciliation remained static/read-only; no project build, test, service, database, provider, migration, deployment, or native runtime was executed centrally.

Follow-ups:

- Audit default successor `20260721_031558_72a825` and the Product Lab Badge/MLS chain beginning `20260624_123800_8292b3`.

## [2026-07-21] ingest | Harvest Vault Validation, Ride/LivelyCura, And Portfolio Featured Projects

What changed:

- Classified eight unique non-subagent records: one process-control vault continuation, four substantive Ride-titled Let’s Ride/LivelyCura records, two substantive Portfolio Featured Projects records, and one Portfolio replay-only shell.
- Advanced coverage from 33 to 41 of 130, leaving 89. The replay shell contributes no knowledge but counts as fully classified.
- Replaced the Let’s Ride placeholder with direct-Hermes-backed foundation architecture, canonical identity, deliberate domain exclusions, and explicit Mongo/runtime/test/deployment gaps.
- Added earlier direct implementation provenance to LivelyCura’s product-level sale lines, exact COGS, movement-based returns/rollback, migrations, interface ownership, and CI closure without duplicating later canonical rules.
- Added Portfolio Featured Projects architecture, repeated design correction, parent import failure, child import repair, current Swiper supersession, and unresolved visual acceptance.
- Preserved that the vault child validated the inherited five-template transitional model but did not own the later six-template/direct-project schema or complete its reconnaissance harvest.

Files touched:

- Three immutable raw reports and three focused source summaries
- Let’s Ride Backend, LivelyCura Backend, and Portfolio Client Portal project pages
- Existing Portfolio and vault-infrastructure source summaries
- Harvest-status synthesis, `index.md`, and `log.md`

Verification:

- `python3 scripts/validate_vault.py` passed with 77 wiki pages, 703 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- Current repository reconciliation remained static/read-only; no project build, service, database, provider, migration, deployment, or native runtime was executed centrally.

Follow-ups:

- Audit default-profile successor `20260721_030948_da545b` and continue ordinary non-subagent classification.

## [2026-07-21] ingest | Harvest Stock/Sales 3, Vault Infrastructure, And GraphQL/Bora Chain

What changed:

- Classified four unique non-subagent records: Stock/Sales #3, one default-profile vault continuation, and two substantive GraphQL/Bora records.
- Advanced coverage from 29 to 33 of 130, leaving 97.
- Promoted final historical full-suite reporting, defensive migration diagnostics, Product non-null data repair, unique Pharmacy menu registration, and real Bora portfolio subaccounts with dedicated settlement metadata.
- Added reusable cautions for provider-side-effect migrations: once-after-success is not exactly-once; use stable keyed mapping, provider idempotency, partial-failure reconciliation, redacted output, and rerun tests.
- Added the direct communication correction to disagree plainly when technical reasoning warrants it.
- Preserved unresolved boundaries: LivelyCura startup still swallows migration failures, exact-session vault validation did not pass before compression, and real Paystack provisioning did not complete.

Files touched:

- Three immutable raw reports and three focused source summaries
- Two predecessor source summaries
- LivelyCura Backend, Pharmacy Portal, and Bora Capital Backend project pages
- Personal, software-development, bootstrap, and harvest-status syntheses
- `index.md`
- `log.md`

Verification:

- `python3 scripts/validate_vault.py` passed with 74 wiki pages, 674 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- Current repository reconciliation remained static/read-only; no project build, provider call, migration, deployment, or native runtime was executed centrally.

Follow-ups:

- Audit default-profile successor `20260721_020029_f66b3b` and identify the separate Ride Ordering Backend chain.

## [2026-07-21] ingest | Harvest Stock/Sales And Bootstrap Continuations

What changed:

- Classified `20260629_193407_346702` as a substantive child continuation and `20260721_001007_1b1aea` as process-control with independent workflow outcomes after replay de-duplication.
- Advanced unique non-subagent coverage from 27 to 29 of 130, leaving 101.
- Promoted exact-cost fixture closure, sale-return identity/index/data/API/client migration, and accepted startup-safe optional native-module loading.
- Preserved historical verification boundaries: the first record compressed before final full-suite reporting, and native runtime was not rebuilt/exercised.
- Added execution provenance for the initial bounded Codex-harvest/bootstrap artifacts and public-vault Git publication while preserving that full archive ingestion remained incomplete.
- Directly verified that requested Portfolio locator `20260627_145719_58520f` is absent from both live stores and the frozen manifest; it was excluded from coverage and promoted no claim.

Files touched:

- Two immutable raw reports and two focused source summaries
- `wiki/sources/hermes-no-cwd-process-triage-batch-1.md`
- `wiki/sources/livelycura-stock-sales-hermes-supplement-1.md`
- `wiki/projects/livelycura-backend.md`
- `wiki/projects/serlp-mobile.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/concepts/codex-project-knowledge-harvest.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Verification:

- `python3 scripts/validate_vault.py` passed with 71 wiki pages, 631 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- Live-store verification confirmed the rejected Portfolio locator is absent from coder/default stores and the frozen manifest.

Follow-ups:

- Process direct successors `20260712_183956_816de0` and `20260721_013536_83fcd9` next.

## [2026-07-21] ingest | Complete No-CWD/Home Hermes Batch 1

What changed:

- Integrated five exact no-cwd/home conversation reports from the bounded read-only agent batch.
- Classified three substantive/process records and two duplicates/reference-only records, advancing unique non-subagent coverage from 22 to 27 of 130 and leaving 103.
- Promoted LivelyCura stock/sales knowledge: one active product line per sale, `saleItemId` return identity, exact `lineCost` COGS, compatible stock flags, and runner-owned production migrations.
- Promoted Call Center cached-location operations, provider-session token lifecycle, coordinate naming, estimate normalization, and tooling provenance while preserving the unsupported direct-payment mutation-field claim.
- Mapped the engineering-partner, audit-correction, and shared-brain parent records to existing canonical pages without duplicating knowledge.

Files touched:

- Three immutable raw evidence reports and three focused source summaries
- `wiki/projects/livelycura-backend.md`
- `wiki/projects/serlp-mobile.md`
- `wiki/projects/call-center-web-app.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Verification:

- `python3 scripts/validate_vault.py` passed with 69 wiki pages, 602 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- Current project reconciliation remained static/read-only; no repository command was executed during centralized integration.

Follow-ups:

- Process direct child continuations `20260629_193407_346702` and `20260721_001007_1b1aea` before broader ordinary-session triage.

## [2026-07-21] ingest | Harvest Generalized Skills And Courier Recovery Session

What changed:

- Classified coder-profile session `20260622_115444_d37ddc` as substantive.
- Captured the correction that exact project skills and generalized backend/frontend-web/frontend-mobile skills are complementary layers, with source inventories preserving provenance.
- Verified the current active profile exposes the historical generalized baseline and later web additions.
- Promoted Courier Mobile’s minimum-consumer-contract recovery rule and verified the current three-file radii design-system structure.
- Patched the reusable project-skill-import workflow with an explicit cross-project synthesis path.
- Advanced unique non-subagent coverage from 21 to 22 of 130, leaving 108.

Files touched:

- One raw report and one source summary for this session
- `wiki/projects/livelycura-courier-mobile.md`
- `wiki/syntheses/personal-operating-manual.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- Active `project-skill-library-import` skill
- `index.md`
- `log.md`

Verification:

- `python3 scripts/validate_vault.py` passed with 66 wiki pages, 572 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- Current skill discovery returned six backend, eight frontend-web, and six frontend-mobile skills; current Courier source contains the three-file radii design-system contract.

Follow-ups:

- Integrate the five no-cwd/home reports and continue ordinary continuation chains.

## [2026-07-21] ingest | Harvest LivelyCura Skills, Keks, And Pharmacy Hermes Chain

What changed:

- Classified coder-profile sessions `20260621_010814_92d057` and `20260621_024824_d0e17a` as substantive.
- Recovered the exact 42-skill LivelyCura import workflow and original Keks Chakra v3 report-log fix.
- Preserved the Pharmacy Portal failure history: false first completion, direct user correction, regex corruption, manual restoration, and limited historical verification.
- Reconciled current Pharmacy source: ten matching components import prop contracts from `../interfaces` and use explicit `React.FC<...>` declarations.
- Promoted the reusable rule that every touched file must be reread and relevant checks run; cached/tool-success output and regex bulk edits are not completion proof.
- Advanced unique non-subagent coverage from 19 to 21 of 130, leaving 109.

Files touched:

- One raw report and one source summary for this chain
- `wiki/projects/keks-admin-portal.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Verification:

- `python3 scripts/validate_vault.py` passed with 65 wiki pages, 558 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- Current static Pharmacy inspection found ten matching `testRequestDetails` components importing prop contracts from `../interfaces` and using `React.FC<...>`.

Follow-ups:

- Integrate the five no-cwd/home reports and continue the remaining ordinary continuation chains.

## [2026-07-21] ingest | Classify Hermes Short Shell Batch 1

What changed:

- Read three exact two-message coder-profile records directly from the Hermes state store.
- Classified two repeated Keks Chakra v3 completed-fix summaries as reference-only/duplicate and one Portfolio undo request as interrupted with no outcome.
- Added one sanitized raw report and source summary; no project page changed because the Keks rule already existed and the Portfolio request lacked a completed action.
- Advanced unique non-subagent coverage from 16 to 19 of 130, leaving 111 conversations before source-marked subagent triage.

Files touched:

- `raw/sources/2026-07-21-hermes-short-shell-triage-batch-1.md`
- `wiki/sources/hermes-short-shell-triage-batch-1.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Verification:

- `python3 scripts/validate_vault.py` passed with 64 wiki pages, 545 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.

Follow-ups:

- Integrate the five no-cwd/home reports now in progress, then process ordinary continuation chains.

## [2026-07-21] correct | De-duplicate Hermes Coverage Denominator

What changed:

- Reconciled the immutable 225-row audit manifest by exact session ID across coder/default stores.
- Corrected the active interpretation from 132 non-subagent store records to 130 unique non-subagent conversations; five IDs occur in both stores, and three empty coder aliases resolve to populated default conversations.
- Preserved 90 unique `source='subagent'` conversations. Clarified that `parent_session_id` also links ordinary CLI/TUI/Desktop continuations and cannot define subagent status.
- Corrected active coverage from 16 of 132 with 116 remaining to 16 of 130 with 114 remaining. Historical log entries remain unchanged and are superseded by this correction.
- Started a bounded read-only classification of all five no-cwd/home conversations.

Files touched:

- `wiki/sources/hermes-session-coverage-audit-2026-07-21.md`
- `wiki/syntheses/personal-operating-manual.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- Coverage now counts unique user-facing conversation IDs rather than physical store rows and preserves ordinary continuation chains for classification.

Verification:

- `python3 scripts/validate_vault.py` passed with 63 wiki pages, 538 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- Focused active-wiki search found no stale `16 of 132`, `116 primary`, or `131-primary` coverage claims.

Follow-ups:

- Integrate the five no-cwd/home evidence reports, then process the remaining ordinary continuation chains before source-marked subagent triage.

## [2026-07-21] ingest | Harvest Hermes Explicit-Project-CWD Batch 1

What changed:

- Classified 15 previously unprocessed primary Hermes sessions from the coder/default SQLite stores: 13 substantive and two interrupted.
- Added three sanitized raw evidence reports and source summaries for C.E.Q.A/Altin, CompFlow/CheckCity, and Kusantec/Bora without copying transcripts, tool chatter, secrets, private payloads, screenshots, or environment values.
- Added direct Hermes provenance to Altin, Keks, four CompFlow surfaces, CheckCity, and Bora Backend; left Call Center and Bora Mobile unchanged where the exact records supported no new implementation claim.
- Corrected the earlier limited-search claim that no direct C.E.Q.A Hermes implementation session existed.
- Promoted only durable cross-project rules: saved-skill references are file-level checklists, principal identity overrides caller identity, provider-backed reads require ownership checks, and a question is not authorization to edit.
- Advanced the canonical checkpoint from one to 16 of 132 directly classified primary Hermes sessions, leaving 116 primary sessions before parent-aware subagent triage.

Files touched:

- Three raw evidence reports under `raw/sources/`
- Three source summaries under `wiki/sources/`
- `wiki/projects/altin-partner-mobile.md`
- `wiki/projects/keks-admin-portal.md`
- `wiki/projects/compflow.md`
- `wiki/projects/compflow-admin.md`
- `wiki/projects/compflow-client-portal.md`
- `wiki/projects/compflow-backend.md`
- `wiki/projects/livelycura-check-city-app.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/sources/ceqa-altin-project-knowledge-harvest-batch-3.md`
- `wiki/syntheses/personal-operating-manual.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- Direct Hermes evidence now materially contributes to the project pages instead of remaining in temporary session storage, while archive-specific counts and current-versus-historical boundaries remain explicit.

Verification:

- `python3 scripts/validate_vault.py` passed with 63 wiki pages, 538 resolved wikilinks, six configured templates, and all six template-index links.
- `git diff --check` passed.
- Focused stale-claim search found only the intentionally historical “before the audit” statement in the Personal Operating Manual; the active C.E.Q.A absence claim is corrected.
- Repository reconciliation remained read-only. No project build, test, API, provider, database, migration, deployment, or Git-history mutation was performed.

Follow-ups:

- Classify the remaining 116 primary Hermes sessions by actual request/outcome, prioritizing no-cwd records, then triage subagents against their parents.

## [2026-07-21] maintenance | Audit Missing Hermes Conversation Coverage

What changed:

- Audited the coder and default Hermes SQLite session stores read-only after the user challenged the claimed shared-brain coverage.
- Added an immutable metadata-only manifest covering 225 records while excluding message bodies, system prompts, tool payloads, secrets, and private identifiers.
- Recorded 132 primary sessions with user messages, 90 subagent sessions requiring duplicate triage, and only one previously documented direct Hermes project-session promotion.
- Corrected the operating model: the same model, stored session history, profile memory, Codex evidence, and repository inspection do not automatically integrate Hermes knowledge into Obsidian.
- Made substantive Hermes-session evaluation or exact-ID checkpointing an explicit vault rule and started bounded read-only evidence reviews for 15 previously unprocessed explicit-project-cwd sessions.

Files touched:

- `AGENTS.md`
- `raw/sources/2026-07-21-hermes-session-coverage-audit.md`
- `wiki/sources/hermes-session-coverage-audit-2026-07-21.md`
- `wiki/concepts/hermes-obsidian-memory-architecture.md`
- `wiki/syntheses/personal-operating-manual.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- The vault now states the real coverage boundary and carries a resumable Hermes backlog instead of implying that Codex-heavy project pages equal Hermes-history completion.

Verification:

- `python3 scripts/validate_vault.py` passed with 60 wiki pages, 494 checked wikilinks, six configured templates, and all six template-index links.
- Focused scanning of the nine touched audit, source, operating, index, schema, and log files found no private-key blocks, bearer values, credential-bearing database URIs, assigned secret values, or email addresses.
- `git diff --check` passed. The vault already contained substantial unrelated/uncommitted knowledge-base work; this operation did not alter project repositories or Git history.

Follow-ups:

- Reconcile and promote the 15 explicit-project-cwd session reports, then classify the 131-primary-session backlog and triage subagents against their parents.

## [2026-07-21] correct | Retract Repository-Only Conversation-Harvest Claims

What changed:

- Captured the user's direct Hermes correction that a Hermes-conversation harvest requires direct Hermes conversation evidence; filesystem or Git-root discovery may verify conversation-derived claims but cannot independently create them.
- Permanently deleted the unsupported Magical Goodall, mywork Git History Generator, Playground, and Portfolio Mock-up Prototype project pages.
- Replaced the old `cando-backend.md` page with the user-confirmed [[wiki/projects/lets-ride-backend|Let's Ride Backend]] name and reduced it to a provenance-review placeholder.
- Reduced MovieFlix Mobile and GoAPI to identifier-only provenance-review placeholders; removed repository-derived stack, architecture, command, runtime, and convention claims.
- Marked Standalone Projects batch 1 superseded, retracted the false 30-Git-root completion boundary, and removed the unsupported package-script safety rule from both development manuals.
- Added the requested-archive provenance rule to `AGENTS.md`, the Personal Operating Manual, the software-development manual, the harvest checkpoint, and the Codex harvest procedure.
- Preserved immutable raw manifests and prior log entries as an audit trail rather than rewriting history.

Files touched:

- `AGENTS.md`
- `raw/sources/2026-07-21-hermes-conversation-harvest-scope-correction.md`
- `wiki/sources/hermes-conversation-harvest-scope-correction.md`
- `wiki/sources/standalone-projects-project-knowledge-harvest-batch-1.md`
- `wiki/sources/portfolio-project-knowledge-harvest-batch-1.md`
- `wiki/sources/kusantec-bora-project-knowledge-harvest-batch-1.md`
- `wiki/projects/movieflix-mobile.md`
- `wiki/projects/go-api.md`
- `wiki/projects/lets-ride-backend.md`
- Deleted: `wiki/projects/magical-goodall.md`, `wiki/projects/mywork-git-history-generator.md`, `wiki/projects/playground.md`, `wiki/projects/portfolio-mockup-prototype.md`, and `wiki/projects/cando-backend.md`
- `wiki/concepts/codex-project-knowledge-harvest.md`
- `wiki/syntheses/personal-operating-manual.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- Conversation-harvest provenance is now archive-specific: no project page or durable claim may be promoted from repository discovery alone, and Let's Ride Backend is the canonical project name.

Verification:

- `python3 scripts/validate_vault.py` passed with 59 wiki pages, 481 checked wikilinks, six configured templates, and all six template-index links.
- Focused link search found zero active wikilinks to the five removed paths.
- Focused filename search found only `wiki/projects/lets-ride-backend.md` among the old/new filename set.
- The only remaining `Cando Backend` mentions in active wiki pages explicitly identify the old label as renamed or superseded.
- Focused synthesis search found zero remnants of the unsupported package-script safety rule.

Follow-ups:

- Rebuild or expand project knowledge only from directly relevant Hermes conversations in bounded, provenance-preserving batches; inspect repositories afterward only to verify those conversation-derived claims.

## [2026-07-21] ingest | Harvest Standalone Projects Project Knowledge Batch 1

What changed:

- Inventoried the final six discovered Git roots read-only: dirty MovieFlix Mobile, the clean but destructive `mywork` Git-history generator, unborn Playground, empty-commit Magical Goodall, clean GoAPI, and clean Cando Backend.
- Matched active/archived Codex rollout metadata and index shells by direct working directory/title; found zero standalone records and processed zero transcript bodies.
- Explicitly excluded two broad `/Users/acazumah/Documents` rollouts: the indexed harvest session is process control, while the unindexed record remains unassigned rather than guessed.
- Added one sanitized raw manifest, one source summary, and six repository-scoped project pages, including first-class seed pages for the two content-empty repositories.
- Updated the Software Development Operating Manual with the standalone map and completed 30-repository discovery boundary.
- Updated both operating manuals only with the supported reusable safety rule that package-script names do not establish harmless behavior.
- Closed the staged family queue for the repositories and direct historical records discovered on 2026-07-21; no next project-family batch was fabricated.

Files touched:

- `raw/sources/2026-07-21-standalone-projects-project-knowledge-harvest-batch-1.md`
- `wiki/sources/standalone-projects-project-knowledge-harvest-batch-1.md`
- `wiki/projects/movieflix-mobile.md`
- `wiki/projects/mywork-git-history-generator.md`
- `wiki/projects/playground.md`
- `wiki/projects/magical-goodall.md`
- `wiki/projects/go-api.md`
- `wiki/projects/cando-backend.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- The canonical brain now covers all 30 Git roots discovered under the approved scope, while standalone knowledge remains honestly repository-only: empty-project intent, MovieFlix’s dirty state, `mywork` side effects, GoAPI’s prototype limits, and Cando’s naming/foundation gaps are explicit rather than inferred away.

Verification:

- Before this entry, `python3 scripts/validate_vault.py` passed with 62 wiki pages, 486 checked wikilinks, six configured templates, and all six template-index links.
- The approved focused public-vault scan checked 12 touched files and found no credential assignments, private-key blocks, bearer values, credential-bearing database URIs, recognized token/key formats, email addresses, phone-number patterns, or trailing whitespace.
- Git whitespace checks passed.
- Final repository-state checks matched every pre-harvest baseline: MovieFlix retained only its original three modified files at `cf26207fe998`; `mywork`, Magical Goodall, GoAPI, and Cando remained clean at their recorded revisions; Playground remained unborn and empty.
- No project file, dependency, test/build output, service, database, migration, deployment, remote, or Git history was changed.

Follow-ups:

- No project-family batch is pending. On a future rescan, reopen the checkpoint only for a newly discovered Git root or direct historical record, preserving the one-family/eight-record limit.

## [2026-07-21] ingest | Harvest Portfolio Project Knowledge Batch 1

What changed:

- Inventoried five Portfolio Git roots read-only: the dirty/diverged parent launcher, clean backend, clean admin portal, clean client portal, and clean historical mock-up prototype.
- Classified exactly five Codex records: four substantive direct working-directory rollouts and one index-only shell with no surviving rollout or promotable claim.
- Reconciled the initial three-application architecture, app-local Yarn correction, backend/admin/client ownership, project visibility, and repeated Hero/About design corrections against current clean nested revisions.
- Preserved current-versus-historical boundaries: the parent is not a coherent aggregate snapshot; admin restructuring was historically unfinished; test claims are inconsistent and current runners permit empty suites; current client supersedes collage, Build Console, glowing CTA, global rail, and Threads experiments.
- Added one sanitized raw manifest, one source summary, and five repository-scoped project pages.
- Updated the Software Development Operating Manual and New Project Bootstrap Operating Manual only with supported app-boundary, data-backed-claim, feature-ownership, asset, responsive-rail, visibility, and verification rules.
- Closed Portfolio coverage for the discovered set and advanced the checkpoint to Standalone Projects batch 1.

Files touched:

- `raw/sources/2026-07-21-portfolio-project-knowledge-harvest-batch-1.md`
- `wiki/sources/portfolio-project-knowledge-harvest-batch-1.md`
- `wiki/projects/portfolio-workspace.md`
- `wiki/projects/portfolio-backend.md`
- `wiki/projects/portfolio-admin-portal.md`
- `wiki/projects/portfolio-client-portal.md`
- `wiki/projects/portfolio-mockup-prototype.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- Portfolio now has repository-scoped current knowledge and sanitized five-record Codex provenance, with the dirty parent topology and superseded UI states explicit rather than flattened into a false monorepo history.

Verification:

- `python3 scripts/validate_vault.py` passed with 55 wiki pages, 448 checked wikilinks, six configured templates, and all six template-index links.
- Focused validation passed: all five project pages retain required sections, all five record IDs have provenance, exactly one top log entry exists, no trailing whitespace was found, and no assigned sensitive value, private-key block, bearer value, or credential-bearing database URI matched the touched batch files.
- Git whitespace checks passed. The Portfolio parent remained at its pre-harvest 55 status entries and unchanged revision `8621a0286205`; backend, admin, client, and prototype remained clean at their recorded revisions. No project repository was modified.

Follow-ups:

- Resume Standalone Projects batch 1: inventory remaining repositories under `/Users/acazumah/Documents` outside completed named families and process at most the eight most recent direct records after discovery.

## [2026-07-21] ingest | Harvest CompFlow Hermes Project Knowledge Supplement 1

What changed:

- Processed exactly the checkpointed Hermes session `20260710_173537_54b264` from the canonical Hermes state database, using its partial retry dump and targeted logs only as supplemental provenance.
- Preserved the explicit correction from an accidental root monorepo to the existing independent `compflow`, `compflow-admin`, and `compflow-backend` folders with Yarn.
- Reconciled the session’s initial architecture, historical tests/builds, service starts, and HTTP smoke claims against the three first commits and all four clean current CompFlow repositories.
- Recorded current evolution: public plan lookup supersedes the minimal landing scaffold; admin still queries/falls back from scaffold-era `adminOverview`; current backend retains health but no longer exposes `adminOverview`; the later client portal was outside the session.
- Added one sanitized raw manifest and one source summary; updated only the three session-targeted project pages. The client-portal project page remained unchanged.
- Updated the Software Development Operating Manual and New Project Bootstrap Operating Manual only with the supported separate-folder/Yarn provenance and reusable rule that a shared parent folder is not monorepo authorization.
- Closed CompFlow coverage at zero discovered Codex sessions and one processed Hermes session, connected the supplement through `index.md`, and advanced the checkpoint to Portfolio batch 1.

Files touched:

- `raw/sources/2026-07-21-compflow-hermes-project-knowledge-harvest-supplement-1.md`
- `wiki/sources/compflow-hermes-project-knowledge-harvest-supplement-1.md`
- `wiki/projects/compflow.md`
- `wiki/projects/compflow-admin.md`
- `wiki/projects/compflow-backend.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- CompFlow’s independent-repository and Yarn boundaries now have direct user/Hermes provenance, while historical bootstrap verification and current integration drift remain clearly separated.

Verification:

- `python3 scripts/validate_vault.py` passed with 49 wiki pages, 411 checked wikilinks, six configured templates, and all six template-index links.
- Focused secret-pattern scanning found no assigned credential, token, private-key, API-key, client-secret, password, or authorization values in the touched batch notes.
- Git whitespace checks passed. All four CompFlow repositories remained clean and read-only; no repository files, dependencies, generation, tests, builds, services, browser sessions, API calls, databases, migrations, deployments, or Git history were changed during the harvest.

Follow-ups:

- Resume Portfolio batch 1: inventory the family and process at most the eight most recent direct historical records.

## [2026-07-21] ingest | Harvest C.E.Q.A/Altin Project Knowledge Batch 3

What changed:

- Rechecked the three C.E.Q.A repositories read-only at their unchanged clean branches/base commits and processed exactly the checkpointed final five records.
- Reconciled Keks standalone launchpad ownership, accessible button semantics, shared System/Dark/Light state, reduced-motion behavior, and responsive employee-hero ownership.
- Reconciled call-center branch changes and line repricing, fulfillment-state invalidation, exact-location/search/map synchronization, MoMo order search, delivery totals, import boundaries, and threshold-discount calculation.
- Preserved three unresolved current tensions: Announcements metadata without an active route, mixed same-feature call-center imports, and uncertain backend role authorization for the Altin estimate flow.
- Added one sanitized raw evidence manifest and one source summary; updated the supported Keks and Call Center project pages and added repository-only current-state corrections to Altin without inventing session evidence.
- Reconciled Hermes history: found no direct C.E.Q.A implementation session, corrected stale Keks deployment and call-center lint claims, and checkpointed the newly discovered CompFlow session `20260710_173537_54b264` as a separate one-session supplement.
- Updated the two operating manuals only with supported reusable accessibility, shared-theme, alias/import, dependent-state, and pricing rules.
- Closed C.E.Q.A/Altin at 21 of 21 classified Codex records, advanced the immediate checkpoint to the CompFlow Hermes supplement before Portfolio batch 1, and connected batch 3 through `index.md`.

Files touched:

- `raw/sources/2026-07-21-ceqa-altin-project-knowledge-harvest-batch-3.md`
- `wiki/sources/ceqa-altin-project-knowledge-harvest-batch-3.md`
- `wiki/projects/keks-admin-portal.md`
- `wiki/projects/call-center-web-app.md`
- `wiki/projects/altin-partner-mobile.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- C.E.Q.A/Altin Codex-history coverage is complete at 21 of 21 records, with no additional direct Hermes family session found. Repository corrections and the source-specific CompFlow history gap remain explicit and provenance-preserving.

Verification:

- `python3 scripts/validate_vault.py` passed before the log edit with 48 wiki pages and 392 checked wikilinks; after Hermes reconciliation it passed again with 48 wiki pages, 393 checked wikilinks, six configured templates, and all six template-index links.
- Focused secret-pattern scanning found no assigned credential, token, private-key, API-key, or client-secret values in the touched batch notes.
- Git whitespace checks passed. All three project repositories remained clean. No repository files, dependencies, generation, tests, builds, services, browser sessions, external integrations, databases, deployments, or Git history were changed.

Follow-ups:

- Resume exactly the one-session CompFlow Hermes supplement for `20260710_173537_54b264`; then continue to Portfolio batch 1.

## [2026-07-21] ingest | Harvest C.E.Q.A/Altin Project Knowledge Batch 2

What changed:

- Rechecked the three C.E.Q.A repositories read-only at their unchanged branches/base commits and processed exactly the checkpointed next eight records.
- Reconciled Keks report endpoint/filter contracts, present-day native date ranges, exception formatting, filter continuity, feature-file separation, and current nested settings routes.
- Reconciled call-center family dimensions/preferences, safe optional rendering, delivery-area/exact-location interaction, courier-type price dispatch, Formik/Yup authority, reverse-geocode ordering, Altin estimate invalidation, and unavailable-item modal behavior.
- Classified the family-config guide as reference-only because that record completed no repository change and no current maintained guide was found.
- Preserved two current-versus-historical drifts: Keks settings superseded the intermediate tab shell, and the call-center product modal again owns mapped picker loops despite the explicit separation correction.
- Added one sanitized raw evidence manifest and one source summary; updated only the supported Keks and Call Center project pages. Altin Partner Mobile remained unchanged because no batch-2 record targeted it.
- Updated the Software Development Operating Manual only with reusable API-filter, feature-ownership, safe-rendering, form-validity, and async-state rules.
- Updated the New Project Bootstrap Operating Manual only with reusable frontend ownership and atomic async-form-state foundation rules.
- Advanced the checkpoint to C.E.Q.A/Altin batch 3 at 16 of 21 records, with the exact final five IDs, and connected batch 2 through `index.md`.

Files touched:

- `raw/sources/2026-07-21-ceqa-altin-project-knowledge-harvest-batch-2.md`
- `wiki/sources/ceqa-altin-project-knowledge-harvest-batch-2.md`
- `wiki/projects/keks-admin-portal.md`
- `wiki/projects/call-center-web-app.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- C.E.Q.A/Altin is checkpointed at 16 of 21 classified records. Current code, explicit user conventions, historical outcomes, reference-only input, and later structural drift remain distinguishable and sourced.

Verification:

- `python3 scripts/validate_vault.py` passed before the log edit with 47 wiki pages, 379 checked wikilinks, six configured templates, and all six template-index links; final validation was rerun afterward.
- Focused secret-pattern scanning found no assigned credential, token, password, private-key, API-key, or client-secret values in the touched batch notes.
- Git whitespace checks passed. All three project repositories remained clean. No repository files, dependencies, generation, tests, builds, services, browser sessions, APIs, maps, databases, migrations, deployments, or Git history were changed.

Follow-ups:

- Resume exactly C.E.Q.A/Altin batch 3 and process the final five record IDs listed in the checkpoint.

## [2026-07-21] ingest | Harvest C.E.Q.A/Altin Project Knowledge Batch 1

What changed:

- Inventoried three clean, independently versioned repositories read-only: Altin Partner Mobile, Keks Admin Portal, and Call Center Web App.
- Discovered 21 direct current/legacy C.E.Q.A/Pizzaman working-directory records and processed exactly the eight most recent, leaving thirteen pending.
- Classified one image-only duplicate shell and one repeatedly interrupted search precursor without promoting them as independent successful implementations.
- Reconciled current code with Designations separation, Keks permission/API-key/search work, the Chakra Select fix, call-center checkout idempotency, and exact-location ordering corrections.
- Added one sanitized raw evidence manifest, one source summary, and three first-class `type: project` pages under `wiki/projects/`.
- Updated the Software Development Operating Manual with the linked family map and supported idempotency, permission, search, one-time-secret, and location-ordering rules.
- Updated the New Project Bootstrap Operating Manual only with reusable permission-layering, retry-idempotency, and public-mobile OAuth/PKCE foundation rules.
- Preserved unresolved contradictions without exposing secrets: Altin centralized module shells and stale README/config, incomplete Keks route coverage, interrupted Select verification, and call-center live-staging Codegen, missing lint config, and unhandled full-test errors.
- Advanced the checkpoint to C.E.Q.A/Altin batch 2 with the exact next eight record IDs and connected the new source/projects through `index.md`.

Files touched:

- `raw/sources/2026-07-21-ceqa-altin-project-knowledge-harvest-batch-1.md`
- `wiki/sources/ceqa-altin-project-knowledge-harvest-batch-1.md`
- `wiki/projects/altin-partner-mobile.md`
- `wiki/projects/keks-admin-portal.md`
- `wiki/projects/call-center-web-app.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- C.E.Q.A/Altin now has a repository-provenance map for all three applications and a bounded historical checkpoint at eight of 21 direct records. Current implementation, desired architecture, interrupted work, and historical verification outcomes remain explicitly distinguished.

Verification:

- `python3 scripts/validate_vault.py` passed with 46 wiki pages, 366 checked wikilinks, six configured templates, and all six template-index links before the log-only edit; final validation was rerun afterward.
- Focused secret-pattern scanning found no assigned credential, token, password, private-key, API-key, or client-secret values in the touched batch notes.
- Git whitespace checks passed. All three project repositories remained clean. No repository files, dependencies, generation, tests, builds, services, APIs, maps, identity providers, databases, migrations, deployments, or Git history were changed.

Follow-ups:

- Resume exactly C.E.Q.A/Altin batch 2 and process the eight record IDs listed in the checkpoint.

## [2026-07-21] ingest | Harvest Kusantec/Bora Project Knowledge Batch 1

What changed:

- Inventoried the Bora backend and Expo mobile repositories read-only, recording their branches, base commits, and pre-existing dirty-tree limitations.
- Processed all six directly matched historical Bora sessions: Fidelity requirements/questionnaire, Expo push notifications, Resend/Oye, KYC fixture repair, and Paystack integration.
- Excluded the separate Cando `letsride-backend`, the current harvest task, unrelated LivelyCura contexts, and Portfolio/CV/job sessions that only carried Bora path references.
- Added one sanitized raw evidence manifest, one source summary, and two first-class `type: project` pages under `wiki/projects/`.
- Updated the Software Development Operating Manual with the linked Bora map and supported provider, notification, Oye, and repository-local skill conventions.
- Updated the New Project Bootstrap Operating Manual only with reusable repository-skill precedence and financial-provider ownership/idempotency rules.
- Preserved unresolved contradictions without exposing secrets: authenticated-principal versus explicit-input deposit identity, planned Fidelity versus active Paystack, configuration validation gaps, dirty current trees, stale mobile documentation, and configured-but-disabled OTA updates.
- Advanced the checkpoint to C.E.Q.A/Altin batch 1 and connected the new source and project pages through `index.md`.

Files touched:

- `raw/sources/2026-07-21-kusantec-bora-project-knowledge-harvest-batch-1.md`
- `wiki/sources/kusantec-bora-project-knowledge-harvest-batch-1.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/projects/bora-capital-mobile-app.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- Kusantec/Bora is documented as two independently versioned applications with repository and session provenance. Its discovered boundary is complete at two repositories and six direct historical sessions, while implementation conflicts remain explicit for future decisions.

Verification:

- `python3 scripts/validate_vault.py` passed with 42 wiki pages, 343 checked wikilinks, six configured templates, and all six template-index links before the log-only edit; final validation was rerun afterward.
- Focused secret-pattern scanning found no assigned credential, token, password, private-key, or client-secret values in the touched batch notes.
- Git whitespace checks passed. Repository status was rechecked and matched the pre-harvest dirty state: backend 30 modified, four deleted, and two untracked paths; mobile one modified lockfile. No repository files, dependencies, builds, tests, services, databases, payment providers, migrations, deployments, or Git history were changed.

Follow-ups:

- Resume exactly C.E.Q.A/Altin batch 1 from the checkpoint.

## [2026-07-21] ingest | Harvest CompFlow Project Knowledge Batch 1

What changed:

- Inventoried the four known CompFlow repositories read-only at recorded clean branches/commits: public frontend, internal admin, business client portal, and backend.
- Searched active/archived Codex session metadata and the session index; found zero historical CompFlow sessions, excluded the current harvest conversation, and promoted no transcript-derived preference or rationale.
- Added one sanitized raw evidence manifest, one source summary, and four first-class `type: project` pages under `wiki/projects/`.
- Updated the Software Development Operating Manual with a linked CompFlow map and current coverage boundary.
- Updated the New Project Bootstrap Operating Manual only with reusable evidence about independent app boundaries, competing lockfiles, and verifying Codegen config/schema inputs.
- Recorded current contradictions without exposing secrets: transitional client/demo paths, onboarding/auth mismatch, incomplete GraphQL generation wiring, mixed client lockfiles, and stale backend database-bypass documentation.
- Advanced the checkpoint to Kusantec/Bora batch 1 and connected the new source/projects through `index.md`.

Files touched:

- `raw/sources/2026-07-21-compflow-project-knowledge-harvest-batch-1.md`
- `wiki/sources/compflow-project-knowledge-harvest-batch-1.md`
- `wiki/projects/compflow.md`
- `wiki/projects/compflow-admin.md`
- `wiki/projects/compflow-client-portal.md`
- `wiki/projects/compflow-backend.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- CompFlow is now documented as four independently versioned applications with repository/branch/commit provenance. Its discovered boundary is complete at four repositories and zero historical sessions rather than being padded with the current harvest task or inferred intent.

Verification:

- `python3 scripts/validate_vault.py` passed with 39 wiki pages and 321 checked wikilinks before the log-only edit; the final validation was rerun after it.
- Focused secret-pattern scanning found no credential, token, private-key, connection-string, or bearer-token values in the batch artifacts.
- Git whitespace checks passed. All four project repositories remained clean and no installs, generation, tests, builds, services, databases, payments, migrations, deployments, or Git mutations were run.

Follow-ups:

- Resume exactly Kusantec/Bora batch 1 from the checkpoint.

## [2026-07-21] maintenance | Connect Project Template To Index

What changed:

- Added the missing `Project` template link to the Maintenance template catalog in `index.md`.
- Updated the human operating schema to require the index to link every template registered in `schema/vault-structure.json`.
- Extended the canonical validator to check the schema-to-index template connection, preventing registered templates from being omitted from navigation.

Files touched:

- `index.md`
- `AGENTS.md`
- `scripts/validate_vault.py`
- `log.md`

Key result:

- All six configured templates—Source Summary, Concept, Entity, Project, Question, and Synthesis—are now linked from the index and validated as a complete set.

Verification:

- The canonical validator passed with six templates and six template-index links.
- The Project template link resolves to `_template/project-template.md`; JSON, wikilink, and Git whitespace checks passed.

Follow-ups:

- None. Future template registrations will fail validation until their index connection is added.

## [2026-07-21] maintenance | Promote Projects To First-Class Wiki Pages

What changed:

- Moved all ten project notes from `wiki/entities/projects/` to the canonical `wiki/projects/` folder without changing their substantive project knowledge.
- Changed project frontmatter from `type: entity` to `type: project` and repaired every moved note's relative source paths.
- Updated source summaries, the project-harvest checkpoint and procedure, the software-development manual, and `index.md` so all real project wikilinks target `wiki/projects/`.
- Added `project` to the human-readable and JSON frontmatter schemas, registered `wiki/projects/` as a required canonical directory, added a project template, and made the validator enforce page-type directory ownership.
- Kept generic entities under `wiki/entities/`, gave projects their own index section, preserved historical log entries unchanged, and left project repositories untouched.

Files touched:

- `AGENTS.md`
- `schema/vault-structure.json`
- `schema/wiki-frontmatter.schema.json`
- `scripts/validate_vault.py`
- `_template/project-template.md`
- `welcome.md`
- `wiki/concepts/codex-project-knowledge-harvest.md`
- Ten project notes moved to `wiki/projects/`
- `wiki/sources/livelycura-project-knowledge-harvest-batch-1.md`
- `wiki/sources/livelycura-project-knowledge-harvest-batch-2.md`
- `wiki/sources/livelycura-project-knowledge-harvest-batch-3.md`
- `wiki/sources/livelycura-project-knowledge-harvest-batch-4.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Projects are now a first-class vault category rather than nested entities: path, frontmatter type, template, index, harvest workflow, backlinks, and machine validation all agree on `wiki/projects/`.

Verification:

- `python3 scripts/validate_vault.py` passed with 12 required directories, 6 templates, 34 wiki pages, and 283 checked wikilinks.
- Exactly ten Markdown notes exist directly under `wiki/projects/`; all ten use `type: project`, all frontmatter source paths resolve, and `wiki/entities/projects/` no longer exists.
- No live old-path references remain outside append-only historical log text and Obsidian's ignored user-local recent-file state. Obsidian's workspace has recognized the new folder and note paths.
- JSON parsing, frontmatter contracts, Git whitespace checks, and provenance-link checks passed. No project repositories were modified.

Follow-ups:

- Create future repository pages from `_template/project-template.md` directly under `wiki/projects/`; the validator will reject project pages placed elsewhere.

## [2026-07-21] maintenance | Complete Core Vault Infrastructure

What changed:

- Added root `schema/`, `.agents/skills/`, and `scripts/` infrastructure.
- Moved the five Obsidian page scaffolds from `wiki/templates/` to root `_template/` and configured Obsidian's enabled core Templates plugin through `.obsidian/templates.json`.
- Added a machine-readable path/section manifest and JSON Schema for wiki frontmatter.
- Vendored the five previously scanned `kepano/obsidian-skills` skills at revision `a1dc48e68138490d522c04cbf5822214c6eb1202`, preserved their MIT license, and added the repository-local `vault-maintenance` skill.
- Added the stdlib-only canonical structural validator and connected the new paths through `AGENTS.md`, `index.md`, and `welcome.md`.

Files touched:

- `AGENTS.md`
- `index.md`
- `log.md`
- `welcome.md`
- `.obsidian/templates.json`
- `_template/`
- `schema/`
- `.agents/skills/`
- `scripts/`

Key result:

- Human-facing rules, machine-readable contracts, Obsidian template configuration, project-local agent capabilities, and executable structural validation now share one path contract.

Verification:

- `python3 scripts/validate_vault.py` passed with six Agent Skills, five templates, eleven required directories, thirty-four wiki pages, eight JSON files, and 283 resolved wikilinks.
- Vendored upstream skill directories were compared against the scanned Hermes installations, and all new root paths were checked for Git trackability.

Follow-ups:

- Restart or open a fresh Codex/OpenCode/skills-compatible agent session so its project skill catalog includes `.agents/skills/`.
- Keep vendored upstream skill revision and license metadata synchronized when updating those skills.

## [2026-07-21] ingest | Harvest LivelyCura Project Knowledge Batch 5

What changed:

- Processed exactly the five final LivelyCura-working-directory sessions fixed by the batch-4 checkpoint; no project repository files or Git state were modified.
- Classified four unindexed records as `guardian` approval-review subagents duplicating the already-processed AI-result-validation task and classified the indexed personalized-pet session as unrelated work.
- Created one sanitized provenance manifest and one source summary. Generated images, pet binaries, copied approval payloads, tool chatter, credentials, and raw private identifiers were excluded.
- Promoted no project architecture, convention, or scaffolding claim because the batch contained zero unique project sessions. Project entity pages and the New Project Bootstrap Operating Manual therefore remain unchanged.
- Updated only the Software Development Operating Manual’s evidence/coverage boundary, the checkpoint, and the index; LivelyCura is complete for all 37 discovered sessions and CompFlow batch 1 is next.

Files touched:

- `raw/sources/2026-07-21-livelycura-project-knowledge-harvest-batch-5.md`
- `wiki/sources/livelycura-project-knowledge-harvest-batch-5.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- The LivelyCura harvest boundary is closed without inflating approval subagents or unrelated artifacts into project knowledge: 32 substantive sessions, four duplicate guardian records, and one unrelated session equal 37 classified records.

Verification:

- The five manifest IDs match the former checkpoint batch exactly; classification arithmetic is `32 + 4 + 1 = 37`, with zero LivelyCura records pending.
- Touched wiki frontmatter and source paths parse/resolve; real wikilinks and local Markdown links resolve; secret-pattern scanning found no secret-like values in the new artifacts.
- No project page or bootstrap-manual edits were made because no unique implementation or scaffolding evidence required promotion. Repository tests, builds, apps, migrations, and external artifacts were not exercised.

Follow-ups:

- Process CompFlow batch 1 only: inventory its four known repositories, discover matching Codex sessions, and process at most eight relevant sessions.

## [2026-07-21] ingest | Harvest LivelyCura Project Knowledge Batch 4

What changed:

- Processed exactly the eight lab-research, courier release/task, Pharmacy Portal delivery-type, and CheckCity interaction sessions fixed by the batch-3 checkpoint; no project repository files or Git state were modified.
- Created one sanitized provenance manifest and one source summary, excluding transcripts, images/binaries, credentials, review-account values, and raw private identifiers.
- Reconciled historical corrections against current Backend, Pharmacy Portal, courier mobile, and CheckCity source, then updated those four project pages.
- Preserved material reversals instead of hardening stale work: JIT/backflush lab research is not implemented, the App Store auth-copy change ended in a revert, the reusable courier OTP component is now unused, and the historical CheckCity grid loader differs from current code.
- Promoted supported reusable rules into the two operating manuals: canonical consumer-boundary ID mapping, caller-owned presentation spacing, native OTP/platform QA, Android elevation/system-bar checks, floating-header refresh insets, and store-review metadata/access preparation.
- Advanced the checkpoint from 24 to 32 processed LivelyCura sessions. Five sessions remain in one exact final relevance-triage batch.

Files touched:

- `raw/sources/2026-07-21-livelycura-project-knowledge-harvest-batch-4.md`
- `wiki/sources/livelycura-project-knowledge-harvest-batch-4.md`
- `wiki/entities/projects/livelycura-backend.md`
- `wiki/entities/projects/livelycura-pharmacy-portal.md`
- `wiki/entities/projects/livelycura-courier-mobile.md`
- `wiki/entities/projects/livelycura-check-city-app.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- The canonical brain now records `SERLP Dispatch` as the courier app’s public identity, one `taskId` consumer contract, structural standalone/multi-pickup classification, and current CheckCity floating-header/modal behavior while keeping superseded lab/auth/loader approaches visibly historical.

Coverage boundary:

- Thirty-seven sessions use a LivelyCura working directory. Thirty-two are processed and five remain. Batch 5 is a bounded relevance triage of one indexed personalized-pet session plus four unindexed sessions; it must explicitly close or defer LivelyCura history before CompFlow begins.

Verification:

- Touched wiki frontmatter parsed successfully; all real wikilinks, local Markdown links, and frontmatter source paths resolve; all four project pages retain required sections; the eight manifest IDs match checkpoint batch 4; and checkpoint arithmetic is `32 + 5 = 37` with no overlap in batch 5.
- Secret-pattern scanning found no secret-like values in the new manifest/source. Current implementation claims were verified read-only against the four clean project worktrees.
- Repository tests, builds, apps, external screenshots, and store workflows were not rerun. Historical outcomes are labeled transcript-reported; binaries and reviewer credentials were excluded.

Follow-ups:

- Process exactly the five-session LivelyCura batch 5 relevance triage recorded in `wiki/syntheses/project-knowledge-harvest-status.md`.
- Keep the JIT proposal, unused courier OTP component, historical CheckCity loader, and reviewer-account verification questions open until current evidence resolves them.

## [2026-07-21] maintenance | Prepare Public Git Versioning

What changed:

- Initialized the vault as an independent Git repository on `main`.
- Configured `https://github.com/ACAZUMAH/my-obsidian-vault.git` as `origin`; the GitHub repository was confirmed public and empty before the first commit.
- Added `welcome.md` as the human-facing entry point with architecture, agent workflow, and public-repository safety guidance.
- Added a security-conscious `.gitignore` covering Obsidian-local state, plugin payloads, OS/editor files, credentials, certificates, signing material, databases, archives, dependencies, build output, caches, logs, and agent-local state.
- Linked the welcome page from `index.md`.

Files touched:

- `.gitignore`
- `welcome.md`
- `index.md`
- `log.md`

Verification:

- Reviewed the exact staged commit set: 56 text files and no ignored Obsidian workspace/plugin payloads.
- Scanned every staged file for common private-key, access-token, JWT, secret-assignment, and credential-bearing database URI formats; no matches were found.
- Searched Markdown for email-address and Ghanaian phone-number patterns; no matches were found.
- Confirmed the only miscellaneous raw asset contains public UI inspiration site names, not private data.

Key result:

- The canonical second brain is prepared for public Git versioning with explicit safety boundaries and reproducible navigation.

Follow-ups:

- Keep reviewing every staged diff because `.gitignore` cannot detect secrets already written into ordinary Markdown.
- Treat the public GitHub remote as a publishing boundary, not as a private backup destination.

## [2026-07-21] ingest | Harvest LivelyCura Project Knowledge Batch 3

What changed:

- Processed exactly the eight distribution-artwork, MLS cleanup, custom-app, Live Activity, native-update, cart/tab, and theme sessions fixed by the batch-2 checkpoint; no project repository files or Git state were modified.
- Created one sanitized provenance manifest and one source summary. Private allow-list identifiers were replaced by `[two allow-listed organizations]`, and historical binaries/transcripts were not copied.
- Reconciled history against six current repositories and updated their project pages: Backend, Admin Portal, Pharmacy Portal, CheckCity, Loop, and SERLP Mobile.
- Preserved three material implementation gaps: the catalog-cleanup migration is currently unregistered, historical store-artwork outputs are absent, and Live Activities exist only on deferred branches whose app snapshot still uses the superseded custom-module approach.
- Promoted only supported reusable rules into the two operating manuals: real screenshot/platform-correct store artwork, maintained-package research, resilient optional native modules, automatic system appearance plus native rebuild, conditional native file config, and isolated deferred-feature branches.
- Advanced the canonical checkpoint from 16 to 24 processed LivelyCura sessions, leaving 13 pending and fixing the exact eight-session batch-4 boundary.

Files touched:

- `raw/sources/2026-07-21-livelycura-project-knowledge-harvest-batch-3.md`
- `wiki/sources/livelycura-project-knowledge-harvest-batch-3.md`
- `wiki/entities/projects/livelycura-backend.md`
- `wiki/entities/projects/livelycura-admin-portal.md`
- `wiki/entities/projects/livelycura-pharmacy-portal.md`
- `wiki/entities/projects/livelycura-check-city-app.md`
- `wiki/entities/projects/livelycura-loop-app.md`
- `wiki/entities/projects/serlp-mobile.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- The canonical brain now separates custom-app assignment, ERP banner management, and mobile consumption; records Live Activities as deferred rather than current; and keeps store-artwork conventions without claiming missing artifacts still exist.

Coverage boundary:

- Thirty-seven sessions use a LivelyCura working directory. Twenty-four are processed and thirteen remain. Batch 4 contains the next eight indexed sessions; the final five then require relevance/unique-evidence triage.

Verification:

- Touched wiki frontmatter parsed successfully; all real wikilinks, local Markdown links, and frontmatter source paths resolve; all six project pages retain their required sections; the eight manifest IDs match checkpoint batch 3; and checkpoint arithmetic is `24 + 13 = 37` with no overlap in the eight-session batch 4.
- Secret-pattern scanning found no secret-like values in the new manifest/source. The backend, Pharmacy Portal, CheckCity, Loop, and SERLP Mobile repositories remained clean. Admin Portal retained only its pre-existing modified generated GraphQL files, which this harvest excluded and did not touch.
- Repository test suites and historical artwork binaries were not exercised because the harvest is read-only. Session-reported outcomes are labeled historical, and current claims come from source inspection.

Follow-ups:

- Process LivelyCura batch 4 exactly as recorded in `wiki/syntheses/project-knowledge-harvest-status.md`.
- Keep the stale migration, deferred Live Activity package replacement, and missing artwork ownership questions open until a scoped implementation or maintenance task resolves them.

## [2026-07-21] ingest | Harvest LivelyCura Project Knowledge Batch 2

What changed:

- Processed exactly the eight MLS, ERP, and CheckCity sessions fixed by the batch-1 checkpoint; no project repository files or Git state were modified.
- Created a sanitized provenance manifest and source summary, then reconciled historical plans and corrections against current backend, pharmacy portal, and CheckCity source.
- Updated the three affected project pages with sale-to-request transaction behavior, TestDefinition/catalog/lifecycle boundaries, technician-facing builder/renderer ownership, standalone POS architecture, Samples/Departments behavior, and reduced-motion-aware theme transitions.
- Promoted reusable scoped-change, lifecycle-operation, existing-catalog, transaction-owner, flow-ownership, mapper-boundary, live-UI-verification, and motion rules into the two operating manuals.
- Advanced the canonical checkpoint from 8 to 16 processed LivelyCura sessions and fixed the exact eight-session batch-3 boundary.

Files touched:

- `raw/sources/2026-07-21-livelycura-project-knowledge-harvest-batch-2.md`
- `wiki/sources/livelycura-project-knowledge-harvest-batch-2.md`
- `wiki/entities/projects/livelycura-backend.md`
- `wiki/entities/projects/livelycura-pharmacy-portal.md`
- `wiki/entities/projects/livelycura-check-city-app.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- The canonical brain now records current MLS behavior as one `TestRequest` per lab-linked `SaleItem` inside the ordinary sale transaction, explicitly superseding the older parent-request/many-tests PDF proposal. It also separates durable technician-facing and lifecycle conventions from the builder/action layouts that changed during review.

Coverage boundary:

- Thirty-seven sessions use a LivelyCura working directory. Sixteen are now processed; twenty-one remain pending, including the exact eight-session batch 3 recorded in the checkpoint.

Verification:

- Touched wiki frontmatter parsed successfully; real wikilinks and the source-summary raw link resolve; checkpoint totals and the exact eight-session next batch were validated; the raw manifest contains no detected secret-like assignments.
- The three inspected project repositories remained clean. Repository test suites were not rerun because this harvest was read-only; historical test/build/browser outcomes are labeled as transcript evidence.

Follow-ups:

- Process LivelyCura batch 3 exactly as recorded in `wiki/syntheses/project-knowledge-harvest-status.md` before continuing to later families.
- Preserve the clinical-request grouping question, historical builder-layout churn, and codegen/runtime verification gaps until future evidence resolves them.

## [2026-07-21] ingest | Harvest LivelyCura Project Knowledge Batch 1

What changed:

- Inventoried ten independently versioned LivelyCura/SERLP repositories without modifying repository code or Git state.
- Processed eight bounded Codex sessions and preserved only sanitized provenance, durable corrections, decisions, verification history, and short supporting statements.
- Created one project page per repository, a raw evidence manifest, a source summary, and the canonical resumable harvest checkpoint.
- Promoted cross-project domain-ownership and infrastructure-reuse rules into the software-development operating manual.
- Left the new-project bootstrap manual unchanged because this batch reinforced existing repository-boundary and Yarn/TypeScript guidance without proving a new universal default.

Files touched:

- `raw/sources/2026-07-21-livelycura-project-knowledge-harvest-batch-1.md`
- `wiki/sources/livelycura-project-knowledge-harvest-batch-1.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `wiki/syntheses/software-development-operating-manual.md`
- Ten pages under `wiki/entities/projects/` for the LivelyCura/SERLP repositories.
- `index.md`
- `log.md`

Key result:

- The canonical brain now distinguishes live LivelyCura implementation from historical intent. MLS workflow boundaries and public result delivery are verified; the broader courier-provider, payout, collection, and remittance model is preserved as desired architecture that current persistence has not yet completed.

Coverage boundary:

- Thirty-seven sessions use a LivelyCura working directory. This batch processed eight; twenty-nine remain unprocessed or pending relevance triage.

Follow-ups:

- Process the exact eight-session LivelyCura batch 2 recorded in `wiki/syntheses/project-knowledge-harvest-status.md` before moving to CompFlow.
- Preserve the Customer Portal lockfile conflict and stale README claims until an explicit maintenance task resolves them.

## [2026-07-21] synthesis | Add Codex Knowledge Harvest And New Project Bootstrap Manual

What changed:

- Recorded the user's correction that Project Knowledge is incomplete because relevant evidence also exists in Codex conversations and live repositories.
- Located 67 indexed Codex threads, 77 Codex transcript/index JSONL files, and 39 project manifests as the recoverable evidence surface at inspection time.
- Added a paste-ready Codex procedure that processes one project family or at most eight sessions per batch, maintains a checkpoint, redacts secrets, distinguishes current code from historical intent, and writes project-specific entity pages.
- Added an evidence-backed new-project bootstrap manual covering backend, web/admin, and Expo mobile foundations before feature logic.
- Marked the software-development operating manual as a compact, currently incomplete project map and linked its expansion path.

Files touched:

- `raw/sources/2026-07-21-project-knowledge-completion-and-bootstrap-directive.md`
- `wiki/sources/project-knowledge-completion-and-bootstrap-directive.md`
- `wiki/concepts/codex-project-knowledge-harvest.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Codex now has a safe, resumable prompt for completing project knowledge from its own archive, while all agents have a detailed shared definition of what constitutes a complete project foundation before screens, pages, or domain logic.

Coverage boundary:

- This operation discovered and mapped the evidence sources but did not claim to have ingested every Codex transcript. Full project completion remains a staged follow-up recorded by the harvest checkpoint.

Follow-ups:

- Run the master prompt in Codex from `/Users/acazumah/Documents` and process the first project-family batch.
- Resolve the open defaults for canonical reference backend, web folder variant, test runner, CI, deployment, and observability as the harvest supplies stronger cross-project evidence.

## [2026-07-20] setup | Unify Shared Brain Across All Hermes Profiles And Codex

What changed:

- Configured `OBSIDIAN_VAULT_PATH=/Users/acazumah/Documents/Work Space` for the `default`, `coder`, `devops`, `personal`, and `researcher` Hermes profiles.
- Added compact shared-brain pointers and communication preferences to every profile's `USER.md` and `MEMORY.md`, with role-specific retrieval and contribution hints.
- Preserved the former default and coder profile memories as raw evidence, then promoted their durable development knowledge into a shared software development operating manual.
- Created Codex global instructions at `~/.codex/AGENTS.md` and exposed the vault path through `~/.codex/config.toml`.
- Expanded the architecture from a single-profile Hermes–Obsidian link into a Hermes–Codex–Obsidian canonical knowledge plane with concurrent-write controls.
- Recorded that the user prefers direct, concise, technically sophisticated explanations that show architecture, relationships, and rationale.

Files touched:

- `AGENTS.md`
- `index.md`
- `log.md`
- `raw/sources/2026-07-20-shared-brain-all-agents-directive.md`
- `raw/sources/2026-07-20-hermes-persistent-memory-import.md`
- `wiki/sources/shared-brain-all-agents-directive.md`
- `wiki/sources/hermes-persistent-memory-import.md`
- `wiki/concepts/hermes-obsidian-memory-architecture.md`
- `wiki/entities/hermes-agent.md`
- `wiki/entities/codex.md`
- `wiki/entities/obsidian.md`
- `wiki/syntheses/personal-operating-manual.md`
- `wiki/syntheses/software-development-operating-manual.md`
- All five Hermes profiles' `.env`, `memories/USER.md`, and `memories/MEMORY.md` files.
- `~/.codex/AGENTS.md`
- `~/.codex/config.toml`

Key result:

- Hermes profiles and Codex now use one canonical Obsidian brain while retaining tool and role specialization through compact local context layers.

Verification:

- All five Hermes profile environment paths, memory files, character limits, and canonical-vault pointers passed validation.
- Codex global instructions and TOML environment configuration passed validation.
- Required vault artifacts exist and all real wikilinks in the touched shared-brain notes resolve.
- An ephemeral, read-only Codex run loaded the global instructions and correctly reported the canonical vault, both operating-manual paths, and the user's preferred communication style.

Follow-ups:

- Split project sections into dedicated linked pages as their sources and conventions grow.
- Introduce a coordinated write queue only if simultaneous vault-edit conflicts become frequent.

## [2026-07-20] setup | Connect Hermes To The Obsidian Second Brain

What changed:

- Configured the active `coder` Hermes profile with `OBSIDIAN_VAULT_PATH=/Users/acazumah/Documents/Work Space`.
- Ingested the user's directive to use Obsidian as Hermes's linked, durable second brain.
- Added a layered memory architecture that separates Hermes memory, Obsidian knowledge, executable skills, and temporary session history.
- Created a personal operating manual and seeded it with durable working preferences already known to Hermes.
- Updated the vault schema with selective workflow-capture, retrieval, linking, privacy, and anti-noise rules.

Files touched:

- `AGENTS.md`
- `index.md`
- `log.md`
- `raw/sources/2026-07-20-hermes-obsidian-second-brain-kickoff.md`
- `wiki/sources/hermes-obsidian-second-brain-kickoff.md`
- `wiki/concepts/hermes-obsidian-memory-architecture.md`
- `wiki/entities/hermes-agent.md`
- `wiki/entities/obsidian.md`
- `wiki/syntheses/personal-operating-manual.md`
- `wiki/syntheses/llm-wiki-operating-model.md`

Key result:

- Future Hermes sessions can discover this vault from compact persistent memory, consult linked operating knowledge before asking the user to repeat it, and keep the second brain updated with durable ways of working.

Follow-ups:

- Add focused project or workflow pages as recurring patterns emerge.
- Promote mature repeatable procedures into Hermes skills when exact operational steps become valuable.

## [2026-05-13] setup | Initialize LLM Wiki Second Brain

What changed:

- Created the root operating schema in `AGENTS.md`.
- Created the content index in `index.md`.
- Created this chronological log in `log.md`.
- Created folder conventions for raw sources, assets, wiki pages, templates, and tools.
- Treated the user's pasted LLM Wiki idea file as the first source and created starter wiki pages from it.

Files touched:

- `AGENTS.md`
- `index.md`
- `log.md`
- `raw/sources/2026-05-13-llm-wiki-idea.md`
- `wiki/sources/llm-wiki-idea.md`
- `wiki/concepts/persistent-compounding-wiki.md`
- `wiki/concepts/raw-source-wiki-schema-architecture.md`
- `wiki/concepts/ingest-query-lint-workflows.md`
- `wiki/entities/obsidian.md`
- `wiki/syntheses/llm-wiki-operating-model.md`
- `wiki/templates/source-summary-template.md`
- `wiki/templates/concept-template.md`
- `wiki/templates/entity-template.md`
- `wiki/templates/question-template.md`
- `wiki/templates/synthesis-template.md`
- `wiki/questions/first-ingest-example.md`

Key result:

- The vault now has a working LLM Wiki scaffold and one fully ingested seed source.

Follow-ups:

- Add the next raw source to `raw/sources/` and ask the agent to ingest it.
- Decide whether to add optional search tooling once the wiki grows beyond what `index.md` and `rg` can comfortably cover.

## [2026-09-21] correction | Align Fleet Operator Forms With Portal Ownership

What changed:

- Recorded the removal of the premature `src/fleet/shared` ownership layer.
- Required feature-owned Formik/Yup hooks for Fleet operator create and update forms.
- Clarified that pages and modals coordinate mutations, payloads, and navigation while form components render supplied state.
- Added the general rule that shared feature folders follow proven reuse rather than acting as default dumping grounds.

Files touched:

- `raw/sources/2026-09-21-fleet-frontend-form-and-shared-folder-correction.md`
- `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Future Fleet frontend work must copy the Portal's existing feature ownership and Formik/Yup structure instead of inventing a generic Fleet shared layer or combining form responsibilities in one component.

Verification:

- `python3 scripts/wiki_tool.py check` completed after the update.

## [2026-09-21] correction | Limit Fleet Operator Detail Metadata

What changed:

- Recorded that Fleet operator details follow established project detail pages and present operational person information.
- Excluded database, account, organization, facility, and duplicate operator IDs from the visible page.
- Excluded routine created/updated timestamps and inactive archive placeholders; archive context appears only for archived operators.

Files touched:

- `raw/sources/2026-09-21-fleet-operator-detail-information-scope.md`
- `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `index.md`
- `log.md`

Key result:

- Future Fleet detail pages distinguish useful operator information from internal persistence and tenancy metadata.

## [2026-09-21] fix | Align LivelyCura GraphQL Compatibility Boundaries

What changed:

- Recorded enum-list serialization handling for historical CRM marketing-message application values.
- Recorded that Admin Courier consumes the standalone platform-rider contract without `agentType` or company ownership fields.
- Required client queries, filters, views, generated types, and fixtures to move together when backend fields are removed.

Files touched:

- `raw/sources/2026-09-21-livelycura-graphql-contract-compatibility-fixes.md`
- `wiki/sources/livelycura-graphql-contract-compatibility.md`
- `wiki/projects/livelycura-backend.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/projects/livelycura-admin-portal.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Retired enum data no longer breaks record reads, and Admin Courier no longer drifts from the platform-rider GraphQL schema.

## [2026-09-21] correction | Complete Fleet Operator UI And Vehicle Slice

What changed:

- Recorded CRM/Product-style Fleet operator details and the revised profile-image presentation.
- Required one typed service parameter named `data`, actor IDs instead of user documents, service-owned user lookup, and Shield-owned endpoint permission checks.
- Recorded the one-feature-at-a-time sequence and the completed Vehicles backend/frontend ownership pattern.

Files touched:

- `raw/sources/2026-09-21-fleet-operator-ui-and-vehicle-feature-slice.md`
- `wiki/sources/livelycura-independent-fleet-and-platform-dispatch.md`
- `wiki/projects/livelycura-backend.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Future Fleet slices must finish the backend contract and complete feature-owned Portal UI before routing, using a single `data` service object and actor IDs only.

## [2026-09-28] implementation | Add Bora Fund Administration And Hybrid Staff Access

What changed:

- Recorded database-backed role/direct-permission unions, staff invitation/admin authentication, privilege ceilings, and immediate admin revocation.
- Recorded the one-fund/one-draft/one-publication model with no version history, BCL live-price ownership, outage fallback, and customer visibility rules.
- Recorded the exact-PDF production seed boundary for BBF1100, BFI1100, and BGF1100 plus the deferred later admin phases.

Files touched:

- `raw/sources/2026-09-28-bora-fund-administration-access-control-plan.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Future Bora admin work must preserve request-time hybrid permissions and the versionless draft/published fund boundary while treating BCL as the live-price source.

## [2026-09-30] implementation | Add Bora Notifications, Campaigns, And Banners

What changed:

- Recorded the stored-notification design (inbox row plus per-channel delivery rows, leased retry worker, paced Hubtel SMS), client-scoped inboxes, and admin-inbox-only staff support notifications.
- Recorded the marketing consent decision (never asked, opt-out per push/email/SMS, in-app never gated, send-time consent check), resumable campaigns, and RFC 8058 one-click email unsubscribe without a web page.
- Recorded home-screen banners on LivelyCura's custom-app banner upload pattern, the dead storage helper and stale `node_modules` findings, and reusable lessons on proving infrastructure is live, validating before upload, and compile-safe mutation checks.

Files touched:

- `raw/sources/2026-09-30-bora-notifications-campaigns-banners.md`
- `wiki/sources/bora-notifications-marketing.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Future Bora notification work goes through `notifyUsers` and the delivery worker, keeps staff alerts inbox-only, preserves opt-out consent, and uploads files the LivelyCura way.

## [2026-10-01] implementation | Add Bora Biometric Login And Consolidate Frontend Handoff

What changed:

- Recorded server-backed biometric login: hashed per-device token, password-free enrolment within 10 minutes of an OTP sign-in, 90-day inactivity lapse, and revocation by logout, password change or reset, and account disablement.
- Recorded the two-file frontend handoff (customer app and admin portal) that replaced the per-feature docs, and the schema validation that caught stale Grow Wealth query names.
- Recorded the open questions on a current-user permissions query and on docs deleted outside the session.

Files touched:

- `raw/sources/2026-10-01-bora-biometric-login-and-handoff-docs.md`
- `wiki/sources/bora-biometric-login-and-handoff-docs.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Future Bora frontend-facing changes update `docs/frontend-handoff-app.md` and `docs/frontend-handoff-admin.md`, and biometric work keeps the device-token design and the `biometric` assurance level in every allow-list.

## [2026-10-01] implementation | Add Bora Current-User Permissions And Customer Inbox Items

What changed:

- Recorded the user's correction that each frontend handoff covers only changes since the previous one.
- Recorded `getMyPermissions` for admin menus and the event-keyed inbox items for welcome, KYC, deposit, and withdrawal notifications; the sign-in welcome-back push stays out of the inbox.
- Resolved the open questions on a current-user permissions query and on the deleted docs, and replaced a stale handoff path.

Files touched:

- `raw/sources/2026-10-01-bora-handoff-delta-permissions-inbox.md`
- `wiki/sources/bora-biometric-login-and-handoff-docs.md`
- `wiki/sources/bora-notifications-marketing.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Future Bora handoffs list only new changes, and customer events that send their own email, SMS, and push also add an event-keyed inbox item.

## [2026-10-01] implementation | Put Bora Campaign SMS On Hold

What changed:

- Recorded the user's decision to hold campaign SMS until Hubtel bulk sending is investigated, and the `CAMPAIGN_SMS_ENABLED` flag that lifts it.
- Replaced the open question on capping SMS campaigns with the hold, and recorded that `.env.default` is not tracked by git.

Files touched:

- `raw/sources/2026-10-01-bora-campaign-sms-hold.md`
- `wiki/sources/bora-notifications-marketing.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- No campaign SMS can be scheduled, sent, tested, or queued unless `CAMPAIGN_SMS_ENABLED` is `true`; OTP and transaction SMS are unaffected.

## [2026-10-01] correction | Correct Bora Frontend Handoff Scope

What changed:

- Recorded the user's correction that only withdrawals, investment accounts, and goals and top-ups were in the previous frontend handoff; Grow Wealth, existing-customer onboarding, KYC, and statements were wrongly assumed sent and are back in the app handoff.
- Replaced the inferred list of sent features with the user's list and a rule to ask rather than infer.

Files touched:

- `raw/sources/2026-10-01-bora-handoff-scope-correction.md`
- `wiki/sources/bora-biometric-login-and-handoff-docs.md`
- `wiki/projects/bora-capital-backend.md`
- `log.md`

Key result:

- Future handoff trims leave out only features the user explicitly names as already sent.

## [2026-10-04] decision | Record LivelyCura Marketplace Single Delivery

What changed:

- Recorded the product owner's decision, relayed by the user, to remove split marketplace fulfillment and all multi-stop courier routes for launch.
- Recorded the follow-up answers: full-coverage single winner, one delivery task per marketplace order created at award, LivelyCura-paid riders, rider request on payment, rider release before pickup, winner-only pickup code, and Admin cancel/refund.
- Replaced multi-pickup route conventions on the Courier Mobile and Pharmacy Portal pages and added the marketplace delivery conventions to the Backend page.

Files touched:

- `raw/sources/2026-10-04-livelycura-marketplace-single-delivery-decision.md`
- `wiki/sources/livelycura-marketplace-single-delivery.md`
- `wiki/projects/livelycura-backend.md`
- `wiki/projects/livelycura-courier-mobile.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `index.md`
- `log.md`

Key result:

- Future agents treat courier deliveries as single tasks and must not reintroduce routes, stops, or split marketplace awards.

## [2026-10-04] decision | Record Marketplace Delivery Design Review Answers

What changed:

- Recorded the user's acceptance of the design-review recommendations: buyer-total ranking, no manual-bid substitutes, a 60-minute payment window, Admin-confirmed parcel returns, buyer cancellation until pickup, distance-only bidder view, and platform payment credentials for bid-order checkout.
- Recorded the deferrals (delivery-fee accounting, parcel-lost action) and the decision to fix the user-account access hole first.

Files touched:

- `raw/sources/2026-10-04-livelycura-marketplace-single-delivery-decision.md`
- `wiki/sources/livelycura-marketplace-single-delivery.md`
- `log.md`

Key result:

- The marketplace single-delivery Source Record now carries the full launch rule set the implementation follows.

## [2026-10-05] implementation | Record Marketplace Single-Delivery Implementation Conventions

What changed:

- Added the implemented conventions to the LivelyCura Backend page: marketplace-order requestor with derived platform payer, settlements keyed by the accepting offer, DRAFT-until-paid publishing, same-task parcel return with custody blocks, and the dry-run-first dev-data cleanup script.

Files touched:

- `wiki/projects/livelycura-backend.md`
- `log.md`

Key result:

- Future backend work on courier finance and marketplace delivery follows the implemented single-task model.

## [2026-10-05] correction | Replace Courier Dev Cleanup With A Migration

What changed:

- The user asked to migrate existing test data instead of deleting it. The delete-first cleanup script was replaced by the registered migration `2026-10-05-single-delivery-courier-marketplace`; the backend page now names the migration.

Files touched:

- `wiki/projects/livelycura-backend.md`
- `log.md`

Key result:

- Courier and marketplace dev data is migrated in place; only untaken multi-stop route tasks are cancelled.

## [2026-10-05] implementation | Record Courier Cleanup Completion Conventions

What changed:

- Replaced the Courier Mobile convention about separate courier-company and standalone provider modes with the independent-rider model and the new Failed deliveries segment.
- Replaced the Backend note about deriving `cashRemittanceAmount` for unmigrated tasks with the stored-amount rule and the exception-review field rename from the provider-model cleanup migration.

Files touched:

- `wiki/projects/livelycura-courier-mobile.md`
- `wiki/projects/livelycura-backend.md`
- `index.md`
- `log.md`

Key result:

- Project pages match the finished courier cleanup.

## [2026-10-06] decision | Record Courier Cleanup Follow-Up Decisions

What changed:

- Recorded the user's answers on customer cancellation windows, immediate replacement delivery tasks with automatic re-request, SMS-only customer tracking at pickup with a status/timeline/ETA page, and leaving Admin Connect Users on hold.

Files touched:

- `raw/sources/2026-10-06-livelycura-courier-cleanup-decisions.md`
- `wiki/sources/livelycura-marketplace-single-delivery.md`
- `wiki/projects/livelycura-backend.md`
- `index.md`
- `log.md`

Key result:

- Backend conventions now carry the cancellation, replacement-dispatch, and tracking rules.

## [2026-10-06] implementation | Update Courier Mobile Leftover-File Note

What changed:

- Replaced the Courier Mobile note about dormant HomeHeader and AnimatedTabItem files with their deletion during the courier cleanup.

Files touched:

- `wiki/projects/livelycura-courier-mobile.md`
- `index.md`
- `log.md`

Key result:

- The project page no longer describes deleted files as present.

## [2026-10-26] decision | Record LivelyCura Match-Existing-UI Correction

What changed:

- Recorded the user's correction that new LivelyCura screens copy existing ones: placeholders instead of hint text under inputs, no extra links or shortcuts in forms, no "Private" tags or lock badges, aligned grids, and HRM date inputs as DD MMM YYYY.

Files touched:

- `raw/sources/2026-10-26-livelycura-match-existing-ui.md`
- `wiki/sources/livelycura-match-existing-ui.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/projects/serlp-mobile.md`
- `wiki/projects/livelycura-loop-app.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Portal, serlp-mobile and Loop conventions and the development manual now carry the UI-matching rule.

## [2026-10-30] update | Record Bora Remaining Funds Production Scripts

What changed:

- Recorded that production BCL now returns `BFI1100`, `BGF1100` and the new `CBF1100` alongside `BBF1100`. Fixed Income and Global Balanced received production Paystack setup and hidden fund seeds from the 30 Sep 2026 sheets, with Paystack bank code `240100` for both Fidelity accounts. `CBF1100` waits for a fact sheet and settlement account.

Files touched:

- `raw/sources/2026-10-30-bora-remaining-funds-production-scripts.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The project page no longer says `BBF1100` is the only production portfolio.

## [2026-11-03] update | Record Bora CDH Balanced Paystack Setup

What changed:

- Recorded that `CBF1100` (CDH Balanced Fund) received production Paystack setup with Republic Bank code `110100`. Its fund seed still waits for a fact sheet.

Files touched:

- `raw/sources/2026-11-03-bora-cdh-balanced-paystack.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The project page no longer says `CBF1100` has no settlement account.

## [2026-11-03] decision | Record Bora No Same-Database Guard Rule

What changed:

- Recorded the user's correction that Bora production scripts carry no guard against `PROD_MONGODB_URI` equalling `MONGODB_URI`, because the user sets both values. Agents must not add the guard, test for it, or flag its absence.

Files touched:

- `raw/sources/2026-11-03-bora-no-same-database-guard.md`
- `wiki/sources/bora-fund-administration-access-control.md`
- `wiki/projects/bora-capital-backend.md`
- `log.md`

Key result:

- The backend project page now states the rule next to the production-script conventions.

## [2026-11-04] decision | Record Bora Node 26 Runtime And Shield chain() Ban

What changed:

- Recorded the production `util.isUndefined` incident and its cause: the buildpack installed the newest Node, and graphql-shield `chain()` calls `util.isUndefined`, which Node 23 removed.
- Recorded the user's decisions: replace `chain()` with `allInOrder()` and run Node 26 LTS everywhere (`>=26.12.1 <27`).

Files touched:

- `raw/sources/2026-11-04-bora-node-26-and-shield-chain.md`
- `wiki/sources/bora-node-runtime-and-shield-composition.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- The backend project page states the Node policy and the `chain()`/`race()` ban.

## [2026-11-04] update | Record Bora Dependency Advisories Cleared

What changed:

- Recorded the user-approved dependency upgrade. The unused nodemailer senders and package were removed, `fast-uri` is pinned to 3.1.9, and `qs`, `@protobufjs/utf8` and `uuid` were refreshed. The production audit is down from 20 moderate and 7 low findings to one unreachable low (`deepmerge`).

Files touched:

- `raw/sources/2026-11-04-bora-dependency-advisories-cleared.md`
- `wiki/sources/bora-node-runtime-and-shield-composition.md`
- `index.md`
- `log.md`

Key result:

- The source record no longer lists the advisories as open.

## [2026-11-10] update | Record LivelyCura Red And Hot App Kickoff

What changed:

- Recorded the owner's new project: Red and Hot, a second branded food-ordering app copied from Check City with identical logic and its own UI later. Captured the identity-only port, the unconfirmed identity defaults, the release-setup steps (including that `eas init` does not restore `updates.url`), the adversarial review result, and inherited Check City defects left unchanged.

Files touched:

- `raw/sources/2026-11-10-livelycura-red-and-hot-app-kickoff.md`
- `wiki/sources/livelycura-red-and-hot-app-kickoff.md`
- `wiki/projects/livelycura-red-and-hot-app.md`
- `wiki/projects/livelycura-check-city-app.md`
- `index.md`
- `log.md`

Key result:

- Red and Hot has its own project page linked to Check City, with the "logic identical, fixes in both apps" convention.

## [2026-11-10] update | Record Red And Hot UI Direction

What changed:

- Recorded the owner's choice of the "Chop Bar" UI direction for Red and Hot, the rule that the UI must look totally different from Check City, what is kept (card price sticker and add button) and what is redesigned (tab bar, product card image, item detail).

Files touched:

- `raw/sources/2026-11-10-livelycura-red-and-hot-ui-direction.md`
- `wiki/sources/livelycura-red-and-hot-ui-direction.md`
- `wiki/projects/livelycura-red-and-hot-app.md`
- `index.md`
- `log.md`

Key result:

- The Red and Hot project page carries the direction, the distinctness rule and the `black` token prerequisite.

## [2026-11-10] update | Record Red And Hot Chop Bar Picks And Build

What changed:

- Recorded the owner's Chop Bar part picks (Signboard plank tab bar, Edge to edge card, Torn paper item screen, photo fill), the build into the app, and that the owner chooses designs by seeing and clicking options.

Files touched:

- `raw/sources/2026-11-10-livelycura-red-and-hot-chop-bar-picks.md`
- `wiki/sources/livelycura-red-and-hot-ui-direction.md`
- `wiki/projects/livelycura-red-and-hot-app.md`
- `log.md`

Key result:

- The Red and Hot pages carry the final picks and the pending device review.

## [2026-11-11] update | Record Red And Hot Brand Colours

What changed:

- Recorded the owner's real logo and brand colours (red and white, red and black), the R&H app icon, the Menu tab icon and the rounded tab bar corners.

Files touched:

- `raw/sources/2026-11-11-livelycura-red-and-hot-brand-colours.md`
- `wiki/sources/livelycura-red-and-hot-ui-direction.md`
- `log.md`

Key result:

- The UI direction record now carries the brand colours that replace Chop Bar's warm palette.

## [2026-11-16] update | Record Agent Workload Limit

What changed:

- Recorded the owner's limit for multi-agent runs on their 16 GB laptop (about four agents at once, a shared two-slot limiter for heavy commands, one headless Chrome at a time) and added it to the software development manual.

Files touched:

- `raw/sources/2026-11-16-agent-workload-limit-on-owner-laptop.md`
- `wiki/sources/agent-workload-limit-on-owner-laptop.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Every agent reading the manual sees the workload limit before starting a parallel run.

## [2026-11-19] ingest | Whole Fix And No Dev Test People Direction

What changed:

- Preserved the owner's direction that an approved fix is delivered whole, including review findings, without "leftovers" questions, and that agents never create test people on the shared dev database for on-screen checks.
- Added both rules to the Personal Operating Manual's change-work preferences.

Files touched:

- `raw/sources/2026-11-19-whole-fix-and-no-dev-test-people-direction.md`
- `wiki/sources/whole-fix-and-no-dev-test-people-direction.md`
- `wiki/syntheses/personal-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Every agent sees that approved fixes are finished in one pass and that on-screen checks never seed the shared dev database.

## [2026-11-20] ingest | SERLP AI Tab And Chats Drawer Direction

What changed:

- Preserved the owner's correction that SERLP AI stays a bottom tab whose tap slides in a full-screen AI screen (no header button, no swipe between pages), that the chats drawer pushes the chat aside like the Claude and ChatGPT apps, and that "tab" in the owner's action descriptions means "tap".
- Added it to the SERLP Mobile project page's durable conventions.

Files touched:

- `raw/sources/2026-11-20-serlp-ai-tab-and-chats-drawer-direction.md`
- `wiki/sources/serlp-ai-tab-and-chats-drawer-direction.md`
- `wiki/projects/serlp-mobile.md`
- `index.md`
- `log.md`

Key result:

- Every agent working on serlp-mobile sees how SERLP AI opens and how its drawer moves, and reads the owner's "tab" as "tap".

## [2026-11-20] update | SERLP AI Drawer Reference And Icons Reversal

What changed:

- Preserved the owner's follow-up: the chats drawer copies the Claude and ChatGPT iPhone apps (from screenshots and a recording), the organization and credits sit at the drawer's foot, and the arrow-up send and boxed-pencil New chat icons go back after the owner withdrew the earlier change.
- Corrected the Source Record and the SERLP Mobile convention, which still said the opposite about the icons.

Files touched:

- `raw/sources/2026-11-20-serlp-ai-drawer-reference-and-icons-reversal.md`
- `wiki/sources/serlp-ai-tab-and-chats-drawer-direction.md`
- `wiki/projects/serlp-mobile.md`
- `index.md`
- `log.md`

Key result:

- Agents see the current drawer design and icons, not the withdrawn ones.

## [2026-11-22] update | Bora Backlog Committed And Deposits Script Made Local-Only

What changed:

- Preserved the owner's "commit everything" instruction and the decision to gitignore `scripts/deposits_production`, like the other production script folders.
- Recorded commit `ca3cfa1` on `feature/updates`: the audit fixes and deposit and withdrawal backlog work that the project page listed as uncommitted, plus the 2026-11-22 handoff. Not pushed.

Files touched:

- `raw/sources/2026-11-22-bora-backlog-committed-and-deposits-script-gitignored.md`
- `wiki/sources/bora-local-only-scripts.md`
- `wiki/projects/bora-capital-backend.md`
- `index.md`
- `log.md`

Key result:

- Agents know the backlog work is committed, not loose in the working tree, and that `scripts/deposits_production` must never be committed.

## [2026-11-22] update | Bora Emails Matched Ignoring Letter Case

What changed:

- Preserved the owner's reversal of the same day's "lookups stay exact" decision and the approval of case-insensitive matching, with emails still stored and sent exactly as typed.
- Recorded the `email_ci_1` collation index, the users-query guard, the migration, the read-only production audit, and the new same-day handoff `docs/frontend-handoff-2026-11-22-emails.md`.
- Replaced the project convention that stored emails lowercase.

Files touched:

- `raw/sources/2026-11-22-bora-email-case-insensitive-matching.md`
- `wiki/projects/bora-capital-backend.md`
- `wiki/sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md`
- `wiki/sources/bora-frontend-handoff-frozen.md`
- `log.md`

Key result:

- Agents know Bora matches emails ignoring letter case and never lowercases a stored or sent email, and that the app's no-lowercase build must ship after this backend.

## [2026-11-23] ingest | Record LivelyCura HRM Roles Decide For All HRM

What changed:

- Preserved the product owner's 2026-11-23 answer verbatim: "roles decide" (HR-led through roles) now covers every HRM approval and action, including open-shift pickups, overtime and leave.
- Added a Source Record and one decision line, plus the source, on the Backend, Pharmacy Portal and SERLP Mobile pages, and an index entry.

Files touched:

- `raw/sources/2026-11-23-livelycura-hrm-roles-decide-all-hrm.md`
- `wiki/sources/livelycura-hrm-roles-decide-all-hrm.md`
- `wiki/projects/livelycura-backend.md`
- `wiki/projects/livelycura-pharmacy-portal.md`
- `wiki/projects/serlp-mobile.md`
- `index.md`
- `log.md`

Key result:

- Agents design every HRM approval and approver notification around roles at the record's branch, with organization-wide roles counting everywhere: HR runs it all where a business has an HR team, branch managers only when given the permissions.

Follow-ups:

- Check the existing HRM approvals and approver notifications against the rule.

## [2026-11-23] ingest | Record Altin Partner Glass UI Redesign

What changed:

- Preserved the user's 2026-11-23 request for a premium glassmorphism look and what the session built and verified.
- Added a Source Record; a convention, evidence line and contradiction on the Altin Partner Mobile page; one React Native glass-gotchas bullet in the development manual; and an index entry.

Files touched:

- `raw/sources/2026-11-23-altin-glass-ui-redesign.md`
- `wiki/sources/altin-glass-ui-redesign.md`
- `wiki/projects/altin-partner-mobile.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Altin Partner Mobile's look is glass over warm light, carried by theme tokens and shared components, with real blur only on non-modal chrome; agents avoid the four React Native pitfalls the pass hit.

Follow-ups:

- Check the glass on Android, where chrome falls back to opaque fills.

## [2026-11-24] ingest | Record Altin UI SERLP Reference Correction

What changed:

- Preserved the user's 2026-11-24 corrections rejecting the 2026-11-23 glassmorphism pass and naming SERLP Mobile as the reference, with the side-by-side comparison and the rebuilt shell.
- Added a Source Record; marked the glass redesign record superseded; replaced the Altin Partner Mobile look convention, contradiction and evidence lines; made SERLP the Altin UI shell reference in the development manual and added two React Native findings; updated the index.

Files touched:

- `raw/sources/2026-11-24-altin-ui-serlp-reference-correction.md`
- `wiki/sources/altin-ui-serlp-reference-correction.md`
- `wiki/sources/altin-glass-ui-redesign.md`
- `wiki/projects/altin-partner-mobile.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Altin Partner Mobile looks like SERLP Mobile: grouped surfaces, Liquid Glass only on floating controls, solid content and header fades, with no decorative glows; agents open the reference app and compare before UI work.

Follow-ups:

- Decide whether Altin moves to a newer Expo SDK for the native iOS 26 tab bar.

## [2026-11-24] update | Correct Altin UI SERLP Reference To Method, Not Copy

What changed:

- Preserved the owner's second 2026-11-24 correction: SERLP Mobile is a reference for the redesign method and quality, not a look to paste into Altin; the apps do different jobs.
- Rewrote the SERLP reference Source Record's claims around the transferable method; corrected the Altin project convention and contradiction lines, the development manual's Altin family bullet, and the index entry.

Files touched:

- `raw/sources/2026-11-24-altin-serlp-reference-not-copy.md`
- `wiki/sources/altin-ui-serlp-reference-correction.md`
- `wiki/projects/altin-partner-mobile.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Agents reuse the SERLP redesign method in Altin's own identity and never describe Altin's UI as matching SERLP.

Follow-ups:

- Owner decision on the 0.3 card border rule versus no-outline light cards.
