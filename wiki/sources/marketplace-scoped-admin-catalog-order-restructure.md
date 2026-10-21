---
type: source
status: active
created: 2026-08-08
updated: 2026-09-01
tags: [livelycura, marketplace, admin, catalog, categories, orders, erp]
sources:
  - ../../raw/sources/2026-08-08-marketplace-scoped-admin-catalog-order-restructure.md
  - ../../raw/sources/2026-08-08-marketplace-admin-launchpad-sidebar-correction.md
  - ../../raw/sources/2026-08-08-marketplace-admin-capability-controls-loading-correction.md
  - ../../raw/sources/2026-08-08-marketplace-admin-table-filter-action-convention.md
  - ../../raw/sources/2026-08-08-marketplace-admin-conditional-table-rendering-correction.md
  - ../../raw/sources/2026-09-01-marketplace-business-product-listing-rename.md
confidence: high
---

# Marketplace-Scoped Admin Catalog And Order Restructure

## Source

- Raw file: [2026-08-08-marketplace-scoped-admin-catalog-order-restructure.md](../../raw/sources/2026-08-08-marketplace-scoped-admin-catalog-order-restructure.md)
- UI correction: [2026-08-08-marketplace-admin-launchpad-sidebar-correction.md](../../raw/sources/2026-08-08-marketplace-admin-launchpad-sidebar-correction.md)
- Controls/loading correction: [2026-08-08-marketplace-admin-capability-controls-loading-correction.md](../../raw/sources/2026-08-08-marketplace-admin-capability-controls-loading-correction.md)
- Table/filter correction: [2026-08-08-marketplace-admin-table-filter-action-convention.md](../../raw/sources/2026-08-08-marketplace-admin-table-filter-action-convention.md)
- Conditional-rendering correction: [2026-08-08-marketplace-admin-conditional-table-rendering-correction.md](../../raw/sources/2026-08-08-marketplace-admin-conditional-table-rendering-correction.md)
- Naming correction: [2026-09-01-marketplace-business-product-listing-rename.md](../../raw/sources/2026-09-01-marketplace-business-product-listing-rename.md)
- Date: 2026-08-08
- Author: User
- Ingested: 2026-08-08

## Core Claims

- Marketplace catalog classification is Admin-owned. ERP organizations manage ordinary products and internal categories but do not assign canonical marketplace categories.
- Marketplace scope begins by selecting a marketplace, then contains Organizations, Products, Categories, Orders, and Settings.
- Marketplace selection uses launchpad-style cards. After selection, the marketplace sections become main-sidebar routes and render the established full table/list pages; they are not tabs inside a marketplace-details surface.
- The selected marketplace's enabled catalog sources and order modes determine which product/order sidebar routes exist. Disabled capabilities must not appear as navigation choices.
- Organization access is a searchable table page. Granting access starts from an Add Organization button and completes through a selection modal rather than an always-visible inline selector.
- List/table headers expose one refresh action, and data-loading states use layout-matched skeletons rather than blank surfaces.
- Marketplace data tables follow the established Admin shape: a leading `#` row-number column, a labeled centered `Actions` column, and action controls within that final cell.
- Table-body loading and loaded-data branches use the shared `Conditional` component, matching the established Admin tables instead of introducing ternary-based branch rendering.
- Page filters are query-backed and domain-specific: Business Products uses organization/category/publication, Direct Orders and Marketplace Orders use organization/status, and category list/tree pages use category status. Search, filters, and pagination remain URL-backed.
- Catalog source and order mode are independent marketplace capabilities: Marketplace Products and ProductLinking remain valid where enabled, while Business Products directly classify ordinary ERP products through an Admin-owned listing.
- `MarketplaceBusinessProductListing` references marketplace, organization, ordinary product, canonical category IDs, and publication state without copying product details or changing `Product.categoryIds`. This supersedes the earlier `MarketplaceBusinessProductConfiguration` code name; the physical MongoDB collection name remains unchanged for data compatibility.
- Marketplace Orders retain bidding demand/lifecycle records. Direct Orders contain direct marketplace fulfillment Orders and accepted-bid fulfillment Orders; accepted bids intentionally appear in both views for different operational purposes.
- Direct consumer checkout, closest-facility allocation, payment, and the ChopRoute app migration remain later stages.

## Useful Details

- Business-product publication requires active marketplace access, an enabled Business Products source, and at least one active leaf category from the same marketplace.
- Revoking organization access deletes its business-product listings transactionally but preserves ERP products and categories.
- Referenced canonical categories cannot be deleted or reparented; rename/media changes require no synchronization because listings store canonical IDs.
- Existing marketplaces default to Marketplace Products plus Bidding. ChopRoute uses Business Products plus Direct.
- Sidebar routes keep Marketplace Products, Business Products, category list/tree, Marketplace Orders, Direct Orders, and Settings independently addressable while retaining one selected marketplace ID.
- The migration is dry-runnable, rerunnable, explicit for Check City/Pice, removes abandoned projection metadata without changing ordinary category relationships, and backfills marketplace IDs on bid fulfillment Orders.

## Connections

- [[../projects/livelycura-backend|LivelyCura Backend]]
- [[../projects/livelycura-admin-portal|LivelyCura Admin Portal]]
- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]]
- [[../projects/serlp-mobile|SERLP Mobile]]
- [[../projects/livelycura-choproute-app|LivelyCura ChopRoute App]]
- [[choproute-marketplace-owned-category-taxonomy|ChopRoute Marketplace-Owned Category Taxonomy]]

## Contradictions Or Tensions

- This supersedes the organization-category projection design and removes marketplace fields, assignment mutations, protections, and UI from ordinary ERP categories/products.
- It does not remove the older Marketplace Product, ProductLinking, or bidding models. Those remain valid for marketplaces whose settings enable them.
- ChopRoute still consumes ordinary organization products, but publication and canonical classification are now configured by Admin instead of projected through organization categories.

## Open Questions

- What exact direct consumer-order contract will connect ChopRoute checkout to server-side closest-facility allocation?
- When should the ChopRoute consumer queries switch fully to the published Business Products contract?
