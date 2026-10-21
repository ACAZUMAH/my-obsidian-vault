---
type: source
status: active
created: 2026-08-07
updated: 2026-08-07
tags: [livelycura, choproute, mobile, navigation, architecture, correction]
sources:
  - ../../raw/sources/2026-08-07-choproute-navigation-hook-convention.md
source_date: 2026-08-07
ingested: 2026-08-07
confidence: high
---

# ChopRoute Navigation Hook Convention

## Source

- Raw file: [2026-08-07-choproute-navigation-hook-convention.md](../../raw/sources/2026-08-07-choproute-navigation-hook-convention.md)
- Date: 2026-08-07
- Author: user correction plus current-code inspection
- Ingested: 2026-08-07

## Core Claims

- ChopRoute navigation actions must use the application abstractions `useAppNavigation` or `useAppNavigationWithRef`.
- Feature code must not bypass them with direct `useNavigation` merely to obtain route-specific typing.
- Route-parameter reads may still use `useRoute` because that is not an action abstraction.

## Useful Details

- `useAppNavigation` exposes stack push, tab jump, stack pop, and stack replace actions for mounted React code.
- `useAppNavigationWithRef` exposes root-ref push, tab jump, and replace actions after checking navigation readiness.
- The direct navigation violations identified during inspection were subsequently removed across both new and legacy screens by [[choproute-navigation-hook-migration|ChopRoute Navigation Hook Migration]].
- If the wrappers' `string`/`Object` signatures are too weak, improve their typing centrally instead of creating local exceptions.

## Connections

- [[../projects/livelycura-choproute-app|LivelyCura ChopRoute App]]
- [[choproute-explore-naming-ownership-correction|ChopRoute Explore Naming And Ownership Correction]]
- [[choproute-home-restaurants-navigation-direction|ChopRoute Home And Restaurant Navigation Direction]]

## Contradictions Or Tensions

The inspected feature implementation used direct typed React Navigation hooks. [[choproute-navigation-hook-migration|ChopRoute Navigation Hook Migration]] resolved that mismatch without treating stronger local typing as a competing convention.

## Open Questions

- Should `useAppNavigation` be generically typed against `RootStackParamList` and `BottomTabParamList` before or during navigation-call remediation?
