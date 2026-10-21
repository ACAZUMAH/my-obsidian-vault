---
type: source
status: active
created: 2026-09-21
updated: 2026-09-26
tags: [livelycura, graphql, compatibility, crm, courier]
sources:
  - ../../raw/sources/2026-09-21-livelycura-graphql-contract-compatibility-fixes.md
  - ../../raw/sources/2026-09-26-livelycura-courier-requestor-identity-correction.md
confidence: high
---

# LivelyCura GraphQL Contract Compatibility

## Source

- Raw file: [GraphQL contract compatibility fixes](../../raw/sources/2026-09-21-livelycura-graphql-contract-compatibility-fixes.md)
- Correction: [Courier requestor identity](../../raw/sources/2026-09-26-livelycura-courier-requestor-identity-correction.md)
- Date: 2026-09-21
- Author: User
- Ingested: 2026-09-21

## Core Claims

- A retired value stored inside a GraphQL enum list must not break serialization of the containing record. While deliberate data cleanup is deferred, return only values represented by the current enum instead of restoring the retired public value.
- Client GraphQL operations must match the live backend contract. Removing a backend field requires removing its client selections, filters, presentation, generated typings, and fixtures.
- Admin Courier manages platform riders. `DeliveryAgent` no longer exposes company-provider `agentType`, organization ownership, facility ownership, or external-request opt-in fields.
- Courier delivery requestors remain `Customer`, `Facility`, and `Organization`. Requestor references identify the requesting party for delivery, order, billing, and remittance workflows; they do not restore company ownership of riders or courier fulfillment.

## Useful Details

- `MarketingMessage.app` filters historical `CUSTOMER` entries at the GraphQL field boundary, preserving the rest of each CRM message.
- Admin Courier list and detail operations no longer request or display `agentType`; the obsolete rider-type filter and generated contract fields are also removed.
- Delivery-task creation and reads preserve `facilityId`/`facility` alongside customer and organization requestor references. Enum resolvers map each supported value explicitly and must not rewrite Facility records as Organization.
- Focused backend contract tests, backend type-check, Admin Courier table tests, and the Admin production build verify the correction.

## Connections

- [[../projects/livelycura-backend|LivelyCura Backend]]
- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]]
- [[../projects/livelycura-admin-portal|LivelyCura Admin Portal]]
- [[livelycura-independent-fleet-and-platform-dispatch|LivelyCura Independent Fleet And Platform Dispatch]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]

## Contradictions Or Tensions

The general preference is to normalize invalid persisted non-null GraphQL data. This compatibility boundary applies because cleanup of retired application enum values is deliberately deferred; it does not make silent fallback resolvers the default.

## Open Questions

- When should historical marketing-message `CUSTOMER` values receive explicit data cleanup?
