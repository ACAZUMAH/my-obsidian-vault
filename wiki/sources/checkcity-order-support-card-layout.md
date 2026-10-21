---
type: source
status: active
created: 2026-09-12
updated: 2026-09-14
tags: [checkcity, mobile, support, layout]
sources:
  - ../../raw/sources/2026-09-12-checkcity-order-support-card-layout.md
  - ../../raw/sources/2026-09-14-checkcity-single-order-chat.md
  - ../../raw/sources/2026-09-14-checkcity-support-conditional-rendering.md
---

# CheckCity Order Support Card Layout

## Source

- Raw file: [Direct user correction](../../raw/sources/2026-09-12-checkcity-order-support-card-layout.md)
- Raw file: [Single order chat requirement](../../raw/sources/2026-09-14-checkcity-single-order-chat.md)
- Raw file: [Conditional rendering correction](../../raw/sources/2026-09-14-checkcity-support-conditional-rendering.md)
- Dates: 2026-09-12, 2026-09-14
- Author: user
- Ingested: 2026-09-12

## Core Claims

Order support belongs inside the existing `OrderDetailHelpCard`, separated from the Help heading with a divider. Each order has one reusable conversation; show its opened or closed state and let the customer reopen a closed chat.

Support screens use the shared `Conditional` component for loading, error, conversation, and attachment branches instead of nested JSX ternaries.

## Useful Details

Keep the Help entry and existing conversation in one card. Offer new-chat creation only when the order has no conversation. A closed chat remains visible with access to its history and a reopen path.

## Connections

- [[../projects/livelycura-check-city-app|LivelyCura CheckCity App]]

## Contradictions Or Tensions

The layout correction supersedes standalone chat cards beneath the Help card. The September 14 requirement supersedes showing only active chats or offering another new-chat action for an order that already has a conversation.

## Open Questions

None.
