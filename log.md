# LLM Wiki Log

Append-only chronological record of wiki operations. New entries go directly under this note.

## [2026-07-21] maintenance | Prepare Public Git Versioning

What changed:

- Initialized the vault as an independent Git repository on `main`.
- Configured `https://github.com/ACAZUMAH/my-obsidian-vault.git` as `origin`; the GitHub repository was confirmed public and empty before the first commit.
- Added `welcome.md` as the human-facing entry point with architecture, agent workflow, and public-repository safety guidance.
- Added a security-conscious `.gitignore` covering Obsidian-local state, plugin payloads, OS/editor files, credentials, certificates, signing material, databases, archives, dependencies, build output, caches, logs, and agent-local state.
- Linked the welcome page from `index.md`.

Files touched:

- `.gitignore`
- `welcome.md`
- `index.md`
- `log.md`

Verification:

- Reviewed the exact staged commit set: 56 text files and no ignored Obsidian workspace/plugin payloads.
- Scanned every staged file for common private-key, access-token, JWT, secret-assignment, and credential-bearing database URI formats; no matches were found.
- Searched Markdown for email-address and Ghanaian phone-number patterns; no matches were found.
- Confirmed the only miscellaneous raw asset contains public UI inspiration site names, not private data.

Key result:

- The canonical second brain is prepared for public Git versioning with explicit safety boundaries and reproducible navigation.

Follow-ups:

- Keep reviewing every staged diff because `.gitignore` cannot detect secrets already written into ordinary Markdown.
- Treat the public GitHub remote as a publishing boundary, not as a private backup destination.

## [2026-07-21] ingest | Harvest LivelyCura Project Knowledge Batch 3

What changed:

- Processed exactly the eight distribution-artwork, MLS cleanup, custom-app, Live Activity, native-update, cart/tab, and theme sessions fixed by the batch-2 checkpoint; no project repository files or Git state were modified.
- Created one sanitized provenance manifest and one source summary. Private allow-list identifiers were replaced by `[two allow-listed organizations]`, and historical binaries/transcripts were not copied.
- Reconciled history against six current repositories and updated their project pages: Backend, Admin Portal, Pharmacy Portal, CheckCity, Loop, and SERLP Mobile.
- Preserved three material implementation gaps: the catalog-cleanup migration is currently unregistered, historical store-artwork outputs are absent, and Live Activities exist only on deferred branches whose app snapshot still uses the superseded custom-module approach.
- Promoted only supported reusable rules into the two operating manuals: real screenshot/platform-correct store artwork, maintained-package research, resilient optional native modules, automatic system appearance plus native rebuild, conditional native file config, and isolated deferred-feature branches.
- Advanced the canonical checkpoint from 16 to 24 processed LivelyCura sessions, leaving 13 pending and fixing the exact eight-session batch-4 boundary.

Files touched:

