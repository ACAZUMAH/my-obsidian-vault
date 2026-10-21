---
type: synthesis
status: active
created: 2026-07-20
updated: 2026-10-19
tags: [software-development, operating-manual, project-conventions]
sources:
  - ../sources/altin-reports-mobile.md
  - ../sources/altin-profile-inline-edit-correction.md
  - ../sources/altin-formik-onsubmit-correction.md
  - ../sources/altin-profile-separate-editors-correction.md
  - ../sources/livelycura-independent-fleet-and-platform-dispatch.md
  - ../sources/livelycura-graphql-contract-compatibility.md
  - ../sources/hermes-persistent-memory-import.md
  - ../sources/shared-brain-all-agents-directive.md
  - ../sources/project-knowledge-completion-and-bootstrap-directive.md
  - ../sources/livelycura-project-knowledge-harvest-batch-1.md
  - ../sources/livelycura-project-knowledge-harvest-batch-2.md
  - ../sources/livelycura-project-knowledge-harvest-batch-3.md
  - ../sources/livelycura-project-knowledge-harvest-batch-4.md
  - ../sources/livelycura-project-knowledge-harvest-batch-5.md
  - ../sources/compflow-project-knowledge-harvest-batch-1.md
  - ../sources/compflow-hermes-project-knowledge-harvest-supplement-1.md
  - ../sources/kusantec-bora-project-knowledge-harvest-batch-1.md
  - ../sources/bora-realtime-support-subscriptions.md
  - ../sources/bora-notifications-marketing.md
  - ../sources/ceqa-altin-project-knowledge-harvest-batch-1.md
  - ../sources/ceqa-altin-project-knowledge-harvest-batch-2.md
  - ../sources/ceqa-altin-project-knowledge-harvest-batch-3.md
  - ../sources/portfolio-project-knowledge-harvest-batch-1.md
  - ../sources/hermes-conversation-harvest-scope-correction.md
  - ../sources/hermes-session-coverage-audit-2026-07-21.md
  - ../sources/ceqa-altin-hermes-conversation-harvest-supplement-1.md
  - ../sources/compflow-checkcity-hermes-conversation-harvest-supplement-1.md
  - ../sources/kusantec-bora-hermes-conversation-harvest-supplement-1.md
  - ../sources/hermes-livelycura-skills-keks-pharmacy-harvest-batch-1.md
  - ../sources/hermes-generalized-skills-courier-recovery-harvest-batch-1.md
  - ../sources/livelycura-stock-sales-hermes-supplement-1.md
  - ../sources/ceqa-call-center-hermes-supplement-2.md
  - ../sources/livelycura-stock-sales-hermes-supplement-2.md
  - ../sources/hermes-project-bootstrap-git-continuation-batch-1.md
  - ../sources/livelycura-stock-sales-hermes-supplement-3.md
  - ../sources/hermes-vault-infrastructure-continuation-batch-2.md
  - ../sources/graphql-product-bora-paystack-hermes-chain.md
  - ../sources/ride-ordering-livelycura-hermes-chain.md
  - ../sources/courier-mobile-evening-work-hermes-chain.md
  - ../sources/portfolio-carousel-skills-livelycura-hermes-supplement.md
  - ../sources/product-lab-badge-mls-hermes-chain.md
  - ../sources/compflow-proper-stack-hermes-continuations.md
  - ../sources/compflow-backend-auth-hermes-continuations.md
  - ../sources/bora-security-hardening-hermes-continuations-6-20.md
  - ../sources/bora-authentication-session-hardening-continuations-21-35.md
  - ../sources/bora-runtime-payment-safety-continuations-36-50.md
  - ../sources/altin-mistitled-casual-greeting-continuations.md
  - ../sources/typescript-service-conditional-flow-decision.md
  - ../sources/altin-orders-mobile-web-reference.md
  - ../sources/altin-mobile-brand-system.md
  - ../sources/altin-theme-navigation-runtime-corrections.md
  - ../sources/altin-permission-gating.md
  - ../sources/altin-module-builds-and-scope-corrections.md
  - ../sources/altin-profile-support.md
  - ../sources/bora-fund-administration-access-control.md
  - ../sources/bora-bcl-error-passthrough-and-secret-files.md
  - ../sources/bora-single-user-update-path.md
  - ../sources/bora-admin-portal-ci-cd-convention.md
confidence: medium
---

# Software Development Operating Manual

## Thesis

This page centralizes durable development preferences and project conventions that should be available to Hermes and Codex. Agents must still inspect live repositories before acting: this is an operating map, not a substitute for current code.

## Coverage And Expansion

- The Project Knowledge below is a compact map, not a complete inventory of every repository or historical decision.
- The initial version was promoted mainly from Hermes persistent memory; additional evidence exists in live repositories, Codex transcripts, and an unclassified Hermes-session backlog.
- Use [[../concepts/codex-project-knowledge-harvest|Codex Project Knowledge Harvest]] only when Codex history is explicitly in scope. A Hermes-conversation harvest requires direct Hermes conversation evidence; repository discovery may verify claims but cannot create them.
- Detailed repository knowledge should move into dedicated project pages. Keep only cross-project rules and navigation here.
- Use [[new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]] for the reusable pre-feature setup sequence across backend, web, and mobile projects.

## Evidence

