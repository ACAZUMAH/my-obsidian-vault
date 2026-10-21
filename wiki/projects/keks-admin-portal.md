---
type: project
status: active
created: 2026-07-21
updated: 2026-09-16
tags: [project, ceqa, keks, admin, hrm, permissions]
sources:
  - ../sources/keks-backend-errors-and-bulk-time-punches.md
  - ../sources/keks-analytics-ui-scope-correction.md
  - ../sources/ceqa-altin-project-knowledge-harvest-batch-1.md
  - ../sources/ceqa-altin-project-knowledge-harvest-batch-2.md
  - ../sources/ceqa-altin-project-knowledge-harvest-batch-3.md
  - ../sources/ceqa-altin-hermes-conversation-harvest-supplement-1.md
  - ../sources/hermes-livelycura-skills-keks-pharmacy-harvest-batch-1.md
confidence: high
---

# Keks Admin Portal

## Summary

Keks Admin Portal is the workforce administration and reporting surface for tenant users. It combines HRM operations, permission-aware navigation/actions, analytics/reports, API-key and webhook settings, and cursor/search-driven backend access.

## Purpose

Give administrators a protected operational interface for employees, organization structure, scheduling, attendance, reports, roles/permissions, and integration credentials.

## Stack

- Yarn, Vite 7, React 19, and TypeScript 5.9.
- Chakra UI 3 and Emotion.
- React Router 7.
- Redux Toolkit/Redux Persist.
- TanStack Query and TanStack Table.
- Axios, Formik/Yup, Day.js, PDF/CSV tooling, Recharts, and Vitest/Testing Library.
- ESLint, Prettier, Husky, Commitlint, and Commitizen.

## Architecture

- Root composition: Redux → Query → System → Chakra → Router.
- Axios centralizes the configured API base URL, bearer header, query serialization, and 401 session reset.
- Route loaders enforce authentication and selected permissions; visible navigation, launchpad cards, and actions also apply permission checks.
- The protected root route renders a standalone launchpad outside `MainLayout`; it reuses application providers, tenant switching, permissions, profile, and theme state without inheriting the operational sidebar shell.
- TanStack Query hooks own remote data, cursor pagination, server-backed filters/search, invalidation, and feedback states.
- Domain folders own their screens, components, hooks, interfaces, helpers, and bulk imports.
- Report families use endpoint-specific hooks and URL-backed filters. Branch, user, and exceptions reporting have distinct request contracts rather than one universal filter shape.
- Settings contains separate profile, appearance, API-key, webhook, and webhook-delivery-log surfaces.

## Folder Ownership

- `src/auth`, `src/redux`, `src/providers`, `src/services`: identity, persisted state, runtime providers, and API/query clients.
- `src/routes`, `src/constants/permission`, `src/Components/permissions`: route and component authorization.
- `src/launchpad`: permission-filtered application discovery, tenant handoff, launch cards, and responsive launchpad styling.
- `src/Components/ThemeModeControl.tsx`: shared System/Dark/Light appearance control used across launchpad, authentication, and the main sidebar.
- `src/hrm/<domain>`: employee, role, designation, department, branch, scheduling, attendance, transfer, absence, overtime, reminder, and announcement ownership.
- `src/reports`: report filters, tables, export/PDF, exceptions, attendance, branches, and report logs.
- `src/reports/components/ReportDateRangeDropdown.tsx`: report-only native date inputs; formatting/conversion helpers and props remain in their established helper/interface files.
- `src/settings/api-keys`: list/create/revoke lifecycle and one-time secret presentation.
- `src/settings/webhooks/webhooks`: webhook configuration lifecycle, one-time secret reveal, enable/disable, rotation, and test delivery.
- `src/settings/webhooks/webhookLogs`: delivery-log filtering, detail inspection, and replay.
- `src/Components`: shared presentation primitives, table status/pagination, selectors, dialogs, and form controls.

## Commands

- `yarn dev`: Vite development server.
- `yarn build`: TypeScript project build then Vite build.
- `yarn test`: Vitest.
- `yarn lint` / `yarn lint:fix`: ESLint.
- `yarn format` / `yarn format:check`: Prettier.
- `yarn preview`: preview the production build.
- `yarn commit`: Commitizen.

