# C.E.Q.A/Altin Project Knowledge Harvest — Batch 2 Evidence Manifest

Date: 2026-07-21

## Scope

- Family: C.E.Q.A/Altin.
- Repository boundary: `/Users/acazumah/Documents/C.E.Q.A` plus historical working directories under `/Users/acazumah/Documents/Pizzaman` for Keks Admin Portal and Call Center Web App.
- Repository writes: none.
- Repositories rechecked: exactly 3.
- Historical Codex records processed or classified: exactly 8, the checkpointed next-oldest batch.
- Direct current/legacy working-directory records discovered: 21.
- Records processed after this batch: 16.
- Records remaining after this batch: 5.
- Full transcripts, uploaded screenshots, generated GraphQL files, dependency trees, environment files, credentials, tokens, private identifiers, and provider values were not copied into the vault.

## Repository Provenance

| Repository | Branch | Base commit | Recheck state |
| --- | --- | --- | --- |
| `/Users/acazumah/Documents/C.E.Q.A/altin-partner-mobile` | `main` | `f05077b67018` | clean; no batch-2 record targeted this repository |
| `/Users/acazumah/Documents/C.E.Q.A/keks-admin-portal` | `develop` | `3521aaadf7ba` | clean |
| `/Users/acazumah/Documents/C.E.Q.A/call-center-web-app` | `develop` | `6a9cff6b681f` | clean |

All three repositories were inspected read-only. No dependency installation, generation, tests, builds, services, browser sessions, API calls, migrations, deployments, or Git mutations were run.

## Session Provenance

| Session ID | Date | Historical working directory | Indexed title | Classification |
| --- | --- | --- | --- | --- |
| `019e64df-8e38-7ef3-ad28-96a779d99465` | 2026-05-26 | `/Users/acazumah/Documents/C.E.Q.A/keks-admin-portal` | Replace report date pickers | substantive multi-task record; completed, with later current-code evolution |
| `019e63bc-dc06-73b1-a669-1b7ae43c69ee` | 2026-05-26 | `/Users/acazumah/Documents/C.E.Q.A/call-center-web-app` | Fix bugs | substantive multi-fix record; completed after repeated corrections |
| `019e5c27-e267-72c0-8d61-17ba7f7e256e` | 2026-05-24 | `/Users/acazumah/Documents/Pizzaman/call-center-web-app` | Update cart delivery toggle | substantive; completed |
| `019e5a50-7389-7092-9165-8019d403ed52` | 2026-05-24 | `/Users/acazumah/Documents/C.E.Q.A/keks-admin-portal` | Fix missed shift and branch filters | substantive; completed |
| `019e5639-855c-7730-a277-f4543d021d3e` | 2026-05-23 | `/Users/acazumah/Documents/Pizzaman/keks-admin-portal` | Get Exceptions Report | substantive; completed after filter-contract correction |
| `019e2825-6af9-7bd2-bb76-69bac885ebfc` | 2026-05-14 | `/Users/acazumah/Documents/Pizzaman/call-center-web-app` | Fix SelectProductModalHeader crash | substantive; completed |
| `019e266d-9d8c-7303-a71b-a7ea7f386abd` | 2026-05-14 | `/Users/acazumah/Documents/Pizzaman/call-center-web-app` | Add product preferences flow | substantive; completed, with current structural drift |
| `019e266b-c22a-7380-9aec-18cd6bd77841` | 2026-05-14 | `/Users/acazumah/Documents/Pizzaman/call-center-web-app` | Document familyConfig API | reference-only input; no implementation was requested or completed in that record |

## Minimal Sanitized Session Evidence

### Keks Reporting

- Shift reporting moved to purpose-specific branch, user, and exceptions endpoints while preserving the existing report layout, URL-backed filters, CSV export, and print/PDF behavior.
- `scope` applies only to branch and exceptions reports; the user explicitly rejected it on employee/user reports because that API does not accept it.
- Branch and exceptions filters retain supported `scope`; exceptions also retain reason and grace-period controls.
- Report date controls use a report-local dropdown with native start/end date inputs and default/reset to the present day. Uploaded screenshots were examples, not permission to copy a foreign visual language instead of the established system UI.
- Single-branch navigation must preserve header/query filters, including the selected branch, and missed-shift details need an explicit drill-down rather than an ambiguous aggregate.
- Exception details map backend keys to readable labels and format datetimes and ISO durations for tables and exports.
- Historical verification reported focused tests, TypeScript/build checks, and in-browser review at different points. Those results belong to the sessions and were not rerun during this harvest.

### Keks Structure And Settings

- User-stated convention: do not combine components, helpers, and interfaces in one file; keep them in their established feature-owned locations.
- Settings belongs in normal sidebar navigation, not as a special footer control. Profile entry points should route into settings.
- The historical task ended with separate Profile, Appearance, and Tenant tab content. Current source has since evolved to nested settings routes for Profile, Appearance, API Keys, and Webhooks; the historical tab shell is not current implementation truth.

