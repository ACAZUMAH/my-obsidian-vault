# ChopRoute Explore Naming And Ownership Correction

## Source Context

- Date: 2026-08-06
- Author: User
- Evidence type: direct Codex conversation correction
- Implementation root: `/Users/acazumah/Documents/LivelyCura/livelycura-pice-app`

## Direct Evidence

- The customer-facing Menu tab is now named Explore.
- Browse behavior must not remain split across separate top-level `menu` and `search` features.
- Everything owned only by Explore should live under `src/explore`, without unnecessary nested folders.
- Obsolete browse folders should be removed rather than retained beside Explore.
- The Explore header must place its search bar and filter button side by side.
- Shared catalog, product-detail, and product-card code used by Home, categories, restaurants, and Explore remains outside Explore under its actual cross-feature owner.

## Evidence Boundary

This record preserves the durable customer-facing name, feature ownership, folder constraint, and Explore-header composition. It excludes temporary implementation progress and unrelated debugging output.
