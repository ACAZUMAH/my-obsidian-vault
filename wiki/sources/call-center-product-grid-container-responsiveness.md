---
type: source
status: active
created: 2026-08-01
updated: 2026-08-01
tags: [ceqa, call-center, catalog, responsive-design, container-queries]
sources:
  - ../../raw/sources/2026-08-01-call-center-product-grid-container-responsiveness.md
---

# Call Center Product Grid Container Responsiveness

## Source

- Raw file: [2026-08-01-call-center-product-grid-container-responsiveness.md](../../raw/sources/2026-08-01-call-center-product-grid-container-responsiveness.md)
- Date: 2026-08-01
- Author: user requirement
- Ingested: 2026-08-01

## Core Claims

- The Sales product grid must adapt to the width of its draggable Products panel, not the browser viewport.
- Grid mode retains the requested `base: 1`, `sm: 3`, `md: 3`, `lg: 4`, and `xl: 5` column progression.

## Useful Details

- Viewport media queries can leave five columns active after the Products panel has been narrowed because the browser itself remains at the `xl` breakpoint.
- Mantine `SimpleGrid` container-query mode evaluates the same theme breakpoint widths against the component's own inline size and reflows during panel resizing.
- List mode remains one column.

## Connections

- [[../projects/call-center-web-app|Call Center Web App]]

## Contradictions Or Tensions

- The earlier viewport-responsive grid contract did not match the nested resizable-panel context.

## Open Questions

- None currently.
