---
type: project
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, bora-capital, backend, graphql, fintech]
sources:
  - ../sources/kusantec-bora-project-knowledge-harvest-batch-1.md
  - ../sources/hermes-persistent-memory-import.md
  - ../sources/kusantec-bora-hermes-conversation-harvest-supplement-1.md
  - ../sources/bora-canonical-identity-authorization-hermes-chain.md
  - ../sources/bora-security-hardening-hermes-continuations-6-20.md
  - ../sources/bora-authentication-session-hardening-continuations-21-35.md
  - ../sources/bora-runtime-payment-safety-continuations-36-50.md
  - ../sources/bora-quality-deployment-continuations-51-52.md
  - ../sources/bora-default-wallet-autotopup-continuations.md
  - ../sources/bora-mistitled-partner-mobile-continuations.md
  - ../sources/graphql-product-bora-paystack-hermes-chain.md
confidence: high
---

# Bora Capital Backend

## Summary

Fintech API and orchestration runtime for Bora Capital authentication, KYC, investment accounts, portfolios, transactions, portfolio-separated payments, wallets, goals, documents, notifications, and financial education.

## Purpose

Serves [[bora-capital-mobile-app|Bora Capital Advisors Mobile App]], integrates with the BCL investment-management system, verifies Paystack deposits before BCL credit, and owns protected financial and identity workflows.

## Stack

- Node `>=22.13.0`, Yarn 1.22.22, TypeScript 5.9.
- Express 5, Apollo Server 5, GraphQL 16, GraphQL WS, GraphQL Shield.
- MongoDB/Mongoose 8, JWT access/refresh sessions, AJV, `http-errors`.
- Winston and Sentry; Jest, Supertest, and TypeScript/Jest tooling.
- Paystack, BCL, DigitalOcean-compatible object storage, Resend/Gmail/SMTP, Expo push, Ollama, React Email.
- Docker plus database/development/production Compose files; GitHub CI, staging, and production workflows.

## Architecture

`src/main.ts` loads and validates core environment configuration, then `src/app.ts` composes Express and the shared HTTP server, connects MongoDB, mounts HTTP routes and GraphQL, listens, and starts existing crons/migrations.

GraphQL resolvers are typed delegates. Domain services own authorization, validation, orchestration, normalization, persistence, external APIs, and notification decisions. The singleton BCL client owns transport/token behavior; each domain owns its BCL request/response shape and normalizer.

Paystack provider functions live under `src/services/payments/paystack`. Deposit orchestration lives under `src/services/transactions/payment`, portfolio subaccount lookup under `src/services/portfolioPaymentConfigs`, and generic transaction persistence under `src/models/transactions`.

## Folder Ownership

- `src/graphql/<domain>` and `src/graphql/shield`: schema, thin resolvers, and operation guards.
- `src/services/<domain>`: one file per operation with domain business behavior.
- `src/services/bcl`: shared BCL transport; caller domains own BCL semantics.
- `src/services/payments`: external payment-provider adapters only.
- `src/services/transactions`: BCL transaction operations plus Paystack orchestration, claims, webhook inbox, BCL sync, and reconciliation.
- `src/models`, `src/common/interfaces`, `src/common/enums`: persistence and domain contracts.
- `src/security`, `src/loggers`, `src/middlewares`, `src/servers`, `src/routes`: cross-cutting runtime/security concerns.
- `scripts/migrations` and `src/crons`: existing startup migration and repeating-job ownership.
- `.agent/skills`: repository-specific implementation/review conventions.

## Commands

- `yarn dev`, `yarn build`, `yarn start`.
- `yarn generate` — requires the GraphQL server available at the configured local endpoint.
- `yarn test`, `yarn test:security`.
- `yarn format`, `yarn format:check`.
- `yarn audit:production`, `yarn check`.
- Docker/Compose commands in README provide database-only, watched development, and production-image paths.

## Runtime/Deployment

Default local port is 8080. Runtime exposes `/health`, `/graphql`, GraphQL subscriptions, auth routes, and `/payments/paystack/webhook`. Startup keeps migrations and cron jobs in their current post-listen placement. Docker defaults to Node 22, and GitHub workflows cover validation plus staging/production delivery.

The inspected branch was `feature/updates` at base commit `49fe85765b8c` with substantial pre-existing uncommitted security/runtime work. This harvest did not modify it.

