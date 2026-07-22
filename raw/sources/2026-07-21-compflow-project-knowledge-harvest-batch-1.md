# CompFlow Project Knowledge Harvest — Batch 1 Evidence Manifest

Date: 2026-07-21

## Scope

- Family: CompFlow.
- Working-directory boundary: `/Users/acazumah/Documents/compFlow`.
- Repository writes: none.
- Repositories inventoried: exactly 4.
- Historical Codex sessions discovered and processed: 0.
- Purpose: current-repository inventory plus bounded session discovery.
- Transcript handling: the current harvest conversation was excluded because it is process control, not historical CompFlow project evidence. No historical session metadata had a working directory containing `compflow`, and the Codex session index contained no CompFlow match.
- Secret-bearing files and values were not inspected or copied. Environment files, credentials, tokens, certificates, private keys, connection strings, dependencies, generated GraphQL output, build output, caches, binaries, and ordinary tool chatter were excluded.
- A binary `.DS_Store` encountered during file inventory was excluded immediately and did not contribute evidence.

## Repository Provenance

| Repository | Branch | Commit | Package boundary | Working tree |
| --- | --- | --- | --- | --- |
| `/Users/acazumah/Documents/compFlow/compflow` | `develop` | `03421056ea70` | Yarn | Clean |
| `/Users/acazumah/Documents/compFlow/compflow-admin` | `main` | `832109de1042` | Yarn | Clean |
| `/Users/acazumah/Documents/compFlow/compflow-client-portal` | `develop` | `55e4e4d16087` | Yarn and npm lockfiles both present | Clean |
| `/Users/acazumah/Documents/compFlow/compflow-backend` | `main` | `b512a40b7b9e` | Yarn 1; Node `>=22.13.0` | Clean |

No repository-local `AGENTS.md` or `CLAUDE.md` was found in the four repository roots. Repository package files, README files when present, tracked workflow/config files, and representative current source established the claims below.

## Codex Session Discovery

- Active and archived Codex rollout metadata were searched by working directory, case-insensitively, for `compflow`.
- The Codex session index was searched for CompFlow titles and paths.
- Result: zero historical CompFlow sessions. No transcript IDs were processed.
- Consequence: this batch promotes observed implementation only. It does not claim transcript-derived user intent, historical rationale, or a complete explanation for every current design choice.

## Repository Evidence

### Public frontend: `compflow`

- Vite 5, React 19, TypeScript 5.5, Mantine 9, Apollo Client 4, GraphQL 16, React Router 7, Vitest, ESLint, and Prettier.
- `src/app` composes Apollo, Mantine, notifications, and browser routing. The only product route is the landing page under the shared layout.
- `src/home` owns landing-page components, content helpers, hooks, interfaces, local styles, and tests.
- `useHomeContent` requests public `platformPlans` from the backend and falls back to static price/content data when live data is unavailable.
- GitHub Actions use Node 22 and Yarn for CI on `main`/`develop`, with staging and production Netlify workflows. Only secret variable names were observed; no values were read or preserved.

### Internal admin: `compflow-admin`

- Vite 5, React 19, TypeScript 5.5, Mantine 9, Apollo Client 4, Redux Toolkit with persisted settings, React Router 7, GraphQL Codegen, and Vitest.
- The provider shell composes persisted Redux state, Apollo, Mantine, modals, notifications, and routing.
- The current router exposes one dashboard route. The dashboard requests `adminOverview` but falls back to static overview data on missing data or error.
- `codegen.ts` expects `../compflow-backend/schema.graphql`; that artifact is absent from the backend checkout, so generation is not runnable from the four current checkouts as written.
- No repository deployment workflow or container configuration was found.

### Business client portal: `compflow-client-portal`

