# ChopRoute Marketplace-Owned Category Taxonomy

Date: 2026-08-07
Author: User

## Decision

- `MarketplaceCategory` is ChopRoute's canonical customer-facing taxonomy.
- Products remain ordinary organization-owned ERP `Product` records. ChopRoute must not use `MarketplaceProduct`, product linking, bidding, or a duplicated product catalog.
- An organization assignment creates or reuses an organization-specific ordinary `Category` mapped by `marketplaceId` and `marketplaceCategoryId`; the mapped category ID remains in the product's existing `categoryIds`.
- Product assignment accepts active leaf marketplace categories only and requires active marketplace organization access.
- Consumer discovery and filtering use canonical marketplace category IDs. The backend translates them to organization-specific mapped category IDs before querying ordinary products.
- Existing local ERP categories remain available for internal classification but do not become ChopRoute categories unless explicitly mapped.
- Marketplace-managed organization categories are protected from ordinary ERP category mutation. Canonical rename, description, and media changes synchronize to projections; mapped canonical categories cannot be reparented or deleted.
- Existing Check City and Pice category mappings must be explicit, rerunnable, dry-runnable, and preserve existing product-category relationships.
- SERLP and ERP product surfaces must distinguish marketplace-managed categories from internal ERP categories.

## Delivery Contract

Implementation proceeds stage by stage: backend category foundation, product assignment, consumer catalog migration, ERP/admin UI, then explicit existing-data migration and verification.

Acceptance requires exact cross-organization category filtering with no unrelated-product fallback, idempotent assignment, access and leaf enforcement, disabled-category handling, synchronization safety, no ChopRoute read of procurement product-linking models, and successful backend/app/ERP validation.
