# Call Center Customer Detail Navigation Correction

Date: 2026-09-07. Source: direct user message in the call-center-web-app task.

## Direct user evidence

> the orders page on light mode where is the total?, also at the customer screen the ui is okay now but the file structuring and layout is wrong, why the fuck will I search a customer and open then it has to appear below the fucking customer search page and I don't do things like looking at the orders part do you see that I open a single order inside the page that shows the orders?

The user supplied dark- and light-mode screenshots of the same order detail. The total amount was visible in dark mode and visually absent on the red light-mode total background. No customer identifiers or screenshots are retained in this record.

## Implementation interpretation and verification

The customer styling was accepted; navigation and ownership required correction. The existing `src/orders` and `src/order` pattern supports plural collection/search ownership and singular detail ownership, with separate sibling routes under the application shell.

The resulting structure uses `/customers` and `src/customers` for search, and `/customers/:id` and `src/customer` for the standalone profile and histories. A back control returns to the original search when available and falls back to the search route for direct links. The entry screen consumes hooks and passes typed data into presentation components. Code-bearing data remains in mounted memory and is cleared or aborted on navigation and context changes.

The observed total-color cause was the theme's tenant override: `colorsTuple(primaryColor)` gives every brand shade the same color. The total used `brand.0` for its light background and `brand` for its amount, making them identical. The total now uses the translucent `brand-light` background in light mode and retains its dark surface.

Verification used real application components and theme providers with synthetic API responses, not authenticated customer data. Both themes, desktop/mobile layouts, list-to-detail/back navigation and direct links were checked; automated coverage includes loading/error back navigation and route-change cleanup.
