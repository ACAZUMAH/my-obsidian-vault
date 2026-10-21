---
type: source
status: active
created: 2026-09-09
updated: 2026-10-07
tags: [altin, react-native, orders, architecture, organization-access]
sources:
  - ../../raw/sources/2026-09-12-altin-toast-mutation-errors.md
  - ../../raw/sources/2026-09-12-altin-form-layer-rejection.md
  - ../../raw/sources/2026-09-12-altin-cross-project-form-structure.md
  - ../../raw/sources/2026-09-12-altin-formik-yup-correction.md
  - ../../raw/sources/2026-09-12-altin-exact-apollo-hook-pattern.md
  - ../../raw/sources/2026-09-12-altin-mobile-query-architecture-correction.md
  - ../../raw/sources/2026-09-12-altin-fleet-query-ownership-correction.md
  - ../../raw/sources/2026-09-11-altin-input-placeholders.md
  - ../../raw/sources/2026-09-11-altin-create-form-input-patterns.md
  - ../../raw/sources/2026-09-11-altin-detail-headers-direct-mutations.md
  - ../../raw/sources/2026-09-11-altin-module-actions-consistency.md
  - ../../raw/sources/2026-09-09-altin-orders-mobile-web-reference.md
  - ../../raw/sources/2026-09-09-altin-orders-implementation-corrections.md
  - ../../raw/sources/2026-09-09-altin-react-fc-convention.md
  - ../../raw/sources/2026-09-10-altin-compact-cards-production-api.md
  - ../../raw/sources/2026-09-11-altin-apps-stack-navigation.md
  - ../../raw/sources/2026-09-11-altin-refresh-and-tip-text.md
confidence: high
---

# Altin Orders Mobile and Web Reference

## Source

- Raw file: [Mutation Toast errors and submission state](../../raw/sources/2026-09-12-altin-toast-mutation-errors.md)

- Raw file: [Rejected form layer and supplied code](../../raw/sources/2026-09-12-altin-form-layer-rejection.md)

- Raw file: [Cross-project form structure correction](../../raw/sources/2026-09-12-altin-cross-project-form-structure.md)

- Raw file: [Formik and Yup correction](../../raw/sources/2026-09-12-altin-formik-yup-correction.md)

- Raw file: [Exact Apollo hook examples and explicit project-wide correction](../../raw/sources/2026-09-12-altin-exact-apollo-hook-pattern.md)

- Raw file: [Mobile query architecture correction](../../raw/sources/2026-09-12-altin-mobile-query-architecture-correction.md)

- Raw file: [Fleet query ownership correction](../../raw/sources/2026-09-12-altin-fleet-query-ownership-correction.md)

- Raw file: [Input placeholder correction](../../raw/sources/2026-09-11-altin-input-placeholders.md)
- Raw file: [Create-form and input UI correction](../../raw/sources/2026-09-11-altin-create-form-input-patterns.md)
- Raw file: [Detail headers and direct mutations](../../raw/sources/2026-09-11-altin-detail-headers-direct-mutations.md)
- Raw file: [Module action consistency correction](../../raw/sources/2026-09-11-altin-module-actions-consistency.md)

- Raw file: [Approved decisions](../../raw/sources/2026-09-09-altin-orders-mobile-web-reference.md)
- Raw file: [Implementation corrections](../../raw/sources/2026-09-09-altin-orders-implementation-corrections.md)
- Raw file: [React.FC convention](../../raw/sources/2026-09-09-altin-react-fc-convention.md)
- Raw file: [Compact cards, shared composition, and production API](../../raw/sources/2026-09-10-altin-compact-cards-production-api.md)
- Raw file: [Apps stack navigation](../../raw/sources/2026-09-11-altin-apps-stack-navigation.md)
- Raw file: [Refresh and tip text](../../raw/sources/2026-09-11-altin-refresh-and-tip-text.md)
- Date: 2026-09-09 to 2026-09-12
- Author: user; scoped repository verification by Codex
- Ingested: 2026-09-09

## Core Claims

- The latest mutation correction rejects error-return/rethrow layers, explicitly naming assertOutletMutation, readOrderActionResponse and ApiError. Hooks show actual API validation field messages in Toast and return no successful result on failure; forms keep client Yup errors and only advance after a successful action. Use Formik/Apollo submission state without a parallel saving ref. The inspected SERLP employee mutation returns a named action plus loading and consumes its caught error with Toast/null.

