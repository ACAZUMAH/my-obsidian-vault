---
type: source
status: active
created: 2026-08-06
updated: 2026-08-06
tags: [livelycura, choproute, explore, navigation, feature-ownership]
sources:
  - ../../raw/sources/2026-08-06-choproute-explore-naming-ownership-correction.md
  - ../../raw/sources/2026-08-06-choproute-explore-feature-structure-correction.md
confidence: high
---

# ChopRoute Explore Naming And Ownership Correction

## Source

- Raw file: [2026-08-06-choproute-explore-naming-ownership-correction.md](../../raw/sources/2026-08-06-choproute-explore-naming-ownership-correction.md)
- Correction: [2026-08-06-choproute-explore-feature-structure-correction.md](../../raw/sources/2026-08-06-choproute-explore-feature-structure-correction.md)
- Date: 2026-08-06
- Author: User
- Ingested: 2026-08-06

## Core Claims

- Explore is the canonical customer-facing browse tab and route; Menu is not a parallel tab identity.
- Explore owns its screen, search, filters, hooks, types, transformations, and constants under `src/explore`, separated through the established `components`, `hooks`, `interfaces`, `helpers`, and `constants` subfolders.
- Obsolete top-level `src/menu`, `src/search`, and standalone `src/categories` browse implementations must not remain active beside Explore.
- The Explore header places a search bar and separate filter button side by side.

## Useful Details

- Cross-entry catalog state remains in `src/marketplace`, the canonical product card remains in `src/components/menu-item`, and product detail remains shared because Home, category grids, restaurants, and Explore all use them.
- “Remove unnecessary folders” means remove obsolete competing top-level browse features; it does not authorize flattening a feature or bypassing the repository's internal ownership convention.
- The same correction applies to the new `categoryProducts` and `restaurants` features: screens compose owned components and hooks while transformations, types, and constants remain in their established subfolders.
- Category chips derive from ordinary backend product-category relationships rather than a duplicate Explore catalog.

## Connections

- [[../projects/livelycura-choproute-app|LivelyCura ChopRoute App]]
- [[choproute-home-restaurants-navigation-direction|ChopRoute Home And Restaurant Navigation Direction]]
- [[choproute-marketplace-stage-one-correction|ChopRoute Marketplace Stage-One Correction]]

## Contradictions Or Tensions

- Earlier ChopRoute notes used Menu as the full-catalog tab name. That wording is superseded by Explore; restaurant detail may still use “Menu” as a content-section label.
- The first ownership record incorrectly interpreted “unnecessary folders” as a flat-feature directive. The direct correction supersedes that interpretation and requires the established feature subfolders.
- Shared product-detail and catalog infrastructure should not be forced into `src/explore`, because doing so would incorrectly assign cross-feature code to one entry route.

## Open Questions

- Which additional filters, beyond backend categories, should Explore support after the catalog data is populated?