- The initial working agreements and project map came from promoted Hermes persistent memory and the shared-brain directives.
- The bootstrap baseline is supported by the user's explicit correction, the coder-profile scaffolding workflow and references, and representative LivelyCura, CompFlow, and Altin repository structures inspected on 2026-07-21.
- The first bounded LivelyCura harvest inventoried ten independently versioned repositories and processed eight Codex sessions. Detailed facts and unresolved implementation conflicts live in the linked project pages and [[project-knowledge-harvest-status|Project Knowledge Harvest Status]].
- The second LivelyCura batch processed eight older MLS, ERP, and CheckCity sessions and reconciled their successive corrections against current code. It supports the scoped-change, explicit-lifecycle, existing-catalog reuse, flow-ownership, and reduced-motion rules below.
- The third LivelyCura batch processed eight mobile distribution, custom-app, migration, native-module, and interaction sessions. Repetition across SERLP, Loop, and CheckCity supports the store-artwork rules; current source plus later corrections supports the optional-native-module, system-theme, and deferred-feature rules.
- The fourth LivelyCura batch processed eight lab-research, courier release/task, Pharmacy Portal classification, and CheckCity interaction sessions. It supports canonical identifier mapping, caller-owned presentation spacing, platform-specific mobile QA, distribution metadata, and floating-header refresh rules while explicitly rejecting several stale intermediate implementations.
- The fifth LivelyCura batch classified the final five working-directory records as four duplicate guardian approval contexts and one unrelated pet-generation task. LivelyCura history is complete for the 37-session discovered set; no project or scaffolding convention was promoted from the triage-only batch.
- The first CompFlow batch inventoried four independently versioned applications and found no historical CompFlow Codex sessions. It verifies the current application boundaries, OTP/onboarding/payroll backend rules, and several unresolved integration/configuration gaps documented in the linked project pages.
- The CompFlow Hermes supplement processed the one discovered scaffolding session. It directly supports the user-stated separate-folder and Yarn conventions for the original promotional, admin, and backend applications; its historical tests/builds/smoke checks are attributed rather than treated as current verification, and the later client portal remains repository-only evidence.
- The first Kusantec/Bora batch inventoried the backend and mobile repositories and reconciled all six directly matched historical Bora sessions. It supports the financial-provider, notification, AI-assistant, and repository-local skill rules below while retaining current-versus-historical conflicts in the linked project pages.
- The first C.E.Q.A/Altin batch inventoried three applications and processed the eight most recent of 21 direct current/legacy working-directory records. It supports module-local mobile ownership, layered permission protection, server-backed search feedback, stable checkout idempotency, and ordered address/location updates while leaving thirteen older records pending.
- The second C.E.Q.A/Altin batch processed the next eight older records. It supports endpoint-shaped filters, feature-file separation, safe optional rendering, schema-owned form validity, and atomic async location updates while preserving current drift in Keks settings and call-center picker ownership.
- The third C.E.Q.A/Altin batch processed the final five records, completing the 21-record discovered set. It supports accessible launch-card semantics, shared theme state, import-boundary discipline, branch-dependent state invalidation, and correct threshold-discount semantics while preserving unresolved route, import-style, and backend-role tensions in the project pages.
- Portfolio batch 1 classified four substantive direct working-directory rollouts plus one missing-rollout index shell. Its repository-only mock-up prototype page was removed because no Hermes conversation supported that page.
- Standalone Projects batch 1 is superseded. It found zero direct conversations but incorrectly promoted repository inventory as project knowledge; four pages were deleted, three retained identifiers were reduced to provenance-review placeholders, and its cross-project script rule was retracted.
- Repository-root coverage is not conversation-harvest completion. Each promoted project page and durable claim must be traceable to the explicitly requested conversation archive.
- The 2026-07-21 Hermes audit found 225 physical store records but only 220 unique IDs after cross-store de-duplication: 130 unique non-subagent conversations and 90 unique `source='subagent'` conversations. The first explicit-project-cwd follow-up classified 15 more conversations—13 substantive and two interrupted—bringing directly classified non-subagent coverage to 16 of 130 while leaving 114 pending. Existing Codex family-completion claims still do not establish Hermes-history completion.
- The direct Hermes supplements add Altin/Keks scaffold-navigation-webhook provenance, CompFlow/CheckCity architecture and interaction provenance, and Bora’s staged security-authorization/Sentry/encryption provenance without conflating those records with the existing Codex batches.
- The LivelyCura skills/Keks/Pharmacy Hermes batch recovers the exact active-profile skill-import procedure, the original Keks Chakra fix, and a user-corrected Pharmacy interface move whose false first completion and regex corruption support stricter file-level verification.
- The generalized-skills/Courier Hermes batch records the correction that exact project skills and reusable stack-level synthesis are complementary layers, and preserves the minimum-consumer-contract approach for recovering untracked shared code.
- The no-cwd stock/sales record adds direct Hermes provenance for exact sale-time COGS, sale-item return identity, stock-behavior compatibility, and runner-owned production migrations; the Call Center record adds provider-session token lifecycle and current cached-location/tooling evidence.
- Stock/Sales continuation 2 closes exact-cost test coverage, completes sale-return identity cleanup across backend/client/presentation, and corrects optional native-module startup loading. The bootstrap/Git continuation establishes execution provenance for the initial bounded harvest/bootstrap artifacts and public-vault safety workflow without adding application-project claims.
- Stock/Sales continuation 3 closes historical full-suite reporting and adds defensive migration diagnostics. The next vault continuation closes the ignore verifier and creates initial skill/schema/template infrastructure but compresses before exact-session validation passes. The GraphQL/Bora chain supports legacy-data backfill over fallback resolvers and exposes provider-migration idempotency, mapping, and logging risks.
- The Ride/LivelyCura chain establishes Let’s Ride’s foundation-only architecture and earlier stock/sales implementation ownership. The Courier chain adds the exact-sibling transfer rule. The Portfolio carousel/Skills supplement establishes the accepted equal-card Swiper baseline, current Skills motion ownership, and the boundary between replayed Portfolio context and unique LivelyCura work.

## General Working Agreements

### Communication And Execution

- Be direct, respectful, technically sophisticated, and concise.
- Disagree plainly when a proposed design is technically wrong or unsafe; explain the issue and recommend the stronger alternative instead of reflexively affirming.
- Explain how components fit together and why a change is correct, without turning the response into a generic tutorial.
- Avoid unexplained abbreviations and project-local shorthand; define necessary terms at first use so decisions remain understandable outside the originating session.
- Treat saved skills and linked references as execution checklists, including exact file responsibilities and project-specific patterns.
- Inspect repository-local `.agent/skills` and `.agents/skills` when present; those instructions can define the project's current file ownership, documentation, and implementation conventions more precisely than older transcripts.
- When project conventions represent the user’s general engineering approach, preserve the exact project skills and synthesize a separate auditable backend/frontend-web/frontend-mobile layer. Do not flatten project-specific names or assumptions into generic skills.
- Application-startup migrations use the runner-owned connection and imported models. Stream large datasets with bounded work, update dependent references before deleting duplicates, backfill before tightening required contracts, and verify idempotence plus reference integrity.
- Defensive migration diagnostics must not throw while formatting malformed historical identifiers. Preserve the primary conflict/error even when legacy IDs are absent or invalid.
- A local migration registry provides once-after-success, not provider-level exactly-once behavior. External side effects need stable entity-to-input mapping, provider idempotency, partial-failure reconciliation, redacted logs, and rerun tests.
- When a financial line changes identity, migrate persistence fields, indexes, API contracts, clients, and presentation together. Detect conflicting active rows before creating replacement uniqueness, never silently merge financial conflicts, and remove stale one-movement presentation that no longer matches the domain.
- When a provider defines suggestions and selected-place resolution as one billable/logical session, generate one token at search start, reuse it through selection resolution, and clear it only after consumption or cancellation.
- Reread live files before editing because the user may modify code during review; preserve those changes.
- New code copies the structure of the nearest existing sibling (hook shape, error handling, where types live) instead of introducing patterns the codebase does not use, such as inline response interfaces or custom error classes in a hook. See [[../sources/call-center-wider-search-hook-and-action-correction|Call Center Wider Search Hook And Action Correction]].
- When the user names a live sibling implementation as the source of truth, reread that exact implementation immediately before editing and compare its complete contract with the destination. Never restore an earlier agent-authored version over newer user changes; preserve the newer code and adapt only what the destination requires.
- Do not treat cached reads, unchanged tool responses, or a successful-looking edit command as proof that source changed. Reread every touched file and run the relevant checks before claiming completion; avoid regex-based bulk edits of TypeScript/TSX structure when targeted edits can preserve syntax and logic.

