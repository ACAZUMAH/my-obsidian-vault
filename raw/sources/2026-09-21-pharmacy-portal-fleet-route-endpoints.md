# Pharmacy Portal Fleet Route Endpoint Correction

- Date: 2026-09-21
- Source: Direct user correction in Codex
- Project: LivelyCura Pharmacy Portal

## Direct Correction

Fleet paths must not be hardcoded across the app registry, menu, router, redirects, or tests. Declare them in the portal's central `routeEndpoints` object and import those constants at every navigation boundary, as the existing modules do.

## Verified Resolution

- Added `FLEET` and `FLEET_OPERATORS` to `src/constants/index.ts`.
- Reused those constants in the Fleet app registration, menu item, route object, redirect, and navigation test.
- Kept the Fleet module guard at the parent route and the operator permission guard at the operator child route, matching the established module route structure.
- The focused Fleet navigation test and ESLint check passed.
