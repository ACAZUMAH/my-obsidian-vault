---
type: source
status: active
created: 2026-09-29
updated: 2026-09-29
tags: [bora-capital, backend, customer-support, admin-portal, graphql]
sources:
  - ../../raw/sources/2026-09-29-bora-customer-support-administration.md
confidence: high
---

# Bora Customer Support Administration

## Source

- Raw file: [2026-09-29-bora-customer-support-administration.md](../../raw/sources/2026-09-29-bora-customer-support-administration.md)
- Date: 2026-09-29
- Author: user-authorized Codex implementation
- Ingested: 2026-09-29

## Core Claims

- Bora's second administration phase adds customer-owned support cases plus a permission-controlled staff queue and conversation workflow.
- Customer reads and writes remain bound to the authenticated principal. Internal notes are excluded from customer responses and require `supportCases.read` in the admin view.
- Staff capabilities are separated into `supportCases.read`, `supportCases.respond`, `supportCases.assign`, and `supportCases.update`, with request-time role/direct-grant resolution and namespace wildcard support inherited from Phase 1.
- Case creation and public/internal replies accept client-generated request IDs so retries return existing records instead of duplicating writes.
- Named, documented resolvers only forward generated GraphQL inputs and authenticated IDs. Documented services own validation, ownership, state transitions, message visibility, persistence, and security auditing.

## Useful Details

- Customer categories are `GENERAL`, `ACCOUNT`, `KYC`, `INVESTMENT`, `DEPOSIT`, `WITHDRAWAL`, `TRANSACTION`, `TECHNICAL`, and `OTHER`.
- Case statuses are `OPEN`, `IN_PROGRESS`, `WAITING_FOR_CUSTOMER`, and `RESOLVED`; priorities are `LOW`, `NORMAL`, `HIGH`, and `URGENT`.
- A staff public reply moves a case to `IN_PROGRESS`. Staff reopen a resolved case before replying; a customer reply automatically reopens a resolved case as `OPEN`.
- The queue supports status, priority, category, assignee, assigned/unassigned, response-needed, text search, and pagination filters. Summary counts cover unresolved, unassigned, urgent, and response-needed cases.
- The implementation adapts LivelyCura's current customer-support structure but intentionally excludes LivelyCura-specific marketplace/organization ownership, order references, uploads, subscriptions, and notification materialization.
- Verification completed GraphQL generation, formatting, TypeScript build, focused support/security coverage, and 112 Jest suites/575 tests.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[bora-fund-administration-access-control|Bora Fund Administration And Access Control]]

## Contradictions Or Tensions

- The broader roadmap includes push, email, and SMS campaigns, but this support phase deliberately ships polling/refetch APIs without automatic support notifications or live subscriptions.
- Superseded on 2026-09-29: live support subscriptions were added. Attachments and automatic support notifications remain deferred. See [[bora-realtime-support-subscriptions|Bora Realtime Support Subscriptions]].
- A user may have both customer and admin channels. Internal-note visibility therefore checks the admin client boundary and support-read authority rather than assuming every admin-channel user is a support responder.

## Open Questions

- Should the next support increment add attachments, subscriptions, and automatic support notifications before marketing/news administration begins?
- What retention, SLA, escalation, and archival rules should apply to resolved customer-support cases?