## Durable Conventions

- Treat `.agent/skills` and referenced sibling implementations as execution checklists.
- Keep resolvers thin, typed, authenticated, and delegated to services.
- Use one service operation per file, local barrels, domain-owned helpers/interfaces/models, and the repository's `@description` JSDoc style.
- BCL services normalize PascalCase provider shapes at the boundary and retain endpoint-specific success-field handling.
- Keep provider adapters, transaction orchestration, portfolio payment configuration, and wallets in separate domains.
- Prefer plain exported payment functions over provider client classes in this project.
- Do not delete an existing provider/flow merely because another becomes the default. Resend is active; Gmail/SMTP remain explicit alternatives.
- Oye is educational only and refuses advice, recommendations, predictions, unrelated requests, and unverifiable Bora/user facts.
- Preserve unrelated withdrawal, migrations, cron, GraphQL, and service behavior during focused payment/security work.
- Bind transaction writes, provider-backed statements, wallet lookup/list/create, and auto-top-up transitions to authenticated principal ownership before any external request or state transition.
- Apply canonical principal identity after spreading compatibility input so caller-controlled user IDs cannot override it. Resolve external IDs to documents, then use fetched canonical IDs downstream.
- Public deposit initialization and single investment-account lookup derive identity from authenticated principal context; public GraphQL inputs omit caller-selected `userId`, while trusted provider/wallet input stays internal.
- A question about continuing is not authorization to edit during paced remediation; wait for the explicit next instruction.
- Portfolio Paystack setup must use real provider subaccounts and dedicated settlement metadata. Do not introduce fake/staging subaccount identifiers into code shared with production.
- External-provider migrations require explicit idempotency and partial-failure handling beyond the local migration registry's once-after-success marker.

## Constraints

- Each portfolio needs its own active Paystack subaccount configuration; deposits must not fall through to a central account.
- Dedicated settlement accounts are a business invariant. Validate uniqueness explicitly and map accounts to stable portfolio identifiers rather than relying on portfolio result order.
- Redact settlement account details from migration/setup output and error logs.
- Never trust frontend payment status. Finalization requires Paystack verification or a signature-verified webhook, matching reference, amount in subunits, and currency.
- Local processing uses atomic claims, durable webhook receipt state, idempotency, and BCL reconciliation. External provider calls remain outside Mongo transactions.
- A user must own the selected investment account. Current code derives the user from the authenticated principal.
- Preserve both human/business `amount` and provider `amountInSubunit`.
- BCL credit completes after Paystack success; customer notification follows durable local/BCL finalization and cannot reverse it.
- Do not claim ISO/SOC or provider capabilities without evidence.
- Do not expose or log provider secrets, tokens, credentials, wallet authorizations, or private user data.
- Owner-scoped by-ID reads should avoid object-existence disclosure. Internal ownerless helpers require an explicit trusted boundary and must not leak into public GraphQL paths.
- Authentication challenge index rollout requires duplicate-record preflight and a migration/cleanup plan; a schema-level unique index is not proof that existing production data can accept it.
- Process-local authentication rate limiting is not sufficient evidence for a multi-replica deployment; shared/durable enforcement remains unresolved.
- Deleting or ignoring a secret-bearing environment artifact does not rotate exposed credentials or purge Git history; provider-side rotation and explicit history disposition require separate verified action.
- Do not enable global ODM filter sanitization when trusted application queries rely on operators; sanitize untrusted filter input at its boundary instead.

## Decisions And Rationale

- A generic `Transaction` with nested `payment.paystack` keeps business lifecycle separate from provider metadata and supports future provider evolution.
- Portfolio subaccounts preserve money separation at settlement, not merely in application reporting.
- Settlement bank code/account number belong to portfolio payment configuration, and deposit initialization must always route through the real configured subaccount with the subaccount as fee bearer.
- Registering provider setup as a one-shot migration simplifies orchestration but does not make external side effects exactly-once; provider idempotency and local reconciliation are still required.
- Claim-before-BCL-sync plus reconciliation avoids double credit and gives failed external synchronization a recoverable state.
- The legacy direct-deposit mutation remains for compatibility, but the Paystack path is the active mobile deposit contract.
- Repository-local skills and a known LivelyCura implementation were chosen over improvised abstractions because the user repeatedly required structural fidelity.
- Gmail was restored when its removal exceeded the requested Resend transition.
- Rollbar was replaced by Sentry. Sending remains disabled without a DSN, default PII is disabled, and event data is redacted before transport.
- DigitalOcean-compatible wallet credential encryption uses exactly `WALLET_CREDENTIAL_ENCRYPTION_KEY` and `WALLET_CREDENTIAL_ACTIVE_KEY_VERSION`. The single-key design derives encryption/fingerprint subkeys and requires coordinated re-encryption for rotation; it is not an online key-ring system.

