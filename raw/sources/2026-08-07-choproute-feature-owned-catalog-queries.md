# ChopRoute Feature-Owned Catalog Queries

Date: 2026-08-07

## Direct Correction

Do not move the former combined marketplace catalog query into the global `src/hooks` folder.

Home already has `src/home/hooks/useMarketplaceProducts.ts` and `src/home/hooks/useMarketplaceCategories.ts`; populate those files and query products and categories separately. Each remaining consumer feature must follow the same ownership rule: read the access-granted organizations from Redux and run the product/category queries it needs from its own hooks folder.

Remove `src/hooks/useMarketplaceCatalogQuery.ts` and its global catalog-filter interface.

## Implemented Interpretation

- Home independently loads products and categories through the two existing Home hook files.
- Explore owns separate product and category query hooks.
- Restaurants owns its product query and reads the organization list from Redux.
- Category Products owns its category-filtered product query.
- Restaurant Details owns separate organization-scoped product and category query hooks.
- Every query builds its allowed `organizationIds` from the Redux marketplace organization list; restaurant-specific queries verify the route organization exists in that list before running.
- Removed the global combined catalog query and its shared filter interface.
- Preserved shared presentation components and the shared client-side category matcher where they are still genuinely reused.

## Verification

- Relaxed-unused TypeScript and `git diff --check` passed.
- Repository search found no `useMarketplaceCatalogQuery` or `MarketplaceCatalogFilters` references.
- The iOS Simulator rendered the populated Home screen using the independent Home queries.
- Strict TypeScript remained blocked only by the pre-existing unused `theme` parameter in `src/restaurantsDetails/components/RestaurantMenuItem.tsx`.
