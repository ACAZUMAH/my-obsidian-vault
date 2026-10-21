---
type: source
status: active
created: 2026-09-28
updated: 2026-09-28
tags: [bora-capital, backend, funds, rbac, admin-portal]
sources:
  - ../../raw/sources/2026-09-28-bora-fund-administration-access-control-plan.md
  - ../../raw/sources/2026-09-28-bora-rbac-livelycura-naming-correction.md
  - ../../raw/sources/2026-09-28-bora-resolver-and-service-documentation-correction.md
  - ../../raw/sources/2026-09-28-bora-resolver-domain-logic-and-generated-enum-correction.md
confidence: high
---

# Bora Fund Administration And Access Control

## Source

- Raw files:
  - [2026-09-28-bora-fund-administration-access-control-plan.md](../../raw/sources/2026-09-28-bora-fund-administration-access-control-plan.md)
  - [2026-09-28-bora-rbac-livelycura-naming-correction.md](../../raw/sources/2026-09-28-bora-rbac-livelycura-naming-correction.md)
  - [2026-09-28-bora-resolver-and-service-documentation-correction.md](../../raw/sources/2026-09-28-bora-resolver-and-service-documentation-correction.md)
  - [2026-09-28-bora-resolver-domain-logic-and-generated-enum-correction.md](../../raw/sources/2026-09-28-bora-resolver-domain-logic-and-generated-enum-correction.md)
- Date: 2026-09-28
- Author: user-approved Codex plan
- Ingested: 2026-09-28

## Core Claims

- Bora administration uses hybrid database-backed authorization: active role permissions and direct user grants are unioned on every request, with exact, namespace-wildcard, and global matching.
- The legacy GraphQL `User.role` remains deprecated compatibility output only. Authorization uses access channels, `platformRoles`, direct `permissions`, staff invitation state, and the `ADMIN_PORTAL` client boundary.
- The live LivelyCura backend is the structural and naming authority for Bora RBAC: use `Role`, `RoleModel`, role operations, `services/roles/permissions`, and a separate staff domain.
- Bora resolver maps reference named, documented, transport-only resolver functions declared above the map. Mapping, filtering, calculation, normalization, and response construction belong to documented domain services. New or rewritten service functions retain repository-style `@description` JSDoc with applicable parameters, errors, and returns.
- Fund administration deliberately stores one record per BCL portfolio, one isolated draft, and one customer-visible publication. Publishing replaces the customer payload and retains no prior version.
- BCL owns the live offer price. Local published facts own analysis and NAV history; customer reads continue with a null price during provider outages.
- The three July 2026 fund records are production fixtures sourced from the supplied PDFs, use only exact printed values and dated NAV points, and skip existing records without mutation.

## Useful Details

- Registered permissions are `funds.read/update/publish`, `roles.read/create/update`, and `staff.read/create/update`, plus namespace and global wildcards.
- The rejected intermediate names `AccessRole`, `accessRoleIds`, `directPermissions`, and `access.*` are not part of the contract. GraphQL uses `getRole`, `getRoles`, `createRole`, and `updateRole`; staff mutations accept `roleIds` and `permissions`.
- Resolver functions stay outside `Query`, `Mutation`, and field maps so their intent and JSDoc remain reviewable. They delegate without transforming domain data. Nested field resolvers that receive GraphQL field arguments pass parent data and generated arguments directly to the owning service. Reuse generated GraphQL argument types and enums instead of handwritten shapes or string unions. Rewriting a documented service function requires preserving or updating its documentation rather than deleting it.
- Staff invitation completion chooses a password, consumes a one-time code, activates admin access, and revokes existing sessions. Removing admin access preserves customer access and becomes effective through request-time permission resolution.
- New BCL portfolios remain customer-hidden until both published facts and visibility are present.
- Customer comparison and favorites do not add backend state in this phase. Support, marketing, and campaign administration remain later work.
- Verification on 2026-09-28 completed GraphQL generation, formatting, TypeScript build, 107 Jest suites/551 tests, and the production audit. The audit retains only two repository-approved temporary lodash exceptions expiring 2026-10-15.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[bora-grow-wealth-existing-customer-valuations|Bora Grow Wealth Existing Customer Valuations]]
- [[bora-production-ci-audit-scope|Bora Production CI Audit Scope]]

## Contradictions Or Tensions

- The approved plan used `AccessRole` naming, but the later direct correction supersedes it with the live LivelyCura `Role`/`platformRoles` structure. The deprecated legacy role output remains queryable and is never an authorization source.
- The initial implementation also inlined resolver functions and omitted service JSDoc; the later direct correction supersedes that structure with named resolver functions and documented services. A follow-up correction moved CIS transformation and NAV-range logic out of field resolvers and replaced a handwritten chart-range union with the generated `FundChartRange` enum.
- Paper fact sheets include chart lines without exact point labels; those visual estimates are intentionally excluded from production seed data.

## Open Questions

- What backend contracts will later phases use for customer-support tickets, marketing/news administration, and scheduled push, email, and SMS campaigns?
- When will new-customer Grow Wealth creation resume, and which BCL operations will authorize it?