## Verification Expectations

Respect the dirty working tree and run no destructive cleanup. For payment changes, run focused Paystack/deposit/webhook/reconciliation tests, BCL transaction tests, build, full Jest, then live sandbox initialization/verification/webhook replay with test credentials and portfolio subaccounts. Provider-setup migration tests must cover duplicate settlement accounts, stable portfolio/account mapping, partial provider success, local-write failure, rerun behavior, redacted output, and startup execution. Verify duplicate events, amount/currency/reference mismatch, BCL failure and reconciliation, tenant ownership, and notification non-atomicity. Run generation only with the local GraphQL server available. Security/deployment work should use `yarn check`, Docker smoke checks, and staging validation without moving migrations/crons or exposing credentials.

## Evidence

- Current package/README, repository skills, startup/routes/GraphQL, auth/KYC, notifications/Oye, BCL, Paystack/transaction/config/model/test source, Docker/workflows, and live Git state at base commit `49fe85765b8c` plus pre-existing dirty work.
- Six sessions—`019da0bb…`, `019de86b…`, `019e132f…`, `019e6018…`, `019eae1b…`, and `019ebc8d…`—in [[../sources/kusantec-bora-project-knowledge-harvest-batch-1|Kusantec/Bora Project Knowledge Harvest — Batch 1]].
- Prior durable project rules in [[../sources/hermes-persistent-memory-import|Hermes Persistent Memory Import]].
- Seven direct Hermes sessions—six substantive and one interrupted—in [[../sources/kusantec-bora-hermes-conversation-harvest-supplement-1|Kusantec/Bora Hermes Conversation Harvest — Supplement 1]]. They provide staged transaction, statement, wallet, and auto-top-up authorization provenance plus Sentry and deployment-compatible wallet-encryption decisions. Historical test/build counts remain session-attributed and were not rerun.
- Four replay-heavy substantive continuations in [[../sources/bora-canonical-identity-authorization-hermes-chain|Bora Canonical Identity And Authorization Hermes Chain]] provide exact provenance and historical closure for canonical-ID handling, owner-scoped auto-top-up cancellation, principal-bound deposits, and principal-bound investment-account lookup.
- Fifteen substantive continuations in [[../sources/bora-security-hardening-hermes-continuations-6-20|Bora Security Hardening Hermes Continuations 6–20]] provide grouped provenance for immutable principal policies, wallet/provider credential isolation, resolver-service ownership, financial notification isolation, and purpose-aware recovery.
- Fifteen substantive continuations in [[../sources/bora-authentication-session-hardening-continuations-21-35|Bora Authentication And Session Hardening Continuations 21–35]] provide grouped provenance for hash-only OTPs, atomic attempts, transactional login, rejected challenge IDs, shared refresh rotation, JWT constraints, structured redaction, and historical-secret obligations.
- Fifteen substantive continuations in [[../sources/bora-runtime-payment-safety-continuations-36-50|Bora Runtime And Payment Safety Continuations 36–50]] provide grouped provenance for runtime restoration, CORS/Helmet corrections, BCL/Paystack transaction boundaries, webhook inboxes, manual reconciliation, session families, and structural enum/interface cleanup.
- Final continuations in [[../sources/bora-quality-deployment-continuations-51-52|Bora Quality And Deployment Continuations 51–52]] close common-interface/enum migration and JSDoc/error-flow work, while separating GitHub trigger, clean repository build, and DigitalOcean component-build evidence.
- Six default-profile records in [[../sources/bora-default-wallet-autotopup-continuations|Bora Default-Profile Wallet And Auto-Top-Up Continuations]] close owner-scoped wallet mutation, public/internal credential boundaries, wallet eligibility, canonical lookup reuse, and owner-scoped auto-top-up updates.
- Two misleadingly titled records in [[../sources/bora-mistitled-partner-mobile-continuations|Bora Mistitled Partner-Mobile Continuations]] actually close Bora session verification and historical production-hardening plan validation; replayed Altin material adds no new Altin ownership.
- Two additional substantive coder-profile records in [[../sources/graphql-product-bora-paystack-hermes-chain|GraphQL Product And Bora Paystack Hermes Chain]] establish real portfolio subaccounts, settlement metadata, rejected fake-provider behavior, and current provider-migration safety gaps. Historical verification stopped at build, six focused deposit tests, and dry-run mapping; real provisioning did not complete.

