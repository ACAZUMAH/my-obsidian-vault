# Altin Orders mobile: approved product-reference and architecture decisions

Source: direct user conversation in Codex, 2026-09-09. Sanitized excerpt of the user's approved implementation plan. This source preserves durable decisions, excluding credentials, private business records, runtime identifiers, and temporary progress.

> Use the cloned `altin-web-apps/apps/partner` as the reference for product behavior, permissions, and API contracts. Keep the mobile app’s feature ownership, React Navigation, Redux, Apollo, and styled-components architecture.

> Apps → Orders opens the overview.

> Show Orders, Outlets, Team, and Accounting for both organization types; Fleet only for `FLEET`, Billing only for `SHIPPER`.

> Require `VIEW_ORDERS` or `ADMIN` for Orders and its screens.

> On organization changes, discard the previous module navigation and local filter state, then return Home. Prevent old responses from populating the new organization’s screens.

> Keep overview, delivery-order, and tip logic under their respective Orders feature folders. Apps remains responsible for directory metadata and availability.

> Each GraphQL operation gets its own hook; reuse generated schema types and request only fields displayed by the mobile UI.

> Follow the web app’s broader API scope, as selected: initially show all tips accessible to the user, labeled **“Across your accessible organizations.”**

> Provide searchable Order and Courier selectors instead of unsupported free-text tip search. Picker results use the active organization; expose Courier selection only when the membership can view fleet couriers.

> The linked order displays its returned organization context, including when it differs from the selected organization.

> Refresh on screen focus and pull-to-refresh; defer realtime subscriptions.

> Defer creation, assignment/status changes, ratings submission, exports, custom date ranges, and live courier maps.

Repository verification: mobile uses Expo AppEntry, React Navigation, Redux, Apollo, generated schema interfaces, and styled-components. Orders owns its overview and feature-specific operation hooks. The web clone is a sibling repository under C.E.Q.A. React Navigation's installed route-config reader uses the nearest group's navigation key; nested groups must retain organization identity to discard the old stack. These are static implementation observations supporting the approved decisions, not evidence of live production behavior.
