# Kusantec/Bora Project Knowledge Harvest — Batch 1 Evidence Manifest

Date: 2026-07-21

## Scope

- Family: Kusantec/Bora Capital.
- Working-directory boundary: `/Users/acazumah/Documents/Kusantec` plus historical Bora paths under `/Users/acazumah/Documents/Bora Capital`.
- Repository writes: none.
- Bora repositories inventoried: exactly 2.
- Historical Codex sessions processed: exactly 6.
- Purpose: current-repository inventory and reconciliation of the complete directly matched Bora session set found within the eight-session cap.
- Secret handling: environment files, credentials, tokens, private keys, certificates, connection strings, provider values, private identifiers, generated GraphQL output, dependencies, build output, caches, binaries, and ordinary tool chatter were excluded. Provider/environment variable names are retained only where needed to explain configuration boundaries; no values are preserved.
- Historical Fidelity PDFs, Word forms, Postman collections, and generated deliverables were not copied into this manifest. Only the minimal sanitized conclusions already present in the Codex sessions were retained.

## Family Boundary

- Included: `bora-capital-backend` and `bora-frontend-mobile-app`.
- Excluded: `letsride-backend`, despite sharing the Kusantec parent folder. Its current README/package identify it as the separate Cando ride-ordering foundation rather than a Bora Capital application.
- Broad transcript path/term search also matched the current harvest, two LivelyCura tasks carrying global Bora context, and three portfolio/CV/job-application tasks. These are not additional Bora project sessions and were excluded.

## Repository Provenance

| Repository | Branch | Base commit | Live working-tree state | Package boundary |
| --- | --- | --- | --- | --- |
| `/Users/acazumah/Documents/Kusantec/bora-capital-backend` | `feature/updates` | `49fe85765b8c` | Dirty before harvest: 30 modified, 4 deleted, 2 untracked paths | Yarn 1.22.22; Node `>=22.13.0` |
| `/Users/acazumah/Documents/Kusantec/bora-frontend-mobile-app` | `develop` | `393bac0ef0dc` | Dirty before harvest: `package-lock.json` modified | npm 10.9.4; Expo/Node workflow uses Node 22 |

The dirty files belong to pre-existing user/concurrent work. They were read only where necessary to establish live behavior, never edited, staged, discarded, or claimed as harvest changes. The base commits identify ancestry, not the complete current state.

No repository-root `AGENTS.md` or `CLAUDE.md` was found. The backend has a current `.agent/skills` catalog for BCL integration, review, CRUD, DataLoaders, GraphQL, Mongoose, and services. The mobile repository has `.agents/skills` focused mainly on interface/design workflows.

## Processed Codex Sessions

| Date | Session ID | Working directory | Indexed title | Durable classification |
| --- | --- | --- | --- | --- |
| 2026-04-18 | `019da0bb-4110-7762-8e1e-c4f5b45beb2d` | Historical Bora backend path | Prepare Fidelity requirements | Fidelity onboarding responsibility and deposit-integration planning |
| 2026-05-02 | `019de86b-a2dc-7d82-a7e1-cb6674223fa2` | Historical Bora backend path | Add Expo push notifications | Push-token ownership, lifecycle triggers, repository-skill correction |
| 2026-05-10 | `019e132f-949f-7700-ad4c-7b9b9a7aeb36` | Historical Bora backend path | Complete Fidelity questionnaire | Conservative security/compliance posture for provider onboarding |
| 2026-05-25 | `019e6018-67c1-7510-a071-10dbed320d41` | Current Kusantec backend path | Use Resend for notifications | Email-provider transition, preserve-old-code correction, Oye/Ollama constraints |
| 2026-06-09 | `019eae1b-c9a4-7b90-ad0a-444b35dad761` | Current Kusantec backend path | Fix KYC test types | Test fixture must track the live KYC contract |
| 2026-06-12 | `019ebc8d-33dc-7e10-9599-fefd138e793d` | Current Kusantec backend path | Integrate Paystack payments | Portfolio-separated deposits, service boundaries, idempotency, BCL sync, transaction shape |

## Minimal Sanitized Session Evidence

### Fidelity onboarding and questionnaire sessions

