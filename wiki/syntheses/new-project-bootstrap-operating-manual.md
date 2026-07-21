---
type: synthesis
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [software-development, project-bootstrap, backend, frontend, mobile]
sources:
  - ../sources/project-knowledge-completion-and-bootstrap-directive.md
  - ../sources/livelycura-project-knowledge-harvest-batch-2.md
  - ../sources/livelycura-project-knowledge-harvest-batch-3.md
confidence: medium
---

# New Project Bootstrap Operating Manual

## Thesis

For this user, “start” or “spin up” a project means create a working engineering foundation before feature logic, screens, or pages are implemented. The foundation includes the real stack, package installation, runtime wiring, folder ownership, shared infrastructure, tests/build scripts, and live smoke verification.

This manual captures conventions verified from representative LivelyCura, CompFlow, Portfolio, Kusantec, and Altin scaffolds plus explicit user corrections. It is a baseline decision system, not permission to ignore a target repository or force one structure onto every product.

## Evidence Status

### Established across explicit corrections and representative projects

- TypeScript is the default language.
- Existing folder names, package manager, lockfile, aliases, and sibling-project patterns must be preserved.
- Yarn is the established package manager in the inspected reference backends; existing lockfiles remain authoritative.
- Backend baseline: Express, Apollo GraphQL, GraphQL subscriptions, MongoDB/Mongoose, JWT/auth context, structured error handling, validation, and Winston logging.
- Web/admin baseline: Vite React, Apollo Client, Redux Toolkit, React Router, a design-system provider such as Mantine, GraphQL Codegen, typed hooks, and feature-owned folders.
- Mobile baseline: Expo with React Navigation, Redux Toolkit, Apollo Client, feature-first modules, shared presentation primitives, theme/safe-area handling, and persistent auth state.
- Expo system-theme support includes native automatic appearance and system-UI integration, with a native rebuild in the acceptance path.
- Shared infrastructure must stay contract-focused and prop-driven; create, edit, view, and list flows retain their own pages, forms, queries, and mutations instead of being collapsed into one business-aware generic runtime.
- A scaffold is not complete until install, generation, type checking, tests, build, startup, and real endpoint/page checks have been attempted and accurately reported.

### Project-specific choices that must be confirmed from references

- Jest versus Vitest.
- Mantine versus Chakra or another established design system.
- Exact Node, React, Expo, GraphQL, Mongoose, and package versions.
- REST routes in addition to GraphQL.
- OTP-only authentication versus password support.
- Redis or distributed subscription transport.
- Docker/Compose, PaaS, CI, observability, email, payments, storage, and AI integrations.

## Universal Bootstrap Sequence

### 1. Establish project boundaries before creating files

1. Identify the exact target folder and whether it already exists, even if empty.
2. Inspect sibling/reference projects named by the user.
3. Read `AGENTS.md`, README, package manifests, lockfiles, TypeScript config, environment examples, build/deployment files, and representative startup files.
4. Classify each application: backend API, public web, admin/operations portal, client portal, or mobile app.
5. Preserve product responsibility boundaries. Do not merge separate applications or create a root monorepo unless requested or already present.
6. Record the package manager, runtime version, default ports, API URL, subscription URL, database assumptions, and deployment target.

### 2. Define the pre-feature acceptance contract

Before business features, every project should promise a small observable baseline:

- Backend: process starts, database policy is explicit, `/health` responds, GraphQL accepts a basic operation, subscriptions initialize, errors are formatted, and shutdown behavior is defined.
- Web/admin: providers initialize, root route renders, Apollo and Redux are wired, generated GraphQL types exist, theme/styles load, and browser console is clean.
- Mobile: Expo starts, navigation renders, theme/safe-area behavior works, auth persistence is wired, and native type/export verification passes.

Write smoke tests around these promises when feasible before implementing the foundation.

### 3. Install the actual stack, not placeholder dependencies

Use the existing lockfile and package manager. Install complete dependency groups, then wire them into runtime code. A package in `package.json` with no provider, server, middleware, client, or test integration does not count as configured.

### 4. Create structure around ownership

Folders should express responsibility:

- Process and transport startup are separate from domain logic.
- GraphQL schemas/resolvers are separate from services.
- Services own validation, authorization, orchestration, and business rules.
- Models own persistence shape.
- Shared helpers remain domain-neutral.
- Frontend/mobile features own their pages/screens, components, hooks, GraphQL operations, interfaces, constants, and styles.
- Shared components are presentation primitives, not centralized business runtimes.
- Separate flow ownership from reusable engines: route-level create/edit/detail/list folders may share builders, renderers, mappers, and design primitives through explicit props, but shared folders do not own flow-specific queries or mutations.
- Identify existing catalogs, relation services, and transaction owners before scaffolding domain models. Do not create a parallel taxonomy, link table, billing path, or inventory path merely because a new feature references those concepts.
- A focused standalone workflow may use its own layout while reusing the application's providers, context switchers, theme, permissions, profile, and design system.

### 5. Wire infrastructure before features

Configure environment loading, aliases, logging, database, middleware, authentication context, GraphQL HTTP/subscription transports, providers, navigation, generated types, and test harnesses before implementing product screens or domain mutations.

### 6. Verify in layers

Run install → generation → format/lint → type check → tests → build/export → startup → live smoke checks. Fix foundation failures before adding product logic.

## Backend Foundation

### Reference architecture

```text
backend/
├── package.json
├── yarn.lock
├── tsconfig.json
├── nodemon.json
├── codegen.ts
├── .env.example
├── public/
├── scripts/
│   └── migrations/                 # only when required; preserve existing ownership
├── tests/ or src/**/*.test.ts
└── src/
    ├── main.ts                     # process entry, env loading, signals, fatal startup errors
    ├── app.ts                      # startup orchestration and lifecycle order
    ├── servers/
    │   ├── createExpressApp.ts
    │   ├── createGraphqlServer.ts
    │   ├── createGraphqlSubscriptionServer.ts
    │   ├── formatGraphqlErrors.ts
    │   └── index.ts
    ├── common/
    │   ├── constants/
    │   ├── db/
    │   ├── enums/
    │   ├── helpers/
    │   ├── interfaces/
    │   └── validators/
    ├── logger/
    ├── middlewares/
    │   ├── error-handler.ts
    │   ├── verify-token.ts
    │   └── index.ts
    ├── graphql/
    │   ├── index.ts
    │   ├── general/
    │   ├── auth/
    │   ├── shield/
    │   ├── subscriptions/
    │   └── <domain>/
    ├── services/
    │   └── <domain>/
    ├── models/
    │   └── <domain>/
    ├── dataloaders/
    ├── routes/
    ├── controllers/                # only when REST/webhooks need controllers
    └── cronJobs/                   # only when required; do not relocate casually
```

Existing projects may use direct `src/graphql/<domain>` and `src/services/<domain>` rather than `src/modules`. Mirror the reference repository instead of introducing a preferred module abstraction.

### Baseline dependency groups

Use current compatible versions from the selected reference repository rather than blindly copying these names.

#### Runtime and TypeScript

- `typescript`, `ts-node`, `tsconfig-paths`, `tsc-alias`.
- `nodemon` for local reload where established.
- `dotenv` for local environment loading; validate required variables early.

#### HTTP and transport

- `express`.
- `cors`, `helmet`.
- `express-async-errors`.
- `http-errors`.
- `compression` when the reference project uses it.
- `morgan` for HTTP access logs when retained alongside application logging.

#### GraphQL

- `graphql`.
- `@apollo/server`.
- Express integration matching the Apollo/Express major versions, such as `@as-integrations/express4`.
- `@graphql-tools/schema`.
- `graphql-ws` and `ws` for subscriptions.
- `graphql-middleware` and `graphql-shield` when permission rules are part of the established architecture.
- GraphQL Codegen packages for schema/resolver types.

#### Database and authentication

- `mongoose`.
- `jsonwebtoken`.
- `bcrypt` only where password hashing is actually required; OTP-only projects should not add password flows by default.
- `dataloader` for request-scoped batch loading when used by the GraphQL context.

#### Validation and logging

- `ajv`, `ajv-formats`, plus project-used AJV extensions.
- `winston`.
- `zod` only when the selected project uses it for environment or domain validation; do not duplicate AJV without a reason.

#### Testing and quality

- `supertest`.
- `mongodb-memory-server` for isolated database tests where appropriate.
- Either Vitest or Jest plus the matching TypeScript and config packages.
- ESLint, Prettier, Husky, lint-staged, Commitlint/Commitizen when established by the project family.

### Runtime composition

The established topology is:

