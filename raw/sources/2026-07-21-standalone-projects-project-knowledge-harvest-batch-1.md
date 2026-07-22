# Standalone Projects Project Knowledge Harvest — Batch 1

## Scope

This sanitized manifest records the final checkpointed project-family batch under `/Users/acazumah/Documents`: Git roots not already represented by the completed LivelyCura, CompFlow, Kusantec/Bora, C.E.Q.A/Altin, or Portfolio batches.

The inventory was read-only. It did not run package installation, project scripts, tests, builds, services, databases, migrations, deployments, or repository mutations.

## Discovery Boundary

- Git roots inventoried in this batch: 6.
- Direct Codex rollout matches: 0.
- Index-only records whose titles directly identify these repositories: 0.
- Codex rollout metadata checked: 77 active/archived records.
- Codex index shells checked: 68.
- Transcript bodies processed: 0, because no direct record was discovered.
- Repository-local `AGENTS.md`, `CLAUDE.md`, `.agent/`, or `.agents/` instructions found: 0.

Two rollouts used the broad parent working directory `/Users/acazumah/Documents` and were excluded from direct project evidence:

- `019f8217-b070-70e1-a77f-dea8125e9413` — indexed as the project-knowledge harvest itself; process control.
- `019f8252-f2d0-70d2-868a-154be491cd4b` — unindexed broad-working-directory record; target cannot be assigned safely, so it remains excluded rather than guessed.

## Repository Provenance

| Project | Repository root | Branch / revision at inspection | Initial state | Safe remote | Current role |
| --- | --- | --- | --- | --- | --- |
| MovieFlix Mobile | `/Users/acazumah/Documents/movieApp` | `main` at `cf26207fe998c265e2740a38802ad66e9ad68393` | Dirty: `app.json`, `package.json`, and `yarn.lock` modified before harvest | `https://github.com/ACAZUMAH/movieApp.git` | Expo movie discovery client |
| mywork Git History Generator | `/Users/acazumah/Documents/mywork` | `main` at `01b38bcfa82fb1732410a6a86fdf4cee37a45d23` | Clean | `https://github.com/ACAZUMAH/mywork.git` | Side-effectful backdated-commit generator |
| Playground | `/Users/acazumah/Documents/Playground` | unborn `master`; no `HEAD` | Empty, no commits | none | Unspecified placeholder repository |
| Magical Goodall | `/Users/acazumah/Documents/antigravity/magical-goodall` | `master` at `9733dd0366b5c2ff03f8a82444402d71aa33e4fd` | Clean; one empty initial commit | none | Unspecified placeholder repository |
| GoAPI | `/Users/acazumah/Documents/Go/GoAPI` | `main` at `e5c3dfeca4fb346b8f085c087c0ce4bf1820b699` | Clean | `https://github.com/ACAZUMAH/GoAPI.git` | Small authenticated coin-balance HTTP API |
| Cando Backend | `/Users/acazumah/Documents/Kusantec/letsride-backend` | `main` at `c8299891281491843c8544edf889d9952c74e12d` | Clean | `https://github.com/Kusantec/Letsride-backend.git` | Foundation for a ride-ordering backend |

## Current-Source Evidence

### MovieFlix Mobile

- Expo 54, React Native, TypeScript, React Navigation, NativeWind, a remote movie-catalog boundary, and Appwrite-backed search-popularity tracking.
- `App.tsx` owns entry; `src/navigation/` owns stack/tab composition; `src/home/`, `src/search/`, and `src/movie/` own current user flows; Save and Profile remain placeholders.
- Current scripts expose Expo start, native Android/iOS runs, web start, lint, and a reset command whose referenced script is absent.
- The scaffold README is stale: it describes Expo Router, an `app/` directory, and npm, while current code uses `App.tsx`, React Navigation, and a Yarn lockfile.
- The three modified configuration/dependency files predate this harvest, so the inspected working tree is not reproduced by its current `HEAD`.
- No tracked first-party tests, CI workflow, EAS file, or native Android/iOS project was found.

### mywork Git History Generator

