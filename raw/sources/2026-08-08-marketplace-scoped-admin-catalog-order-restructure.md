# Marketplace-Scoped Admin Catalog And Order Restructure

Date: 2026-08-08
Author: User

## Decision

Marketplace catalog classification and marketplace order administration belong to the LivelyCura Admin Portal, not participating organizations or ERP product forms.

- Selecting a marketplace opens one scoped workspace for Organizations, Products, Categories, Orders, and Settings.
- Each marketplace independently enables `MARKETPLACE_PRODUCTS`, `BUSINESS_PRODUCTS`, `BIDDING`, and `DIRECT` capabilities in valid combinations.
- Marketplace Products preserve the existing marketplace-owned catalog and ProductLinking flow.
- Business Products are ordinary sellable ERP products from access-granted organizations. Admin-owned configuration stores only canonical marketplace category IDs and publication state; it never copies product data or changes ERP categories.
- Marketplace Orders preserve bidding demand and lifecycle records. Direct Orders show direct marketplace-created ordinary Orders plus ordinary fulfillment Orders created from accepted bids.
- ERP organizations continue managing ordinary products and ordinary internal categories exactly as before. Pharmacy Portal and SERLP Mobile do not expose marketplace category assignment.
- Revoking organization access deletes only that marketplace's business-product configurations and leaves ERP products and categories untouched.
- Consumer-app ordering, closest-facility allocation, checkout, and payment remain a later stage.

## Migration And Verification Boundary

The migration defaults existing marketplaces to Marketplace Products plus Bidding and configures ChopRoute for Business Products plus Direct. It converts only the explicit Check City/Pice mappings, removes the abandoned projection metadata without changing ordinary product-category relationships, and backfills marketplace IDs on accepted bid fulfillment Orders. It is dry-runnable, rerunnable, and fail-closed.

The ChopRoute consumer app is intentionally not changed until the backend, Admin Portal, Pharmacy Portal, and SERLP Mobile foundation passes.
