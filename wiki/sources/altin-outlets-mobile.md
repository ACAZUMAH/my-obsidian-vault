---
type: source
status: active
created: 2026-09-11
updated: 2026-09-11
tags: [altin, outlets, react-native, architecture, production-safety]
sources:
  - ../../raw/sources/2026-09-11-altin-input-placeholders.md
  - ../../raw/sources/2026-09-11-altin-create-form-input-patterns.md
  - ../../raw/sources/2026-09-11-altin-detail-headers-direct-mutations.md
  - ../../raw/sources/2026-09-11-altin-outlet-bulk-import.md
  - ../../raw/sources/2026-09-11-altin-module-actions-consistency.md
  - ../../raw/sources/2026-09-11-altin-outlets-scope.md
confidence: high
---

# Altin Outlets Mobile

## Source

- Raw file: [Input placeholder correction](../../raw/sources/2026-09-11-altin-input-placeholders.md)
- Raw file: [Create-form and input UI correction](../../raw/sources/2026-09-11-altin-create-form-input-patterns.md)
- Raw file: [Detail headers and direct mutations](../../raw/sources/2026-09-11-altin-detail-headers-direct-mutations.md)
- Raw file: [Bulk import scope addition](../../raw/sources/2026-09-11-altin-outlet-bulk-import.md)

- Raw file: [Module action consistency correction](../../raw/sources/2026-09-11-altin-module-actions-consistency.md)

- Raw file: [Outlets scope and rounded statuses](../../raw/sources/2026-09-11-altin-outlets-scope.md)
- Date: 2026-09-11
- Author: user; scoped source verification by Codex
- Ingested: 2026-09-11

## Core Claims

- Every text input needs a useful placeholder example or expected format, including optional/edit fields when empty. Keep labels visible and placeholders separate from saved values. Catch missing placeholders through the shared FormField type instead of waiting for user correction.

- The SERLP create/edit reference includes rendered form and input UI, not only mutation hooks: compact uppercase labels, bordered fields, field-shaped selection triggers, reusable form panels, and Screen footer actions inside outer keyboard avoidance, using Altin tokens.

- No detail screen shows a module drawer button. Order details place Report an issue on the right side of the header.
- Use Apollo useMutation directly in feature hooks, following SERLP create/edit patterns. Shared form controls remain reusable; forms own validation, draft state, errors and submission guards. The user explicitly rejected the generic mutation-resource wrapper and asked for simple, maintainable code.

- Bulk import is explicitly in scope after the subsequent 2026-09-11 request. Expose it in both Quick actions and the drawer; require read access plus CREATE_OUTLETS and UPDATE_OUTLETS, or ADMIN.

- The 2026-09-11 correction requires shared Quick actions and View all presentation, no repeated organization overview heading, and the same permission-filtered actions in each module drawer. Consult the cloned web source before asking the user to explain its behavior.

- Outlets is the next concrete module after Orders: overview, searchable/filterable list, details, and create/edit API integration.
- The user explicitly prohibited production API testing for this pass and will switch the endpoint and perform live testing. Use offline checks and mocks; do not treat source checks as native or API acceptance.
- All status badges use fully rounded radii through shared presentation.

## Useful Details

- Bulk import uses CSV upload/paste, a local row review, and one atomic organization.outlet.bulkUpsert operation, capped at 500 outlets. Match by id then externalId. The mobile feature reuses outletForm field validation and shared list/form/status presentation. No production import is authorized for development testing.

- The cloned web Outlets store passes the selected organization ID. Keep that scope and distinguish a successful empty response from an error; production-wide record existence alone does not establish an organization-scoped query defect.

- Web partner routes require VIEW_ALL_OUTLETS or ADMIN for both organization types; CREATE_OUTLETS and UPDATE_OUTLETS separately gate their actions/routes. The backend remains authoritative.
- Module features own complete operations, filters, form validation, and navigation. Read resources and presentation are shared; mutations use Apollo directly; sibling list/detail/create/edit folders avoid mixing screens by lifecycle.
- Create/edit share fields and validation. Optional clears send null, and inactive/zero coordinates remain valid. Coordinates are entered manually; deletion and a map picker remain outside this pass. Bulk import was added by the subsequent explicit request.
- Focus reloads remain silent, pull refresh is explicit, and stale organization results are ignored. Mutations are explicit and never automatically retried. An in-flight write cannot be undone by discarding its UI result.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]]
- [[altin-orders-mobile-web-reference|Altin Orders Mobile and Web Reference]]

## Contradictions Or Tensions

The follow-up correction rejects treating the direct-mutation refactor as completion of the create/edit request; form layout and input controls also require alignment with the actual SERLP reference.

The later explicit instruction removes useMutationResource; earlier guidance to retain it is superseded. The no-drawer rule now covers all detail screens as well as lists.

The explicit bulk-import request supersedes its earlier exclusion from the first Outlets pass.

Outlets explicitly includes create/edit; the subsequent Orders correction also adds order creation and issue reporting. The prior allowance for minimal production reads does not authorize testing this Outlets implementation against production.

## Open Questions

What will the user find during native and API validation after changing the endpoint?