- Node.js ECMAScript-module scripts use `simple-git`, `jsonfile`, `moment`, and random-number generation.
- The package `start` command rewrites an opaque tracked JSON payload, creates dated commits, and pushes the configured remote. Alternate unexposed scripts generate hourly commits across configured date ranges.
- The data payload was not read or copied.
- Current history contains 6,066 commits; recent subjects and script behavior corroborate synthetic timestamp generation.
- Of 716 tracked files, 709 are under `node_modules/`; no `.gitignore` is tracked.
- No dry-run mode, confirmation prompt, remote validation, first-party tests, CI, or deployment configuration was found.

### Playground

- Unborn `master` repository with no `HEAD`, tracked files, remote, documentation, manifest, source, command, or runtime evidence.
- Purpose is unknown and was not inferred from the generic folder name.

### Magical Goodall

- Clean `master` repository with one empty initial commit, no tracked files, and no remote.
- Purpose is unknown and was not inferred from the generated-looking folder name.

### GoAPI

- Go module using Chi, Gorilla Schema, and Logrus.
- `cmd/api/main.go` is the composition root; `internal/handlers/` owns route/handler behavior; `api/` owns response/error shapes; an internal database abstraction currently resolves to mock/in-memory behavior.
- The current API binds locally and exposes an authorization-protected account-balance route.
- Current response structs omit explicit JSON tags, missing records map to an internal failure, handlers construct data access directly, and the database factory returns a pointer to an interface.
- No README, documented command, first-party test, CI, task runner, container, or deployment manifest was found. Tracked `.DS_Store` files are repository-hygiene debt.
- Authorization and fixture values were excluded from inspection and promotion.

### Cando Backend

- Yarn/TypeScript foundation using Express 5, Apollo GraphQL, GraphQL WebSocket subscriptions, Mongoose, Winston, Helmet, CORS, Morgan, and centralized error handling.
- `src/main.ts` owns environment-first process startup; `src/app.ts` composes Express/HTTP, database connection, GraphQL, subscriptions, 404/error handling, listening, and signals; `src/servers/` owns transport details.
- Current GraphQL schema intentionally exposes only a health query. No ride, rider, driver, trip, booking, payment, wallet, notification, or administration domain is implemented yet.
- Startup blocks on database connection; HTTP GraphQL and subscriptions share one server.
- Current risks include unresolved product naming (`letsride`, `Cando`, and `ride-ordering-api`), empty non-development CORS allowlists, possible unknown-error detail exposure, incomplete graceful resource draining, and no GraphQL authentication/context layer.
- No first-party tests, CI, container, or deployment manifest was found. Exact runtime configuration and connection details were excluded.

## Historical Record Classification

No direct historical Codex record was discovered for any of the six repository roots. Therefore:

- No transcript-derived preference, decision, rationale, correction, or verification result was promoted.
- All project claims in this batch are current-source or Git-metadata claims.
- Broad parent-directory records were not attributed to a project without direct working-directory or title evidence.

## Promotion Decisions

- Create one first-class project page for each Git root, including the two empty repositories.
- Add the six-page standalone map and current coverage boundary to the Software Development Operating Manual.
- Promote one reusable execution-safety rule to both manuals: inspect package scripts before execution because script names such as `start` do not imply safety.
- Leave project-specific architecture, bugs, naming drift, and repository-hygiene issues in project pages rather than universalizing them.
- Do not claim runtime readiness: no project command was run.

## Sensitive And Noisy Material Excluded

- Environment values, connection details, authorization values, credentials, tokens, fixture identities, and opaque data payloads.
- Log files, dependency contents, lockfile contents, binaries, `.DS_Store` contents, generated/build output, and image/media content.
- Raw transcript bodies, tool chatter, broad-working-directory process sessions, and inference from folder names alone.

## Open Questions

- Are Playground and Magical Goodall intentional placeholders, abandoned experiments, or missing worktrees/remotes?
- Should MovieFlix’s dirty Expo upgrade/configuration be completed and verified or discarded?
- Is `mywork` intentionally retained as a history generator, and should its destructive behavior be guarded before any future execution?
- Should GoAPI’s authorization, response contract, data-access ownership, and test baseline be modernized?
- Which public/product name is canonical for the `letsride-backend` foundation: Cando, Let’s Ride, or `ride-ordering-api`?