- Bora management/company owns provider onboarding: complete forms, provide corporate/compliance evidence, sign agreements, obtain approval, and receive credentials.
- The developer owns API integration, backend-only secret handling, deposit flow, and UAT after credentials are issued.
- Deposit requirements should remain conservative until sandbox access: do not claim certifications without evidence; confirm volumes/timelines after testing; cover authentication, verification, pending/failure, duplicate/reference, callback, retry, and reconciliation scenarios.
- Historical document review identified a Fidelity wallet-debit collection path but did not establish a customer bank-account direct-debit endpoint. That capability remained a question for Fidelity.
- Current reconciliation: Fidelity/Orange source documents remain in the repository, but the payment integration folder is empty and no current source implements Fidelity. The historical work remains onboarding/planning evidence, not live behavior.

### Expo push notifications

- The backend should store Expo push tokens by user/application/OS and expose authenticated add/remove mutations.
- User-requested lifecycle notifications were signup completion, signin completion, KYC completion, withdrawal request, and pending/completed deposit activity.
- The user explicitly corrected the implementation to follow repository-local skills and a LivelyCura reference: resolvers stay thin; services own notification orchestration; one operation lives per service file; touched exported functions use the local JSDoc style.
- Historical verification reported a passing build and 12 focused transaction tests. Current code still implements the token mutations and all requested trigger families; the mobile app registers/rotates tokens, stores local notification history, and deep-links by notification type.

### Resend, Gmail preservation, and Oye

- Resend became the default email provider, but the user explicitly rejected deleting the previous Gmail implementation. Provider transition does not authorize removing adjacent legacy capability.
- Comment/JSDoc style must be copied from the referenced repository folder rather than invented.
- Oye is Bora Capital's educational finance assistant. It may answer general Bora/finance/investment-education questions but must refuse personal advice, buy/sell instructions, predictions, advisor behavior, unrelated topics, and unverifiable Bora/account facts.
- The user chose the installed Ollama library, placed the feature in `src/services/agent`, moved the system instruction into source, preserved the GraphQL mutation shape, and later explicitly restored module-level client setup while changing tests to accommodate it.
- Historical verification reported build plus 62-test full-suite success after that restoration. Current source retains the Oye restrictions and module-level Ollama setup, but its string interpolation makes the documented default-model fallback ineffective when the environment value is absent.

### KYC test correction

- Tests must be updated when the production KYC input contract adds required identity-image strings; weakening the live interface to satisfy a stale fixture was not the chosen fix.
- Historical focused verification reported three passing KYC tests.

### Paystack deposit integration

- Each portfolio has separate money ownership and requires an active Paystack subaccount mapping. A deposit cannot proceed without that mapping.
- The backend owns initialization, amount conversion to subunits, reference generation, provider verification, webhook signature validation, final status, and BCL posting. Frontend-reported success is never trusted.
- Preserve the existing direct deposit and withdrawal operations while introducing the Paystack flow; do not rewrite unrelated BCL transaction paths.
- Provider calls belong in `src/services/payments/paystack` as plain exported functions. Transaction orchestration belongs in `src/services/transactions/payment`; portfolio configuration, wallets, helpers, interfaces, and models remain separately owned.
- Use one generic transaction record with provider data nested under `payment.paystack`; keep business amount and Paystack subunit amount separately. Verification compares Paystack's subunit amount to `amountInSubunit`.
- Current code uses a unique reference, raw-body HMAC verification, provider-side verification, atomic processing claims, durable webhook inbox state, BCL synchronization, reconciliation state, and post-finalization notifications. Mongo sessions protect related database writes; external Paystack/BCL calls remain outside database transactions.
- Historical user direction kept `userId` in deposit input despite a protected endpoint because context could fail. Current GraphQL schema/mobile contract instead derive identity from the authenticated principal, matching the current repository review skill. The desired-vs-current disagreement is unresolved and must not be silently erased.
- Historical verification reported the focused deposit/route suites, a 77-test full suite, and build passing. Those results describe the session endpoint, not the later dirty working tree.

## Current Backend Evidence

