# Bora RBAC LivelyCura Naming Correction

Date: 2026-09-28
Source: direct user correction in Codex

## Correction

The initial Phase 1 role and permission implementation did not follow the requested LivelyCura reference structure or naming. The current live LivelyCura backend is the authority for this Bora RBAC layer.

## Required Direction

- Use the LivelyCura role vocabulary and structure: `Role`, `RoleModel`, `platformRoles`, and `permissions`.
- Use role operations `getRole`, `getRoles`, `createRole`, and `updateRole`.
- Keep role permissions under `services/roles/permissions`, with the permission tree, permission map, resolver, utilities, and GraphQL permission shield separated as in the live reference.
- Keep staff invitation and access-management code in its own staff domain.
- Remove the intermediate `AccessRole`, `accessRoleIds`, `directPermissions`, and `access.*` naming.
- Preserve the deprecated legacy `User.role` field for compatibility, but never use it for authorization.