- `raw/sources/2026-07-21-livelycura-project-knowledge-harvest-batch-3.md`
- `wiki/sources/livelycura-project-knowledge-harvest-batch-3.md`
- `wiki/entities/projects/livelycura-backend.md`
- `wiki/entities/projects/livelycura-admin-portal.md`
- `wiki/entities/projects/livelycura-pharmacy-portal.md`
- `wiki/entities/projects/livelycura-check-city-app.md`
- `wiki/entities/projects/livelycura-loop-app.md`
- `wiki/entities/projects/serlp-mobile.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- The canonical brain now separates custom-app assignment, ERP banner management, and mobile consumption; records Live Activities as deferred rather than current; and keeps store-artwork conventions without claiming missing artifacts still exist.

Coverage boundary:

- Thirty-seven sessions use a LivelyCura working directory. Twenty-four are processed and thirteen remain. Batch 4 contains the next eight indexed sessions; the final five then require relevance/unique-evidence triage.

Verification:

- Touched wiki frontmatter parsed successfully; all real wikilinks, local Markdown links, and frontmatter source paths resolve; all six project pages retain their required sections; the eight manifest IDs match checkpoint batch 3; and checkpoint arithmetic is `24 + 13 = 37` with no overlap in the eight-session batch 4.
- Secret-pattern scanning found no secret-like values in the new manifest/source. The backend, Pharmacy Portal, CheckCity, Loop, and SERLP Mobile repositories remained clean. Admin Portal retained only its pre-existing modified generated GraphQL files, which this harvest excluded and did not touch.
- Repository test suites and historical artwork binaries were not exercised because the harvest is read-only. Session-reported outcomes are labeled historical, and current claims come from source inspection.

Follow-ups:

- Process LivelyCura batch 4 exactly as recorded in `wiki/syntheses/project-knowledge-harvest-status.md`.
- Keep the stale migration, deferred Live Activity package replacement, and missing artwork ownership questions open until a scoped implementation or maintenance task resolves them.

## [2026-07-21] ingest | Harvest LivelyCura Project Knowledge Batch 2

What changed:

- Processed exactly the eight MLS, ERP, and CheckCity sessions fixed by the batch-1 checkpoint; no project repository files or Git state were modified.
- Created a sanitized provenance manifest and source summary, then reconciled historical plans and corrections against current backend, pharmacy portal, and CheckCity source.
- Updated the three affected project pages with sale-to-request transaction behavior, TestDefinition/catalog/lifecycle boundaries, technician-facing builder/renderer ownership, standalone POS architecture, Samples/Departments behavior, and reduced-motion-aware theme transitions.
- Promoted reusable scoped-change, lifecycle-operation, existing-catalog, transaction-owner, flow-ownership, mapper-boundary, live-UI-verification, and motion rules into the two operating manuals.
- Advanced the canonical checkpoint from 8 to 16 processed LivelyCura sessions and fixed the exact eight-session batch-3 boundary.

Files touched:

- `raw/sources/2026-07-21-livelycura-project-knowledge-harvest-batch-2.md`
- `wiki/sources/livelycura-project-knowledge-harvest-batch-2.md`
- `wiki/entities/projects/livelycura-backend.md`
- `wiki/entities/projects/livelycura-pharmacy-portal.md`
- `wiki/entities/projects/livelycura-check-city-app.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `index.md`
- `log.md`

Key result:

- The canonical brain now records current MLS behavior as one `TestRequest` per lab-linked `SaleItem` inside the ordinary sale transaction, explicitly superseding the older parent-request/many-tests PDF proposal. It also separates durable technician-facing and lifecycle conventions from the builder/action layouts that changed during review.

Coverage boundary:

- Thirty-seven sessions use a LivelyCura working directory. Sixteen are now processed; twenty-one remain pending, including the exact eight-session batch 3 recorded in the checkpoint.

Verification:

- Touched wiki frontmatter parsed successfully; real wikilinks and the source-summary raw link resolve; checkpoint totals and the exact eight-session next batch were validated; the raw manifest contains no detected secret-like assignments.
- The three inspected project repositories remained clean. Repository test suites were not rerun because this harvest was read-only; historical test/build/browser outcomes are labeled as transcript evidence.

Follow-ups:

- Process LivelyCura batch 3 exactly as recorded in `wiki/syntheses/project-knowledge-harvest-status.md` before continuing to later families.
- Preserve the clinical-request grouping question, historical builder-layout churn, and codegen/runtime verification gaps until future evidence resolves them.

## [2026-07-21] ingest | Harvest LivelyCura Project Knowledge Batch 1

What changed:

- Inventoried ten independently versioned LivelyCura/SERLP repositories without modifying repository code or Git state.
- Processed eight bounded Codex sessions and preserved only sanitized provenance, durable corrections, decisions, verification history, and short supporting statements.
- Created one project page per repository, a raw evidence manifest, a source summary, and the canonical resumable harvest checkpoint.
- Promoted cross-project domain-ownership and infrastructure-reuse rules into the software-development operating manual.
- Left the new-project bootstrap manual unchanged because this batch reinforced existing repository-boundary and Yarn/TypeScript guidance without proving a new universal default.

Files touched:

- `raw/sources/2026-07-21-livelycura-project-knowledge-harvest-batch-1.md`
- `wiki/sources/livelycura-project-knowledge-harvest-batch-1.md`
- `wiki/syntheses/project-knowledge-harvest-status.md`
- `wiki/syntheses/software-development-operating-manual.md`
- Ten pages under `wiki/entities/projects/` for the LivelyCura/SERLP repositories.
- `index.md`
- `log.md`

Key result:

- The canonical brain now distinguishes live LivelyCura implementation from historical intent. MLS workflow boundaries and public result delivery are verified; the broader courier-provider, payout, collection, and remittance model is preserved as desired architecture that current persistence has not yet completed.

Coverage boundary:

- Thirty-seven sessions use a LivelyCura working directory. This batch processed eight; twenty-nine remain unprocessed or pending relevance triage.

Follow-ups:

- Process the exact eight-session LivelyCura batch 2 recorded in `wiki/syntheses/project-knowledge-harvest-status.md` before moving to CompFlow.
- Preserve the Customer Portal lockfile conflict and stale README claims until an explicit maintenance task resolves them.

## [2026-07-21] synthesis | Add Codex Knowledge Harvest And New Project Bootstrap Manual

What changed:

- Recorded the user's correction that Project Knowledge is incomplete because relevant evidence also exists in Codex conversations and live repositories.
- Located 67 indexed Codex threads, 77 Codex transcript/index JSONL files, and 39 project manifests as the recoverable evidence surface at inspection time.
- Added a paste-ready Codex procedure that processes one project family or at most eight sessions per batch, maintains a checkpoint, redacts secrets, distinguishes current code from historical intent, and writes project-specific entity pages.
- Added an evidence-backed new-project bootstrap manual covering backend, web/admin, and Expo mobile foundations before feature logic.
- Marked the software-development operating manual as a compact, currently incomplete project map and linked its expansion path.

Files touched:

- `raw/sources/2026-07-21-project-knowledge-completion-and-bootstrap-directive.md`
- `wiki/sources/project-knowledge-completion-and-bootstrap-directive.md`
- `wiki/concepts/codex-project-knowledge-harvest.md`
- `wiki/syntheses/new-project-bootstrap-operating-manual.md`
- `wiki/syntheses/software-development-operating-manual.md`
- `index.md`
- `log.md`

Key result:

- Codex now has a safe, resumable prompt for completing project knowledge from its own archive, while all agents have a detailed shared definition of what constitutes a complete project foundation before screens, pages, or domain logic.

Coverage boundary:

- This operation discovered and mapped the evidence sources but did not claim to have ingested every Codex transcript. Full project completion remains a staged follow-up recorded by the harvest checkpoint.

Follow-ups:

- Run the master prompt in Codex from `/Users/acazumah/Documents` and process the first project-family batch.
- Resolve the open defaults for canonical reference backend, web folder variant, test runner, CI, deployment, and observability as the harvest supplies stronger cross-project evidence.

## [2026-07-20] setup | Unify Shared Brain Across All Hermes Profiles And Codex

What changed:

- Configured `OBSIDIAN_VAULT_PATH=/Users/acazumah/Documents/Work Space` for the `default`, `coder`, `devops`, `personal`, and `researcher` Hermes profiles.
- Added compact shared-brain pointers and communication preferences to every profile's `USER.md` and `MEMORY.md`, with role-specific retrieval and contribution hints.
- Preserved the former default and coder profile memories as raw evidence, then promoted their durable development knowledge into a shared software development operating manual.
- Created Codex global instructions at `~/.codex/AGENTS.md` and exposed the vault path through `~/.codex/config.toml`.
- Expanded the architecture from a single-profile Hermes–Obsidian link into a Hermes–Codex–Obsidian canonical knowledge plane with concurrent-write controls.
- Recorded that the user prefers direct, concise, technically sophisticated explanations that show architecture, relationships, and rationale.

Files touched:

