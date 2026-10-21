---
type: source
status: active
created: 2026-09-07
updated: 2026-09-07
tags: [ceqa, call-center, navigation, feature-ownership, theming]
sources:
  - ../../raw/sources/2026-09-07-call-center-customer-detail-navigation-correction.md
---

# Call Center Customer Detail Navigation Correction

## Source

- Raw file: [2026-09-07-call-center-customer-detail-navigation-correction.md](../../raw/sources/2026-09-07-call-center-customer-detail-navigation-correction.md)
- Date: 2026-09-07
- Author: direct user correction; implementation interpretation is labeled in the raw record.
- Ingested: 2026-09-07

## Core Claims

- Accepted styling does not imply accepted navigation or feature ownership.
- Selecting a customer must open a standalone detail page, following the existing order-list/order-detail behavior; never append the selected profile under customer search.
- Match the existing plural collection and singular detail folder pattern when implementing this separation.

## Useful Details

- `/customers` belongs to `src/customers`; `/customers/:id` belongs to `src/customer`. They are sibling routes under the protected application shell.
- Preserve the accepted customer presentation while adding normal back navigation, direct-link support and cleanup of the previous customer's history.
- Tenant color overrides can make all `brand.N` shades identical. Use a translucent semantic tint when a light background must differ from brand-colored text; verify totals in both themes.

## Connections

- [[../projects/call-center-web-app|Call Center Web App]]
- [[call-center-customer-ui-consistency-correction|Call Center Customer UI Consistency Correction]]

## Contradictions Or Tensions

- This extends the earlier visual-consistency correction: the revised appearance was accepted, while inline profile mounting and mixed list/detail ownership remained unacceptable.

## Open Questions

- None for this scoped convention.
