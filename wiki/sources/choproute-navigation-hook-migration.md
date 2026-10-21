---
type: source
status: active
created: 2026-08-07
updated: 2026-08-07
tags: [livelycura, choproute, mobile, navigation, architecture, remediation]
sources:
  - ../../raw/sources/2026-08-07-choproute-navigation-hook-migration.md
source_date: 2026-08-07
ingested: 2026-08-07
confidence: high
---

# ChopRoute Navigation Hook Migration

## Source

- Raw file: [2026-08-07-choproute-navigation-hook-migration.md](../../raw/sources/2026-08-07-choproute-navigation-hook-migration.md)
- Date: 2026-08-07
- Author: user-authorized remediation plus verified implementation
- Ingested: 2026-08-07

## Core Claims

- ChopRoute navigation actions now consistently use `useAppNavigation` or `useAppNavigationWithRef`.
- Direct React Navigation hooks remain only for route/state reads or inside the application abstraction itself.
- The migration applies to legacy screens as well as the new marketplace surfaces.

## Useful Details

- The custom bottom tab bar now calls `navigateToBottomTab`; its raised Restaurants action calls the application stack `navigate` helper.
- `useRoute` still reads typed route parameters for Explore, Category Products, Restaurant Details, Menu Item, and Order Detail.
- Root-ref notification and authentication redirects retain readiness-checked ref navigation.
- Feature-specific navigation type aliases were removed after their direct-hook consumers disappeared.

## Connections

- [[../projects/livelycura-choproute-app|LivelyCura ChopRoute App]]
- [[choproute-navigation-hook-convention|ChopRoute Navigation Hook Convention]]

## Contradictions Or Tensions

This resolves the known direct-navigation violation documented in the convention source. The remaining open typing question is an enhancement, not a blocker to abstraction compliance.

## Open Questions

- Should the app navigation hooks receive generic route/parameter typing while preserving their single abstraction boundary?