### Change Control

- Handle security remediation one issue at a time.
- Explain and verify each fix before starting the next issue.
- A question about continuing is not authorization to edit. During review-gated remediation, wait for the user’s explicit next instruction.
- Never read `.env` or other secret-bearing files (credentials, keys, tokens), not even to make a live or staging provider call. When a check needs real credentials, give the user the exact call to run instead. See [[../sources/bora-bcl-error-passthrough-and-secret-files|Bora BCL Error Passthrough And Secret-File Boundary]].
- Mirror exact UI and scaffolding references when the user asks for exact fidelity. When screenshots are examples, preserve the established system visual language and extract only the requested interaction pattern.
- When the user asks to copy a sibling implementation exactly, transfer its real components, dependencies, theme/form contracts, and platform assumptions; adapt only the destination project’s business hooks and navigation. A visual approximation is not equivalent.
- Treat visual references as inspiration unless exact fidelity is requested. Preserve approved regions while iterating on unresolved regions, and validate real asset formats before integration rather than trusting filename extensions.
- Stay within requested scope and distinguish launch blockers from long-term roadmap work.
- Web portal CI/CD copies the `livelycura-pharmacy-portal` workflows: reusable CI, self-contained `staging.yml` (`develop`) and `production.yml` (`main`) with build → artifact → Netlify deploy jobs. API URLs are repository variables named per environment (`STAGING_…`/`PRODUCTION_…`), secrets are repository-level and environment-named (`NETLIFY_STAGING_SITE_ID`); never hardcode API URLs in workflow YAML or rely on environment-scoped values. See [[../sources/bora-admin-portal-ci-cd-convention|Bora Admin Portal CI/CD Convention]].
- A mutation check counts only when the mutated code compiles and a test assertion fails; a compile error is a false pass for the test suite.
- Yarn v1 can leave stale nested packages that `yarn install --force` does not prune. `yarn check --verify-tree` exposes them and rebuilding the affected scopes fixes them; a cached build image can carry the same drift, so clear the build cache when a newly imported dependency fails to load.

- Make the narrow requested change without deleting or collapsing adjacent architecture. Preserve existing reads, filters, permission rules, loaders, hooks, and extension points unless removal is explicitly in scope.
- Verify UI work in the real running page after static checks when a live surface is available; say which visual paths were not exercised.
- For store-distribution artwork, use real product screenshots and the correct project identity, render exact platform dimensions in RGB without alpha, and avoid invented UI, unrelated logos, or artificial heavy device frames/backing. Keep repeatable rendering inputs distinct from unverified historical output files.
- When deferring a feature, isolate only its files and hunks on a dedicated branch while preserving unrelated active work. A preserved branch is a historical snapshot that must still be checked against later package and architecture decisions.
- Shared presentation components accept contextual layout props; callers own spacing that differs by surface. Do not move one caller’s margin or positioning into a shared component when another caller needs different layout.
- For retryable create/checkout commands, keep one idempotency key for the same semantic payload and rotate it only when meaningful input changes or the operation completes. An in-flight UI guard reduces duplicate calls but does not replace the server-visible idempotency contract.

### TypeScript And Backend Boundaries