- TypeScript, Express 5, Apollo Server 5, GraphQL/GraphQL WS, MongoDB/Mongoose, GraphQL Shield, AJV, JWT access/refresh sessions, Winston, Sentry, Jest, Docker/Compose, and GitHub CI/staging/production workflows.
- Startup validates core environment configuration, connects MongoDB, mounts routes and GraphQL, listens, then starts crons and migrations in their existing placement.
- Main domains include auth, users/KYC, portfolios/investment accounts, transactions, wallets, goals/auto-top-ups, documents, news, calculations, uploads/storage, BCL integration, payments, notifications, and Oye.
- Backend `.agent/skills` define one-file-per-operation services, thin typed resolvers, domain-local helpers/normalizers, BCL request/response normalization, and project JSDoc/error/model conventions.
- Codegen currently reads the live GraphQL endpoint at port 8080 rather than a checked-in schema artifact.

## Current Mobile Evidence

- Expo SDK 54, React Native 0.81, React 19, Expo Router 6, Apollo Client 3, Redux Toolkit, SecureStore/AsyncStorage, notifications, biometrics, analytics, Sentry, Jest, npm, and EAS.
- `app/` owns route entry points; `src/features`, `src/components`, `src/hooks`, `src/services`, `src/api`, `src/store`, `src/context`, `src/theme`, and `src/utils` own reusable behavior.
- The root composes Redux, Apollo, auth/theme/balance providers, route gating, secure logging, privacy/screen-capture/integrity controls, offline/toast behavior, analytics, diagnostics, and monitoring.
- Deposit UI requires KYC and transaction authentication, initializes Paystack through GraphQL, opens only an allowed authorization URL, polls backend verification, and refreshes balances only after backend/BCL success. The legacy direct-deposit mutation remains defined for compatibility but is not used by the production deposit hook.
- Mobile CI uses Node 22/npm and validates audit, OTA runtime safety, lint, typecheck, and Jest before EAS preview/build/update paths. Production validation requires a nonpublic HTTPS endpoint, disables a public KYC bypass, rejects secret-like public environment names, and checks TLS-pinning configuration.

## Promotion Decision

- Created two first-class project pages under `wiki/projects/`.
- Updated the Software Development Operating Manual with a linked Bora map and the supported financial/provider/service-boundary rules.
- Updated the New Project Bootstrap Operating Manual only for reusable evidence: inspect repository-local skills; treat provider adapters, domain orchestration, and configuration as separate ownership; and use idempotent claim/reconciliation patterns when database work surrounds external financial calls.
- Preserved existing personal/manual rules about withdrawal scope, migrations/crons, canonical IDs, and financial separation rather than duplicating or weakening them.

## Verification Boundary

- Repository inspection was read-only. Existing dirty state was preserved.
- Package manifests, README/configuration, repository skills, routes/providers, representative services/models, tests inventory, Docker/workflows, and live Git state were inspected selectively.
- No dependency install, generation, lint, test, build, application startup, database operation, migration, cron, external API call, payment, webhook, EAS build/update, deployment, or Git mutation was run.
- Historical test/build reports are attributed to their sessions; they are not presented as current verification of the dirty working trees.

## Contradictions And Uncertainty

- Historical explicit direction required deposit `userId` in input; current backend/mobile contracts derive it from the authenticated principal, and the current review skill prefers context-based scoping.
- Historical Oye tests expected a real default model and missing-key failure; current string interpolation can turn missing values into the truthy string `undefined`, bypassing both intentions.
- Resend is current default and Gmail was preserved as requested, but current environment string coercion does not reliably detect a missing Resend key.
- Fidelity is planned and documented, not implemented. Paystack is the current live deposit provider path.
- The backend and mobile repositories were already dirty, so base commit IDs alone cannot reproduce the inspected state.
- The mobile README describes an older/simpler project tree and Node 18 prerequisite; current package/workflow use Expo 54 and Node 22 CI.
- Mobile OTA hooks/workflows exist while current app configuration disables updates. Treat OTA publication as configured-but-disabled until the release configuration is reconciled.

## Completion Boundary

- Kusantec/Bora batch 1 is complete for the two Bora repositories and all six directly matched historical Bora sessions discoverable as of 2026-07-21.
- The next project-family batch is C.E.Q.A/Altin batch 1: inventory its repositories/apps, discover matching Codex sessions, and process one family batch or at most eight relevant sessions.
