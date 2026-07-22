# CompFlow Hermes Project Knowledge Harvest — Supplement 1 Evidence Manifest

Date: 2026-07-21

## Scope

- Family: CompFlow.
- Historical Hermes sessions processed: exactly 1, `20260710_173537_54b264`.
- Repository boundary: `/Users/acazumah/Documents/compFlow/compflow`, `/Users/acazumah/Documents/compFlow/compflow-admin`, `/Users/acazumah/Documents/compFlow/compflow-client-portal`, and `/Users/acazumah/Documents/compFlow/compflow-backend`.
- Repository writes: none.
- The session directly scaffolded only the promotional frontend, admin, and backend. The client portal was created later and is included only to establish the current four-repository family boundary.
- Full transcript payloads, reasoning, dependency trees, generated GraphQL files, environment files, credentials, tokens, private identifiers, and request headers were not copied into the vault.

## Source Provenance

- Canonical historical record: session `20260710_173537_54b264` in `/Users/acazumah/.hermes/state.db`, with 94 stored messages and 50 recorded tool calls.
- Supplemental runtime chronology: targeted session lines in the Hermes coder-profile agent and error logs.
- Partial retry artifact: `/Users/acazumah/.hermes/sessions/request_dump_20260710_173537_54b264_20260710_174001_525141.json`. This dump ends at an early connection failure and is not the complete session; the state database contains the continued turn and final outcome.
- Source date: 2026-07-10.
- No request headers or secret-bearing configuration were inspected.

## Repository Provenance

| Repository | Current branch | Current commit | State | First recorded commit consistent with the scaffold |
| --- | --- | --- | --- | --- |
| `/Users/acazumah/Documents/compFlow/compflow` | `develop` | `03421056ea70` | clean | `21dbe81`, 2026-07-11 |
| `/Users/acazumah/Documents/compFlow/compflow-admin` | `main` | `832109de1042` | clean | `5fd5786`, 2026-07-11 |
| `/Users/acazumah/Documents/compFlow/compflow-client-portal` | `develop` | `55e4e4d16087` | clean | later repository; not part of the session scaffold |
| `/Users/acazumah/Documents/compFlow/compflow-backend` | `main` | `b512a40b7b9e` | clean | `5ffd875`, 2026-07-11 |

All four repositories were rechecked read-only. No dependency installation, generation, tests, builds, services, browser sessions, API calls, database connections, commits, pushes, migrations, or deployments were run during this supplement.

## Sanitized Session Evidence

### Product and initial scope

- The user defined ComplianceFlow as a Ghana-focused payroll, HR, and statutory-compliance product for small and medium businesses.
- Payroll was the requested MVP priority. Employee records, salary setup, configurable PAYE/SSNIT rules, payslips, monthly reports, and export were prioritized ahead of broader HR, direct disbursement, attendance, leave, and accountant-portal expansion.
- Statutory percentages and bands in the proposal are historical product inputs, not current legal authority. They must remain versioned configuration and be verified against authoritative current rules before production use.

### Explicit correction

- The agent initially started an accidental root `apps/*` monorepo under `/Users/acazumah/Documents/compFlow`.
- The user explicitly corrected the destination and package manager: use the existing sibling folders `compflow` for the promotional web, `compflow-admin` for the dashboard, and `compflow-backend` for the API; follow existing project flow; use Yarn.
- The agent then scaffolded the three applications directly inside those separate folders and removed the accidental root monorepo artifacts.
- Durable convention: a shared parent directory does not imply a monorepo. Confirm named application folders and package-manager expectations before creating files.

### Historical scaffold and verification

- Promotional web and admin used Vite, React, TypeScript, Mantine, Apollo, Redux, React Router, GraphQL Codegen structure, Vitest, and distinct ports `5173` and `5174`.
- Backend used TypeScript, Express, Apollo GraphQL, GraphQL subscriptions, MongoDB/Mongoose wiring, Jest/Supertest, REST health, and port `4000`.
- The session wrote baseline tests before application source, observed expected missing-source failures, then implemented the applications.
- Yarn v1 hit a dependency-linking problem with newer Vite/Vitest packages; the session selected compatible versions instead of switching package managers.
- A backend TypeScript mismatch around compression middleware was resolved by removing that nonessential baseline middleware.
- The session reported final historical results: promotional test 1 passing, admin test 1 passing, backend tests 2 passing, all three builds passing, all three development servers starting, successful HTTP responses from both Vite roots and backend health/admin-overview paths.
- These are attributed 2026-07-10 session outcomes. They were not rerun during this read-only harvest.

## Current Repository Reconciliation

### Promotional frontend

- The first commit preserves the separate Vite/Yarn app, port `5173`, payroll-first paid-pilot message, provider/router/service/Redux shape, and one Vitest smoke test described by the session.
- Current code retains the public acquisition and paid-pilot lineage but has expanded into a backend `platformPlans` query with resilient fallback content and broader layouts/tests.
- Current HEAD therefore supersedes the session’s minimal static scaffold while preserving its repository boundary and product direction.

### Admin

- The first commit preserves the separate Vite/Yarn admin app, port `5174`, provider/router/Redux structure, `adminOverview` GraphQL query, fallback overview, and one Vitest smoke test.
- Current admin still queries `adminOverview` and falls back locally, but the current backend no longer exposes that resolver. A visually populated dashboard is therefore not proof of current backend integration.

### Backend

- The first commit preserves the separate Yarn backend, port `4000`, Express/Apollo/WebSocket composition, health transport, `adminOverview` GraphQL baseline, and three repository tests. The difference from the session’s final “two tests” report is historical evolution before the first Git commit, not a fresh verification result.
- Current backend retains REST and GraphQL health while expanding into authentication, organizations, roles, subscriptions/payments, employees, payroll, reports, and permission rules.
- Current source no longer exposes `adminOverview`; the session’s admin-overview endpoint claim is historical and is superseded by the current backend schema.

### Client portal

- The client portal was not named in the correction, was not scaffolded by this session, and has no session-derived claim.
- Its current independent repository boundary remains repository evidence from [[../../wiki/sources/compflow-project-knowledge-harvest-batch-1|CompFlow Project Knowledge Harvest — Batch 1]].

## Promoted Knowledge Boundary

- The three session-targeted project pages receive the explicit separate-repository/Yarn correction, attributed historical verification, and current-versus-initial reconciliation.
- The client-portal page remains unchanged because this session did not target it.
- The Software Development Operating Manual receives the sourced CompFlow correction and updated history-coverage boundary.
- The New Project Bootstrap Operating Manual receives only the reusable rule that a parent directory is not monorepo authorization and that named application roots/package-manager conventions must be confirmed before scaffolding.

## Completion Boundary

- Exactly one Hermes session was processed.
- CompFlow history coverage is complete for zero discovered Codex sessions and one discovered Hermes session as of 2026-07-21.
- Portfolio batch 1 remains the next pending project-family batch.