- Add JSDoc to every new or exported TypeScript function.
- Write functional code: exported functions and factory functions that return plain objects with closure state. Do not author classes, including infrastructure adapters and test fakes; when a library expects a subclass, wrap a library instance in a factory. Instantiating library-provided classes remains acceptable.
- Confirm deployment topology—instance count and process model—before adding cross-process infrastructure. An in-process event bus is correct for a single instance; keep the swap point to one export so scaling later does not touch callers.
- Pass related function parameters as one typed data object rather than positional arguments; define that input in the domain-owned interface layer.
- Do not chain or nest conditional expressions to orchestrate service work. Use explicit branches and move loading, validation, calculation, and document construction into documented, domain-owned helpers.
- Map catch blocks to one deliberate `http-errors` outcome; do not rethrow an unchanged error with `throw error`.
- Keep GraphQL resolvers transport-only: use generated operation argument types and enums, delegate mapping, filtering, calculation, normalization, and response construction to the owning service, and never repeat schema enums as handwritten string unions. A nested field resolver may pass its parent value and generated field arguments directly to a service when GraphQL supplies arguments at that field. For root operations, pass one typed domain object named `data` to the owning service. When actor identity is required, add only the authenticated actor ID to that object; do not pass a full user document or split related input across positional arguments. GraphQL Shield owns endpoint permission and tenant-context checks where the project already routes them through Shield; services fetch referenced records and own business validation, domain invariants, and scoped persistence without repeating those endpoint checks.
- Let each feature service own its model queries and persistence. Keep helper directories pure; name database services for the domain operation they perform. Start and close a transaction in the concrete multi-document workflow that needs atomicity instead of routing unrelated CRUD through a feature-wide transaction wrapper.
- Never pass the full `GraphqlContext` into a domain service. Resolve only required transport-owned values at the GraphQL boundary—such as actor ID, organization IDs, platform scope, or client-app classification—and merge that subset into the service's typed `data` object.
- When a GraphQL query or mutation needs multiple client values, expose one generated input-object argument (normally `data`) and type the resolver with the generated operation args; do not declare multiple root-field arguments or hand-write resolver arg shapes.
- When a non-null GraphQL contract exposes invalid legacy storage, backfill persisted data and normalize writes rather than masking bad state with fallback field resolvers when migration is the accepted correction.
- When cleanup is explicitly deferred for retired values inside an enum list, filter output against the current enum at the owning GraphQL field boundary. Do not restore a retired enum member merely to serialize stale storage. Separately, remove deleted backend fields from every client operation, filter, view, generated type, and fixture.
- Do not restore fake schema fields, resolvers, permissions, or hardcoded data merely to satisfy stale tests. Remove the unsupported contract and update consumers, Shield rules, generated artifacts, and tests honestly.
- Separate domain concerns into owned folders, interfaces, models, services, and tests. Do not centralize a feature in one file or import a convenient helper from an unrelated business domain.
- Reuse established domain infrastructure—such as agent workflows, email templates, and generated GraphQL contracts—before creating parallel mechanisms.
- Write a repeated operation once and import it everywhere. When the same model write, query options, or projection appears in several services, extract one shared function instead of copying it. Keep transactional and non-transactional variants separate, with the session as a required parameter on the transactional one (for example Bora's `updateUserInSession` and `updateUser`). User corrections, 2026-10-16. See [[../sources/bora-single-user-update-path|Bora User-Update Paths]].
- Search for existing catalogs and relationship services before adding a new model. Reuse first-class records and dedicated add/remove operations rather than creating parallel taxonomies or link tables.
- Give materially different domain transitions their own services, mutations, permissions, and tests. Do not overload publish, update, or another nearby action to implement activate, deactivate, archive, or status progression.
- Keep commercial and operational ownership explicit. A new domain side effect should join the established transaction when atomicity is required; it should not duplicate inventory, billing, audit, or accounting responsibility.
- For external financial providers, separate provider transport, domain orchestration, configuration, persistence, and GraphQL entry points. Keep external calls outside database transactions, then use verified provider state, idempotent claims, and reconciliation to make local finalization safe.
- Scope ODM/query sanitization to untrusted filter input boundaries; a global sanitization switch can corrupt trusted application operators and background-job queries.
- When one security operation is exposed through multiple transports, delegate every transport to one owning service and add transport-level regression coverage so REST, GraphQL, and subscription behavior cannot drift.
- When multiple notification channels are acceptable alternatives, attempt them independently or concurrently, proceed only when at least one configured channel succeeds, and fail when all configured channels fail. Preserve channel-specific diagnostics without exposing private payloads.
- Mocked provider adapters prove deterministic orchestration, not live credentials, signatures, network behavior, settlement, or production delivery. State live-provider evidence separately.
- Before building on existing infrastructure, prove it is live: trace its callers and history, and load it outside mocked tests. A helper with no callers may have lost its API, and a dependency that tests always mock may not load at all.
- Validate every field of the owning record before uploading its file, so rejected requests never leave objects in storage.
- When marketing sends are queued or paced, check consent again at send time; an opt-out must stop messages already queued.
- With graphql-shield on graphql-middleware, a Subscription field that has a custom `resolve` is authorized per event, not at `subscribe`; guard stream setup explicitly in the subscribe path. Return deliberate `http-errors` from Shield rules—thrown rule errors are replaced by the generic fallback error—and configure a client-facing `fallbackError` so denials never surface as internal server errors.
- If GraphQL authorization uses an allow fallback, maintain an exhaustive root-operation coverage test that fails for every unmapped query, mutation, and subscription. Deny-by-default remains safer when the project can adopt it without compatibility breakage.
- Treat current package scripts and test configuration as authoritative when historical docs name a superseded runner. New tests use the repository's current runner.
- Keep one canonical identifier per route/domain concept. When an existing external payload uses a different field location, map it at the consumer boundary rather than adding duplicate backend aliases or route fallbacks for the same value.
- Apply visibility rules deliberately across query filters, public transformations, and GraphQL authorization. Redact only fields required by the visibility contract; do not strip unrelated media or canonical domain data as a shortcut.
- Bind provider-backed reads and financial writes to authenticated principal ownership before external calls. When a compatibility input still carries identity, apply canonical principal identity after caller data so it cannot be overridden; resolve incoming IDs and use fetched document identity downstream.

### Frontend State And Rendering Boundaries

- A named mobile reference requires reuse of its actual composition patterns: shared screens, compact rows, skeletons, and state presentation, with data/filter/navigation logic still feature-owned. Show a few useful scan fields and reveal full information in details rather than filling each card with every field. The [[../sources/altin-orders-mobile-web-reference|Altin compact-card and SERLP reuse correction]] supplies direct evidence.

- Use the established `const Component: React.FC<Props> = (...) => ...` declaration style, with `React.FC` for no-props components and props interfaces in owned interface files. The direct [[../sources/altin-orders-mobile-web-reference|Altin React.FC correction]] makes this preference explicit; changing annotation style must preserve enum/literal value safety and existing behavior.
- Reuse the project’s existing Conditional and skeleton components. In the established mobile feature structure, list and detail screens occupy sibling feature folders. UI cleanup preserves the user’s current card/navigation structure and intervening edits; it does not authorize restoring removed elements or creating parallel runtimes when the app is already running. The [[../sources/altin-orders-mobile-web-reference|Altin Orders corrections]] provide direct evidence.

- Keep feature components, hooks/queries, helpers, constants, and interfaces in their established owned files or folders. Do not accumulate transport, iteration, conversion, and presentation concerns in one large component.
- Keep one primary UI component per component file when that is the project's established structure. Compose named files at the parent boundary instead of creating files that bundle several independent editors or sections.
- Do not create a feature-level `shared` folder as a default home for unrelated forms, scope wrappers, uploaders, helpers, and list components. Keep code in the owning create, list, detail, or update flow until repeated current implementations prove a stable shared abstraction.
- Each GraphQL operation hook owns exactly one query, mutation, or subscription. Keep operations in separate hook files and compose those hooks at the screen or component boundary; never combine different GraphQL operations in one hook. Do not bundle separate count/list reads as aliased roots in an overview query.
- Follow the user's actual Apollo hook contract: private complete gql in the hook file; typed useQuery with context/filters, named domain data/pageInfo, error/empty display flags, then `...result`. Mutation hooks use typed useMutation with relevant refetchQueries, a generated-input named action with try/catch success/error feedback, successful server-data return and mutation-owned Toast feedback; the current mobile reference exposes a named action plus loading. Keep screen interactions outside operation hooks; do not replace this pattern with a generic request engine or bare mutation tuple. The [[../sources/altin-orders-mobile-web-reference|September 12 exact hook examples]] explicitly require consulting the available reference projects and Obsidian before implementing.
- Preserve native interactive semantics. Use styling classes for group selectors, keep buttons exposed as buttons, and add specific accessible names instead of replacing semantic roles for CSS convenience.
- Keep one shared System/Dark/Light appearance state across application surfaces, expose selection accessibly, and honor reduced-motion preferences for decorative transitions.
- Configure TypeScript and the bundler with the same aliases. Use absolute imports across top-level feature roots and relative imports within the same root feature unless the selected repository establishes a different explicit rule.
- Make visible filters match the selected API contract. Do not copy a control from an adjacent report when its endpoint does not accept that parameter; keep shareable filter state URL-backed when that is the established pattern.
- Avoid proliferating form-specific folders, wrapper files and schema factories where the reference declares fields and rules directly. The user explicitly rejected Altin’s outletForm layer and the supplied order schema/controller; moving the same code into different files is not a correction. See [[../sources/altin-orders-mobile-web-reference|the form-layer rejection]].
- Preserve the same form code structure across projects: inspect actual hooks and component bindings before editing. Use private module-level `const validationSchema = yup.object().shape(...)`, named `use…Form` hooks and real Formik bindings in components; requests run from screen handlers, not onSubmit (see the 2026-10-09 rule above). Do not substitute callback-driven form controllers, single-use schema folders or promise orchestration merely because Formik/Yup are installed; the user explicitly rejected that migration. See [[../sources/altin-orders-mobile-web-reference|the cross-project form-structure correction]].
- Formik `onSubmit` never makes backend requests (user correction 2026-10-09; supersedes the SERLP onSubmit shape and the repo-committed-hooks rule). Form hooks hold state only: private Yup schema, `initialValues` (edit forms: record parameter, `useMemo`, `enableReinitialize: true`), `validateOnMount: true`, `onSubmit: () => {}`, `return form`. Screens own `handleSubmit`, which reads `form.values`, calls the named mutation action and navigates on success; multi-step screens use a `use…Screen` hook. Buttons use mutation `loading` and `form.isValid`. Reference the LivelyCura pharmacy portal (`accounting/createCurrency`), admin portal (`organizationBasicInfoSection`) and Check City (`login/components/Auth.tsx`, `cart/hooks/useCheckoutScreen.ts`). See [[../sources/altin-formik-onsubmit-correction|the Formik onSubmit correction]].
- Values saved by different APIs get separate editors and separate saves; never bundle them into one form to save several mutations. Phone inputs in LivelyCura-family apps take local numbers and convert with `awesome-phonenumber` (`validatePhoneNumber`, `getPhoneNumberWithCode`, `getPhoneNumberWithZero`, region GH); never make users type the country code. See [[../sources/altin-profile-separate-editors-correction|the separate editors correction]].
- Mutation errors belong in the hook's Toast feedback, including actual API validation field messages. Do not add ApiError/assertion/response-unwrapping layers or rethrow merely to populate form banners. Failed actions return no successful result; forms keep drafts and advance only on success. Use Apollo loading instead of parallel saving refs. Keep client Yup and read-query errors distinct. See [[../sources/altin-orders-mobile-web-reference|the mutation Toast correction]].
- Use Formik and Yup for forms, following Caleb’s actual reference hooks: typed useFormik, validationSchema, validateOnMount and onSubmit, returning the real form to the UI. Formik owns values, errors/touched, dirty state and validity; screens own submission. Fix schemas or state transitions instead of duplicating field-presence rules or introducing manual form engines. See [[../sources/altin-orders-mobile-web-reference|the explicit Formik/Yup correction]].
- Presentation conditionals do not make unsafe JSX expressions lazy. Derive optional values safely before constructing child elements.
- Commit interdependent async form values as one valid transition. If coordinates require a resolved address, do not publish the coordinates first and leave the form in an invalid intermediate state.
- Keep controls visible but disabled with specific feedback when the workflow benefits from spatial continuity and the user must satisfy a prerequisite.
- Scope asynchronous loading state to the control that initiated the request. A shared mutation loading flag must not make independent sibling upload or action buttons appear busy.
- Drive public product claims, counts, profile facts, and capability labels from authoritative API/CMS data with explicit fallbacks; do not invent metrics to fill a layout.
- Use section-specific responsive rails when a hero or immersive surface needs breathing room. Do not constrain the entire page with one percentage width; verify mobile, tablet, desktop, and ultra-wide behavior plus reduced-motion paths.
- When one selection invalidates derived state, reset all dependents before accepting the new source value and recompute every affected line or total. Do not carry branch-dependent addresses, estimates, availability, or pricing into a new branch context.
- Keep pricing eligibility separate from the deduction itself. A threshold decides whether a discount applies; the configured fixed or percentage discount value decides how much to deduct.
- With Apollo's normalized cache, every object a query shares with another query must select its `id`. Without it Apollo replaces the shared object, which can trigger refetches that remount providers or navigation. See [[../sources/altin-module-builds-and-scope-corrections|the Altin module builds record]].

### React Native

- Use Expo with React Navigation under `src/navigation`, not Expo Router, when working in the established mobile architecture.
- Mirror existing applications and preserve text contrast plus safe-area, status-bar, and home-indicator backgrounds.
- Prefer restrained motion built on the project's existing animation stack, honor the platform reduce-motion preference, and keep decorative/theme transitions behind readable interactive content.
- Research maintained Expo-compatible packages before building a custom native module. If an optional native module may be absent, load it only on the supported path and fail softly rather than crashing application startup.
- Treat system appearance as native and JavaScript configuration together. Native automatic appearance and relevant Expo system-UI integration require a rebuilt native binary; a JavaScript reload is insufficient.
- Emit variant-specific native file configuration only when the selected variant resolves a valid path.
- For phone/OTP authentication, prefer controlled native input behavior with numeric filtering, paste/autofill, exact-length validation, and explicit Android/iPhone/iPad QA. Do not rely on a hidden overlay pattern without testing how each platform renders and focuses it.
- Matching visual treatment across iOS and Android requires auditing Android `elevation` separately from iOS shadow properties.
- A floating-header list should remain full-screen so content can pass underneath. Disable surprise automatic inset adjustment and use explicit safe-area content insets/offsets plus visible, themed pull-to-refresh placement.
- Bottom-sheet modals that must reach the Android screen edge should account for full device dimensions and translucent system bars; verify after a cold/full reload, not only fast refresh.
- System-area color consistency spans every mounted layer: root, safe-area provider, status bar, navigation theme, scene/tab containers, screens, and headers. Preserve accepted navigation structure when the request is color normalization, not redesign.
- Before dynamically importing a native Expo package, check `requireOptionalNativeModule`; on a binary built before the package was added, the import is a fatal error under Metro rather than a rejected promise. A native `Modal` covers the root toast host, so a modal that runs mutations needs its own host while open. See [[../sources/altin-profile-support|the Altin Profile and Support record]].
- After adding a native Expo module, confirm the iOS rebuild actually happened before debugging a missing module. `pod install` fails silently without a UTF-8 locale, so set `LANG=en_US.UTF-8`. See [[../sources/altin-reports-mobile|the Altin Reports record]].
- When an app-gating query reads a root field (such as `currentUser`) without normalizable ids, any other query on that field must use `no-cache`: writing it can replace the gating data and unmount navigation, even when ids match, because the response envelope itself is not normalized. See [[../sources/altin-profile-support|the Altin Profile and Support record]].
- Do not wrap a scrollable sheet panel in a Pressable; it claims scroll and switch touches. Put a separate backdrop Pressable behind the panel. A Pressable style function must not return `undefined` for a property the styled component sets, because it overrides the base fill; set it only in the pressed branch. See [[../sources/altin-module-builds-and-scope-corrections|the Altin module builds record]].
- Gate mobile screens the SERLP way: keep every route registered and wrap guarded screens so a failed check shows a No access screen. Unregistering routes makes navigation fail silently and ejects users when permissions change. Gate the buttons and screens that trigger mutations; mutation hooks do not re-check permissions, and the backend stays authoritative. Query hooks keep their permission skip because they run on mount and are reused on ungated screens, and refetches need the same gate since Apollo Client 3 `refetch()` sends a skipped query. See [[../sources/altin-permission-gating|the Altin permission gating decision]].
- Store-review readiness includes concrete permission purpose strings, every declared device class, accurate public product naming, and a reviewer-accessible seeded account when protected functionality cannot otherwise be inspected. Never persist review credentials in the vault.

### Financial Separation

- Preserve money separation. Each portfolio or subaccount requires its own settlement account details.
- Enforce distinct settlement details and map them to stable portfolio identifiers; array length and result ordering are not sufficient financial invariants.

## Project Knowledge

### LivelyCura Family

- Ten independent repositories share one product family; preserve their app/service boundaries rather than introducing a root monorepo implicitly.
- API and shared domains: [[../projects/livelycura-backend|LivelyCura Backend]].
- ERP and administration: [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]] and [[../projects/livelycura-admin-portal|LivelyCura Admin Portal]].
- Customer surfaces: [[../projects/livelycura-customer-portal|LivelyCura Customer Portal]] and [[../projects/livelycura-customer-mobile|LivelyCura Customer Mobile]].
- Workforce, delivery, and branded ordering: [[../projects/livelycura-loop-app|LivelyCura Loop App]], [[../projects/livelycura-courier-mobile|LivelyCura Courier Mobile]], and [[../projects/livelycura-check-city-app|LivelyCura CheckCity App]].
- SERLP public and operator mobile surfaces: [[../projects/serlp|SERLP]] and [[../projects/serlp-mobile|SERLP Mobile]].
- MLS AI validation, result delivery, marketplace bidding, and notifications are separate domains. Use MLS agent workflows and existing email templates; do not repurpose marketplace helpers.
- MLS sale integration keeps ordinary selling as transaction owner: one lab-linked `SaleItem` creates one `TestRequest` without bypassing normal stock, COGS, or invoice behavior. Test definitions reference existing Departments, Samples, and product Categories; the portal maps technician-facing configuration into the generated contract and renders it through shared operational infrastructure.
- Stock behavior is item-driven: non-stock/service revenue creates no phantom inventory or COGS; bundle composition belongs to BOMs rather than Product-owned duplicate arrays; displayed BOM purpose derives from current product behavior when stored purpose would drift.
- The approved courier direction is business-agnostic and separates provider quote, customer delivery fee, rider payout, collection, delivery progress, and remittance. Current backend persistence has not yet completed this model; see the backend and courier-mobile contradictions.
- Custom-app ownership is explicit across surfaces: Admin Portal assigns fixed managed apps to organizations, Pharmacy Portal manages banners only for assigned apps, and branded mobile apps consume only their enabled organization/app pair. Reads do not create assignments.
- CheckCity Live Activities are deferred on local feature branches and absent from active code. The preserved app branch’s custom-module snapshot is superseded by the later maintained-package direction and must be reworked before use.
- The courier app is publicly branded `SERLP Dispatch`; its LivelyCura repository name is internal. The backend keeps its existing notification payload while the app maps the nested identifier to canonical `taskId` navigation.

