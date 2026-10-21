# Bora Customer Support Administration Phase

Date: 2026-09-29
Source: direct user authorization in Codex, following the previously approved phase order

## Authorization

The user directed work to move to the next phase after Phase 1 fund administration and access control. The earlier approved plan named customer-support tickets before marketing/news administration and scheduled notification campaigns, so this phase implements customer support.

## Implemented Scope

- Add customer-owned support cases and chronological public conversations.
- Add admin queue, case detail, summary counts, public staff replies, internal notes, assignment, priority, and explicit status actions.
- Reuse the existing LivelyCura customer-support structure where applicable while removing its marketplace, organization, order, upload, subscription, and notification-event concerns from Bora's current phase.
- Add Bora categories for account, KYC, investment, deposit, withdrawal, transaction, technical, general, and other issues.
- Protect admin operations with `supportCases.read`, `supportCases.respond`, `supportCases.assign`, and `supportCases.update`, including the `supportCases.*` wildcard.
- Keep resolvers as named, documented transport delegates. Services own validation, ownership, visibility, state, persistence, and audit behavior.
- Use generated GraphQL enums and generated resolver argument types instead of repeating enum unions.
- Use client-generated request IDs to make case creation and message writes idempotent.
- Keep internal notes out of customer responses and require support-read permission for an originating customer who also signs into the admin portal.

## Deferred Scope

- Support attachments and uploads.
- Live support subscriptions.
- Automatic support push, email, or SMS notifications.
- Marketing/news administration and outbound campaigns.

## Verification

GraphQL generation, Prettier validation, TypeScript build, focused customer-support tests, GraphQL root-policy coverage, and the full Jest suite passed. The full suite completed 112 suites and 575 tests.
