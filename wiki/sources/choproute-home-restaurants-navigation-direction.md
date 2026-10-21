---
type: source
status: active
created: 2026-08-06
updated: 2026-08-06
tags: [livelycura, choproute, food-marketplace, navigation, product-design]
sources:
  - ../../raw/sources/2026-08-06-choproute-home-restaurants-navigation-direction.md
  - ../../raw/sources/2026-08-06-choproute-shaped-tab-shelf-category-group-correction.md
confidence: high
---

# ChopRoute Home And Restaurant Navigation Direction

## Source

- Raw file: [2026-08-06-choproute-home-restaurants-navigation-direction.md](../../raw/sources/2026-08-06-choproute-home-restaurants-navigation-direction.md)
- Correction: [2026-08-06-choproute-shaped-tab-shelf-category-group-correction.md](../../raw/sources/2026-08-06-choproute-shaped-tab-shelf-category-group-correction.md)
- Date: 2026-08-06
- Author: User
- Ingested: 2026-08-06

## Core Claims

- Home is product-led and must not display restaurant cards.
- Home order is Categories, Popular, then up to four category product rails with about five products each; a secondary campaign may remain between product sections.
- Popular `View all` is the only Home shortcut to the full Explore catalog. Category actions open category-specific product grids.
- Restaurant discovery opens from the raised center action into a standalone stack screen. Selecting a restaurant opens an organization-scoped menu with category filters.
- Restaurant cards use compact, bright, image-led compositions, and restaurant detail uses the supplied expand/fade transition direction.
- All product surfaces continue to use the canonical shared backend-driven `MenuItem`.

## Useful Details

- Restaurant detail filtering requires an organization ID, but the backend must intersect requested IDs with organizations that have active access to the current ChopRoute marketplace.
- The restaurant detail contract does not expose facilities. Delivery still resolves the closest eligible branch behind the server boundary.
- Home category sections use the shared marketplace category matcher. ERP product-category relationships are authoritative; only clearly named products with no relationships use the bounded display fallback, without creating a duplicate or hard-coded marketplace catalog.

## Connections

- [[../projects/livelycura-choproute-app|LivelyCura ChopRoute App]]
- [[choproute-marketplace-stage-one-correction|ChopRoute Marketplace Stage-One Correction]]
- [[pice-home-ui-direction|Pice Home UI Direction]]

## Contradictions Or Tensions

- The previous temporary Home restaurant rail is superseded; organizations remain discoverable only through the raised Restaurants action.
- The previous Menu-tab wording and five-tab interpretation are superseded: Home, Explore, Cart, and Orders are the true tabs, while Restaurants is the raised center stack action. The newest reference keeps the four ordinary labels visible.
- The earlier `All`-only test-data limitation is superseded. Accessible categories are read directly, and the current uncategorized, clearly named test meals populate their matching Home, Explore, and category-detail groups.

## Open Questions

- What server signal will define Popular ordering instead of the current catalog order?
- Should Home's four category sections be selected by configuration, ranking, or stable backend order?