### Bora Capital

- Backend API and financial orchestration: [[../projects/bora-capital-backend|Bora Capital Backend]].
- Expo customer application: [[../projects/bora-capital-mobile-app|Bora Capital Advisors Mobile App]].
- “Go live” or “finish once” means freeze scope and complete one pass; long-term roadmap items are not launch blockers.
- Do not touch withdrawal code unless explicitly asked.
- Follow `.hermes/plans` only within requested scope.
- Preserve architecture, contracts, runtime, canonical IDs, `OTP=email+code`, and the native mobile app's empty CORS whitelist.
- During security remediation, leave migrations and cron jobs in their current placement and do not treat them as remediation targets.
- Resolve incoming Mongo IDs, then use fetched documents' canonical IDs in downstream queries and writes.
- Follow repository-local skills: keep GraphQL resolvers typed and thin, keep one operation per file, and let domain services own validation, authorization, and orchestration.
- Each portfolio has a distinct Paystack subaccount. The backend owns initialization, references, subunit conversion, provider verification, webhook authentication, idempotent finalization, and BCL synchronization; the mobile app must not treat browser return state as payment proof.
- Portfolio setup uses real provider subaccounts and dedicated settlement metadata. Fake/staging identifiers in production-shared code are rejected; provider-setup migrations still require idempotency and partial-failure recovery.
- Preserve unrelated provider and notification implementations unless removal is explicitly authorized. Adding Resend did not authorize deleting Gmail, and adding Paystack did not authorize rewriting the legacy withdrawal/direct-deposit paths.
- Oye is limited to Bora and general finance/investment education. It must not provide personal advice, buy/sell instructions, recommendations, predictions, unrelated answers, or invented facts.
- Transaction statements, wallet lookup/list/create, and auto-top-up transitions are principal/owner scoped before BCL or state changes. Sentry replaces Rollbar with PII disabled and event redaction; DigitalOcean-compatible wallet encryption uses the explicit two-variable scalar contract recorded in the backend page.

