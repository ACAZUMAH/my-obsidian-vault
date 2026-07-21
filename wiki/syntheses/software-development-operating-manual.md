---
type: synthesis
status: active
created: 2026-07-20
updated: 2026-07-21
tags: [software-development, operating-manual, project-conventions]
sources:
  - ../sources/hermes-persistent-memory-import.md
  - ../sources/shared-brain-all-agents-directive.md
  - ../sources/project-knowledge-completion-and-bootstrap-directive.md
  - ../sources/livelycura-project-knowledge-harvest-batch-1.md
  - ../sources/livelycura-project-knowledge-harvest-batch-2.md
  - ../sources/livelycura-project-knowledge-harvest-batch-3.md
confidence: medium
---

# Software Development Operating Manual

## Thesis

This page centralizes durable development preferences and project conventions that should be available to Hermes and Codex. Agents must still inspect live repositories before acting: this is an operating map, not a substitute for current code.

## Coverage And Expansion

- The Project Knowledge below is a compact map, not a complete inventory of every repository or historical decision.
- The initial version was promoted mainly from Hermes persistent memory; additional evidence exists in live repositories and Codex transcripts.
- Use [[../concepts/codex-project-knowledge-harvest|Codex Project Knowledge Harvest]] to ingest that evidence in bounded, resumable batches with provenance and secret filtering.
- Detailed repository knowledge should move into dedicated project entity pages. Keep only cross-project rules and navigation here.
- Use [[new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]] for the reusable pre-feature setup sequence across backend, web, and mobile projects.

## Evidence

- The initial working agreements and project map came from promoted Hermes persistent memory and the shared-brain directives.
- The bootstrap baseline is supported by the user's explicit correction, the coder-profile scaffolding workflow and references, and representative LivelyCura, CompFlow, and Altin repository structures inspected on 2026-07-21.
- The first bounded LivelyCura harvest inventoried ten independently versioned repositories and processed eight Codex sessions. Detailed facts and unresolved implementation conflicts live in the linked project pages and [[project-knowledge-harvest-status|Project Knowledge Harvest Status]].
- The second LivelyCura batch processed eight older MLS, ERP, and CheckCity sessions and reconciled their successive corrections against current code. It supports the scoped-change, explicit-lifecycle, existing-catalog reuse, flow-ownership, and reduced-motion rules below.
- The third LivelyCura batch processed eight mobile distribution, custom-app, migration, native-module, and interaction sessions. Repetition across SERLP, Loop, and CheckCity supports the store-artwork rules; current source plus later corrections supports the optional-native-module, system-theme, and deferred-feature rules.
- Codex history and the wider repository inventory remain partially unprocessed evidence. Future bounded harvests must cite their batch manifests and project pages rather than implying complete coverage.

## General Working Agreements

### Communication And Execution

- Be direct, respectful, technically sophisticated, and concise.
- Explain how components fit together and why a change is correct, without turning the response into a generic tutorial.
- Treat saved skills and linked references as execution checklists, including exact file responsibilities and project-specific patterns.
- Reread live files before editing because the user may modify code during review; preserve those changes.

### Change Control

- Handle security remediation one issue at a time.
- Explain and verify each fix before starting the next issue.
- Mirror exact UI and scaffolding references; do not invent structure when a reference exists.
- Stay within requested scope and distinguish launch blockers from long-term roadmap work.
- Make the narrow requested change without deleting or collapsing adjacent architecture. Preserve existing reads, filters, permission rules, loaders, hooks, and extension points unless removal is explicitly in scope.
- Verify UI work in the real running page after static checks when a live surface is available; say which visual paths were not exercised.
- For store-distribution artwork, use real product screenshots and the correct project identity, render exact platform dimensions in RGB without alpha, and avoid invented UI, unrelated logos, or artificial heavy device frames/backing. Keep repeatable rendering inputs distinct from unverified historical output files.
- When deferring a feature, isolate only its files and hunks on a dedicated branch while preserving unrelated active work. A preserved branch is a historical snapshot that must still be checked against later package and architecture decisions.

### TypeScript And Backend Boundaries

- Add JSDoc to every new or exported TypeScript function.
- Map catch blocks to one deliberate `http-errors` outcome; do not rethrow an unchanged error with `throw error`.
- Keep GraphQL resolvers thin: pass input and principal identity to services. User loading, input whitelisting, authorization, and business logic belong in services.
- Separate domain concerns into owned folders, interfaces, models, services, and tests. Do not centralize a feature in one file or import a convenient helper from an unrelated business domain.
- Reuse established domain infrastructure—such as agent workflows, email templates, and generated GraphQL contracts—before creating parallel mechanisms.
- Search for existing catalogs and relationship services before adding a new model. Reuse first-class records and dedicated add/remove operations rather than creating parallel taxonomies or link tables.
- Give materially different domain transitions their own services, mutations, permissions, and tests. Do not overload publish, update, or another nearby action to implement activate, deactivate, archive, or status progression.
- Keep commercial and operational ownership explicit. A new domain side effect should join the established transaction when atomicity is required; it should not duplicate inventory, billing, audit, or accounting responsibility.
- Treat current package scripts and test configuration as authoritative when historical docs name a superseded runner. New tests use the repository's current runner.

### React Native

