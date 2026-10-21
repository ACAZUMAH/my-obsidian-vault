---
type: source
status: active
created: 2026-08-07
updated: 2026-08-07
tags: [livelycura, choproute, mobile, marketplace, graphql, redux, architecture, correction]
sources:
  - ../../raw/sources/2026-08-07-choproute-feature-owned-catalog-queries.md
source_date: 2026-08-07
ingested: 2026-08-07
confidence: high
---

# ChopRoute Feature-Owned Catalog Queries

## Source

- Raw file: [2026-08-07-choproute-feature-owned-catalog-queries.md](../../raw/sources/2026-08-07-choproute-feature-owned-catalog-queries.md)
- Date: 2026-08-07
- Author: user correction plus verified implementation
- Ingested: 2026-08-07

## Core Claims

- The only general marketplace hook is the Redux state hook `src/hooks/useMarketPlace.ts`.
- Product and category GraphQL operations belong to their consuming feature hooks folders, not global hooks.
- Home must load products and categories through separate query hooks.
- Every feature query derives allowed organization IDs from the Redux marketplace organization list.

## Useful Details

- Home uses the user's existing `useMarketplaceProducts.ts` and `useMarketplaceCategories.ts` files.
- Explore and Restaurant Details also separate product and category operations because they consume both datasets.
- Restaurants and Category Products own only product operations because those screens do not independently need a category-list request.
- Restaurant-specific hooks fail closed by skipping their queries when the routed organization is absent from Redux access state.

## Connections

- [[../projects/livelycura-choproute-app|LivelyCura ChopRoute App]]
- [[choproute-redux-marketplace-state-correction|ChopRoute Redux Marketplace State Correction]]
- [[choproute-marketplace-feature-folder-removal|ChopRoute Marketplace Feature Folder Removal]]

## Contradictions Or Tensions

This supersedes the transitional relocation of the combined catalog query to `src/hooks/useMarketplaceCatalogQuery.ts`. Shared main folders remain valid for genuinely shared presentation/helpers, but not for feature data operations.

## Open Questions

- Should the shared category-name fallback be removed once all ERP products have authoritative category relationships?