## Runtime/Deployment

- The client reads a public API base URL and attaches the persisted bearer token at request time.
- GitHub Actions use Node 22, Yarn frozen-lockfile installation, build, and tests.
- No tracked Netlify, Vercel, Docker, Procfile, or other deployment configuration was found. Deployment destinations and credentials remain external and unverified.

## Durable Conventions

- Single-employee updates use `PUT /users` with the existing internal `id` and editable `employee_id`; preserve branch and role assignments. Bulk-import updates keep `PATCH /users/bulk`. Do not infer a field is uneditable by checking only the PATCH schema; read the supplied operation contract. Apply create-form validation, optional-field, and layout improvements to editing too. See [[../sources/keks-backend-errors-and-bulk-time-punches|Keks Backend Errors And Bulk Time Punches]].

- Preserve backend error messages across mutation notifications, including multiple validation errors; generic text is a fallback. Keep the create-user form's required fields limited to first name, last name, gender, phone number, and role, with optional payload fields omitted when blank. See [[../sources/keks-backend-errors-and-bulk-time-punches|Keks Backend Errors And Bulk Time Punches]].
- Bulk manual time punching processes unique selected shift owners sequentially with per-employee outcomes and progress. The override contract accepts employee IDs and follows pending punch requests; do not assume it accepts a selected shift ID.

- Add features without redesigning unrelated existing interfaces.
- UI criticism means restyle the requested section while preserving its data, actions, and presence. When feedback targets recent additions, change only those additions; do not redesign the whole page or remove a disliked section. For analytics, preserve both Workforce Attendance and Needs Attention. See [[../sources/keks-analytics-ui-scope-correction|Keks Analytics UI Scope Correction]].
- Roles and Designations remain separate domain folders with independent components, hooks, interfaces, helpers, bulk import, and exports.
- Use Formik for input-heavy forms when that is the established local form pattern. Reuse onBlur and touched/error handling at the inputs. In stepped forms, disable Next until the current step is valid; avoid submit-time bulk-touching and automatic step jumping. See [[../sources/keks-backend-errors-and-bulk-time-punches|Keks Backend Errors And Bulk Time Punches]].
- Send supported `search` filters to APIs, normally through debounced/URL-backed state; do not replace server search with local filtering of one fetched page.
- Make report filters match the selected endpoint. Employee/user reports do not send or display `scope`; branch and exceptions reports keep it where the backend supports it.
- Keep report filters URL-driven across query cards, headers, and detail navigation. A selected branch and date range must remain visible after navigating to a single-branch report.
- Report date controls default and reset to `today`; use system-native date inputs inside the established Chakra visual language rather than copying example screenshots literally.
- Keep feature components, helpers, hooks, constants, and interfaces in separate owned files/folders. Do not collapse them into one convenient component file.
- Use the shared `Conditional` component from `@/Components/Conditional` for conditional JSX rendering rather than ternary-rendered UI branches. Preserve mutually exclusive loading, error, empty, permission, and content states. See [[../sources/keks-analytics-ui-scope-correction|Keks Analytics UI Scope Correction]].
- Map backend report-detail keys and values into audience-readable labels, local datetimes, and durations before tables, CSV, or PDF output.
- Shared API selectors expose loading, empty, error, and search states and adapt Chakra detail events at the component boundary.
- Permission constants are first-class product contracts. Protect routes, navigation/launchpad entries, and mutating actions; preserve `super_admin` bypass.
- API-key secrets are shown once, kept in the modal until explicit close, and never persisted in ordinary UI state after dismissal.
- Webhook configuration and delivery logs remain separate feature responsibilities and routes. Do not invent a frontend-only webhook permission; use the synchronized backend permission catalog and change both sides together when a dedicated capability is introduced.
- The launchpad advertises only implemented, routable modules the current user can access. When an authenticated user has no selected tenant but has credentials, select an available tenant before rendering its cards.
- Launch cards remain native buttons with explicit accessible labels. Use CSS classes for grouped hover/focus styling; never replace button semantics with a presentational ARIA role.
- System, Dark, and Light are one shared appearance contract across authentication, launchpad, and the operational shell. Expose the selected state with `aria-pressed` and let compact/expanded layouts change presentation without forking theme state.
- Keep decorative launchpad motion slow enough for text to remain readable, avoid clipping animated labels, and honor `prefers-reduced-motion`.
- Preserve the employee page header and controls while the hero adapts across breakpoints. Keep reusable hero facts and their interfaces in feature-owned files instead of rebuilding them inline in the page.

