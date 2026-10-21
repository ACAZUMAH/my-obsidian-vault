# Altin Partner Permission Gating — 2026-10-08

Sanitized record of a Claude Code session on Altin Partner Mobile (`feature/apps`). It records the user's instructions and corrections, the approved design, and the verified result. No credentials, tokens, or personal identifiers are included.

## User request

- The user asked for an explanation of how the logged-in user's assigned permissions protect screens and data. They said it looked like the app was not doing that and pointed to SERLP Mobile as the model.

## Findings presented to the user

- Partner mobile already gated by permission through one helper, `getAppAccess` in `src/apps/helpers/access.ts`. It turned the active membership's role permissions and the organization type into about 45 boolean flags, with ADMIN granting everything.
- Those flags gated three layers: routes were registered only when allowed (`access.x ? <Stack.Screen/> : null`), query hooks skipped without permission, and buttons and mutation hooks checked the flags.
- SERLP Mobile uses `usePermissions().can(check)` with single, any-of, and all-of checks; `withPermission(Screen, check, title, module)` around every stack screen, rendering a lock "No access" screen; and `PermissionGate` for in-screen buttons and rows. Routes stay registered.
- The Altin web partner app also keeps routes defined, treats ADMIN as granting everything, and redirects a failed check to an unauthorized page.
- Gaps identified: unregistered routes make navigation and notification taps fail silently and eject the user when permissions change mid-session; Notifications and support-ticket routes had no gate; the seven Home analytics report queries ran without their report permissions and showed backend errors; the flag object lived in `src/apps`, so every module imported from Apps.

## Approved plan

The user said "go" to a four-step plan, approving each step separately after reviewing its result:

1. Add `usePermissions().can`, `withPermission`, `NoAccessScreen`, and `PermissionGate`.
2. Register every route and wrap guarded screens with `withPermission`.
3. Gate each Home analytics report by its report permission and hide cards the membership cannot view.
4. Move every consumer from the flags to `can(...)` and delete `getAppAccess`/`useAppAccess`.

## User correction: no permission checks in mutation hooks

- Between steps 1 and 2 the user said not to check permissions inside mutations: when the user lacks the permission the button that triggers the mutation is never shown, so a second check in the mutation is redundant.
- The agent agreed: the backend stays authoritative and SERLP does the same. Permission checks were removed from 21 mutation hooks after confirming every trigger was gated.
- Organization-context guards in those hooks were kept because they protect a different rule (never write to a different organization after a switch); their toast copy was corrected.
- Query hooks keep their permission `skip`, because queries run on mount and list hooks are reused on ungated screens such as Home and Search.

## Implemented result

- `src/hooks/usePermissions.ts` exposes `can(access)`, where `access` is one `OrganizationPermission`, an `{ any }` or `{ all }` check, or a named rule. ADMIN passes every permission check; every check also needs an active organization.
- `src/constants/permissions.ts` holds `permissionRules`: named rules for sub-features that also need their parent's view permission and for Fleet (FLEET-only) and Billing (SHIPPER-only) organization-type limits. Single permissions are checked inline.
- `coreRoutes` registers all 57 routes; 52 are wrapped with `withPermission`. Tabs, Apps, Notifications, support-ticket details, and organization switching stay ungated as before.
- Home analytics passes an organization ID to each report hook only when its report permission passes, so denied reports skip, their refetch is never called, and their cards, chart, and View report action are hidden. Apollo Client 3 `refetch()` on a skipped query still sends the request, so refetches are gated separately.
- Apps directory entries and module feature lists declare a `permission`; screens use `PermissionGate` or named booleans from their screen hooks.
- Verification: exhaustive comparisons over 15,189 role combinations across fleet, shipper, and no organization showed zero differences between the old flags or route conditions and their replacements. Type-check and formatting passed. Read-only simulator checks confirmed the lock screen, in-place recovery without a Home bounce, partial and full analytics denial, and unchanged admin screens. No production mutation was triggered.

## Documentation approval

- On 2026-10-08 the user asked to update the stale repository documentation and the vault ("update them and update the vaults"). `AGENTS.md`, `docs/fleet.md`, and `docs/outlets.md` were corrected.
