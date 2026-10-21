# Bora Fund Administration And Access Control Plan

Date: 2026-09-28
Source: direct user-approved implementation plan in Codex

## Requested Phase

Implement Phase 1 fund administration and access-control APIs while preserving the existing Grow Wealth, KYC, withdrawal, Oye-agent, and dirty working-tree changes.

## Access-Control Requirements

- Use hybrid RBAC: permissions from active roles unioned with direct user grants on every request.
- Support exact permissions, namespace wildcards such as `funds.*`, and global `*`.
- Deprecate legacy GraphQL `User.role` in favor of dynamic `accessRoles`; do not use or persist the legacy role for authorization.
- Add customer/admin access channels, staff invitations with one-time `STAFF_INVITE` codes, admin-portal sign-in checks, immediate admin revocation, an immutable system Administrator role, and an idempotent first-admin bootstrap command.
- Prevent users from granting permissions they do not possess; only a global administrator may assign `*` or the system Administrator role.
- Audit role and staff-access changes without credentials or sensitive payloads.

## Fund Requirements

- Keep one `Fund` document per BCL portfolio ID with stable management fields, one `draftFacts` payload, and one customer-visible `publishedFacts` payload.
- Do not create versions, revision history, publication history, or a separate version collection.
- Editing a published fund creates or updates an isolated draft. Publishing atomically replaces the published payload and clears the draft; discarding only clears the draft.
- Store all explicit paper fact-sheet data, validate required values, unique periods/dates, percentages, and allocation totals.
- Customer CIS reads expose only approved display fields from visible published facts, enrich them with BCL's live offer price, support chart ranges, and return a null live price during BCL outages.
- Hide BCL portfolios until local facts are published and enabled.

## Production Seed And Boundaries

- Seed `BBF1100`, `BFI1100`, and `BGF1100` from the three 31 July 2026 production fact sheets.
- Transcribe every explicit table value, keep only exact dated NAV points, and never estimate chart values.
- Skip an existing fund completely so administrator changes are never overwritten.
- Keep comparison frontend-only, preserve the existing account flow for Add, defer favorites and new-customer Grow Wealth, and leave support, marketing, and notification campaigns for later phases.
