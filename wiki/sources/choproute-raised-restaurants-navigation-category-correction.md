---
type: source
status: active
created: 2026-08-06
updated: 2026-08-06
tags: [livelycura, choproute, navigation, categories, marketplace]
sources:
  - ../../raw/sources/2026-08-06-choproute-raised-restaurants-navigation-category-correction.md
  - ../../raw/sources/2026-08-06-choproute-shaped-tab-shelf-category-group-correction.md
confidence: high
---

# ChopRoute Raised Restaurants Navigation And Category Correction

## Source

- Raw file: [2026-08-06-choproute-raised-restaurants-navigation-category-correction.md](../../raw/sources/2026-08-06-choproute-raised-restaurants-navigation-category-correction.md)
- Correction: [2026-08-06-choproute-shaped-tab-shelf-category-group-correction.md](../../raw/sources/2026-08-06-choproute-shaped-tab-shelf-category-group-correction.md)
- Date: 2026-08-06
- Author: User
- Ingested: 2026-08-06

## Core Claims

- Home, Explore, Cart, and Orders are the actual bottom-tab routes. Restaurants is a raised center action that opens a standalone root-stack screen outside the bottom navigator.
- The navigation follows a full-width shelf with two labeled controls on each side of the raised center Restaurants action.
- The shelf border is one continuous shape that curves down around the center action and reconnects to both tab groups; a circle overlapping a straight divider is not an acceptable approximation.
- ChopRoute category discovery reads active ordinary ERP categories for organizations with active marketplace access; it does not infer the available filter list only from returned products.
- Home must render product rails under its discovered category groups below Popular and the marketing section.
- New work must preserve newer live user edits instead of restoring an earlier agent-authored version.

## Useful Details

- The standalone Restaurants screen owns its Back action. Closing it returns to the unchanged bottom-tab state rather than selecting a fifth tab.
- Requested organization filters are intersected with active marketplace access before category reads, matching product access isolation.
- Same-name categories across organizations are merged into one marketplace-facing filter while retaining every underlying category ID.
- Explicit ERP product-category relationships remain authoritative. For the current uncategorized test products only, a whole-name match keeps clearly named meals visible in Home, Explore filters, and category detail until ERP assignments are populated.

## Connections

- [[../projects/livelycura-choproute-app|LivelyCura ChopRoute App]]
- [[choproute-home-restaurants-navigation-direction|ChopRoute Home And Restaurant Navigation Direction]]
- [[choproute-marketplace-stage-one-correction|ChopRoute Marketplace Stage-One Correction]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]

## Contradictions Or Tensions

- The earlier five-tab Restaurants contract is superseded. Restaurants remains first-class navigation, but it is a center action into the root stack rather than a bottom-tab route.
- The earlier selected-route-only label rule is superseded for this navigation by the newest supplied reference, which keeps all four ordinary labels visible.
- Earlier category discovery depended on product-category relationships and could show only `All`; that is superseded by an access-scoped ERP category query.
- The earlier claim that category sections must remain empty until ERP assignments exist is superseded for the current test data by the bounded uncategorized-name fallback; it does not create marketplace product links or override real ERP relationships.

## Open Questions

- Should Home category order follow a marketplace configuration, ERP creation order, or an engagement-based ranking once more organizations join?
