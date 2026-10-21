# Fleet Operator Details Page

- Date: 2026-09-21
- Author: User
- Context: LivelyCura Pharmacy Portal Fleet operator frontend

## Direct Correction

- The operator detail view must be a page rather than a modal.
- The detail page must show every part of the operator record.

## Durable Interpretation

The roster navigates to a protected `/fleet/operators/:id` page. The detail flow owns its route, by-ID query, components, document previews, loading/error states, and complete profile/work-state/lifecycle presentation in `src/fleet/operatorDetails`.