- Vite 5, React 19, TypeScript 5.5, Mantine 9, Apollo Client 4, Redux Toolkit with persisted auth/settings state, React Router 7, GraphQL Codegen, and Vitest.
- Public routes are login, registration, and verification. Protected routes are dashboard, employees, payroll, settings, and subscription; organization verification gates authenticated access.
- The Apollo client injects the persisted bearer token and client name. Employee hooks use live GraphQL CRUD operations.
- Dashboard, payroll, subscription, and security-settings services still contain demo/static or delay-based behavior. A separate in-memory employee service remains alongside the live GraphQL employee hook; sample private identifiers were deliberately excluded.
- Registration directly creates an organization and returns placeholder identity/token values before OTP verification. That differs from the backend's current verified-signup then authenticated-checkout flow.
- Password, passcode, and two-factor settings are simulated in the client even though current backend authentication is OTP-only.
- `codegen.ts` expects the same absent sibling `schema.graphql` artifact. Both `yarn.lock` and `package-lock.json` are present, while package scripts and CI use Yarn.
- GitHub Actions use Node 22 and Yarn for CI plus staging/production Netlify workflows. Secret values were not inspected.

### Backend: `compflow-backend`

- TypeScript 5.9, Express 4, Apollo Server 5, GraphQL/GraphQL WS, MongoDB/Mongoose 9, GraphQL Shield, AJV, JWT, Winston, PDFKit, React Email/Resend, Jest, Paystack, and Moolre integration code.
- Startup composes Express and a shared HTTP server, `/graphql`, `/subscriptions`, security/request middleware, `/health`, payment webhooks, MongoDB, migrations, and centralized error handling.
- GraphQL domains cover auth, users, employees, organizations, roles, subscription plans/checkouts, and payroll. Resolvers delegate domain behavior to services; Shield rules enforce named permissions.
- Authentication is OTP-only through email/phone login and `completeLoginWithToken`, with portal checks for admin and business-owner access.
- Platform onboarding is public plan selection, signup OTP, verification/JWT, authenticated checkout, payment verification/webhook, then organization creation and owner assignment. Enterprise/contact-sales plans are rejected from self-service checkout.
- Tenant users are restricted to their organization; Admin and SuperAdmin can operate without organization membership and may supply an organization scope.
- List services fetch `limit + 1` and return `getPageConnection`; page-info `total` is the number of returned edges, not an overall database count.
- Payroll creates immutable run-item calculations from active employees and the selected tax rule, then enforces draft-to-approved-to-paid transitions. Cancellation is a separate permissioned operation. Reports and payslips are generated from persisted run items.
- The README's `SKIP_DB_CONNECTION=true` smoke command is stale: startup always calls `connectToDb`, and the connector does not inspect that flag.
- The package `generate` script points to `codegen.ts`, but no tracked backend `codegen.ts` exists. No backend `schema.graphql`, deployment workflow, or container file was found.
- A legacy aggregate `src/models/payroll/Payroll.ts` coexists with the split payroll model files exported by `src/models/payroll/index.ts`.

## Promotion Decision

- Created four first-class project pages under `wiki/projects/` with `type: project`.
- Updated the Software Development Operating Manual with a linked compact CompFlow map and this batch's coverage boundary.
- Updated the New Project Bootstrap Operating Manual only for reusable evidence: preserve independent application boundaries; verify lockfile authority when lockfiles conflict; and test generation configuration/schema paths rather than treating a script's presence as readiness.
- No personal preference was promoted because no historical CompFlow session was found.

## Verification Boundary

- Repository evidence was read-only and based on the branches/commits above.
- Package manifests, README files, current routes/providers/hooks/services, GraphQL schema/resolvers/shield/services, workflows, and Git status were inspected selectively.
- No install, dependency update, code generation, lint, test, build, application startup, network call, payment, webhook, migration, database operation, or deployment was run.
- Therefore command and deployment descriptions are configuration-level observations, not successful execution claims.

## Contradictions And Uncertainty

- Client portal onboarding and security settings do not currently match the backend's verified OTP-only onboarding contract.
- Several client/admin data paths deliberately or implicitly fall back to static/demo state, so route presence does not prove end-to-end backend integration.
- All three GraphQL Codegen entry points are incomplete in the current family checkout: the portal configs reference an absent backend schema artifact, and the backend script references an absent config.
- Client portal lockfiles disagree about package-manager ownership; current scripts and CI favor Yarn.
- The backend README advertises a database bypass that current source does not implement.
- With no historical CompFlow sessions, rationale for these incomplete or transitional paths is unknown.

## Completion Boundary

- CompFlow batch 1 is complete for the four known repositories and the historical session set discoverable as of 2026-07-21.
- The next project-family batch is Kusantec/Bora batch 1: inventory its repositories/apps, discover matching Codex sessions, and process one family batch or at most eight relevant sessions.