```text
main.ts
  └─ loads environment and process handlers
      └─ StartServer() in app.ts
          ├─ createExpressApp()
          ├─ create HTTP server from Express
          ├─ apply global middleware and REST/webhook routes
          ├─ connectToDb() through Mongoose
          ├─ create GraphQL HTTP server at /graphql
          ├─ create graphql-ws server at /subscriptions
          ├─ attach 404 and centralized error middleware
          ├─ listen on configured PORT
          └─ initialize approved migrations/crons after core startup
```

The HTTP and WebSocket GraphQL transports share the executable schema and underlying HTTP server. Subscription cleanup must participate in Apollo/HTTP shutdown.

### Express baseline

`createExpressApp` should deliberately configure:

- `x-powered-by` disabled.
- Helmet security headers.
- CORS from explicit environment-aware allowlists.
- Static assets only when required.
- URL-encoded and JSON body parsing with intentional limits.
- Raw body preservation when webhook signature verification requires it.
- `/health` with stable status, service, and version information.
- Request logging without secrets or authentication values.

### MongoDB/Mongoose connection

Keep connection ownership in `src/common/db/index.ts` or the established equivalent:

- Validate `MONGODB_URI` before use.
- Connect once during startup.
- Log success/failure through the application logger.
- Fail startup deliberately when a required database is unavailable.
- Use an explicitly named test-only bypass only for transport smoke tests; never present it as real database verification.
- Define graceful disconnect behavior for tests and controlled shutdown when needed.

### JWT and authentication foundation

JWT configuration should include:

- Environment-validated signing secret, issuer/audience, and expiry policy.
- A token creation/verification helper with narrow return types.
- `verify-token` middleware that extracts the supported bearer/header/cookie transport, verifies deliberately, and attaches principal identity without leaking token values.
- A GraphQL context that exposes principal identity, request metadata, and request-scoped data loaders.
- Thin resolvers. Authentication loading, input whitelisting, authorization, and domain decisions belong in services and shield/guard rules.
- OTP login flows where the project family uses them; do not invent password sign-in.

### Error handling

Use one coherent pipeline:

1. Async route failures reach Express through `express-async-errors` or explicit wrappers.
2. Services create intentional `http-errors` outcomes.
3. Catch blocks map unknown failures to one deliberate public error instead of `throw error` passthrough.
4. `formatGraphqlErrors` converts internal GraphQL failures to stable client responses while logging server detail safely.
5. The terminal Express `error-handler` normalizes REST/webhook errors.
6. Production responses omit stacks, raw database errors, tokens, internal paths, and configuration values.

### Winston logging

Create a singleton logger module with:

- Timestamp, level, service, environment, and structured metadata.
- Human-readable development output and structured production output.
- Error serialization that retains stack internally.
- Redaction for authorization headers, tokens, cookies, credentials, OTP codes, and sensitive personal data.
- Optional transports such as OpenTelemetry/Sentry only when the target project requires them.

Do not scatter independent logger instances or use `console.log` as the application logging architecture. Process-entry fallback logging may remain for fatal boot failures before Winston is available.

### GraphQL organization

A domain normally owns:

```text
src/graphql/<domain>/
├── index.ts
├── typeDefs.ts
├── resolvers.ts
└── <subdomain>/
```

Services, models, interfaces, validators, and permission rules remain in their appropriate layers. Compose type definitions and resolvers centrally in `src/graphql/index.ts`; create one executable schema; use it for HTTP and subscriptions.

Model distinct lifecycle intentions as distinct operations when their permissions, validation, or side effects differ. A generic update or publish mutation should not be the hidden implementation of activate, deactivate, archive, or domain status progression.

### Backend baseline verification

Typical commands—adapt script names to the live package:

```bash
yarn install --frozen-lockfile
yarn generate
yarn lint
yarn test
yarn build
yarn dev
curl -fsS http://localhost:<port>/health
curl -fsS http://localhost:<port>/graphql \
  -H 'content-type: application/json' \
  --data '{"query":"{ health { status service version } }"}'
```

Also establish a real WebSocket subscription connection when subscriptions are part of the acceptance contract. A successful TypeScript build does not prove HTTP, WebSocket, or database startup.

## Web And Admin Frontend Foundation

### Reference architecture

