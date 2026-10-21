# Bora Customer Support Subscription Contract

Date: 2026-09-29
Source: user-authorized Claude Code implementation (paced steps 3 and 4 of the realtime support plan)

## Authorization

The user approved each step with an explicit "go" after reviewing the previous one: the support subscription itself, then the frontend contract and knowledge update.

## Implemented Contract

- One subscription mirrors LivelyCura: `customerSupportCaseUpdated(filters: CustomerSupportCaseSubscriptionFilters): CustomerSupportCaseUpdateEvent!`, where the event is `{ case: CustomerSupportCase!, summary: CustomerSupportCaseSummary }` and the only filter is an optional `caseId`.
- The verified client key selects the audience. `ADMIN_PORTAL` viewers need `supportCases.read`, receive every case, see internal notes through the existing `messages` visibility rule, and receive queue counts. Other clients receive only their own cases, public messages only, a null summary, and never staff-only events.
- A post-commit `publishCustomerSupportCaseUpdated` service publishes after case creation, customer messages, staff replies, internal notes (flagged staff-only), assignment/claim, priority changes, and status transitions. Replayed creates/messages, no-op assignment/status changes, failed transactions, and read receipts publish nothing. A failed publication is logged and never fails the saved write.
- Events carry only the case ID, customer user ID, and a staff-only flag. Each subscriber's resolve loads current case state. This deviates from LivelyCura's publish-time snapshot to keep private data out of events and keep the multi-instance swap to one export.
- Stream setup calls `assertCustomerSupportSubscriptionAccess`; a Shield rule re-runs it per event and returns a 403 when access is lost.
- The frontend handoff documents the `/subscriptions` endpoint, lazy `connectionParams.headers`, close codes 4401/4403, audience rules, event triggers, error behavior, and refetch-on-reconnect.

## Technical Findings

- graphql-middleware wraps a Subscription field's custom `resolve` instead of its `subscribe`. Shield therefore evaluates such fields per event, and stream setup must be guarded separately.
- graphql-shield replaces an error thrown inside a rule with its generic `Not Authorised!` error; only a returned error reaches the client.
- Bora's Shield configuration has no `fallbackError`. Every denial therefore becomes the generic error, which `formatGraphqlErrors` maps to `INTERNAL_SERVER_ERROR` and reports to Sentry. This was verified on an unauthenticated protected query and left for a separate task.

## Verification

Six end-to-end tests over the real schema, Shield, WebSocket server, and graphql-ws client, plus nineteen publishing and filter tests. Four deliberate guard removals each failed tests. GraphQL generation, TypeScript build, Prettier, `git diff --check`, and the full suite passed at 116 suites and 623 tests. All twelve GraphQL blocks in the frontend handoff validated against the schema with the depth limit.