## Contradictions

- Historical explicit direction kept `userId` in protected deposit input because context could fail. Current GraphQL/mobile derive identity from the authenticated principal, and the current review skill recommends context-based scoping.
- Fidelity onboarding and API documents exist, but the current Fidelity payment boundary is empty; Paystack is the implemented deposit provider.
- Historical Oye verification expected a real default model and missing-key failure. Current module-level setup is user-chosen, but string interpolation makes an absent environment value become the truthy string `undefined`, so the fallback is ineffective.
- Resend is the default and Gmail was preserved as requested, but similar string coercion weakens the current missing-key guard.
- Historical sessions reported passing builds/tests, but the current working tree contains extensive later uncommitted changes and was not re-tested during this read-only harvest.
- Repository skills contain some legacy/example naming and conventions that do not exactly match all live files; current code plus explicit user corrections outrank generic examples.
- The broad July 13 “high risk” audit is a historical snapshot; later remediation and current source repaired many findings.
- The auto-top-up lookup helper still supports an internal ownerless path when no user ID is supplied. Public GraphQL paths are scoped, but the helper is not universally fail-closed.
- The reviewed historical wallet design separated stable fingerprint material from rotating encryption keys; the current dirty working tree derives both from one scalar root and accepts only the active envelope version. Reconcile this material change before deployment.
- Temporary plaintext provider-credential compatibility and its migration remain incomplete; challenge identifiers are absent and rate limiting remains process-local.
- Likely historical JWT access/refresh, Rollbar, and Expo credentials require verified provider-side rotation and an explicit Git-history decision; values are intentionally excluded from the vault.
- Password reset currently revokes session records separately before password/legacy-token update, so full session-family revocation and password mutation are not one database transaction.
- Historical payment review required monotonic successful BCL finalization, but current `bclSync/finalizeDeposit.ts` updates by transaction ID without an exact expected processing/sync-state predicate.
- Startup announces readiness and starts crons before unawaited migrations, so uppercase-only jobs/reads can race legacy persisted-value normalization.
- Current source still contains unchanged caught-error rethrows despite the accepted one-deliberate-mapped-error-per-catch convention.
- `getAutoTopUpById` still permits an ownerless internal lookup fallback when identity is omitted, even though public paths are owner-scoped.
- Current logger/deposit/email boundaries still include an unredacted Winston path plus a `productions` typo, public client-supplied `depositCash`, and weak Resend missing-configuration/failure semantics.
- Sentry and wallet-encryption changes are present only in the dirty working tree, and the historical security plan is deleted locally despite remaining in `HEAD` history.
- Current settlement setup checks array length but not account-number uniqueness and associates accounts by portfolio result order.
- The migration registry records success only after completion, but provider side effects can occur before a local failure; provider-level idempotency and recovery are not demonstrated.
- Startup triggers migrations without awaiting them, and provider setup calls BCL/Paystack during startup. Current documentation also lists Paystack commands absent from `package.json`.
- Current setup/migration results may expose settlement account details, and the claimed V2 fake-configuration cleanup migration is absent from current source.

## Confidence

High for current static architecture, explicit session corrections, and financial-flow ownership; medium for runtime/deployment status because the working tree is dirty and no commands or external integrations were executed.

## Open Questions

- Deposit identity is currently principal-derived across backend and mobile; any reversal would require an explicit product/security decision and coordinated contract migration.
- Is Fidelity still planned beside Paystack, and has the exact collection/direct-debit capability been confirmed?
- Should Oye/Resend configuration validation be repaired without changing the user-selected module layout?
- When will the current security/runtime work be committed and revalidated as a reproducible release candidate?
- How will dedicated settlement-account uniqueness and stable portfolio mapping be enforced?
- What provider idempotency/reconciliation contract prevents duplicate subaccounts after partial failure and retry?