```text
frontend/
├── package.json
├── yarn.lock
├── tsconfig.json
├── vite.config.ts
├── codegen.ts
├── .env.example
└── src/
    ├── main.tsx
    ├── app/
    │   ├── App.tsx
    │   └── providers/AppProviders.tsx
    ├── router/
    │   ├── router.tsx
    │   └── routes/
    ├── services/
    │   └── apollo-client.ts
    ├── redux/
    │   ├── store.ts
    │   ├── rootReducers.ts
    │   └── <slice>/
    ├── hooks/
    │   └── useReduxHooks.ts
    ├── components/
    ├── constants/
    ├── helpers/
    ├── interfaces/
    │   └── graphql/                 # generated output or generated subfolder
    ├── test/
    │   └── setup.ts
    └── <feature>/
        ├── <Feature>.tsx
        ├── components/
        ├── hooks/
        ├── graphql/
        ├── interfaces/
        ├── constants/
        └── helpers/
```

Some reference apps use `src/app/store`, `src/app/graphql`, and `src/features`; others use direct `src/redux`, `src/services`, `src/router`, and top-level feature folders. Inspect siblings and select one pattern—never create both in parallel.

### Baseline dependency groups

- Vite, React, React DOM, TypeScript, React Vite plugin.
- Apollo Client and GraphQL.
- Redux Toolkit, React Redux, and Redux Persist where persistent state is required.
- React Router DOM.
- Mantine core/hooks/form/modals/notifications where Mantine is the chosen family design system.
- GraphQL Codegen CLI and client/type operation presets.
- Testing Library, jest-dom, jsdom, and Vitest or the established test runner.
- `vite-tsconfig-paths` or synchronized aliases in Vite and TypeScript.
- TanStack Query only when REST/server-state needs it alongside Apollo; avoid duplicate state ownership without a reason.

### Provider composition

Create one explicit provider boundary that wires the real infrastructure before feature pages:

```text
AppProviders
  ├─ Redux Provider + persistence gate when used
  ├─ Apollo Provider
  ├─ design-system/theme provider
  ├─ notifications/modals provider
  └─ Router provider
```

Import design-system global CSS in `main.tsx`. Drive API endpoints from environment variables such as `VITE_GRAPHQL_URL`; define a separate WebSocket URL or derive it deliberately for subscriptions.

### State ownership

- Apollo cache owns GraphQL server state.
- Redux owns durable cross-feature client/application state such as auth/session, settings, workflow state, and local coordination.
- Component state owns ephemeral UI interaction.
- URL/search params own shareable navigation and filters.
- Do not mirror the same server entity into Apollo, Redux, and component state without an explicit synchronization reason.

### GraphQL Codegen

Before features:

1. Provide a stable backend schema source or running introspection endpoint.
2. Configure `codegen.ts`.
3. Establish where `.graphql` operations live.
4. Generate typed documents/interfaces into the chosen output folder.
5. Add `generate` or `codegen` script.
6. Run generation before test/build so stale types fail early.

### Shared frontend foundations

Create only genuinely reusable primitives:

- Application shell/layout.
- Loading, empty, error, and unauthorized states.
- Route guards.
- Error boundary.
- Notification/toast bridge.
- Form and validation adapters when a common pattern exists.
- Typed Redux hooks.
- API/Apollo client and link configuration.
- Constants and environment access.

Do not build product-specific pages in shared `components`, and do not centralize every feature into one generic renderer.

For complex form/view domains, place backend-shaped conversion at an explicit mapper boundary. UI state may use audience-appropriate controls while generated GraphQL types remain the transport contract; never expose JSON-shaped persistence merely because it is convenient for the API.

### Web baseline verification

```bash
yarn install --frozen-lockfile
yarn generate
yarn lint
yarn test
yarn build
yarn dev
```

Open the actual Vite URL, verify the root route and provider shell, inspect browser console/network failures, test responsive baseline behavior, and report the actual port if Vite selected a fallback.

## Expo React Native Foundation

### Reference architecture