## Constraints

- A staging-only backend capability can still be represented as a normal permission/feature when the user explicitly wants automatic production compatibility; do not add speculative staging comments.
- Do not combine Roles and Designations because their APIs and feature ownership are distinct.
- Do not add filters that an endpoint does not accept merely because an adjacent report exposes them.
- Do not infer complete authorization from one permission-sync pass; verify every current route and action against the current backend model.
- Do not expose bearer tokens, API-key values, webhook secrets, or deployment credentials in logs, docs, tests, or the vault.
- Do not publish placeholder or dead launchpad cards merely because metadata exists; the card and route must agree.
- Do not overwrite native interactive semantics to satisfy a styling selector.

## Decisions And Rationale

- Route loaders prevent direct URL access while navigation/action filtering prevents unusable affordances; both layers are necessary.
- Any/all permission helpers and a super-admin bypass keep permission checks consistent without scattering special cases.
- API-key creation stays open in a one-time reveal state because closing early would make the secret unrecoverable.
- Server-backed search preserves correctness across cursor-paginated datasets.
- Endpoint-specific report filters prevent unsupported parameters and keep query state explainable.
- A report-local native date dropdown preserves familiar browser input behavior while matching Keks styling and keeping reusable conversion logic outside the component.
- Exception mappers format once for table and export consumers so raw API keys, timestamps, and ISO durations do not leak into operator-facing reports.
- A standalone launchpad preserves application-wide identity and theme context while keeping task-oriented navigation out of the discovery surface.
- Native button semantics plus an accessible label make the whole launch card operable without misrepresenting it as a generic group.
- One appearance state prevents authentication, launchpad, and sidebar controls from drifting into contradictory modes.

## Verification Expectations

- Run focused permission, settings/API-key, search/filter, and changed-domain tests.
- Run `yarn build`, `yarn test --run`, `yarn lint`, and `yarn format:check` as appropriate.
- Exercise guarded routes with no permission, one required permission, and `super_admin`.
- Verify sidebar, launchpad, global search, settings tabs, and create/edit/revoke actions match route protection.
- Verify report query cards, page-header filters, URL synchronization, single-branch drill-down, CSV/PDF output, and unsupported-parameter absence for each endpoint.
- Check create-secret and webhook-secret flows without recording secret values.
- Verify the protected root with no permission, one module permission, multiple module permissions, `super_admin`, and an authenticated user who has credentials but no selected tenant.
- Verify every visible launch card resolves to an active route, keyboard activation and accessible names remain intact, theme selection is shared across all three surfaces, and reduced-motion removes decorative movement.
- Verify the employee hero at narrow and wide breakpoints without changing the established page header or actions.
- Historical batch outcomes reported 29 tests for permission synchronization and 33 tests for the later Designations work. Batch 2 also reported focused report tests, TypeScript/build checks, and browser review at different task endpoints; treat all of these as session provenance, not current test results.

## Evidence

