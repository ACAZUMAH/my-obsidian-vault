---
type: source
status: active
created: 2026-09-29
updated: 2026-09-29
tags: [bora-capital, backend, graphql, subscriptions, websocket, code-style]
sources:
  - ../../raw/sources/2026-09-29-bora-realtime-support-subscriptions.md
  - ../../raw/sources/2026-09-29-bora-support-subscription-contract.md
confidence: high
---

# Bora Realtime Support Subscriptions

## Source

- Raw file: [2026-09-29-bora-realtime-support-subscriptions.md](../../raw/sources/2026-09-29-bora-realtime-support-subscriptions.md)
- Raw file: [2026-09-29-bora-support-subscription-contract.md](../../raw/sources/2026-09-29-bora-support-subscription-contract.md)
- Date: 2026-09-29
- Author: direct user direction with Claude Code implementation
- Ingested: 2026-09-29

## Core Claims

- Customer support must update live through GraphQL subscriptions; polling or refetch alone is not an acceptable conversation experience.
- Bora's active PubSub is LivelyCura's ordinary in-memory `new PubSub()`. It is correct because the API runs as one Node process on a single App Platform instance.
- A functional `createMongoPubSub()` change-stream fan-out remains in the repository, unwired, for a future multi-instance deployment. Adopting it is a one-line swap of the exported `pubsub`.
- WebSocket connections are authenticated to the same standard as HTTP: known client, verified access token, active session, and enabled account. Session and account status are revalidated before every operation and every delivered event.
- The user writes functional code and does not author classes. Factories with closure state replace classes, including test fakes.
- The live contract is one LivelyCura-shaped subscription, `customerSupportCaseUpdated(filters: { caseId })`, returning `{ case, summary }`. The verified `ADMIN_PORTAL` client with `supportCases.read` receives every case, internal notes, and queue counts; other clients receive only their own cases, public messages, and no staff-only events.
- Writes publish after commit. Events carry identifiers only, and each subscriber loads current case state; replays, no-op changes, failed transactions, and read receipts publish nothing.

## Useful Details

- Clients send `connectionParams: { headers: { authorization, client } }`. Close code 4401 means re-authenticate and reconnect; 4403 means the account is disabled.
- Forced socket closure at 15-minute token expiry was rejected because the graphql-ws client treats 4401 as fatal and would terminate every subscription on each expiry.
- WebSocket operations share the HTTP depth limit and error redaction. Every Subscription root field needs an explicit Shield policy, enforced by the root-policy coverage test.
- graphql-subscriptions v3 registers listeners on the first iterator pull, so clients must refetch after subscribing or reconnecting to cover missed events.
- graphql-middleware wraps a Subscription field's custom `resolve`, not its `subscribe`, so Shield runs per event and stream setup calls the access service directly. Losing `supportCases.read` turns later events into `FORBIDDEN` errors.
- graphql-shield replaces errors thrown inside rules with a generic `Not Authorised!`; the rule returns its 403 instead. Bora's missing `fallbackError` makes every other Shield denial surface as `INTERNAL_SERVER_ERROR` and report to Sentry.
- The frontend handoff is `docs/customer-support-api.md` → Live updates.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[bora-customer-support-administration|Bora Customer Support Administration]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]

## Contradictions Or Tensions

- The Phase 2 support record deferred live subscriptions; this direction brings them into the support scope.
- Event payloads deviate from LivelyCura's publish-time document snapshot: identifiers keep private data out of events and keep the multi-instance swap to one export, at one read per event per subscriber.
- A multi-instance deployment was inferred from Mongo-backed cooldowns and a change-stream engine was built before the instance count was confirmed. The user rejected it as unnecessary for the current deployment; confirm instance count before choosing cross-process infrastructure.

## Open Questions

- Should Shield denials across Bora return `UNAUTHORIZED`/`FORBIDDEN` through a configured `fallbackError` instead of the current generic 500?
- If App Platform instance count or autoscaling is ever raised, will the team adopt `createMongoPubSub()` or introduce Redis, and has the MongoDB tier's change-stream support been verified?
