---
type: source
status: active
created: 2026-08-07
updated: 2026-08-07
tags: [livelycura, choproute, marketplace, redux, architecture]
sources:
  - ../../raw/sources/2026-08-07-choproute-redux-marketplace-state-correction.md
confidence: high
---

# ChopRoute Redux Marketplace State Correction

## Source

- Raw file: [2026-08-07-choproute-redux-marketplace-state-correction.md](../../raw/sources/2026-08-07-choproute-redux-marketplace-state-correction.md)
- Date: 2026-08-07
- Author: User
- Ingested: 2026-08-07

## Core Claims

- The current ChopRoute marketplace and its access-granted organizations are application state and must live in Redux, not React context.
- The correction must be implemented one stage at a time: Redux ownership first, then Home product and category query separation.
- Home will own separate product and category query files in the next stage instead of continuing to consume one combined catalog query.

## Useful Details

- The Redux bootstrap query can load the current marketplace and accessible organizations together because both define the app-wide marketplace boundary.
- Product and category query ownership is intentionally unchanged during the Redux-only stage.
- Screens that need the restaurant list should consume the access-granted organizations already stored in Redux rather than re-requesting them with every catalog query.

## Connections

- [[../projects/livelycura-choproute-app|LivelyCura ChopRoute App]]
- [[choproute-marketplace-stage-one-correction|ChopRoute Marketplace Stage-One Correction]]
- [[choproute-explore-naming-ownership-correction|ChopRoute Explore Naming And Ownership Correction]]

## Contradictions Or Tensions

- The first ChopRoute implementation used `MarketplaceContext` and a `MarketplaceProvider`. That implementation is superseded by the Redux marketplace slice and bootstrap component.
- The current combined product/category catalog query remains temporarily active only because the user explicitly sequenced its replacement after the Redux correction.

## Open Questions

- After Home receives separate product and category query files, which query ownership should Explore, category detail, and restaurant detail use without duplicating operations unnecessarily?
