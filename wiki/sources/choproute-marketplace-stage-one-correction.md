---
type: source
status: active
created: 2026-08-06
updated: 2026-08-06
tags: [livelycura, choproute, marketplace, food-ordering, architecture]
sources:
  - ../../raw/sources/2026-08-06-choproute-marketplace-stage-one-correction.md
confidence: high
---

# ChopRoute Marketplace Stage-One Correction

## Source

- Raw file: [2026-08-06-choproute-marketplace-stage-one-correction.md](../../raw/sources/2026-08-06-choproute-marketplace-stage-one-correction.md)
- Date: 2026-08-06
- Author: User
- Ingested: 2026-08-06

## Core Claims

- Continue the existing ChopRoute marketplace plan and deliver it stage by stage.
- The existing marketplace access grant is the consumer catalog boundary: active access organizations contribute their ordinary ERP products directly.
- ChopRoute must not introduce `FoodMerchant`, `FoodMerchantBranch`, `FoodMenuListing`, duplicated modifier models, a duplicate food-marketplace checkout, allocation, payout models, procurement bidding, `MarketplaceProduct`, or product-linking for this consumer catalog.
- ERP organization and facility data remain authoritative. The consumer app selects a delivery location and does not own branch selection for delivery.
- Future order orchestration resolves the closest eligible organization facility on the server; explicit branch selection is reserved for a possible pickup flow.
- Stage one contains only marketplace-aware product discovery and the ChopRoute UI redesign. Ordering remains intentionally gated until its own stage.

## Useful Details

- Check City and Pice Restaurant are the first two organizations granted ChopRoute access for testing; the access list must remain dynamic as more organizations are added.
- The Home header's former branch control becomes delivery-location search/GPS.
- Home and Menu remain distinct names. The bottom tabs remain Home, Menu, Cart, and Orders; only the selected tab shows a label, and Cart quantity affects only its badge.
- The established shared `MenuItem` remains the vertical product card for Home and backend-loaded Menu products; recent/favourite content keeps its separate horizontal variant.

## Connections

- [[../projects/livelycura-choproute-app|LivelyCura ChopRoute App]]
- [[pice-home-ui-direction|Pice Home UI Direction]]
- [[../projects/livelycura-backend|LivelyCura Backend]]

## Contradictions Or Tensions

- The earlier Pice-specific project identity and explicit branch header are superseded for this repository. Pice remains a prospective separate app, while ChopRoute owns the current implementation.
- Existing procurement marketplace models remain valid for their original workflows but are explicitly outside ChopRoute consumer catalog discovery.
- Branch-specific price resolution may occur server-side for display, but it must not expose a branch contract to the app or predetermine future order allocation.

## Open Questions

- What exact backend `appIdentifier` is configured for the live ChopRoute marketplace?
- What rules beyond distance will define an eligible fulfillment branch in the ordering stage?
- When ordering begins, how will one cart handle products from multiple organizations?