- The latest form correction explicitly rejects the `outletForm` feature, unnecessary files/folders, and the supplied order schema/controller. Treat that pasted code as rejected evidence. Follow actual SERLP screen field bindings and straightforward Formik/Yup hooks; do not merely relocate the same abstractions or declare conformance after tests pass.

- The follow-up rejects the assistant’s Formik/Yup migration because its code structure still differs from the reference projects. Cross-project consistency includes schema placement, named form-hook ownership, direct mutation submission and component bindings; the same libraries and passing tests are insufficient. Actual SERLP hooks declare private `yup.object().shape` schemas, use typed Formik in `use…Form`, call named mutations directly in async onSubmit, and return form plus mutation state.

- The 2026-09-12 form correction explicitly requires Formik and Yup. Follow the actual SERLP form hooks: typed useFormik, validationSchema, validateOnMount, onSubmit, and the real form returned to the UI. Formik owns editable values, touched/errors, dirty state, validity and submission; do not invent manual draft/error engines or duplicate field rules. Preserve feature ownership, shared inputs and workflow guards.

- The later 2026-09-12 correction supplies exact Customers/Menu Products and Add Customer/Add Employee hooks and explicitly orders a project-wide update. Query hooks own a private complete gql document, call typed useQuery, inject context/filters, derive named data/pageInfo and error/empty display flags, and return `...result`. Mutations own a private document, call typed useMutation with relevant refetchQueries, expose a generated-input named action with try/catch success/error feedback, return server data, and originally exposed `{ action, ...results }`; the later Toast correction removes forwarding mutation errors to forms. Remove combined aliased overview requests; compose independent operation hooks at screen boundaries. Read the available project examples and Obsidian before implementing.

- On 2026-09-12 the user rejected the Fleet query implementation and then rejected the assistant’s string-relocation fix. Follow the actual local Home query hooks: private gql document in the hook file, direct Apollo useQuery with generated Query/argument types, memoized domain data and returned Apollo results. The web clone supplies product/API contracts, not mobile query architecture. The prior function-body-only interpretation is superseded; see the linked mobile-query correction.

- Every text input needs a useful placeholder example or expected format, including optional/edit fields when empty. Keep labels visible and placeholders separate from saved values. Catch missing placeholders through the shared FormField type instead of waiting for user correction.

- The SERLP create/edit reference includes rendered form and input UI, not only mutation hooks: compact uppercase labels, bordered fields, field-shaped selection triggers, reusable form panels, and Screen footer actions inside outer keyboard avoidance, using Altin tokens.

- No detail screen shows a module drawer button. Order details place Report an issue on the right side of the header.
- Use Apollo useMutation directly in feature hooks, following SERLP create/edit patterns. Shared form controls remain reusable; forms own client validation, draft state and submission guards; mutation hooks own server-error toasts. The user explicitly rejected the generic mutation-resource wrapper and asked for simple, maintainable code.

- The 2026-09-11 correction requires shared Quick actions and View all presentation, no repeated organization overview heading, and the same permission-filtered actions in each module drawer. Consult the cloned web source before asking the user to explain its behavior.

- Apps remains the center bottom-bar action but opens a separate root-stack directory with a header Back button; Home, Search, Notifications, and More remain the actual tabs. Preserve the tab underneath when returning.

- `altin-web-apps/apps/partner` supplies behavior, permission, and API contracts; the mobile application's feature-first architecture and Altin identity remain authoritative.
- Modules open mobile overviews with current work, recent activity, Browse links, and a section drawer. Orders is the first concrete overview/list/read-only-detail workflow.
- Orders requires VIEW_ORDERS or ADMIN. Fleet and Billing are organization-type-specific; directory, pinned apps, and route registration share these rules.
- Organization switches discard module/filter state and stale responses and return Home.
- Tips deliberately follows the API's broader accessible-organization scope. Order/Courier pickers are organization-scoped; linked order details disclose the returned organization.

## Useful Details

- Focus reloads fetch in the background; native pull controls reflect explicit refresh only. Clear that state on completion, failure, blur, and scope changes. Tip amount clipping exposed the need for custom list titles to own their text metrics outside the smaller plain-title Text line box.