- Use Expo with React Navigation under `src/navigation`, not Expo Router, when working in the established mobile architecture.
- Mirror existing applications and preserve text contrast plus safe-area, status-bar, and home-indicator backgrounds.
- Prefer restrained motion built on the project's existing animation stack, honor the platform reduce-motion preference, and keep decorative/theme transitions behind readable interactive content.
- Research maintained Expo-compatible packages before building a custom native module. If an optional native module may be absent, load it only on the supported path and fail softly rather than crashing application startup.
- Treat system appearance as native and JavaScript configuration together. Native automatic appearance and relevant Expo system-UI integration require a rebuilt native binary; a JavaScript reload is insufficient.
- Emit variant-specific native file configuration only when the selected variant resolves a valid path.

### Financial Separation

- Preserve money separation. Each portfolio or subaccount requires its own settlement account details.

## Project Knowledge

### LivelyCura Family

- Ten independent repositories share one product family; preserve their app/service boundaries rather than introducing a root monorepo implicitly.
- API and shared domains: [[../entities/projects/livelycura-backend|LivelyCura Backend]].
- ERP and administration: [[../entities/projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]] and [[../entities/projects/livelycura-admin-portal|LivelyCura Admin Portal]].
- Customer surfaces: [[../entities/projects/livelycura-customer-portal|LivelyCura Customer Portal]] and [[../entities/projects/livelycura-customer-mobile|LivelyCura Customer Mobile]].
- Workforce, delivery, and branded ordering: [[../entities/projects/livelycura-loop-app|LivelyCura Loop App]], [[../entities/projects/livelycura-courier-mobile|LivelyCura Courier Mobile]], and [[../entities/projects/livelycura-check-city-app|LivelyCura CheckCity App]].
- SERLP public and operator mobile surfaces: [[../entities/projects/serlp|SERLP]] and [[../entities/projects/serlp-mobile|SERLP Mobile]].
- MLS AI validation, result delivery, marketplace bidding, and notifications are separate domains. Use MLS agent workflows and existing email templates; do not repurpose marketplace helpers.
- MLS sale integration keeps ordinary selling as transaction owner: one lab-linked `SaleItem` creates one `TestRequest` without bypassing normal stock, COGS, or invoice behavior. Test definitions reference existing Departments, Samples, and product Categories; the portal maps technician-facing configuration into the generated contract and renders it through shared operational infrastructure.
- The approved courier direction is business-agnostic and separates provider quote, customer delivery fee, rider payout, collection, delivery progress, and remittance. Current backend persistence has not yet completed this model; see the backend and courier-mobile contradictions.
- Custom-app ownership is explicit across surfaces: Admin Portal assigns fixed managed apps to organizations, Pharmacy Portal manages banners only for assigned apps, and branded mobile apps consume only their enabled organization/app pair. Reads do not create assignments.
- CheckCity Live Activities are deferred on local feature branches and absent from active code. The preserved app branch’s custom-module snapshot is superseded by the later maintained-package direction and must be reworked before use.

### Bora Capital

- “Go live” or “finish once” means freeze scope and complete one pass; long-term roadmap items are not launch blockers.
- Do not touch withdrawal code unless explicitly asked.
- Follow `.hermes/plans` only within requested scope.
- Preserve architecture, contracts, runtime, canonical IDs, `OTP=email+code`, and the native mobile app's empty CORS whitelist.
- During security remediation, leave migrations and cron jobs in their current placement and do not treat them as remediation targets.
- Resolve incoming Mongo IDs, then use fetched documents' canonical IDs in downstream queries and writes.

### LivelyCura Stock And Sales

- `SaleItem` is one customer-facing product line per sale; batch and component relief belongs in `InventoryMovement`.
- `SaleItem.lineCost` is the exact COGS source; `unitCost` is a derived summary.
- Returns use `saleItemId`, restore from original `SALE` movements, and set `SALE_RETURN` movement `sourceItemId` to the `SaleReturnItem` ID.

### CompFlow

- `compflow`: public frontend.
- `compflow-admin`: internal team portal.
- `compflow-client-portal`: business payroll and compliance workspace.
- `compflow-backend`: Express/Apollo API.
- Authentication mirrors LivelyCura: Winston logging, AJV validation, OTP login via `login`, `loginWithEmail`, or `loginWithPhoneNumber`, then `completeLoginWithToken`; no password sign-in.
- Onboarding and payment sequence: public `platformPlans` → `startPlatformSignup` OTP → `completePlatformSignupVerification` JWT → authenticated `startPlatformSubscriptionCheckout` → Paystack verification or webhook → organization and owner creation pending document review.
- Admin manual subscription is back-office only.
- Lists use `getPageConnection` with `limit + 1`; by-ID operations accept only the ID.
- Admin and SuperAdmin bypass organization membership; tenant users remain scoped.

### Altin Mobile

- Preserve `#F40F1B` as primary and `#F9F1EF` as background.
- SERLP is architecture and configuration only.
- Each app module owns its root screen, local drawer, sections, constants, styles, hooks, data, and concrete feature screens.
- `Apps` provides directory metadata and root navigation only; shared components are presentation-only.
- Do not centralize modules in `AppModuleScreen`, `AppFeatureScreen`, or a module resolver.

## Implications

- Search this page and linked sources before asking the user to restate development conventions.
- Verify project-specific claims against current code before modifying a repository.
- Split a project into its own page when its section becomes too large or needs independent sources and contradictions.

## Contradictions Or Tensions

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

## Open Questions

- How should the approved LivelyCura courier-provider, payout, COD collection, and remittance model map into the current delivery-task architecture?
- Should a future MLS clinical encounter/order aggregate sit above per-test requests, or should the sale remain the grouping boundary?
