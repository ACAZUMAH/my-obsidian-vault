# ChopRoute Navigation Hook Convention

Date: 2026-08-07

## Direct Correction

ChopRoute already provides `src/hooks/useAppNavigation.ts` and `src/hooks/useAppNavigationWithRef.ts`. All navigation actions are supposed to go through those abstractions rather than importing React Navigation's `useNavigation` directly in feature screens and hooks.

## Current Mismatch

Home, Explore, Category Products, Restaurants, and Restaurant Details currently call typed `useNavigation` directly. That happened because route-specific typing and nested parameters were prioritized over the established application wrapper. This was not a valid architectural reason to bypass the project convention.

## Intended Ownership

- Use `useAppNavigation` for navigation actions initiated by mounted React components and hooks.
- Use `useAppNavigationWithRef` for navigation that must occur through the root navigation ref, such as notification/external flows or code without the mounted screen navigation object.
- `useRoute` remains valid for reading route parameters because neither app navigation hook exposes route state.
- Home's Explore action should use `navigateToBottomTab`.
- Stack destinations should use `navigate`, Back should use `navigateBack`, and replacements should use `navigateByReplace`.
- If stronger route/parameter typing is required, improve the application navigation hooks rather than bypassing them.

## Scope

This record documents the correction only. No navigation code was changed during the explanatory turn.
