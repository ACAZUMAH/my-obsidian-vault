# LivelyCura POS Missing-Price Decision

Date: 2026-07-31

## User Decision

> I removed that check because it doesn't make sense just show the 0 price and rather disable the cart that's fine

## Verified Implementation

- `PosProductCard` displays the missing facility price as `0.00`.
- The add-to-cart control is disabled when the product has no persisted facility-price ID.
- Clicking the disabled product card does not invoke the add callback.
- The focused `PosProductCard` suite passed both tests after its stale expectation for “Set a facility price” was removed.