### Call-Center Product Families And Preferences

- `familyConfig` is per-variant metadata describing selectable dimensions and order. Preferences are variant annotations that do not create a different SKU or price.
- Product queries include `familyConfig` and `preferences`; helpers group/sort variants, selection logic resolves a concrete variant, required preferences gate Add to Cart, and selected preferences travel with each cart line into checkout input.
- User-stated structure: GraphQL queries belong in hooks; helpers, interfaces, picker/list components, and mapped option items should be separated according to the surrounding feature structure.
- Conditional wrappers do not make unsafe child expressions lazy. Values such as `selectedVariant.unitPrice` and `product.productionCategory` must be derived or guarded before JSX children are evaluated.
- The family-config admin guide was supplied as reference-only evidence. No repository documentation file was created in that record, and no such guide was found in the current checkout.

### Call-Center Delivery And Checkout

- Delivery-area controls remain visible and become disabled with tooltip feedback until a compatible order method is selected; the exact-location control explicitly toggles the collapsed location search.
- Exact-location delivery pricing branches by courier type: Altin courier branches use the Altin cart-estimate mutation, while other courier types use the ordinary delivery-price query.
- Checkout eligibility remains anchored on the Formik/Yup `form.isValid` contract plus branch, availability, and required Altin-estimate state. Ad hoc duplicate field-presence validation in the cart component was explicitly rejected.
- Map-pin selection must not commit coordinates before reverse geocoding supplies the required human-readable address. The existing backend-compatible latitude/longitude transport order must remain unchanged.
- Altin estimate input accepts an absent address when the generated contract permits it; do not invent fallback copy. Estimate identifiers are invalidated as relevant branch, cart, location, method, or payment inputs change.
- Unavailable products are surfaced before order creation through a modal rather than a transient notification.
- Historical build/browser reports are session provenance only and were not rerun during this harvest.

## Current Repository Reconciliation

### Keks Admin Portal

- `src/reports/components/ReportDateRangeDropdown.tsx` remains a dedicated report component; its helpers and prop interface live outside the component, and Clear returns filters to `today`.
- Branch, employee, exception, and check-in report hooks default their URL-backed range to `today`.
- Employee filters omit `ScopeControl`; branch and exception filters retain it. Exceptions also expose reason and grace-period controls.
- `src/reports/helpers/reportMappers.ts` labels clock-in fields and converts ISO durations to readable values; focused mapper tests include the historical late-shift payload shape.
- Current settings use nested routes and separate feature folders. Sidebar navigation owns Profile, Appearance, API Keys, and Webhooks; profile menus route to the profile settings path.

### Call Center Web App

- Current product queries request family configuration and preferences. Selection helpers, interfaces, query hooks, and option item components remain separated.
- `SelectProductModalHeader` derives optional display values before rendering, and the modal derives a safe selected-variant price before the conditional child.
- Current `SelectProductModal.tsx` again contains the dimension, size, and preference `.map` loops. This conflicts with the latest explicit structural correction and with the historical completion report that said picker/list wrappers owned those loops.
- `ConfirmOrder` keeps the delivery-area picker visible, disables incompatible controls, and toggles exact-location search explicitly.
- `CartTotals` chooses Altin estimate pricing only for Altin courier branches and ordinary delivery-price querying for non-Altin branches with an exact delivery location.
- `Cart` keeps `form.isValid` in the checkout-disabled contract and waits for an Altin estimate when required.
- `useLocationSearchActions` commits a map point only after successful reverse geocoding and preserves the existing coordinate mapping.
- `UnavailableItemsModal` is wired into the cart checkout surface.

## Promoted Knowledge Boundary

- Project pages receive current implementation, explicit conventions, historical outcomes, and current-versus-historical contradictions.
- The Software Development Operating Manual receives only reusable rules about API-shaped filters, feature ownership, safe conditional rendering, and authoritative form/async-state boundaries.
- The New Project Bootstrap Operating Manual receives only the reusable frontend ownership and async-form-state conventions supported by this batch.
- No Altin Partner Mobile project claim or operating rule was added from this batch because none of the eight records targeted that repository.

## Completion Boundary

- C.E.Q.A/Altin batch 2 processes exactly eight records.
- Sixteen of 21 discovered direct current/legacy working-directory records are now classified.
- The final five older records remain for C.E.Q.A/Altin batch 3: `019e17fc-ab90-7390-8ae8-bc670a4738fb`, `019e087e-8415-7fb0-b296-bf7897049dbf`, `019de9d4-d4fa-7a70-8e07-0358896f1d03`, `019dda2a-5872-7f83-b151-a4a0163a1e42`, and `019caebd-b7ec-7e60-a01f-8fd02bec2e52`.