### CompFlow

- The user explicitly rejected an inferred root monorepo: the promotional web, admin dashboard, and backend use their named independent folders and per-repository Yarn lifecycles. The client portal was added later as a fourth independent application.
- Public acquisition and live-plan surface: [[../projects/compflow|CompFlow Public Frontend]].
- Internal team surface: [[../projects/compflow-admin|CompFlow Admin]].
- Business payroll/compliance workspace: [[../projects/compflow-client-portal|CompFlow Client Portal]].
- Shared Express/Apollo domain runtime: [[../projects/compflow-backend|CompFlow Backend]].
- Authentication mirrors LivelyCura: Winston logging, AJV validation, OTP login via `login`, `loginWithEmail`, or `loginWithPhoneNumber`, then `completeLoginWithToken`; no password sign-in.
- Onboarding and payment sequence: public `platformPlans` → `startPlatformSignup` OTP → `completePlatformSignupVerification` JWT → authenticated `startPlatformSubscriptionCheckout` → Paystack or Moolre verification/webhook → organization and owner creation pending document review.
- Subscription-plan administration and enterprise/contact-sales onboarding are back-office concerns; self-service checkout rejects contact-sales plans.
- Lists use `getPageConnection` with `limit + 1`; its current `total` is the returned-edge count, not a database total.
- Admin and SuperAdmin bypass organization membership; tenant users remain scoped.
- By-ID operations fetch the entity first and derive tenant scope from persisted ownership rather than trusting redundant client-supplied organization identity.
- Database-managed subscription plans replace provider-named amount environment values. The public site uses Apollo client/provider, a feature-local query hook, and a formatter with explicit static fallback; the current Admin plan manager remains unimplemented.
- Required bootstrap roles belong in the registered migration lifecycle, not ad hoc package seeds unless explicitly requested. CompFlow currently triggers migrations after server readiness without awaiting them and logs failures, so registered does not mean fail-closed.
- The client portal is transitional: employee CRUD is GraphQL-backed, while several dashboard, payroll, subscription, and security paths remain demo/static and its registration flow does not yet match backend onboarding.
- “Spin up” requires the actual dependencies, providers, runtime, tests/smokes, and exact saved-skill file ownership. A minimal rendering or green build that violates the accepted architecture is not completion.
- CompFlow payment and OTP adapters preserve provider separation: Moolre and Paystack remain switchable, email/SMS use at-least-one-channel success, and mocked provider tests are not live execution. Its payroll/RBAC chain leaves four legacy files and a final authorization rerun unresolved.