- Declare components as `React.FC<Props>` (or `React.FC` without props), with the interface imported from its owned file. The user explicitly rejected props annotations on the component function parameter.
- Later user corrections require the existing Conditional component, shared skeleton loaders, separate sibling list/detail features, and separately owned UI, types, helpers, constants, and styles.
- Each complete GraphQL operation stays in its hook. Imported selection fragments in separate GraphQL folders are rejected for this implementation.
- Order records remain individual compact cards with only a few useful fields; full information belongs in the detail view. This later correction supersedes the earlier pickup/drop-off two-column row. List headers have no module drawer button; preserve the user's feature navigation and supported actions without restoring an Overview entry.
- Inspect the actual SERLP Mobile shared Screen/list-row composition and reuse presentation across Altin features; do not merely copy its folder names or duplicate screen shells. Keep Altin tokens and feature-owned business logic.
- The user confirmed that the running app uses the production API. Keep verification read-only and request volume minimal; use local mocks/tests for failure and edge cases rather than mutating production data.
- Verify with the app and simulator already running. Preserve intervening user edits and removals; an implementation or review verdict is not evidence of user visual acceptance.

- One operation per hook; generated schema types; business errors and transport failures both count as failures. Backend totals remain unavailable when missing.
- Delivery Orders defaults to all dates, with debounced server search, cursor pagination, and applied draft filters.
- Courier selection requires a FLEET membership with VIEW_FLEET_COURIERS or ADMIN. The installed navigation library uses the nearest group's key, so nested authenticated route groups retain the organization key.
- The latest correction explicitly adds Create order and order-linked Report an issue. Assignment/status changes, rating submission, exports, custom ranges, realtime, and maps remain deferred. Creation is permission-gated; reporting follows the web support-ticket contract and selected filing organization.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]

## Contradictions Or Tensions

The Notifications tab named in this record was later replaced by Reports; Notifications opens from the Home bell. See [[altin-theme-navigation-runtime-corrections|the Reports tab correction]].

The later Toast correction supersedes the assistant's insistence on rethrowing/mapping mutation errors into forms and returning full mutation results. Query-result spreading remains unchanged. The removal of saving refs is the response to the user's necessity question, using existing Formik/Apollo control state; it does not imply cancellation or backend idempotency.

The explicit rejection of `outletForm` supersedes earlier assistant-authored guidance to retain dedicated shared form-feature folders and extracted field rules. The first two reported form corrections remain rejected; none is evidence of user acceptance.

The user explicitly rejected the first Formik/Yup migration. Its library-only completion claim is superseded; the earlier raw evidence remains intact. Apply the inspected reference structure instead of promoting custom schema-folder, callback-adapter or promise-wrapper designs as accepted conventions.

The Formik/Yup correction supersedes assistant-authored custom form-state/validation implementations. Generic references to forms owning validation do not authorize substituting another form engine.

The exact hook examples supersede the assistant's earlier claim that moving gql or switching only the transport call established architectural conformity. The correction applies across Orders, Outlets and Fleet, including remaining imperative read-resource wrappers. Existing raw records remain evidence of the earlier rejected interpretations, not accepted conventions.

The follow-up correction rejects treating the direct-mutation refactor as completion of the create/edit request; form layout and input controls also require alignment with the actual SERLP reference.

The later explicit instruction removes useMutationResource; earlier guidance to retain it is superseded. The no-drawer rule now covers all detail screens as well as lists.

The explicit Create order and Report an issue correction supersedes the initial read-only release boundary for those two actions. It does not authorize production mutation testing.

The direct 2026-09-11 Apps instruction supersedes the earlier five-route tab contract while preserving five visible controls. The same instruction requests another detail refinement; it does not establish acceptance of the replacement UI.

The initial plan requested a drawer on every Orders screen, but the subsequent direct correction explicitly removes it from list headers and all detail screens. The user rejected the first UI and a later grouped-card replacement. These corrections supersede that plan detail and any prior assistant visual approval.

Earlier project notes described Orders as an empty module shell. The approved Orders implementation supersedes that scope; other module placeholders remain distinct work. The web reference supplies product truth without transferring its architecture.

## Open Questions

The user selected [[altin-outlets-mobile|Outlets]] next, including create/edit integration while reserving live API testing to themselves.
