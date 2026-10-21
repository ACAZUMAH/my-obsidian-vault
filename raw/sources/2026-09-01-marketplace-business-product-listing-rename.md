# Marketplace Business Product Listing Rename

Date: 2026-09-01
Author: User

The persisted Admin-owned relationship previously named `MarketplaceBusinessProductConfiguration` should use a clearer domain name. It represents an ordinary organization product being listed in a marketplace, including its canonical marketplace categories and publication state.

The accepted name is `MarketplaceBusinessProductListing`. Model, interface, service, GraphQL, Admin hook, and UI terminology should use “listing.” The deployed MongoDB collection name remains unchanged so existing marketplace catalog records are preserved without a data migration.
