# ChopRoute Marketplace Stage-One Correction

## Source Context

- Date: 2026-08-06
- Author: User
- Evidence type: direct Codex conversation correction
- Implementation roots: `/Users/acazumah/Documents/LivelyCura/livelycura-pice-app` and `/Users/acazumah/Documents/LivelyCura/livelycura-backend`

## Direct Evidence

- Continue the already established marketplace plan; do not replace it with a different plan.
- Execute the plan one stage at a time so each stage can be understood and verified before the next begins.
- The marketplace feature already exists. The user created the ChopRoute marketplace and granted Check City and Pice Restaurant access for initial testing; more organizations may be granted access later.
- ChopRoute is a consumer food marketplace. It must display the ordinary products managed by organizations in the ERP and must not use procurement bidding, duplicate marketplace products, or links between marketplace and organization products.
- Organizations continue to manage their own branches in the ERP. The app knows the customer, restaurant, product, and delivery location, but does not expose or persist a customer-selected fulfillment branch for delivery.
- Future delivery ordering must resolve the closest eligible branch on the server. A later pickup flow may let the customer explicitly choose a branch.
- Stage one is limited to the ChopRoute redesign and discovery of ordinary products from organizations with active ChopRoute access.
- The former branch selector in the Home header becomes a delivery-location selector.
- Pice may receive a separate custom application later only if that engagement is agreed; the current repository is being pivoted to ChopRoute rather than branching another app now.

## Evidence Boundary

This record preserves only the durable architectural correction. It excludes credentials, private identifiers, temporary debugging output, and unrelated implementation chatter.