```text
mobile/
├── package.json
├── yarn.lock
├── app.json or app.config.*
├── eas.json                         # when EAS is used
├── tsconfig.json
├── App.tsx or expo/AppEntry.js
└── src/
    ├── navigation/
    │   ├── index.tsx
    │   ├── stack.tsx
    │   ├── bottomTab.tsx
    │   ├── routes/
    │   ├── constants/
    │   └── interfaces/
    ├── theme/
    ├── redux/
    │   ├── store.ts
    │   ├── ReduxProvider.tsx
    │   └── reducers/
    ├── apollo/
    ├── hooks/
    ├── components/
    ├── constants/
    ├── login/
    │   ├── LoginScreen.tsx
    │   ├── components/
    │   ├── hooks/
    │   ├── services/
    │   ├── helpers/
    │   └── interfaces/
    └── <module>/
        ├── <Module>Screen.tsx
        ├── styles.ts
        ├── constants/
        ├── components/<Module>Drawer.tsx
        ├── hooks/
        ├── graphql/
        ├── interfaces/
        └── <feature>/<Feature>Screen.tsx
```

Use Expo with `expo/AppEntry.js` and React Navigation when matching the established Altin pattern. Do not introduce Expo Router into those applications.

### Baseline dependency groups

- Expo-compatible React and React Native versions selected by the Expo SDK.
- React Navigation native, native-stack, and bottom-tabs.
- `react-native-safe-area-context`, screens, gesture-handler, and Reanimated/worklets versions compatible with Expo.
- Apollo Client and GraphQL.
- Redux Toolkit, React Redux, Redux Persist, AsyncStorage.
- Styled Components where the selected mobile family uses it.
- Expo auth session, web browser, crypto, splash screen, and status bar when the auth/runtime requires them.
- Toast/notification presentation and vector icons from the established stack.

Never force arbitrary package versions into Expo. Start from the selected SDK compatibility matrix and use Expo’s installer for native packages.

Before scaffolding a custom native module, check maintained Expo-compatible packages and their Expo Go/development-build constraints. Optional native capabilities should be loaded only on supported paths and degrade safely when their native module is absent.

### Mobile ownership rules

- `Apps` or launchpad owns directory metadata and navigation to module roots only.
- Each module owns its root composition, drawer state/configuration, visible sections, feature routes, hooks, GraphQL operations, and future data.
- Shared headers, drawers, rows, cards, screen wrappers, loading states, and error states accept presentation props; they do not resolve active modules or own feature data.
- Every route points to a concrete screen under the owning feature/module.
- Preserve target product colors, typography, safe areas, status bar, home indicator, and interaction behavior instead of copying a reference app’s visual identity.

### Mobile startup sequence

1. Create the Expo TypeScript project using Yarn and the project-family-supported Expo SDK.
2. Configure `App.tsx` or `expo/AppEntry.js` and required native imports.
3. Wire safe-area, gesture, theme, Redux/persistence, Apollo, and navigation providers.
4. Define typed route names and stack/tab param lists.
5. Implement the honest authentication/navigation shell before feature modules.
6. Add reusable presentation primitives.
7. Add module roots and concrete empty feature screens only when their ownership is established.
8. Configure app identifiers, schemes, icons/splash, permissions, and EAS profiles before device/distribution work.
9. If system theme is supported, configure native appearance as automatic, add the family-compatible Expo system-UI package/plugin, and make the system preference clear any manual React Native color-scheme override.

### Mobile baseline verification

```bash
yarn install
yarn type-check
yarn format:check
yarn start
```

Then verify at least the intended platform path—Expo Go, development build, simulator/emulator, or device—and run an Expo export or EAS-compatible validation when appropriate. Check login persistence, stack/tab navigation, safe areas, keyboard behavior, back handling, drawer dismissal, and system/light/dark theme behavior. Rebuild the native binary after native appearance, plugins, identifiers, permissions, or native dependencies change; a JavaScript reload is not sufficient. Where a native capability is optional, also verify startup without the linked module.

## Environment And Configuration Contract

Each project should provide a safe `.env.example` or documented configuration contract containing names and descriptions, never secrets.

Typical backend variables:

- `NODE_ENV`, `PORT`.
- `MONGODB_URI`.
- JWT signing/verification settings.
- CORS allowlists.
- Public application URLs.
- Provider-specific variables only when that provider is part of the project.

Typical web/mobile variables:

- GraphQL HTTP URL.
- GraphQL WebSocket URL when subscriptions are used.
- Public environment/feature flags.
- OAuth/app identifiers that are safe to expose; secret material remains server-side.

Fail early for missing required server configuration. Do not accidentally bundle server secrets into `VITE_*` or Expo public variables.

For optional variant-specific native files, omit the config key when no valid path resolves. Do not emit a known-missing placeholder that makes unrelated variants fail configuration or startup.

## Scripts And Quality Baseline

