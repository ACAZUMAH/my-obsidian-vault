# Hermes LivelyCura Skills, Keks, And Pharmacy Harvest — Batch 1

Sanitized read-only evidence report for coder-profile sessions `20260621_010814_92d057` and `20260621_024824_d0e17a` from `/Users/acazumah/.hermes/profiles/coder/state.db`. System prompts, tool chatter, secrets, private identifiers, environment values, and full transcripts are excluded.

## Session `20260621_010814_92d057`

- Source/profile: coder `cli`
- Historical cwd: `/Users/acazumah/Documents`
- Title: Importing Codebase Skills to Profile
- Classification: substantive multi-task record
- Promotion status: promote/current for skill-import workflow and Keks fix; continuation-required for the final Pharmacy Portal request

### Durable evidence

- The user explicitly requires agents to read project-local skills before serious work because those files define how the codebases are written, structured, maintained, and kept clean.
- The backend source was requested from an exact commit and `.agent/skills`; the frontend source was `.agents/skills` in the Pharmacy Portal.
- Historical outcome reported: 16 backend and 26 frontend skills imported into the coder profile, project grouping preserved, private-GitHub 404 handled via local clones, backend extracted from the exact commit, one missing `name` repaired, frontend `reference/` folders normalized to `references/`, and Hermes skill-list/view checks performed.
- The same session contains the original completed Keks report-log fix: Chakra v3 `Select.Root` requires a `createListCollection(...)` object, and the shared selector detail event must be adapted to the first selected value. Historical verification reported a passing production build and unrelated pre-existing lint failures.
- The final user request moved Pharmacy Portal test-request-detail interfaces into a dedicated interfaces folder; the actual work continued in the next session.

## Session `20260621_024824_d0e17a`

- Source/profile: coder `cli`
- Historical cwd: `/Users/acazumah/Documents`
- Title: Move Interfaces to Dedicated Folder
- Classification: substantive, completed after direct user correction and recovery from a bad bulk edit
- Promotion status: promote/current with historical verification caveat

### Durable corrections and outcome

- The first completion claim was false: the user reread the files and reported that interfaces were still declared inside components.
- The assistant attributed the miss to cached/unchanged read responses, then reported bypassing that condition and rereading a representative file.
- A later regex-based bulk change corrupted component content. The assistant reported manually restoring logic, moving prop interfaces into `src/mls/testRequestDetails/interfaces/index.ts`, applying explicit `React.FC<InterfaceName>` component declarations, and removing local interface declarations.
- Historical verification was limited to spot-reading a representative component; no session-attributed full project checks were reported.

## Current Static Reconciliation

- Current Pharmacy Portal source contains ten matching test-request-detail components that import prop interfaces from `../interfaces` and declare components with `React.FC<...>`.
- The current `project-skill-library-import` workflow preserves the exact-commit, private-repo fallback, grouping, supporting-file normalization, minimal frontmatter repair, and Hermes API verification lessons.
- No current build, test, lint, service, database, provider, migration, or deployment command was run during this harvest.

## Completion

- Exact IDs processed: 2 of 2
- Classifications: two substantive
- Repositories or profile skills modified during this harvest: none
