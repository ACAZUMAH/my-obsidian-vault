# Fleet Operator Create Page And Courier Route Removal

- Date: 2026-09-21
- Source: Direct user correction in Codex
- Project: LivelyCura Pharmacy Portal

## Direct Corrections

- Creating a Fleet operator is a full workflow and must use its own page rather than a modal on the operator roster.
- The retired Courier product must not retain a Pharmacy Portal catch-all route or a “Courier has moved” page.

## Verified Resolution

- Added the centrally declared `/fleet/operators/create` route with a Fleet module parent guard and `fleet.operators.manage` child guard.
- The roster button navigates to the create page. The page owns the create mutation; the edit modal owns only profile updates; both reuse the operator profile form.
- Removed the Courier catch-all, legacy Courier billing redirects, Courier route constants, route registration, and route tests. Historical provider billing remains available through Billing routes only.
- Focused Fleet navigation testing, targeted ESLint, and the production Vite build passed.
- Full TypeScript checking remains blocked by pre-existing unfinished Fleet draft screens and Courier billing contract mismatches; it reported no errors in the operator create-page files changed here.