A mature scaffold normally exposes the applicable subset of:

- `dev` / `start`.
- `build` or mobile export.
- `type-check`.
- `generate` / `codegen`.
- `test`, with unit/integration separation where useful.
- `lint`, `lint:fix`.
- `format:check`, `format:fix`.
- `prepare` for Git hooks when used.

Commands must match real configuration files. Do not add a script whose config or dependency is absent.

## Definition Of Ready For Feature Logic

A project is ready for screens, pages, or domain logic only when:

- [ ] Exact app boundaries and folder destinations are confirmed.
- [ ] Package manager and supported runtime versions are locked.
- [ ] Dependencies are installed without competing lockfiles.
- [ ] TypeScript aliases resolve in editor, build, tests, and runtime.
- [ ] Environment contract exists without committed secrets.
- [ ] Backend startup, database policy, health endpoint, GraphQL HTTP, subscriptions, auth context, logger, and error pipeline are wired where applicable.
- [ ] Web/mobile providers, router/navigation, Apollo, Redux, theme, persistence, and typed hooks are wired where applicable.
- [ ] GraphQL Codegen runs against a valid schema when used.
- [ ] Baseline tests and type checks pass.
- [ ] Production build/export succeeds.
- [ ] Development server/app starts.
- [ ] A real endpoint, route, or device screen has been exercised.
- [ ] Runtime warnings, unavailable dependencies, and unverified paths are reported honestly.

## What Is Not Automatically Part Of Every Scaffold

Do not add these without project evidence or explicit scope:

- Kubernetes, microservices, message queues, Redis, event sourcing, or a monorepo.
- Password authentication in OTP-only products.
- Docker topology that relocates migrations, cron jobs, subscriptions, or deployment responsibilities.
- Sentry, OpenTelemetry, PostHog, analytics, AI providers, payments, email, SMS, object storage, or push notifications.
- Generic repositories/services/use-case abstractions that the reference projects do not use.
- Placeholder business modules solely to make the tree look complete.

## Implications

- New projects should be compared against the nearest successful sibling before scaffolding.
- The complete foundation should be built and verified once, then product features can grow inside stable ownership boundaries.
- Repeated corrections discovered during the Codex history harvest should update this manual only when they are reusable across projects; project-specific details belong in project entity pages.

## Contradictions Or Tensions

- The reference repositories contain both Jest and Vitest, and multiple frontend folder variants. This manual deliberately preserves them as choices resolved by the target project family.
- Existing repositories may retain older dependency versions or legacy structure. Matching architecture does not require copying known vulnerabilities or obsolete versions; choose current compatible versions without silently redesigning ownership.
- Altin’s inspected tree still exposed names associated with an earlier centralized module-shell anti-pattern, while the durable correction requires module-local ownership. The correction defines the desired architecture; live cleanup status must be verified before changes.

## Related

- [[software-development-operating-manual|Software Development Operating Manual]]
- [[../concepts/codex-project-knowledge-harvest|Codex Project Knowledge Harvest]]
- [[personal-operating-manual|Personal Operating Manual]]
- [[../concepts/hermes-obsidian-memory-architecture|Hermes–Codex–Obsidian Shared Brain Architecture]]

## Sources

- [[../sources/project-knowledge-completion-and-bootstrap-directive|Project Knowledge Completion And Bootstrap Directive]]
- [[../sources/livelycura-project-knowledge-harvest-batch-2|LivelyCura Project Knowledge Harvest — Batch 2]]
- [[../sources/livelycura-project-knowledge-harvest-batch-3|LivelyCura Project Knowledge Harvest — Batch 3]]
- Live representative project manifests and startup/source layouts inspected on 2026-07-21 under `/Users/acazumah/Documents/LivelyCura`, `/Users/acazumah/Documents/compFlow`, and `/Users/acazumah/Documents/C.E.Q.A`.
- Coder-profile `project-scaffolding-workflows` skill and linked correction references inspected on 2026-07-21.

## Open Questions

- Which sibling project should be the canonical reference for a brand-new backend when no product family exists?
- Should the default new web project use the `src/app/providers + src/features` variant or the direct `src/router + src/redux + top-level feature` variant?
- Should Vitest become the default across new backends, or should Jest remain the baseline for CompFlow-style services?
- Which CI, Docker, deployment, and observability layers are universal enough to add to the baseline rather than project-specific extensions?