### Portfolio Family

- Dirty external launcher and provenance boundary: [[../projects/portfolio-workspace|Portfolio Workspace]].
- API and CMS runtime: [[../projects/portfolio-backend|Portfolio Backend]].
- Administrative content surface: [[../projects/portfolio-admin-portal|Portfolio Admin Portal]].
- Public portfolio and case studies: [[../projects/portfolio-client-portal|Portfolio Client Portal]].

- The production applications own independent Git histories, dependencies, lockfiles, and verification. The parent launcher is not currently a coherent committed monorepo snapshot.
- Public project visibility preserves media while redacting intended case-study detail by mode. Home profile, education, skills, counts, projects, resume, and availability should be CMS/API-backed with explicit fallbacks.
- Current client source supersedes the historical collage, Build Console, glowing CTA, constrained global rail, and mounted Threads background. Preserve current light hierarchy, responsive breathing room, and reduced-motion behavior unless explicitly redesigned.
- Featured Projects uses equal responsive Swiper cards with the established full-image/details-on-hover interaction; coverflow, centered enlargement, neighbor dimming, and prominent navigation were rejected. Skills keeps six API-aware groups with visible-default Framer Motion, but anchor-navigation acceptance and dedicated reduced-motion behavior remain open.

### C.E.Q.A/Altin Family

- Mobile partner operations: [[../projects/altin-partner-mobile|Altin Partner Mobile]].
- Workforce administration and reports: [[../projects/keks-admin-portal|Keks Admin Portal]].
- Assisted selling and order operations: [[../projects/call-center-web-app|Call Center Web App]].
- Altin mobile theming follows the repository's `docs/app-theme-guide.md` (palette, light/dark semantic colors, system typography, spacing, radii), with the user's later token tuning taking precedence. The user rejected the [[../sources/altin-mobile-brand-system|Brand Book]] palette and Plus Jakarta Sans / IBM Plex fonts as the app theme; never restore them or the old look. Keep the supplied lockups and app icon masters. Primary icons in icon wells look identical in both appearances, and a visual request changes only the named detail. See [[../sources/altin-theme-navigation-runtime-corrections|the theme correction]].
- SERLP is architecture and configuration only.
- SERLP does not authorize copying Altin branding, typography, spacing, radii, shadows, modules, or product identity.
- Each app module owns its root screen, local drawer, sections, constants, styles, hooks, data, and concrete feature screens.
- `Apps` provides directory metadata and root navigation only; shared components are presentation-only.
- Shared list primitives own reusable mechanics and presentation; concrete feature screens own query/data, filter state and controls, entity types, row rendering, and navigation.
- Do not centralize modules in `AppModuleScreen`, `AppFeatureScreen`, or a module resolver.
- In Keks, Roles and Designations are separate domains. Protect permissions at direct routes, navigation/launchpad discovery, and individual actions; preserve the explicit `super_admin` bypass and use server-backed search for paginated data.
- Keks uses a standalone protected launchpad outside the operational layout. It reuses tenant, permission, profile, and theme context; every visible card must be routable, permission-filtered, keyboard-operable, and correctly named for assistive technology.
- In Keks reporting, employee/user filters omit unsupported `scope`; branch and exceptions filters retain it. Report date controls use native start/end inputs, remain URL-backed, and default/reset to the present day.
- API-key secrets are one-time reveal data. Keep the creation modal open until explicit acknowledgement/close, gate token-exchange capability independently, and never persist or log the secret.
- In call-center checkout, stable payload idempotency and an in-flight guard work together. When a location update can reset form state, commit the reset-producing coordinate change before writing the final human-readable address.
- Call-center branch changes remain available for non-empty carts, reprice every line, and invalidate branch-dependent fulfillment state. Delivery area and exact location are mutually exclusive, while search suggestions and map pins commit address plus coordinates atomically.
- Call-center exact-location pricing dispatches by branch courier type: Altin courier uses an Altin cart estimate; other courier types use ordinary delivery-price calculation. Form-schema validity remains the checkout field gate.
- Call-center threshold discounts use base line total for eligibility and the configured fixed/percentage discount value for deduction; current delivery estimates contribute to the cart total.
- Call-center product selection is preference-first for the exact opened product: non-empty `preferences` suppress `familyConfig` pickers and preserve that product's own price; only products without preferences enter ordered family-dimension selection. Family expansion uses `exactFamily` so normal, `PLUS`, and `ASSORTED` families cannot mix. Required preferences gate cart insertion and selected values travel with the cart line.
- Treat changing catalog content as data, not application logic: never hardcode product IDs, names, family names, prices, preference keys/labels, or option labels in production selection behavior. Derive the complete picker and pricing state from the latest API metadata; use concrete catalog examples only as contract-focused test fixtures.
- Preserve the call-center backend-compatible coordinate mapping until the backend contract is deliberately normalized and tested.

