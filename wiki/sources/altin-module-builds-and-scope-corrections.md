---
type: source
status: active
created: 2026-10-08
updated: 2026-10-08
tags: [altin, mobile, team, accounting, billing, notifications, apollo, scope]
sources:
  - ../../raw/sources/2026-10-08-altin-module-builds-and-scope-corrections.md
confidence: high
---

# Altin Module Builds and Scope Corrections

## Source

- Raw file: [Altin module builds and scope corrections](../../raw/sources/2026-10-08-altin-module-builds-and-scope-corrections.md)
- Date: 2026-10-07 to 2026-10-08
- Author: user, through an Altin Partner Mobile Claude Code session
- Ingested: 2026-10-08

## Core Claims

- Team, Accounting, Billing, API keys, Webhooks, Notifications, and support-ticket details are built in Altin Partner Mobile; only the Reports tab and the More tab's Profile and Support rows remain placeholders.
- Team includes full views and actions: invite, change role, remove member, and role create/edit with a permissions picker. Confirmations use the ported SERLP action sheet.
- API-key and webhook secrets are shown once from local screen state and copied with `expo-clipboard`, which needs a native rebuild.
- Notifications open from the Home bell with an unread badge; tapping marks read and opens the ticket. Ticket reply is limited to the reporter, ADMIN, or members with both view and manage support-ticket permissions. Push is deferred.
- Bottom sheets slide up on open and back down on close, skipping motion under Reduce Motion.
- Every object shared with the System query must select `id`; a missing `user.id` caused the Team bounce to Home.
- User corrections: change only what was requested, and treat an unanswered proposal as declined. An explicit instruction to update or do something covers its whole reasonable scope; do it all instead of doing part and asking about the rest.

## Useful Details

- The Orders status history is a collapsible accordion: header with the latest status and update count, checked markers for passed statuses, a red ring for the current status, and no "By :" actor label. Arrival statuses use the pending tone.
- A Pressable wrapped around a sheet panel claims scroll and switch touches; the backdrop must be a separate Pressable behind the panel.
- A pressed-style function that returns an undefined `backgroundColor` overrides the styled-component fill.
- The `tests/` directory was removed in commit `e4c14fa`, but the `test:*` scripts remain in `package.json`.
- Run sessions from the repository root; the parent `C.E.Q.A` folder is not a Git repository, so diff review sees nothing.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]].
- [[altin-permission-gating|Altin Permission Gating]].
- [[../syntheses/personal-operating-manual|Personal Operating Manual]].
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]].

## Contradictions Or Tensions

- Supersedes the project summary that Team, Accounting, and Billing were placeholders, and the Commands claim that focused Orders and Outlets test suites exist.

## Open Questions

- When to add push notifications, which needs Firebase/FCM, APNs, and a rebuild.
- Whether to harden `useSystemQuery` so only the first load blocks; the user deferred it.
- Whether to change the shared keyboard-avoiding view for Android so the ticket reply composer stays visible.
