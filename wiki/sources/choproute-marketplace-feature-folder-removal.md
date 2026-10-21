---
type: source
status: active
created: 2026-08-07
updated: 2026-08-07
tags: [livelycura, choproute, mobile, marketplace, architecture, folders, correction]
sources:
  - ../../raw/sources/2026-08-07-choproute-marketplace-feature-folder-removal.md
source_date: 2026-08-07
ingested: 2026-08-07
confidence: high
---

# ChopRoute Marketplace Feature Folder Removal

## Source

- Raw file: [2026-08-07-choproute-marketplace-feature-folder-removal.md](../../raw/sources/2026-08-07-choproute-marketplace-feature-folder-removal.md)
- Date: 2026-08-07
- Author: user correction plus verified implementation
- Ingested: 2026-08-07

## Core Claims

- ChopRoute has no top-level `src/marketplace` client feature.
- Marketplace identity/access remains system-owned and Redux-backed.
- Shared catalog code belongs in the established top-level `components`, `hooks`, `helpers`, and `interfaces` folders until feature-owned query separation is performed.
- Removing the folder is an ownership correction, not a catalog redesign.

## Useful Details

- The relocation preserved the current Home, Explore, category, restaurant, and restaurant-detail behavior.
- The Redux reducer remains correctly named `marketplace` because it models application state, not a feature folder.
- Current GraphQL operations still use marketplace API field names because those are backend contracts, not frontend folder ownership.

## Connections

- [[../projects/livelycura-choproute-app|LivelyCura ChopRoute App]]
- [[choproute-system-marketplace-ownership-custom-app-removal|ChopRoute System Marketplace Ownership And Custom-App Removal]]
- [[choproute-redux-marketplace-state-correction|ChopRoute Redux Marketplace State Correction]]

## Contradictions Or Tensions

This immediately supersedes the prior temporary note that allowed `src/marketplace` to retain catalog-domain code after bootstrap moved to `src/system`. No client marketplace feature directory remains.

Its temporary relocation of the combined catalog query into the global hooks folder is itself superseded by [[choproute-feature-owned-catalog-queries|ChopRoute Feature-Owned Catalog Queries]]. Product and category operations now live with their consuming features.

## Open Questions

- In the next data-loading stage, which shared catalog pieces remain genuinely cross-feature after Home receives separate product and category queries?
