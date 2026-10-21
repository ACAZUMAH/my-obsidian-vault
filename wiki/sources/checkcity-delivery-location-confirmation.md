---
type: source
status: active
created: 2026-09-14
updated: 2026-09-21
tags: [checkcity, delivery, location, checkout]
sources:
  - ../../raw/sources/2026-09-21-checkcity-delivery-warning-threshold-correction.md
  - ../../raw/sources/2026-09-14-checkcity-delivery-location-confirmation.md
  - ../../raw/sources/2026-09-14-checkcity-delivery-warning-correction.md
---

# CheckCity Delivery Location Confirmation

## Source

- Raw file: [September threshold correction](../../raw/sources/2026-09-21-checkcity-delivery-warning-threshold-correction.md)

- Raw file: [Direct request and clarification](../../raw/sources/2026-09-14-checkcity-delivery-location-confirmation.md)
- Raw file: [Warning and fee correction](../../raw/sources/2026-09-14-checkcity-delivery-warning-correction.md)
- Date: 2026-09-14
- Author: user; initial warning values selected by assistant under delegated judgment.
- Ingested: 2026-09-14

## Core Claims

After estimating delivery for a selected location, show a warning when BOTH distance is at least 15 km and the delivery fee is at least GH₵60. This implements the latest “60 cides and 15km to 20km” correction using 15 km as the start of the range. Show the full destination, branch, distance, and fee. Customers can check/change the location or continue to checkout after accepting the location and fee; do not label it outside the delivery area or prevent continuation solely for distance.

## Useful Details

Duplicate place names in Ghana motivate this check. A 10.2 km / GH₵41 delivery must not warn. The September 21 correction supersedes the assistant-selected 10 km independent trigger. Confirmation is specific to the branch, destination, and fee; changing them requires renewed confirmation. Dismissal does not mean acceptance. Continuing closes the warning and returns to checkout; it does not itself place an order.

## Connections

- [[../projects/livelycura-check-city-app|LivelyCura CheckCity App]]

## Contradictions Or Tensions

The September 21 correction supersedes the previous 10 km OR GH₵60 rule. The assistant interpreted “and” as requiring both thresholds and selected 15 km as the lower edge of the stated 15–20 km range.

The latest warning-only correction supersedes the earlier instruction to keep a 20 km hard cap. The customer must be allowed to continue after confirming the location and fee, including beyond 20 km. Raw evidence of both instructions remains preserved.

## Open Questions

- The exact lower boundary is implemented as 15 km; the user expressed a 15–20 km range rather than a single value.
