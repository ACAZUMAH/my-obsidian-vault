# ChopRoute Shaped Tab Shelf And Category Group Correction

Date: 2026-08-06
Author: User

## Direct Correction

- The raised Restaurants action must not be implemented as a circle overlapping a straight tab-bar divider.
- The tab-bar border is one continuous shelf shape: its top edge leaves the left tab group, curves down around the raised center action, and reconnects to the right tab group.
- Preserve the existing four tab routes and the current tab behavior while correcting only that shelf structure.
- Home must continue below Popular and the marketing card with product rails grouped under the available marketplace categories; showing category chips without the corresponding grouped sections is incomplete.

## Implementation Verification

- The live ChopRoute response contained the marketplace-facing categories Fried Rice, Jollof, and Pizza while all five current test products returned empty category relationships.
- A shared presentation matcher keeps explicit ERP category relationships authoritative. Only uncategorized products whose whole product name contains a category name use a temporary display fallback, such as `Pizza - large` under Pizza.
- The same matcher is used by Home groups, Explore category filtering, and category detail so the grouped rail and its `View all` destination do not disagree.

## Evidence

- Navigation target, dark variant: `../assets/2026-08-06-choproute-raised-center-navigation-dark.jpeg`
- Navigation target, light variant: `../assets/2026-08-06-choproute-raised-center-navigation-light.jpeg`
- Failed straight-divider implementation: `../assets/2026-08-06-choproute-straight-divider-failed-implementation.png`
- Direct conversation correction, live marketplace query, and 393 × 852 in-app Browser verification in the active Codex task on 2026-08-06.