- Current repository: `/Users/acazumah/Documents/C.E.Q.A/keks-admin-portal`, branch `develop`, base commit `3521aaadf7ba`, clean at inspection.
- Current package manifest, provider/router composition, API client, permission constants/helpers/tests, HRM modules, report selectors, settings/API-key code, and CI workflows.
- Processed records: `019f591c-6c7e-71d1-97ef-a9106eea3397`, `019ee1a9-7cd2-7d90-a4fb-b8c25b09f2ef`, `019ecd35-0464-7ab0-9e64-f30a23af157c`, `019ecd33-ffcc-76c1-ac22-bf74103288c3`, `019e6f57-af39-74d0-8386-cd0434ad8830`, `019e6b33-73e7-7890-aad5-e482daa302eb`, `019e64df-8e38-7ef3-ad28-96a779d99465`, `019e5a50-7389-7092-9165-8019d403ed52`, `019e5639-855c-7730-a277-f4543d021d3e`, `019e17fc-ab90-7390-8ae8-bc670a4738fb`, and `019e087e-8415-7fb0-b296-bf7897049dbf`.
- [[../sources/ceqa-altin-project-knowledge-harvest-batch-1|C.E.Q.A/Altin Project Knowledge Harvest — Batch 1]].
- [[../sources/ceqa-altin-project-knowledge-harvest-batch-2|C.E.Q.A/Altin Project Knowledge Harvest — Batch 2]].
- [[../sources/ceqa-altin-project-knowledge-harvest-batch-3|C.E.Q.A/Altin Project Knowledge Harvest — Batch 3]].
- Direct Hermes session `20260701_023719_412401` plus interrupted/no-promotion record `20260707_234054_86cb50` in [[../sources/ceqa-altin-hermes-conversation-harvest-supplement-1|C.E.Q.A/Altin Hermes Conversation Harvest — Supplement 1]]. The substantive session historically reported one focused test file with six passing tests, a passing production build, changed-file lint success, and unrelated pre-existing full-lint failures.
- Direct Hermes session `20260621_010814_92d057` in [[../sources/hermes-livelycura-skills-keks-pharmacy-harvest-batch-1|Hermes LivelyCura Skills, Keks, And Pharmacy Harvest — Batch 1]] is the original completed report-log selector fix. It establishes `createListCollection(...)` plus detail-event adaptation and historically reports a passing production build with unrelated pre-existing lint failures; the two short-shell records are duplicate summaries.

## Contradictions

- [[../sources/keks-analytics-ui-scope-correction|Keks Analytics UI Scope Correction]] rejects the assistant's interpretation that a disliked new section should be removed. Preserve the section and improve its UI; no deletion was requested.

- The README remains the generic Vite template and does not document Keks architecture or commands beyond scaffold defaults.
- Permission support is broad, but some routes are unguarded and Announcements is currently commented out; “permission synchronization” is not proof of universal coverage.
- The June 19 Chakra Select record was interrupted; current code confirms the collection/event-adapter fix, but no completed historical test result exists for that task.
- Current tracked workflows define build/test CI for `main` and `develop` but no deployment job; earlier Netlify staging/production claims are not verifiable from the repository.
- Staging exposed API-key permissions before production. Current code treats them as normal features by explicit user choice; live production availability still depends on the backend.
- The May 26 settings task ended with a Profile/Appearance/Tenant tab shell, but current source uses separate nested Profile, Appearance, API Keys, and Webhooks routes. Current source supersedes that intermediate UI while preserving the feature-separation convention.
- Current Webhooks Configs and Logs loaders/sidebar entries remain guarded by `API_KEYS_MANAGE`; a dedicated webhook permission may exist elsewhere, but live backend compatibility was not verified.
- Launchpad metadata currently includes Announcements while its route remains commented out. That conflicts with the explicit rule that launchpad cards represent implemented, routable modules.
- Historical sidebar corrections alternated between compact horizontal and vertical theme-control layouts. Current source is authoritative: expanded presentation is horizontal and collapsed presentation is compact/vertical while both share the same theme state.

## Confidence

High for current static architecture, explicit user corrections, permission/search/API-key conventions, and historical task outcomes; medium for live backend/deployment compatibility because no runtime or provider was exercised.

## Open Questions

- Which currently unguarded HRM/settings routes are intentionally public to authenticated users?
- Are API-key and token-exchange permissions now present in the production backend?
- Should the README be replaced with a Keks-specific setup, architecture, and permission model?
- What is the canonical production acceptance matrix for every route, navigation entry, and action permission?
- Are nested settings routes now the settled replacement for the earlier Chakra-tab direction?
- Should Announcements be restored as a protected route, or removed from launchpad metadata until it is routable?
- Where is the authoritative staging/production deployment contract maintained if it is intentionally external to this repository?
