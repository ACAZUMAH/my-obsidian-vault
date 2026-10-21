---
type: source
status: active
created: 2026-09-24
updated: 2026-09-24
tags: [altin, mobile, search, navigation]
sources:
  - ../../raw/sources/2026-09-24-altin-search-browse-grouping.md
  - ../../raw/sources/2026-09-24-altin-search-isolation-sections.md
  - ../../raw/sources/2026-09-24-altin-search-empty-query-correction.md
  - ../../raw/sources/2026-09-24-altin-search-browse-restoration.md
confidence: high
---

# Altin Search Browse Grouping

## Source

- Direct user corrections: [Browse grouping](../../raw/sources/2026-09-24-altin-search-browse-grouping.md), [Search isolation and sections](../../raw/sources/2026-09-24-altin-search-isolation-sections.md), [empty-query scope](../../raw/sources/2026-09-24-altin-search-empty-query-correction.md), and [Browse restoration](../../raw/sources/2026-09-24-altin-search-browse-restoration.md).
- Ingested: 2026-09-24.

## Core Claims

- Search shows available apps together in one grouped Browse section when the query is empty or has just begun; matching apps stay grouped under Apps in search results. The Apps directory may retain its own product-area sections.
- Each Search app row shows that app’s feature names beneath the app name.
- Search owns its own styles and row presentation rather than importing the Apps directory’s styles or components. It may read the directory’s available app metadata.
- On first opening Search with an empty query, show Browse, Actions, and Suggestions. The Actions and Suggestions naming applies to the other empty-query sections; preserve the sections and behavior used after typing starts and after results arrive.

## Useful Details

- The correction is scoped to Search presentation; Search suggestions and the Apps directory remain separate concerns.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]].

## Contradictions Or Tensions

- Supersedes the previous Search implementation that split available apps into multiple product-area sections. The latest direct follow-up restores Browse to the empty-query screen and clarifies that only its other sections become Actions and Suggestions.

## Open Questions

- None.
