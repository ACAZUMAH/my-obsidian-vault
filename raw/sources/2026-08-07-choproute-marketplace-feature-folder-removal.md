# ChopRoute Marketplace Feature Folder Removal

Date: 2026-08-07

## Direct Correction

After marketplace identity/access loading moved into `src/system` and general Redux access moved into `src/hooks`, the user challenged why a top-level `src/marketplace` feature folder still existed.

The folder was leftover temporary ownership and must be removed. Shared catalog pieces belong in the repository's established top-level `components`, `hooks`, `helpers`, and `interfaces` folders. This relocation must not redesign the visible UI or change query behavior.

## Implemented Interpretation

- Removed the physical `src/marketplace` directory.
- Moved shared catalog loading, error, and empty components to `src/components/catalog`.
- Moved the shared catalog query to `src/hooks/useMarketplaceCatalogQuery.ts`.
- Moved its filter contract to `src/interfaces/marketplace.ts`.
- Moved the shared category matcher to `src/helpers/getMarketplaceProductsForCategory.ts`.
- Moved temporary Cart/Orders stage screens to the shared components layer instead of retaining marketplace-feature ownership.
- Updated Home, Explore, category products, Restaurants, restaurant details, navigation, and checkout imports without changing runtime behavior.

## Verification

- Repository search found no imports from `src/marketplace`.
- The `src/marketplace` filesystem directory no longer exists.
- Focused formatting, relaxed-unused TypeScript, and `git diff --check` passed.
- Strict TypeScript remains blocked only by the pre-existing unused `theme` parameter in `src/restaurantsDetails/components/RestaurantMenuItem.tsx`.
