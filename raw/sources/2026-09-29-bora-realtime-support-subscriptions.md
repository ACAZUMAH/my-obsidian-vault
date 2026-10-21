# Bora Realtime Support Subscriptions — Transport And Style Decisions

Date: 2026-09-29
Source: direct user direction in Claude Code during Bora backend customer-support work

## User Direction

- The user reported that Phase 2 customer support was not live: a reply only appeared after the other party acted or refetched. Support conversations must update in real time through GraphQL subscriptions, which the backend already hosts on its WebSocket server.
- The user approved a paced plan: harden WebSocket authentication first, then the event transport, then the support subscription, then the frontend contract.
- After the transport step, the user challenged the MongoDB change-stream fan-out as unnecessary over-engineering and asked why the ordinary in-memory PubSub with event listeners was insufficient.
- The user confirmed the API is deployed on DigitalOcean App Platform and did not treat it as a multi-instance deployment.
- The user directed that the MongoDB fan-out code remain in the repository but unused, and that the active PubSub follow the ordinary LivelyCura initialization.
- The user stated that they write in a functional paradigm and do not use classes; the class-based PubSub engine was confusing and had to be rewritten.

## Agent Evidence

- LivelyCura's backend implements support subscriptions with `src/pubsub` (`new PubSub()` plus event-name constants), a post-commit `publishCustomerSupportCaseUpdated` service, a `customerSupportCaseUpdated` subscription built with `withFilter`, and Shield rules that authorize at subscribe time and per event.
- In-memory `graphql-subscriptions` PubSub is a per-process event emitter. It delivers only to subscribers connected to the same Node process. Bora's production start command runs one Node process per container, and App Platform's default component instance count is one.
- The existing Bora WebSocket server did not check session activity, did not set the client application, and applied no operation-depth limit. The graphql-ws client treats close code 4401 as fatal, so a forced close at access-token expiry would terminate every subscription every 15 minutes.
- graphql-subscriptions v3 registers PubSub listeners lazily on the iterator's first pull; events published before that pull are not delivered.

## Implemented Scope

- WebSocket connections require a known `client` and an access token supplied through `connectionParams.headers` (falling back to upgrade-request headers), verify the JWT, require an active session when the token carries a session ID, and reject disabled accounts.
- Authentication failures close with 4401; disabled accounts close with 4403.
- Session activity and account status are revalidated before each operation and before each delivered event, instead of closing sockets at token expiry.
- WebSocket operations share the HTTP depth limit and error redaction, receive a fresh context per operation, and require explicit Shield policies for every Subscription root field.
- The active `pubsub` is the in-memory `new PubSub()`, documented as single-instance only.
- An unwired functional `createMongoPubSub()` factory records identifier-only events in a TTL-bounded collection and fans them out through a resumable MongoDB change stream with capped backoff. It is excluded from the pubsub barrel so its model never loads until explicitly adopted.

## Verification

TypeScript build, Prettier, `git diff --check`, focused WebSocket and engine tests, deliberate guard mutations, and the full Jest suite passed at 114 suites and 598 tests. The change stream was not exercised against a live replica set.