### Standalone Projects

- Provenance-review identifiers retained pending direct Hermes conversations: [[../projects/movieflix-mobile|MovieFlix Mobile]] and [[../projects/go-api|GoAPI]].
- Direct Hermes evidence now establishes [[../projects/lets-ride-backend|Let's Ride Backend]] as a foundation-only Express/Apollo/Mongoose service with separate process/app/transport ownership and deliberate absence of ride-domain logic. Current package/README Cando branding and Mongo-backed runtime remain unresolved.
- Repository-only pages for Magical Goodall, mywork Git History Generator, Playground, and Portfolio Mock-up Prototype were deleted under [[../sources/hermes-conversation-harvest-scope-correction|the scope correction]].

## Implications

- Search this page and linked sources before asking the user to restate development conventions.
- Verify project-specific claims against current code before modifying a repository.
- Split a project into its own page when its section becomes too large or needs independent sources and contradictions.

## Contradictions Or Tensions

The later September 12 mutation-error correction supersedes earlier assistant guidance to forward full Apollo mutation results and rethrow/map errors into forms. It keeps query-result spreading and client validation intact; the SERLP source supports consuming errors in Toast with a null/no-result return.

The 2026-09-12 Formik/Yup correction makes the required form tools explicit; the earlier “or an equivalent schema” wording must not be used to substitute a custom form implementation. See [[../sources/altin-orders-mobile-web-reference|the source]].

- Exact mirroring and established architecture take precedence when they conflict with generic framework conventions.
- Compact answers should still expose the architectural relationship needed to understand the decision.

## Related

- [[personal-operating-manual|Personal Operating Manual]]
- [[new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]]
- [[../concepts/codex-project-knowledge-harvest|Codex Project Knowledge Harvest]]
- [[../concepts/hermes-obsidian-memory-architecture|Hermes–Codex–Obsidian Shared Brain Architecture]]

## Sources

- [[../sources/hermes-persistent-memory-import|Hermes Persistent Memory Import]]
- [[../sources/shared-brain-all-agents-directive|Shared Brain Across Hermes Profiles And Codex]]
- [[../sources/project-knowledge-completion-and-bootstrap-directive|Project Knowledge Completion And Bootstrap Directive]]
- [[../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]]
- [[../sources/livelycura-project-knowledge-harvest-batch-2|LivelyCura Project Knowledge Harvest — Batch 2]]
- [[../sources/livelycura-project-knowledge-harvest-batch-3|LivelyCura Project Knowledge Harvest — Batch 3]]
- [[../sources/livelycura-project-knowledge-harvest-batch-4|LivelyCura Project Knowledge Harvest — Batch 4]]
- [[../sources/livelycura-project-knowledge-harvest-batch-5|LivelyCura Project Knowledge Harvest — Batch 5]]
- [[../sources/compflow-project-knowledge-harvest-batch-1|CompFlow Project Knowledge Harvest — Batch 1]]
- [[../sources/compflow-hermes-project-knowledge-harvest-supplement-1|CompFlow Hermes Project Knowledge Harvest — Supplement 1]]
- [[../sources/kusantec-bora-project-knowledge-harvest-batch-1|Kusantec/Bora Project Knowledge Harvest — Batch 1]]
- [[../sources/bora-realtime-support-subscriptions|Bora Realtime Support Subscriptions]]
- [[../sources/bora-notifications-marketing|Bora Notifications, Campaigns, And Banners]]
- [[../sources/ceqa-altin-project-knowledge-harvest-batch-1|C.E.Q.A/Altin Project Knowledge Harvest — Batch 1]]
- [[../sources/ceqa-altin-project-knowledge-harvest-batch-2|C.E.Q.A/Altin Project Knowledge Harvest — Batch 2]]
- [[../sources/ceqa-altin-project-knowledge-harvest-batch-3|C.E.Q.A/Altin Project Knowledge Harvest — Batch 3]]
- [[../sources/portfolio-project-knowledge-harvest-batch-1|Portfolio Project Knowledge Harvest — Batch 1]]
- [[../sources/hermes-conversation-harvest-scope-correction|Hermes Conversation Harvest Scope Correction]]
- [[../sources/hermes-session-coverage-audit-2026-07-21|Hermes Session Coverage Audit — 2026-07-21]]
- [[../sources/ceqa-altin-hermes-conversation-harvest-supplement-1|C.E.Q.A/Altin Hermes Conversation Harvest — Supplement 1]]
- [[../sources/compflow-checkcity-hermes-conversation-harvest-supplement-1|CompFlow And CheckCity Hermes Conversation Harvest — Supplement 1]]
- [[../sources/kusantec-bora-hermes-conversation-harvest-supplement-1|Kusantec/Bora Hermes Conversation Harvest — Supplement 1]]
- [[../sources/hermes-livelycura-skills-keks-pharmacy-harvest-batch-1|Hermes LivelyCura Skills, Keks, And Pharmacy Harvest — Batch 1]]
- [[../sources/hermes-generalized-skills-courier-recovery-harvest-batch-1|Hermes Generalized Skills And Courier Recovery Harvest — Batch 1]]
- [[../sources/livelycura-stock-sales-hermes-supplement-1|LivelyCura Stock And Sales Hermes Supplement — 1]]
- [[../sources/ceqa-call-center-hermes-supplement-2|C.E.Q.A Call Center Hermes Supplement — 2]]
- [[../sources/livelycura-stock-sales-hermes-supplement-2|LivelyCura Stock And Sales Hermes Supplement — 2]]
- [[../sources/hermes-project-bootstrap-git-continuation-batch-1|Hermes Project Bootstrap And Git Continuation — Batch 1]]
- [[../sources/livelycura-stock-sales-hermes-supplement-3|LivelyCura Stock And Sales Hermes Supplement — 3]]
- [[../sources/hermes-vault-infrastructure-continuation-batch-2|Hermes Vault Infrastructure Continuation — Batch 2]]
- [[../sources/graphql-product-bora-paystack-hermes-chain|GraphQL Product And Bora Paystack Hermes Chain]]
- [[../sources/bora-bcl-error-passthrough-and-secret-files|Bora BCL Error Passthrough And Secret-File Boundary]]

## Open Questions

- How should the approved LivelyCura courier-provider, payout, COD collection, and remittance model map into the current delivery-task architecture?
- Should a future MLS clinical encounter/order aggregate sit above per-test requests, or should the sale remain the grouping boundary?
