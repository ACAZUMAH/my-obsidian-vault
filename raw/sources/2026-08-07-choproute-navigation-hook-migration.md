# ChopRoute Navigation Hook Migration

Date: 2026-08-07

## Authorized Remediation

Use the existing application navigation hooks everywhere instead of leaving the direct React Navigation calls as a documented follow-up.

## Implemented Scope

- Replaced direct feature `useNavigation` actions across Home, Explore, Category Products, Restaurants, Restaurant Details, Menu Item, Cart, Orders, Order Detail, Profile, Notifications, shared profile navigation, and the custom bottom tab bar.
- Mounted React code now uses `useAppNavigation` for stack pushes, Back, and tab jumps.
- Existing notification/root-reset flows continue to use `useAppNavigationWithRef`.
- Direct `useRoute` and `useNavigationState` remain only for route/state reads.
- Removed obsolete feature-specific navigation prop aliases that existed only for direct `useNavigation` typing.

## Verification

- Repository search found direct `useNavigation` only inside `src/hooks/useAppNavigation.ts` itself.
- Remaining navigation-action matches are calls on the two application abstractions.
- Relaxed-unused TypeScript and `git diff --check` passed.
- The iOS Simulator reloaded and rendered the populated Home screen after the migration.
- Strict TypeScript remained blocked only by the pre-existing unused `theme` parameter in `src/restaurantsDetails/components/RestaurantMenuItem.tsx`.
