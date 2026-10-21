---
type: source
status: active
created: 2026-10-08
updated: 2026-10-08
tags: [altin, mobile, permissions, navigation, apollo]
sources:
  - ../../raw/sources/2026-10-08-altin-permission-gating.md
confidence: high
---

# Altin Permission Gating

## Source

- Raw file: [Altin permission gating](../../raw/sources/2026-10-08-altin-permission-gating.md)
- Date: 2026-10-08
- Author: user, through an Altin Partner Mobile Claude Code session
- Ingested: 2026-10-08

## Core Claims

- Altin Partner Mobile follows SERLP Mobile's permission pattern: every route stays registered, guarded screens are wrapped with `withPermission`, and a failed check renders a "No access" lock screen. Gating a route by leaving it unregistered is prohibited.
- Access checks go through `usePermissions().can(...)`. A single permission is written inline; combined permissions and organization-type limits use a named `permissionRules` entry in `src/constants/permissions.ts`. `PermissionGate` hides buttons and rows inside an open screen. ADMIN passes every permission check.
- User correction: mutation hooks do not check permissions. The UI that triggers a mutation is gated instead, and the backend remains authoritative. Organization-context guards in mutation hooks stay.
- Query hooks keep a permission `skip`, because queries run on mount and list hooks are reused on ungated screens.
- Each Home analytics report runs only with its report permission; denied reports hide their cards instead of showing errors.

## Useful Details

- Unregistered routes made navigation fail silently and ejected the user to Home when permissions or membership data changed; a registered guarded route swaps to the lock screen in place.
- Apollo Client 3 `refetch()` on a skipped query still sends the request, so pull-to-refresh must gate each refetch, not only the query's `skip`.
- Fleet sub-features also need `VIEW_FLEET_COURIERS` (the web parent route) and a FLEET organization; Billing needs a SHIPPER organization.
- The old `getAppAccess` flags were deleted after exhaustive comparisons showed identical access for every flag and route.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]].
- [[../projects/serlp-mobile|SERLP Mobile]].
- [[altin-outlets-mobile|Altin Outlets Mobile]].
- [[altin-orders-mobile-web-reference|Altin Orders Mobile and Web Reference]].
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]].

## Contradictions Or Tensions

- Supersedes the earlier rule that availability is applied by registering module routes, and that Apps owns availability. Apps still owns directory metadata; each entry now declares its own `permission`.

## Open Questions

- Whether viewing a support ticket from a notification should also require `VIEW_SUPPORT_TICKETS` for non-reporters; it currently relies on backend authorization.
