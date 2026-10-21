---
type: concept
status: active
created: 2026-08-30
updated: 2026-08-30
tags: [livelycura, customer-support, crm, marketplace, tenancy, notifications]
sources: []
confidence: high
related:
  - "[[../projects/livelycura-backend]]"
  - "[[../projects/livelycura-admin-portal]]"
  - "[[../projects/livelycura-pharmacy-portal]]"
  - "[[../projects/livelycura-customer-portal]]"
  - "[[../projects/livelycura-customer-mobile]]"
  - "[[../projects/livelycura-check-city-app]]"
  - "[[../projects/livelycura-choproute-app]]"
---

# LivelyCura Customer Support Architecture

## Working Definition

One audited, threaded, tenant-aware support-case domain serves every authenticated customer frontend. The verified backend client context selects the support owner and channel; customers and frontend input never select the destination.

## Current Synthesis

- LivelyCura Customer Mobile and Customer Portal create marketplace-owned cases handled in the Admin Portal.
- ChopRoute direct-order cases remain marketplace-owned because the verified ChopRoute client carries a marketplace identity, even though an organization fulfills the order.
- CheckCity cases are organization-owned and handled in Pharmacy Portal under CRM at organization scope.
- `ORGANIZATION_STOREFRONT` is reserved for a shared future storefront; those cases are organization-owned and reuse the ERP CRM queue without a domain redesign.
- Customer list/detail access is scoped by customer, owner, and verified source client key. Responder queues span every channel owned by the authorized marketplace or organization.
- Public replies and agent-only internal notes share one case thread, but customer queries and customer notifications exclude internal notes.
- Replies reopen resolved cases for customers; agent replies move cases to in-progress; only agents resolve cases.
- Create/reply mutations use client request IDs, including duplicate-key recovery for simultaneous retries.
- Support attachments are private JPEG, PNG, or WebP uploads: at most five per public message and at most 5 MiB each. Authorized URLs are resolved only through an already-authorized case thread.
- Support notifications use privacy-safe previews, strict entity routes, mobile push, Admin/ERP/customer web push, in-app records, and email. Message bodies, attachments, and internal notes are excluded from customer previews.
- Admin support access is marketplace-scoped and permission-protected. ERP support is organization-scoped and permission-protected but deliberately bypasses the general CRM-module gate so organizations with customer channels or historical cases retain access.

## Supporting Sources

- Direct user architecture and implementation request on 2026-08-30.
- Current support-domain, notification, GraphQL, portal, and Expo application source across the linked projects.

## Related

- [[../projects/livelycura-backend|LivelyCura Backend]]
- [[../projects/livelycura-admin-portal|LivelyCura Admin Portal]]
- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]]
- [[../projects/livelycura-customer-portal|LivelyCura Customer Portal]]
- [[../projects/livelycura-customer-mobile|LivelyCura Customer Mobile]]
- [[../projects/livelycura-check-city-app|LivelyCura CheckCity App]]
- [[../projects/livelycura-choproute-app|LivelyCura ChopRoute App]]

## Open Questions

- When should SLA policies, automatic assignment, transfer between owners, chatbot intake, guest intake, and configurable retention enter the domain?
- What eligibility rule should automatically grant `supportCases.*` to organization owners when a customer channel is first enabled?
