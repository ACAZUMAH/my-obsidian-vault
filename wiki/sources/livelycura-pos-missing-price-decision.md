---
type: source
status: active
created: 2026-07-31
updated: 2026-07-31
tags: [livelycura, pharmacy-portal, pos, pricing]
sources:
  - ../../raw/sources/2026-07-31-livelycura-pos-missing-price-decision.md
---

# LivelyCura POS Missing-Price Decision

## Source

- Raw file: [2026-07-31-livelycura-pos-missing-price-decision.md](../../raw/sources/2026-07-31-livelycura-pos-missing-price-decision.md)
- Date: 2026-07-31
- Author: user correction
- Ingested: 2026-07-31

## Core Claims

- A product without a facility price remains visible in the POS and displays a zero price.
- The POS prevents sale of that product by disabling its add-to-cart control instead of replacing the price with an instructional message.

## Useful Details

- Product sellability is determined by the presence of the persisted facility-price ID, not by whether the numeric price is greater than zero.
- A configured zero-priced product remains sellable.

## Connections

- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]]

## Contradictions Or Tensions

- The previous regression test expected the removed “Set a facility price” message and incorrectly described the zero-price display as undesirable.

## Open Questions

- None.
