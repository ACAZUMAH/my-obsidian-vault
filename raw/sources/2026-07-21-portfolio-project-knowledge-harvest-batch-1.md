# Portfolio Project Knowledge Harvest — Batch 1 Evidence Manifest

Date: 2026-07-21

## Scope

- Family root: `/Users/acazumah/Documents/Portfolio`.
- Repository writes: none.
- Git roots inventoried: exactly 5.
- Codex records processed or explicitly classified: exactly 5.
- Direct historical working-directory rollouts: 4.
- Index-only title match with no surviving rollout: 1.
- Records pending after this batch: 0 for the discovered Portfolio set.
- Hermes history was searched separately. No direct Portfolio implementation session was found; the only hit used Portfolio as a reference while scaffolding another family.
- Full transcripts, system/developer text, tool chatter, environment files, credentials, tokens, private contact values, fixture data, generated GraphQL output, images/base64, logs, dependency trees, and large code excerpts were not copied into the vault.

## Repository Provenance

| Repository | Branch | Revision | State | Role |
| --- | --- | --- | --- | --- |
| `/Users/acazumah/Documents/Portfolio` | `main` | `8621a0286205` | dirty; 55 normal porcelain entries; ahead 1/behind 4 | working-tree launcher/orchestration layer |
| `/Users/acazumah/Documents/Portfolio/backend` | `main` | `c211320705f5` | clean; aligned with `origin/main` | API and CMS backend |
| `/Users/acazumah/Documents/Portfolio/admin-portal` | `main` | `b0a86f9009d7` | clean; aligned with `origin/main` | administrative CMS/dashboard |
| `/Users/acazumah/Documents/Portfolio/clients-portal` | `main` | `d54e1e4466d9` | clean; aligned with `origin/main` | public portfolio application |
| `/Users/acazumah/Documents/Portfolio/mock-ups/porfolio` | `main` | `a8c12d52b492` | clean; aligned with `origin/main` | earlier standalone prototype |

The parent is not one coherent committed multi-app snapshot. Its `HEAD` contains an ordinary tracked client subtree, while the working tree contains independent nested repositories and untracked launcher documentation/configuration. The parent remote points at the independent client lineage, producing unrelated-root divergence. Current application facts are therefore attributed to each clean nested repository, not to the parent snapshot.

No installs, generation, lint, tests, builds, servers, browser sessions, APIs, databases, uploads, deployments, commits, pushes, or Git mutations were run during this harvest.

## Record Provenance

| Record ID | Date | Historical working directory | Indexed title | Classification |
| --- | --- | --- | --- | --- |
| `019e31e1-c083-7f73-bad1-722ad841ccd1` | 2026-05-16 | unknown | Build portfolio platform | missing-rollout/index-only; no project claim promoted |
| `019e31e4-a539-7722-887e-156f664e1a3f` | 2026-05-16 | `/Users/acazumah/Documents/Portfolio` | Build developer portfolio | substantive multi-application build record |
| `019e7bf6-61af-73a0-a344-e7873557e31d` | 2026-05-31 | `/Users/acazumah/Documents/Portfolio` | Add home about section | substantive; current core behavior, evolved implementation |
| `019e7c24-1c66-7a22-87eb-a49f40e3150d` | 2026-05-31 | `/Users/acazumah/Documents/Portfolio/clients-portal` | Refine about section layout | substantive; final record state later superseded |
| `019ea3a7-2e9e-7771-9a30-389e8ad797c7` | 2026-06-07 | `/Users/acazumah/Documents/Portfolio` | Add hero section subtext | substantive; core decisions current, visual experiments partly superseded |

## Sanitized Durable Evidence

### Platform Boundary

- The platform was designed as three applications: GraphQL/MongoDB backend, administrative CMS/dashboard, and public portfolio/case-study portal.
- The later dependency correction superseded the initial root-workspace plan: use Yarn, but keep app-local dependencies and lockfiles; no root Yarn workspace or root `node_modules`.
- The root may delegate commands to children without owning their dependencies.
- Backend domains own model, service, interface, GraphQL, and permission boundaries. Resolvers stay thin.
- Admin and client operations/hooks are feature-local; GraphQL Codegen reads the backend endpoint rather than a checked-in schema snapshot.
- Public project visibility distinguishes public, restricted-summary, and protected content. Current code preserves media while redacting selected case-study details and composes GraphQL Shield permissions centrally.

### Public Portfolio

- Home composition keeps Hero followed by a CMS-driven About introduction, then skill/experience/project/contact sections. A dedicated full About page was intended but is not present in current source.
- References are inspiration, not templates. New panels should inherit the site’s colors, spacing, hierarchy, and surface language.
- Skills, counts, profile facts, education, availability, and other claims should come from real backend/CMS data with explicit fallbacks, not invented metrics.
- Preserve approved regions while iterating on unresolved regions; validate real asset formats before integration.
- Hero breathing room is section-specific. Do not squeeze the whole page with a global percentage rail; verify mobile and ultra-wide layouts separately.
- Motion must be purposeful, preserve CTA interaction, and provide reduced-motion behavior.

## Historical Outcomes And Limits

- The initial build record reported app scaffolding, repeated builds, Codegen, browser checks, GraphQL Shield work, and iterative public-project UI corrections. These are historical reports, not fresh verification.
- The initial record contradicted itself on test coverage: early summaries reported visibility tests, while later Jest runs reported no tests. Current repositories contain no tracked focused tests and their runners allow empty suites.
- The initial record’s admin project-flow claim was later rejected by the user as structurally unfinished; the restructuring was not completed in that record.
- About/Hero records reported multiple successful builds and responsive browser checks. Later iterations reported builds blocked by unrelated TypeScript errors. Each claim applies only to its own iteration.
- Current client source supersedes the historical collage, Build Console, glowing CTA, global width rail, and mounted Threads/WebGL hero background.
- No current build, lint, test, browser, API, or runtime verification was performed during this read-only harvest.

## Current Reconciliation

- Backend currently composes Express, Apollo GraphQL, GraphQL Shield, MongoDB/Mongoose, request DataLoaders, WebSocket subscriptions, Socket.IO, storage/media, auth, content, leads, resumes, availability, and analytics domains.
- Admin currently protects dashboard/CMS routes and composes persisted Redux state, Apollo, Mantine, modals/notifications, and React Router.
- Client currently queries an aggregate portfolio graph, renders responsive CMS-driven Hero/About content, and keeps reduced-motion CSS. Some displayed hero availability/location copy remains hardcoded.
- No tracked CI, deployment/container contract, or substantive test suite was found in the three current production applications.
- The mock-up has a separate 2025 lineage and is treated as a historical prototype, not part of the 2026 production lineage.

## Completion Boundary

- Portfolio batch 1 closes the discovered family set at five classified Codex records: four substantive rollouts and one missing-rollout index shell.
- Five repository-scoped project pages receive current implementation, provenance, constraints, and contradictions.
- The two operating manuals receive only reusable app-boundary, feature-ownership, data-backed-claim, design-system, asset, responsive, and verification rules supported by the records and current source.
- The next pending family is Standalone Projects batch 1: inventory remaining repositories under `/Users/acazumah/Documents` and process at most eight direct historical records after discovery.