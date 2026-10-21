---
type: source
status: active
created: 2026-08-01
updated: 2026-08-02
tags: [ceqa, call-center, catalog, graphql, categories]
sources:
  - ../../raw/sources/2026-08-01-call-center-product-category-filter-contract.md
---

# Call Center Product Category Filter Contract

## Source

- Raw file: [2026-08-01-call-center-product-category-filter-contract.md](../../raw/sources/2026-08-01-call-center-product-category-filter-contract.md)
- Date: 2026-08-01
- Author: backend guidance relayed by the user
- Ingested: 2026-08-01

## Core Claims

- Product category document IDs must be sent through `GetAllProductsInput.categoryIds`.
- `categoryPaths` is a separate slug-path filter and must contain slug values such as `beef`, not document IDs.

## Useful Details

- The Call Center category selector lists root categories. To include products assigned to child categories, its options use each root's `slug`; it writes `categoryPaths` and clears `categoryIds` when the selection changes.
- `categoryIds` remains appropriate for an exact category selection, while a root-category browsing control needs slug-backed path matching.

## Connections

- [[../projects/call-center-web-app|Call Center Web App]]

## Contradictions Or Tensions

- Earlier frontend behavior placed category `_id` values in `categoryPaths`; the backend guidance supersedes that request shape.
- The first frontend correction moved the root selector to `categoryIds`, which was identifier-valid but semantically too narrow because it excluded products assigned below the root. The 2026-08-02 correction uses root slugs in `categoryPaths` instead.

## Open Questions

- None currently.
