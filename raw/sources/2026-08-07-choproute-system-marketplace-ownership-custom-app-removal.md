# ChopRoute System Marketplace Ownership And Custom-App Removal

Date: 2026-08-07

## Direct Correction

Remove the remaining custom-app client feature from ChopRoute.

The current marketplace and its access-granted organizations must be loaded during system startup, beside the existing user bootstrap flow. Their reusable Redux access must be exposed through one general hook in the top-level `src/hooks` folder. Marketplace feature code must not own application bootstrap, a provider-like gate, or its own general state hook.

Follow the repository's established structure rather than inventing feature-local ownership for application-wide concerns.

## Implemented Interpretation

- `src/system/useMarketplaceQuery.ts` owns the startup GraphQL operation that loads both the current marketplace and its accessible organizations and synchronizes them into Redux.
- `src/system/SystemProvider.tsx` runs the user and marketplace startup queries and owns the application render gate.
- `src/hooks/useMarketPlace.ts` is the one general Redux hook for reading and updating marketplace state.
- `src/marketplace` retains marketplace catalog/domain behavior only; it no longer owns bootstrap or a general Redux selector hook.
- The obsolete `src/customApp` client feature and the unused custom-app-specific banner loading/event infrastructure were removed.
- Generated GraphQL schema types may still mention CustomApp because the mobile repository consumes a shared backend schema; generated files are not client feature ownership and must not be hand-edited.

## Verification

- Focused formatting passed.
- `git diff --check` passed.
- TypeScript passed with unused-local checks disabled to isolate this change.
- The iOS Simulator opened the live ChopRoute Home screen after the new system bootstrap completed, showing marketplace products and categories.
- Strict TypeScript remained blocked only by the pre-existing unused `theme` parameter in `src/restaurantsDetails/components/RestaurantMenuItem.tsx`.
