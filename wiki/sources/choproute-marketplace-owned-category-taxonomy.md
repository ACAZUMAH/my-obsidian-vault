---
type: source
status: superseded
created: 2026-08-07
updated: 2026-08-08
tags: [livelycura, choproute, marketplace, categories, taxonomy, graphql, erp]
sources:
  - ../../raw/sources/2026-08-07-choproute-marketplace-owned-category-taxonomy.md
confidence: high
---

# ChopRoute Marketplace-Owned Category Taxonomy

## Source

- Raw file: [2026-08-07-choproute-marketplace-owned-category-taxonomy.md](../../raw/sources/2026-08-07-choproute-marketplace-owned-category-taxonomy.md)
- Date: 2026-08-07
- Author: User
- Ingested: 2026-08-07

## Core Claims

- `MarketplaceCategory` is the canonical customer-facing ChopRoute taxonomy; same-name organization-category merging and product-name fallback are superseded.
- Products stay in the ordinary organization-owned ERP catalog. Marketplace assignments reuse the existing `Product.categoryIds` relationship through protected organization-category projections, so no `MarketplaceProduct` or `ProductLinking` catalog is introduced.
- Canonical category IDs are the client filtering contract. The backend resolves those IDs to the matching projections for every organization with active marketplace access.
- Local ERP categories remain valid for internal classification but are invisible to ChopRoute unless explicitly mapped.
- Marketplace administrators own the canonical tree. Organizations may assign active leaf categories to products but cannot mutate canonical meaning through ordinary category operations.

## Useful Details

- `Category` carries optional `marketplaceId` and `marketplaceCategoryId`, with one projection per organization and canonical category.
- Projection creation is idempotent, recreates canonical parent hierarchy, and requires active marketplace access.
- Canonical rename, description, and media changes synchronize projections. Reparenting and deletion are blocked after mappings exist; disabling hides discovery and prevents new assignments without breaking history.
- Check City and Pice mappings for Fried Rice, Jollof, and Pizza are explicit. The migration is dry-runnable, rerunnable, fail-closed, and rolls back only mapping metadata.
- SERLP and ERP product forms expose grouped marketplace-category assignment separately from internal ERP categories.

## Connections

- [[../projects/livelycura-choproute-app|LivelyCura ChopRoute App]]
- [[choproute-marketplace-stage-one-correction|ChopRoute Marketplace Stage-One Correction]]
- [[choproute-feature-owned-catalog-queries|ChopRoute Feature-Owned Catalog Queries]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]

## Contradictions Or Tensions

- The organization-category projection and ERP assignment contract documented here were superseded on 2026-08-08 by [[marketplace-scoped-admin-catalog-order-restructure|Marketplace-Scoped Admin Catalog And Order Restructure]]. Canonical categories remain marketplace-owned, but Admin now stores category/publication configuration directly against ordinary products and ERP no longer participates in marketplace classification.
- This decision supersedes earlier ChopRoute guidance to discover active ordinary ERP categories directly, merge categories by name, and allow a bounded uncategorized product-name fallback.
- Marketplace categories now participate in consumer catalog classification, but procurement `MarketplaceProduct` and product-linking models remain explicitly excluded.

## Open Questions

- Which canonical categories beyond Fried Rice, Jollof, and Pizza will marketplace administrators approve next?
- When should the deprecated consumer `categoryIds` filter be removed after client migration?