- `AGENTS.md`
- `index.md`
- `log.md`
- `raw/sources/2026-07-20-shared-brain-all-agents-directive.md`
- `raw/sources/2026-07-20-hermes-persistent-memory-import.md`
- `wiki/sources/shared-brain-all-agents-directive.md`
- `wiki/sources/hermes-persistent-memory-import.md`
- `wiki/concepts/hermes-obsidian-memory-architecture.md`
- `wiki/entities/hermes-agent.md`
- `wiki/entities/codex.md`
- `wiki/entities/obsidian.md`
- `wiki/syntheses/personal-operating-manual.md`
- `wiki/syntheses/software-development-operating-manual.md`
- All five Hermes profiles' `.env`, `memories/USER.md`, and `memories/MEMORY.md` files.
- `~/.codex/AGENTS.md`
- `~/.codex/config.toml`

Key result:

- Hermes profiles and Codex now use one canonical Obsidian brain while retaining tool and role specialization through compact local context layers.

Verification:

- All five Hermes profile environment paths, memory files, character limits, and canonical-vault pointers passed validation.
- Codex global instructions and TOML environment configuration passed validation.
- Required vault artifacts exist and all real wikilinks in the touched shared-brain notes resolve.
- An ephemeral, read-only Codex run loaded the global instructions and correctly reported the canonical vault, both operating-manual paths, and the user's preferred communication style.

Follow-ups:

- Split project sections into dedicated linked pages as their sources and conventions grow.
- Introduce a coordinated write queue only if simultaneous vault-edit conflicts become frequent.

## [2026-07-20] setup | Connect Hermes To The Obsidian Second Brain

What changed:

- Configured the active `coder` Hermes profile with `OBSIDIAN_VAULT_PATH=/Users/acazumah/Documents/Work Space`.
- Ingested the user's directive to use Obsidian as Hermes's linked, durable second brain.
- Added a layered memory architecture that separates Hermes memory, Obsidian knowledge, executable skills, and temporary session history.
- Created a personal operating manual and seeded it with durable working preferences already known to Hermes.
- Updated the vault schema with selective workflow-capture, retrieval, linking, privacy, and anti-noise rules.

Files touched:

- `AGENTS.md`
- `index.md`
- `log.md`
- `raw/sources/2026-07-20-hermes-obsidian-second-brain-kickoff.md`
- `wiki/sources/hermes-obsidian-second-brain-kickoff.md`
- `wiki/concepts/hermes-obsidian-memory-architecture.md`
- `wiki/entities/hermes-agent.md`
- `wiki/entities/obsidian.md`
- `wiki/syntheses/personal-operating-manual.md`
- `wiki/syntheses/llm-wiki-operating-model.md`

Key result:

- Future Hermes sessions can discover this vault from compact persistent memory, consult linked operating knowledge before asking the user to repeat it, and keep the second brain updated with durable ways of working.

Follow-ups:

- Add focused project or workflow pages as recurring patterns emerge.
- Promote mature repeatable procedures into Hermes skills when exact operational steps become valuable.

## [2026-05-13] setup | Initialize LLM Wiki Second Brain

What changed:

- Created the root operating schema in `AGENTS.md`.
- Created the content index in `index.md`.
- Created this chronological log in `log.md`.
- Created folder conventions for raw sources, assets, wiki pages, templates, and tools.
- Treated the user's pasted LLM Wiki idea file as the first source and created starter wiki pages from it.

Files touched:

- `AGENTS.md`
- `index.md`
- `log.md`
- `raw/sources/2026-05-13-llm-wiki-idea.md`
- `wiki/sources/llm-wiki-idea.md`
- `wiki/concepts/persistent-compounding-wiki.md`
- `wiki/concepts/raw-source-wiki-schema-architecture.md`
- `wiki/concepts/ingest-query-lint-workflows.md`
- `wiki/entities/obsidian.md`
- `wiki/syntheses/llm-wiki-operating-model.md`
- `wiki/templates/source-summary-template.md`
- `wiki/templates/concept-template.md`
- `wiki/templates/entity-template.md`
- `wiki/templates/question-template.md`
- `wiki/templates/synthesis-template.md`
- `wiki/questions/first-ingest-example.md`

Key result:

- The vault now has a working LLM Wiki scaffold and one fully ingested seed source.

Follow-ups:

- Add the next raw source to `raw/sources/` and ask the agent to ingest it.
- Decide whether to add optional search tooling once the wiki grows beyond what `index.md` and `rg` can comfortably cover.
