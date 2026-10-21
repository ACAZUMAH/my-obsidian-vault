# LivelyCura Preproduction Courier Has No Legacy Compatibility Surface

Date: 2026-09-27
Source: Direct user correction

## Decision

- The retired company-facing Courier feature was never used in production.
- Remove that feature directly. Do not preserve it through legacy delivery-history screens, routes, menu entries, permission bridges, migrations, cutover materializers, or reconciliation layers.
- Pharmacy Portal must not contain `src/billing/legacyDeliveries` or another renamed replacement for the same retired surface.
- Current merchant/order references remain only where the active Selling, Billing, and platform Courier workflows own them.
- This correction does not change unrelated production migration or compatibility requirements in other domains.
