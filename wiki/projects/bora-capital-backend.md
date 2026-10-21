---
type: project
status: active
created: 2026-07-21
updated: 2026-10-21
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
  - ../sources/bora-kyc-supervision-and-statement-update.md
  - ../sources/bora-frontend-handoff-frozen.md
  - ../sources/bora-existing-customer-account-ownership.md
  - ../sources/bora-error-format-consistency.md
  - ../sources/bora-production-ci-audit-scope.md
  - ../sources/bora-oye-website-grounding.md
  - ../sources/bora-grow-wealth-existing-customer-valuations.md
  - ../sources/bora-fund-administration-access-control.md
  - ../sources/bora-customer-support-administration.md
  - ../sources/bora-realtime-support-subscriptions.md
  - ../sources/bora-notifications-marketing.md
  - ../sources/bora-biometric-login-and-handoff-docs.md
  - ../sources/bora-bcl-error-passthrough-and-secret-files.md
  - ../sources/bora-single-user-update-path.md
  - ../sources/bora-local-only-scripts.md
  - ../sources/bora-push-device-binding.md
  - ../sources/bora-single-input-object-convention.md
confidence: high
---

# Bora Capital Backend

## Summary

Fintech API and orchestration runtime for Bora Capital authentication, hybrid staff authorization, fund administration, customer support, KYC, investment accounts, portfolios, transactions, portfolio-separated payments, wallets, goals, documents, notifications, and financial education.

## Purpose

Serves [[bora-capital-mobile-app|Bora Capital Advisors Mobile App]], integrates with the BCL investment-management system, verifies Paystack deposits before BCL credit, and owns protected financial and identity workflows.

## Stack

- Node `>=22.13.0`, Yarn 1.22.22, TypeScript 5.9.
- Express 5, Apollo Server 5, GraphQL 16, GraphQL WS, GraphQL Shield.
- MongoDB/Mongoose 8, JWT access/refresh sessions, AJV, `http-errors`.
- Winston and Sentry; Jest, Supertest, and TypeScript/Jest tooling.
- Paystack, BCL, DigitalOcean-compatible object storage, Resend/Gmail/SMTP, Hubtel SMS, Expo push, Ollama, and React Email with Tailwind.
- Docker plus database/development/production Compose files; GitHub CI, staging, and production workflows.

## Architecture

`src/main.ts` loads and validates core environment configuration, then `src/app.ts` composes Express and the shared HTTP server. Startup connects MongoDB with automatic index creation disabled, awaits fail-closed data migrations, builds declared model indexes, initializes GraphQL, starts listening, and only then starts cron jobs.

GraphQL resolvers are typed delegates. Domain services own authorization, validation, orchestration, normalization, persistence, external APIs, and notification decisions. The singleton BCL client owns transport/token behavior; each domain owns its BCL request/response shape and normalizer. Every `/api/partner/fetchdata` call goes through the shared `fetchBclData` (`src/services/bcl/fetchData.ts`), which turns BCL's status envelope into client-visible errors.

Portfolio services distinguish BCL's two asset families. Existing collective-investment operations live under `src/services/portfolios/CIS`; Grow Wealth uses separate linked-portfolio and valuation services under `src/services/portfolios/growWealth`. GraphQL exposes explicitly named CIS operations plus `getMyGrowWealth` for grouped existing-customer NAV and `getMyGrowWealthValuationReport` for detailed holdings. Both Grow Wealth reads derive identity from the authenticated principal and resolve portfolio IDs through BCL; new-customer Grow Wealth creation remains deferred.

Access control resolves effective permissions from active database roles plus direct grants for every protected request. Fund administration stores one local record per BCL portfolio ID with isolated draft and published fact payloads; the customer CIS contract reads only visible published facts and overlays BCL's live offer price when available.

Customer support stores cases separately from chronological messages. Customer operations are principal-owned; the admin queue exposes internal notes, assignment, priority, and status actions through dedicated support permissions. Client request IDs make case and message writes idempotent, while customer views receive public replies only.

GraphQL subscriptions run on the `/subscriptions` graphql-ws server. Connections require a known client plus an access token in `connectionParams.headers`, an active session, and an enabled account; session and account status are revalidated before every operation and delivered event. Customer support exposes one live `customerSupportCaseUpdated(filters: { caseId })` stream: admin-portal responders see every case, internal notes, and queue counts, and customers see only their own public conversation. Events flow through LivelyCura's in-memory `new PubSub()` in `src/pubsub`, which is correct for the single App Platform instance. An unwired functional `createMongoPubSub()` change-stream fan-out is the prepared swap if the instance count ever rises.

Paystack provider functions live under `src/services/payments/paystack`. Deposit orchestration lives under `src/services/transactions/payment`, portfolio subaccount lookup under `src/services/portfolioPaymentConfigs`, and generic transaction persistence under `src/models/transactions`.

Notification templates share a React Email `Tailwind` layout under `src/services/notifications/template`; the layout owns the Bora palette, explicit light/dark color schemes, and primary-color anti-inversion treatment. Gmail iOS full inversion is handled separately with Gmail-targeted `screen`/`difference` blend wrappers around light header/footer text while the navy gradient preserves the brand background. Simple Hubtel SMS uses the user-verified `GET https://smsc.hubtel.com/v1/messages/send` contract with URL-encoded credentials and message fields while Bora logging retains redacted error metadata.

## Folder Ownership

- `src/graphql/<domain>` and `src/graphql/shield`: schema, thin resolvers, and operation guards.
- `src/services/<domain>`: one file per operation with domain business behavior.
- `src/services/bcl`: shared BCL transport and the shared `fetchdata` envelope/error handling; caller domains own BCL request and row semantics.
- `src/services/portfolios/CIS` and `src/services/portfolios/growWealth`: separate CIS and Grow Wealth BCL portfolio contracts behind the stable portfolio barrel.
- `src/services/roles`, `src/models/roles`, and `src/graphql/roles`: database-backed roles and LivelyCura-style permission resolution/tree ownership.
- `src/services/staff` and `src/graphql/staff`: staff invitation lifecycle, direct grants, access changes, and admin operations.
- `src/graphql/shield/permission`: registered permission guards backed by the role permission map and request-time resolver.
- `src/services/funds`, `src/models/funds`, and `src/graphql/funds`: complete fact-sheet validation, isolated draft/publication lifecycle, visibility, and admin APIs.
- `src/services/customerSupport`, `src/models/customerSupport`, and `src/graphql/customerSupport`: customer-owned cases, message visibility, responder queue, assignment, priority, and lifecycle APIs.
- `src/services/payments`: external payment-provider adapters only.
- `src/services/transactions`: BCL transaction operations plus Paystack orchestration, claims, webhook inbox, BCL sync, and reconciliation.
- `src/models`, `src/common/interfaces`, `src/common/enums`: persistence and domain contracts.
- `src/security`, `src/loggers`, `src/middlewares`, `src/servers`, `src/routes`: cross-cutting runtime/security concerns.
- `src/pubsub`: GraphQL subscription event bus; `pubsub.ts` is the only exported instance, and `mongoPubSub.ts` stays out of the barrel until multi-instance deployment.
- `scripts/migrations` and `src/crons`: existing startup migration and repeating-job ownership.
- `.agent/skills`: repository-specific implementation/review conventions.

## Commands

- `yarn dev`, `yarn build`, `yarn start`.
- `yarn generate` — requires the GraphQL server available at the configured local endpoint.
- `yarn test`, `yarn test:security`.
- `yarn format`, `yarn format:check`.
- `yarn audit:production`, `yarn check`.
- `yarn bootstrap:admin` — idempotently create or promote the first immutable-system-role administrator from environment values.
- `yarn seed:fund-catalog` — insert the three July 2026 production fund fixtures and skip any existing portfolio ID completely.
- Docker/Compose commands in README provide database-only, watched development, and production-image paths.

## Runtime/Deployment

Default local port is 8080. Runtime exposes `/health`, `/graphql`, GraphQL subscriptions, auth routes, and `/payments/paystack/webhook`. Startup now completes migrations and model-index creation before GraphQL readiness, HTTP listening, or cron startup; migration failure prevents the server from accepting traffic. Docker defaults to Node 22, and GitHub workflows cover validation plus staging/production delivery.

A 2026-07-30 staging Hubtel request reached the simple-message API but returned HTTP 400 with provider status `100`, meaning the supplied SMS Client ID was not recognized. This is a credential-provisioning/rotation failure rather than an endpoint, phone-normalization, or sender-ID result; rotate the exposed pair, replace both staging values together, redeploy, and retest before evaluating later provider checks. The incident's raw Axios logging exposed the credential-bearing URL plus private notification data; the adapter now emits only allowlisted error type/code, HTTP status, and provider status metadata. Existing external log copies still require operator-owned purge/restriction according to incident policy.

A 2026-07-31 local comparison corrected the transport diagnosis: the known-working request used `smsc.hubtel.com`, while the application used the separate `sms.hubtel.com` gateway and loaded a different Client ID. Probes with deliberately invalid credentials confirmed that both hosts exist but return distinct status-`100` descriptions. Bora now uses the user-verified `smsc` host, and the endpoint regression plus no-raw-console-log regression are enforced in the Hubtel adapter test. Environment credentials still have to be one matching active pair and must be rotated after exposure.

The inspected branch was `feature/updates` at base commit `49fe85765b8c` with substantial pre-existing uncommitted security/runtime work. This harvest did not modify it.

## Durable Conventions

- Admin authorization is the request-time union of active role permissions and direct grants. Use `Role`, `RoleModel`, `platformRoles`, and `permissions`, with `getRole`/`getRoles`/`createRole`/`updateRole`; never restore `AccessRole`, `accessRoleIds`, `directPermissions`, or `access.*`. Support exact keys, namespace wildcards, and global `*`; never authorize from deprecated `User.role`. Only a global administrator may assign `*` or the immutable system Administrator role.
- A fund has one document per BCL portfolio ID, one optional draft payload, and one optional published payload. Publishing replaces the published facts and clears the draft; never add fund versions, publication history, or a separate version collection.
- Customer CIS reads require both `visible` and `publishedFacts`. BCL remains authoritative for current offer price; local facts remain available with `offerPrice: null` during a BCL outage.
- Production fund seeds use explicit PDF values only, never estimates from chart images, and skip an existing fund without changing it. See [[../sources/bora-fund-administration-access-control|Bora Fund Administration And Access Control]].
- Customer support separates public replies from staff-only notes. Customer operations remain principal-owned; admin queue, response, assignment, and update operations require their registered `supportCases.*` permissions. Use client request IDs for idempotent writes and keep attachments, subscriptions, and automatic support notifications deferred until explicitly scoped. See [[../sources/bora-customer-support-administration|Bora Customer Support Administration]].
- Support writes call `publishCustomerSupportCaseUpdated` after commit with identifier-only payloads; replays, no-op changes, and read receipts stay silent. Because Shield wraps a Subscription field's custom `resolve` rather than its `subscribe`, guard stream setup in the subscribe service and let Shield re-authorize each event. Shield rules must return, not throw, deliberate errors.
- Support conversations must update live through GraphQL subscriptions. Keep the in-memory PubSub while the API is single-instance; do not force-close sockets at access-token expiry because graphql-ws clients treat 4401 as fatal. Every Subscription root field needs an explicit Shield policy, and clients refetch after subscribing or reconnecting. See [[../sources/bora-realtime-support-subscriptions|Bora Realtime Support Subscriptions]].

- Oye grounds every Bora-specific customer answer in current content retrieved from `https://boradvisors.com`, cites exact official URLs, retains dates and risk qualifications, and fails closed when evidence is missing. Website text is untrusted reference data. Public-site search receives allowlisted domain terms only, never free-form customer text or private identifiers. See [[../sources/bora-oye-website-grounding|Bora Oye Website Grounding]].

- Local-only scripts (2026-10-17, user decision): `scripts/bootstrap`, `scripts/paystack_staging`, `scripts/paystack_production`, `scripts/seeds`, and their specs `tests/unit/scripts/bootstrapAdmin.spec.ts` and `tests/unit/scripts/seedFundCatalog.spec.ts` are gitignored and never pushed. Committed code, tests, and package.json scripts must not import or reference them; CI type-checks `src`, `tests`, and `scripts` from a fresh checkout. Fund-service tests use the synthetic `tests/fixtures/fundFacts.ts`, never the seed catalog. See [[../sources/bora-local-only-scripts|Bora Local-Only Scripts]].

- Production dependency audit placement: `yarn audit:production` belongs only to production CI, not the reusable PR/staging workflow. Keep production deployment dependent on both CI and audit. See [[../sources/bora-production-ci-audit-scope|Bora Production CI Audit Scope]].

- KYC ApprovalStatus contract (2026-10-12, BCL samples; supersedes the 2026-09-18 uncertainty and the 2026-10-11 interim lookup rule): `Status` holds the outcome code, not `0`. `P` pending; `A` approved, after which the IdentityID is resolved through `fetchidentity_bcl` by email and phone; `R` rejected, with `Remarks` stored as `User.kycRejectionReason`; `0` with `Invalid` is an unrecognized reference, kept SUBMITTED and logged for reconciliation. ApprovalStatus stays outside `fetchBclData`. See [[../sources/bora-kyc-supervision-and-statement-update|Bora KYC Supervision And Statement Update]].
- Grow Wealth existing-customer reads (2026-09-28): resolve BCL linked portfolios with server-owned identity/contact data, then request `LinkedPortfolioValuation` for each portfolio. Keep the grouped dashboard summary and detailed valuation report as separate authenticated GraphQL queries; keep new-customer creation on hold. The cash movement statement (2026-10-16, `LinkedPortfolioCMS`) is `getMyGrowWealthCashMovementStatement(filters: { portfolioId, fromDate, toDate })`, scoped to linked portfolios. It returns opening and closing balances plus `DEBIT`/`CREDIT` entries with thousands separators parsed. See [[../sources/bora-grow-wealth-existing-customer-valuations|Bora Grow Wealth Existing Customer Valuations]].
- BCL `fetchdata` errors pass through (2026-10-11): BCL status codes are unreliable, and its `Description` explains what happened. Do not model BCL error shapes. Route every `/api/partner/fetchdata` call, including Grow Wealth, through `fetchBclData`. A non-zero `Status[0].Status` or a BCL `Message` becomes a 400 `BAD_REQUEST` carrying BCL's text to the frontend. Use a 502 `BAD_GATEWAY` with a hidden message only when BCL is unreachable or returns an unreadable envelope or malformed rows. See [[../sources/bora-bcl-error-passthrough-and-secret-files|Bora BCL Error Passthrough And Secret-File Boundary]].
- Never read `.env` or other secret-bearing files in this repository, even to call staging BCL; ask the user to run credentialed calls. This is a cross-project rule; see [[../syntheses/software-development-operating-manual|Software Development Operating Manual]].
- Client IP (2026-10-11): the API points straight at DigitalOcean App Platform, so rate limits and the signup cap key on `do-connecting-ip` through `getClientIp`, with the socket address as a fallback. Leave Express `trust proxy` unset, because App Platform's `X-Forwarded-For` holds its own ingress address. When the user's own Cloudflare zone goes in front, switch `getClientIp` to `CF-Connecting-IP`, trusted only from Cloudflare's ranges; otherwise all limits become shared again. Per-IP limits are a flood guard only. Sign-in passwords are limited per phone number: 5 attempts per 15 minutes, spent before the password check, with unknown numbers counted alike. Any password reset or change clears the lock. `refreshToken` is not rate limited (2026-10-13): the signed, single-use token and reuse detection are the protection. Clients must still refresh one at a time, because a reused refresh token revokes the session family. Signup is capped at a flat 20 per IP per hour, replacing the escalating IP cooldown. Durable per-key limits share `createRateLimitWindow` (`rateLimitWindows` collection, one scope per limit). See [[../sources/bora-client-ip-app-platform|Bora Client IP Behind DigitalOcean App Platform]].
- Account ownership (2026-10-12): `userOwnsAccount` checks the local `portfolioAccountNumbers` list, which caches accounts BCL confirmed for the user's `identityId`. The list fills when an account is opened in the app, at existing-customer onboarding, and on every BCL account read (add-only, never failing the read), so existing clients can transact without a per-transaction BCL call. See [[../sources/bora-existing-customer-account-ownership|Bora Existing-Customer Account Ownership]].
- Error format (2026-10-12): every error, GraphQL or Express/REST, is `errors: [{ message, extensions: { code } }]`, with codes from the shared `getErrorCode` (unlisted 4xx statuses map to `BAD_REQUEST`). Apollo 5 sets `originalError` on its own request errors, so `formatGraphqlErrors` maps Apollo client error codes to `BAD_REQUEST` with the real message and no Sentry report before unwrapping. `hideSchemaDetailsFromClientErrors` is on outside development. Test the formatter through a real `ApolloServer`. See [[../sources/bora-error-format-consistency|Bora Error Format Consistency]].

- New KYC submissions enter BCL supervision and remain `SUBMITTED` until `me` observes approval and resolves the final identity ID. The ApprovalStatus outcome code decides; the identity lookup only supplies the IdentityID after approval. Use the provider's `SuperviosionID` response field and XML `SupervisionID` request field at their respective boundaries.
- Approval checks run on app profile refresh, with no background polling. `createKyc` (renamed from `updateKyc`, 2026-10-13) creates only a `PENDING` user's first KYC. `updateKyc` (2026-10-16) corrects a `REJECTED` KYC by re-posting it through `addindividualidentity_bcl`, which is BCL's workflow; BCL has no update endpoint. Sent fields merge with the saved `kycSubmissions` form, and saved images (stored in the same document) are reused. The reference and the form are saved in one transaction, and the form is deleted in the approval transaction. It is owner-only. Use atomic claims and reference/state guards, retain ambiguous submissions for reconciliation, and send completion notifications only after persisted approval. See [[../sources/bora-kyc-supervision-and-statement-update|Bora KYC Supervision And Statement Update]].
- Date-range statements use `fetchministatement_bcl` with BCL-formatted date bounds; preserve public operations and account ownership checks. Multiple CI account numbers may belong to one portfolio and must remain distinct.

- Treat `.agent/skills` and referenced sibling implementations as execution checklists.
- Keep resolvers transport-only, typed, authenticated, and delegated to services. Declare named resolver functions above the resolver map, document them, and reference those names from `Query`, `Mutation`, and field maps instead of inlining functions. Put mapping, filtering, calculations, normalization, and response construction in documented services. Use generated GraphQL argument types and enums rather than handwritten resolver shapes or string unions.
- Use one service operation per file, local barrels, domain-owned helpers/interfaces/models, and the repository's `@description` JSDoc style. Every new or rewritten service function preserves or adds applicable `@param`, `@throws`, and `@returns` entries.
- User writes (2026-10-16, user corrections): inside a transaction use `updateUserInSession(filter, update, session)`, with the session required. Outside one, use `updateUser(filter, update, options?)`, whose options reject a session. Never call `userModel.findOneAndUpdate`, `findByIdAndUpdate`, `updateOne`, or `user.save()` directly. Both take an ID or a conditional filter and return the user without `password` or `refreshToken`; the shared logic lives once in `helpers/userUpdate.ts`. The profile service is `updateUserProfile`. Write any repeated operation once and import it. See [[../sources/bora-single-user-update-path|Bora User-Update Paths]].
- BCL services normalize PascalCase provider shapes at the boundary and retain endpoint-specific success-field handling.
- Keep CIS and Grow Wealth portfolio services and GraphQL types separate. Grow Wealth reads accept only an optional valuation date; user identity and linked portfolio IDs remain server-resolved.
- KYC exposes proof of address and ID-side names in app terminology, while the BCL boundary translates them to `imgBankProofString`, `imgIDFString`, and `imgIDBString` in both request and response directions.
- Existing Bora customers start with email and phone; BCL identity ID is optional. After BCL KYC verification, an existing-customer OTP authorizes password creation only. Completion returns no tokens and directs the customer through the ordinary phone/password login flow.
- Existing-customer OTPs are not login OTPs. Only signup and signin OTP purposes may create session tokens.
- Phone login uses the frontend's canonical `+233…` value as an exact lookup. Do not add local/country-code lookup variants unless the input contract changes.
- Keep provider adapters, transaction orchestration, portfolio payment configuration, and wallets in separate domains.
- Write functional code: plain exported functions and factories with closure state. Never author classes—for providers, infrastructure, or test fakes. See [[../sources/bora-realtime-support-subscriptions|Bora Realtime Support Subscriptions]].
- Functions take one input object typed by an interface, not separate positional parameters (user correction, 2026-10-20). For values a function does not forward, extend the input interface and strip them before forwarding rather than widening a shared interface. See [[../sources/bora-single-input-object-convention|Bora Service Functions Take One Input Object]].
- Do not delete an existing provider/flow merely because another becomes the default. Resend is active; Gmail/SMTP remain explicit alternatives.
- Oye is educational and customer-informational: it refuses personal advice, recommendations, predictions, unrelated requests, and unverifiable Bora/user facts while answering supported Bora questions from live official website evidence.
- Preserve unrelated withdrawal, migrations, cron, GraphQL, and service behavior during focused payment/security work.
- Bind transaction writes, provider-backed statements, wallet lookup/list/create, and auto-top-up transitions to authenticated principal ownership before any external request or state transition.
- Apply canonical principal identity after spreading compatibility input so caller-controlled user IDs cannot override it. Resolve external IDs to documents, then use fetched canonical IDs downstream.
- Public deposit initialization and single investment-account lookup derive identity from authenticated principal context; public GraphQL inputs omit caller-selected `userId`, while trusted provider/wallet input stays internal.
- A withdrawal instruction is submitted once through `requestWithdrawalOtp` and persisted as a pending withdrawal resource. `withdrawCash` accepts only `otpRequestId` and `otp`; after verification it atomically claims the stored account, amount, and comment, then generates the current `YYYY-MM-DD` date before BCL submission.
- A question about continuing is not authorization to edit during paced remediation; wait for the explicit next instruction.
- Portfolio Paystack setup must use real provider subaccounts and dedicated settlement metadata. Do not introduce fake/staging subaccount identifiers into code shared with production.
- Paystack provisioning is an explicit manual operation, one stable portfolio ID at a time. Keep staging and production scripts small, do not map settlement accounts by provider result order, and never invoke provider setup from startup migrations.
- When LivelyCura is named as the implementation reference, compare against its current live files rather than an earlier agent version. Newer user edits are authoritative and must not be overwritten.
- Keep Bora email templates on the shared React Email Tailwind layout. Preserve explicit dark-mode colors and the navy gradient fallback so iOS/email-client dark mode does not invert the primary header and footer to a light color. Gmail iOS force-inverts light text independently of that gradient, so the body class, Gmail-targeted CSS selector, and nested `screen`/`difference` blend wrappers around header/footer light text form one compatibility contract; removing any one of them recreates dark text on navy.
- Keep Hubtel simple SMS on the user-verified `GET https://smsc.hubtel.com/v1/messages/send` endpoint with URL-encoded query fields. Do not treat `sms.hubtel.com` and `smsc.hubtel.com` as interchangeable merely because both accept the same path and field names. Because credentials are provider-required query parameters, never log the request URL, Axios request config, raw provider error object, or temporary diagnostic serialization.
- Store account emails trimmed/lowercase and account phones in canonical international form; friendly existence checks do not replace database unique indexes or duplicate-key handling.
- Signup creates separate email and SMS challenges and activates the account only after both are consumed. Sign-in accepts phone plus password and sends its second factor only to the registered email.
- Challenge verification and resend use opaque challenge document IDs rather than caller-supplied email addresses. Adaptive request cooldowns are durable and atomic across replicas: 30 seconds, 60 seconds, then exponential growth capped at one hour, with a 24-hour idle reset. Signup also applies a hashed IP scope before account/provider work.
- Wallet destination identity is immutable. Updating labels must not change mobile number, network, bank account number, or bank code; adding another destination always creates another wallet.
- Mobile-money wallets use `createMobileMoneyWallet`: normalize the Ghana number, create an inactive pending wallet, send an SMS challenge bound to that wallet resource, and activate only after challenge verification. Bank wallets continue to use insert-based `createWallet` and may coexist.
- Send every new notification through `notifyUsers`: it writes the inbox item and one delivery row per channel in one transaction, and the cron worker delivers them with leases, retries, and SMS pacing. Do not call Expo, Resend, or Hubtel inline for new notification types.
- Staff-facing notifications are admin-portal inbox items only (`channels: []`); ask before adding email, push, or SMS for staff.
- Signup welcome, KYC approval, deposit, and withdrawal events keep their own templated email, SMS, and push and add an inbox-only item through `addCustomerInboxNotification`, keyed by the event. A customer-app sign-in sends a `NEW_SIGNIN` security alert ("New sign-in to your account") to the account's other signed-in phones, replacing the welcome-back push; it stays out of the inbox, and admin-portal sign-ins send no push.
- Push registrations are per install, never per user (2026-10-21): one `PushDevice` row per install with a unique token and installation id, bound to the signed-in user and session. Session revocation deletes the matching devices, and every send uses only devices whose session is active, unexpired, and owned by the same user. Registration needs the customer-app client, a session-bound token, `installationId`, `buildType`, and `appId`; production accepts only the store build. Any push Expo refuses is retried; only `DeviceNotRegistered` deletes a device. Push tokens are credentials and never reach logs. See [[../sources/bora-push-device-binding|Bora Push Notifications Bound To Device And Session]].
- Marketing: customers are never asked for consent, receive marketing by default, and may switch off push, email, or SMS. In-app inbox items and banners are never gated. Transactional notifications ignore preferences; marketing deliveries re-check consent at send time.
- The notification worker sends one SMS per 30 seconds because Hubtel's 5 requests per minute are shared with OTP delivery.
- Campaign SMS is on hold until the user finishes investigating Hubtel bulk sending: `CAMPAIGN_SMS_ENABLED` must be exactly `true` to schedule, send, or test SMS campaigns or to queue campaign SMS. Do not lift the hold or wire Hubtel batch sending without the user.
- Uploads follow the LivelyCura pattern: validate the owning record first, upload inside its create/update service, store an `Upload` record, reference it by ID, and build public URLs from `UPLOADS_BASE_URL`. Storage stays private unless the folder is in the public-folder list.
- Customer audience queries treat a missing `accessChannels` as CUSTOMER and a missing `kycStatus` as PENDING, matching sign-in and model defaults.
- Frontend handoffs are frozen once sent (user corrections, 2026-10-12 and 2026-10-13): never edit `docs/frontend-handoff-app.md`, `docs/frontend-handoff-admin.md`, or any sent dated handoff. All updates not yet committed and pushed form one batch with ONE `docs/frontend-handoff-YYYY-MM-DD.md`, extended and corrected in place until the batch is pushed and sent. It covers only changes since the last handoff, is marked for the customer app or the admin portal, and states corrections to sent items. Validate GraphQL examples against the live schema. Never infer what was already sent; ask. A pushed handoff is probably sent: check `git reflog show origin/<branch>` before extending one. `docs/frontend-handoff-2026-10-13.md` is sent and frozen at its `fc3fa4a` content; the current file is `docs/frontend-handoff-2026-10-17.md`. See [[../sources/bora-frontend-handoff-frozen|Bora Frontend Handoffs Frozen Once Sent]].
- Biometric login is a hashed per-device token exchanged by `loginWithBiometric` for a normal session with assurance level `biometric`. Enabling needs no password within 10 minutes of an OTP sign-in and the password otherwise; it lapses after 90 days unused and is turned off by logout, password change or reset, and account disablement.

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
- Hubtel credentials travel in the provider-required query string; observability must remain limited to redacted error classification and must not capture the generated URL.
- Owner-scoped by-ID reads should avoid object-existence disclosure. Internal ownerless helpers require an explicit trusted boundary and must not leak into public GraphQL paths.
- User-contact and user-managed mobile-wallet unique-index rollout must keep duplicate/invalid-data preflight ahead of mutation. Startup fails closed rather than partially normalizing colliding records.
- Process-local GraphQL burst limiting remains defense in depth only; provider-cost controls use shared Mongo-backed user/action cooldowns plus a hashed signup-IP scope.
- Deleting or ignoring a secret-bearing environment artifact does not rotate exposed credentials or purge Git history; provider-side rotation and explicit history disposition require separate verified action.
- Do not enable global ODM filter sanitization when trusted application queries rely on operators; sanitize untrusted filter input at its boundary instead.

## Decisions And Rationale

- A generic `Transaction` with nested `payment.paystack` keeps business lifecycle separate from provider metadata and supports future provider evolution.
- Portfolio subaccounts preserve money separation at settlement, not merely in application reporting.
- Settlement bank code/account number belong to portfolio payment configuration, and deposit initialization must always route through the real configured subaccount with the subaccount as fee bearer.
- Paystack subaccounts are provisioned manually rather than through startup migrations. One-portfolio scripts make the selected portfolio, bank account, environment, provider result, and local configuration write visible to the operator without a bulk orchestration layer.
- Claim-before-BCL-sync plus reconciliation avoids double credit and gives failed external synchronization a recoverable state.
- The legacy direct-deposit mutation remains for compatibility, but the Paystack path is the active mobile deposit contract.
- Repository-local skills and a known LivelyCura implementation were chosen over improvised abstractions because the user repeatedly required structural fidelity.
- Gmail was restored when its removal exceeded the requested Resend transition.
- Rollbar was replaced by Sentry. Sending remains disabled without a DSN, default PII is disabled, and event data is redacted before transport.
- DigitalOcean-compatible wallet credential encryption uses exactly `WALLET_CREDENTIAL_ENCRYPTION_KEY` and `WALLET_CREDENTIAL_ACTIVE_KEY_VERSION`. The single-key design derives encryption/fingerprint subkeys and requires coordinated re-encryption for rotation; it is not an online key-ring system.
- Separate signup channel codes prove ownership of both registered contacts; sending one shared code to two channels would prove only that the registrant controls at least one channel.
- A resource-bound auth challenge (`userId + purpose + channel + resourceId`) permits multiple independent wallet challenges without allowing one flow to overwrite another. Deploying the new challenge index invalidates legacy pending OTPs because their delivery/resource scope cannot be reconstructed safely.
- CIS remains the established collective-investment portfolio implementation. Grow Wealth is a distinct linked-portfolio valuation flow with typed summary and detailed-report GraphQL contracts for existing customers only.
- Withdrawal OTP challenges bind to the persisted pending-withdrawal resource through `resourceId`. The request lifecycle is `PENDING_VERIFICATION` → `PROCESSING` → `SUBMITTED` or `FAILED`; clients never resend or alter the stored financial instruction during OTP completion.
- The fund catalog uses draft and published payloads on the same document because administrators need safe editorial isolation while customers need one stable current publication; omitting versions prevents accidental retention of superseded production facts.
- Hybrid RBAC keeps reusable role policy while allowing narrow per-user exceptions, and request-time resolution makes role disabling or admin-channel removal effective immediately.
- Notifications are stored rows plus a retry worker rather than inline sends, so provider outages never fail user writes and deliveries survive restarts (user choice, 2026-09-29).
- Marketing opt-out was kept after the user proposed removing it: without it, customers' only escape (blocking the SMS sender, reporting spam, disabling notifications) also stops OTPs, and Apple guideline 4.5.4, Act 843 section 40, and Gmail/Yahoo one-click rules expect it (2026-09-30).
- Email unsubscribe uses RFC 8058 one-click headers that post to the API itself, with no web page; a GET on the link never changes state because mail scanners open links.

## Verification Expectations

Respect the dirty working tree and run no destructive cleanup. For payment changes, run focused Paystack/deposit/webhook/reconciliation tests, BCL transaction tests, build, full Jest, then live sandbox initialization/verification/webhook replay with test credentials and configured portfolio subaccounts. Compile and statically inspect provider-setup scripts without executing them unless the user explicitly authorizes the live operation. Verify duplicate events, amount/currency/reference mismatch, BCL failure and reconciliation, tenant ownership, and notification non-atomicity. Run generation only with the local GraphQL server available; Codegen formats generated output through its post-write hook. Security/deployment work should use `yarn check`, Docker smoke checks, and staging validation without exposing credentials. Startup-order tests must prove migrations and index builds finish before readiness and that migration failure prevents listen/cron startup.

For notification changes, run the focused email/Hubtel/send-SMS tests, render the compiled email HTML, inspect light/dark presentation, then run `yarn run check`. Mocked Hubtel tests verify request construction and redaction only; staging delivery with real credentials remains a separate live-provider check.

For Hubtel status `100`, confirm that the deployment uses one active Messaging/SMS Client ID and Client Secret pair—not payment/checkout credentials or a mixed old/new pair—then restart the process and perform one controlled delivery. Do not reuse credentials that appeared in logs or chat.

For fund administration and access-control changes, verify permission unions/wildcards/ceilings, invitation expiry and replay, bootstrap idempotency, immediate revocation, draft isolation/publication/deletion, seed idempotency, customer field restrictions, BCL outage fallback, GraphQL generation, formatting, build, full Jest, and the production audit. For customer-support changes, verify principal ownership, internal-note isolation, permissions, idempotent writes, assignment eligibility, lifecycle transitions, audit metadata, GraphQL generation, formatting, build, and full Jest. For CIS/Grow Wealth or KYC boundary changes, run focused portfolio/account/KYC/schema tests, regenerate GraphQL bindings for schema changes, build, and run full Jest. For Grow Wealth, verify linked-portfolio resolution, valuation-date formatting, provider normalization, summary grouping, report details, principal-only arguments, explicit Shield policies, and the unlinked-customer empty state. For supervised KYC, cover submission claims, pending/approved/rejected outcomes, identity availability, stale responses, resubmission, and notification failure isolation.

## Evidence

- The direct user-approved 2026-09-28 Phase 1 plan and later LivelyCura naming correction establish hybrid RBAC, staff invitations/admin authentication, single-record draft/published fund facts, enriched customer CIS reads, and the three production PDF-derived seeds. Provenance: [[../sources/bora-fund-administration-access-control|Bora Fund Administration And Access Control]].
- Direct user direction on 2026-09-29 established live support subscriptions, WebSocket authentication parity with HTTP, the single-instance in-memory PubSub, the unwired functional change-stream fallback, and the no-classes code style. Build, formatting, focused tests with guard mutations, and 114 suites/598 tests passed; no live replica-set change stream was exercised. Provenance: [[../sources/bora-realtime-support-subscriptions|Bora Realtime Support Subscriptions]].
- Direct authorization to continue to the next roadmap phase plus the current implementation establish customer-owned support cases, an RBAC-protected staff queue, public replies, internal notes, assignment, priority, and explicit lifecycle actions. Provenance: [[../sources/bora-customer-support-administration|Bora Customer Support Administration]].

- Direct user clarification and the approved implementation plan on 2026-09-06 establish supervised KYC, profile-refresh status checks, corrected resubmission after rejection, the statement endpoint update, and continued linked-portfolio deferral. Provenance: [[../sources/bora-kyc-supervision-and-statement-update|Bora KYC Supervision And Statement Update]].

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
- Direct user correction plus live Bora/LivelyCura repository comparison on 2026-07-30 established the Tailwind email and Hubtel simple-SMS reference contracts. Bora verification passed 14 focused notification tests, compiled-template dark-mode rendering, build, formatting, 70 full suites/348 tests, and the production audit gate; live Hubtel staging delivery was not rerun from the local environment.
- User-supplied staging evidence on 2026-07-30 returned Hubtel HTTP 400/provider status `100` and demonstrated raw Axios serialization of the credential-bearing URL. The focused remediation retained the LivelyCura transport, replaced raw-error logging with allowlisted metadata, added an Axios-shaped no-secret/no-recipient/no-message regression, passed 17 focused notification tests, and passed `yarn run check` with 70 suites/348 tests plus the production audit gate. Provider-side rotation and successful staging delivery remain operator-owned.
- User-supplied local evidence on 2026-07-31 showed that the previously working request used `smsc.hubtel.com` while Bora called `sms.hubtel.com`, and that the two displayed requests loaded different Client IDs. A red-green endpoint regression corrected Bora to `smsc`; a second red-green regression removed temporary raw Axios console logging. Focused Hubtel tests passed and `yarn run check` passed with 70 suites/348 tests plus the production audit gate. A real delivery with rotated credentials remains operator-owned.
- User-supplied Gmail iOS screenshots on 2026-07-31 showed a coherent dark content panel but force-inverted header/footer light text against gradient-preserved navy, while Gmail's “view in light theme” rendered correctly. The focused repair added Gmail-only blend-mode targeting and wrappers without changing the ordinary light/dark palette. The regression was red before implementation, compiled HTML retained two wrapper pairs plus the Gmail selector, browser rendering showed no fallback black blocks, and `yarn run check` passed with 70 suites/349 tests plus the production audit gate. A post-deployment Gmail iOS delivery remains the final client proof.
- Direct user requirements plus current repository implementation on 2026-07-31 established canonical unique user contacts, separate dual-channel signup verification, phone/password plus email-OTP sign-in, challenge-ID resend, shared exponential cooldowns, immutable wallet destinations, and SMS ownership verification for pending mobile-money wallets. Fail-closed migrations preflight contact/mobile-wallet collisions and install resource-scoped challenge indexes before readiness. Fresh `yarn run check` passed formatting, TypeScript, 83 suites/396 tests, and the production audit gate; live provider delivery and deployment against production legacy data remain operator-owned checks.
- Direct user requirements, the supplied BCL endpoint document, and current repository implementation on 2026-08-28 established separate SIC/GrowWealth portfolio service ownership and bidirectional KYC image-field translation. Verification passed focused portfolio/account/KYC/schema coverage, TypeScript build, and full Jest at 89 suites/420 tests. The GrowWealth response fields and GraphQL contract remain intentionally open.
- Later direct user requirements on 2026-08-28 added email/phone-first existing-client linking with optional BCL identity ID and OTP-bound password creation without automatic login. A review correction retained exact frontend-supplied `+233…` phone lookup and removed premature GrowWealth GraphQL types/resolvers, leaving GrowWealth service-only and SIC explicitly named at GraphQL. Generation, formatting, TypeScript build, 73 focused tests, and full Jest passed at 91 suites/428 tests.
- Direct user requirements plus the supplied BCL valuation contract and portal reference on 2026-09-28 authorized typed Grow Wealth reads for existing linked customers. The backend now resolves linked portfolios before valuation, exposes separate grouped-summary and detailed-report queries, keeps all identity and portfolio selection server-owned, and leaves new-customer creation deferred.
- A direct withdrawal-contract correction on 2026-08-28 removed `transactionDate` from both public withdrawal inputs and their OTP context. The service now generates the current `YYYY-MM-DD` date for the BCL request after OTP verification. GraphQL generation, formatting, TypeScript build, 56 focused tests, and full Jest passed at 91 suites/428 tests.
- A follow-up withdrawal design correction on 2026-08-28 removed account, amount, and comment from the completion input as well. A dedicated pending-withdrawal model now stores the instruction once, the OTP challenge references it by `resourceId`, and completion accepts only `otpRequestId` plus `otp`. GraphQL generation, formatting, TypeScript build, focused coverage, and full Jest passed at 92 suites/430 tests.
- Direct user direction on 2026-09-29 and 2026-09-30 produced the notification inbox and worker, support notifications, marketing preferences, campaigns, email unsubscribe, and home-screen banners with LivelyCura-style uploads; see [[../sources/bora-notifications-marketing|Bora Notifications, Campaigns, And Banners]]. Final verification: 138 suites and 835 tests passing.
- Direct user direction on 2026-10-01 added server-backed biometric login and consolidated the frontend handoff into one app file and one admin file; see [[../sources/bora-biometric-login-and-handoff-docs|Bora Biometric Login And Consolidated Frontend Handoff]]. Verification: 140 suites and 857 tests passing.
- Direct user direction later on 2026-10-01 added `getMyPermissions`, added welcome, KYC, deposit, and withdrawal notifications to the customer inbox, and trimmed the app handoff to changes since the previous handoff; see [[../sources/bora-biometric-login-and-handoff-docs|Bora Biometric Login And Consolidated Frontend Handoff]]. Verification: 142 suites and 878 tests passing.
- Direct user direction later on 2026-10-01 put campaign SMS on hold behind `CAMPAIGN_SMS_ENABLED` while the user investigates Hubtel; see [[../sources/bora-notifications-marketing|Bora Notifications, Campaigns, And Banners]]. Verification: 142 suites and 888 tests passing.
- Direct user direction from 2026-10-19 to 2026-10-21 rebuilt push delivery around per-install, session-bound devices, client-bound sign-in codes, Expo receipt checks, and per-message retries, and replaced the welcome-back push with a new sign-in alert; see [[../sources/bora-push-device-binding|Bora Push Notifications Bound To Device And Session]]. Verification: 167 suites and 1124 tests passing; not run against a real MongoDB or Expo account.
- Direct user direction on 2026-10-11 set BCL `fetchdata` error passthrough, extended it to Grow Wealth, and barred reading `.env`. The shared `fetchBclData` and the authenticated `getCurrencies` (RequestID `Currency`) and `getCurrencyRates` (RequestID `CurrencyRate`) lookups were added; see [[../sources/bora-bcl-error-passthrough-and-secret-files|Bora BCL Error Passthrough And Secret-File Boundary]]. No live BCL call was made.

## Contradictions

- The Architecture section's startup description predates the current start script. On 2026-09-29, `yarn start` ran `dist/scripts/runMigrations.js` as a separate process before `dist/src/main.js`, and application `connectDB` used default Mongoose index options; re-verify the startup ordering before relying on the older description.
- Earlier supervision notes implied the helper accepted known provider approval/rejection strings. The user clarified on 2026-09-18 that those exact responses are unknown; the implementation and mocked tests are not provider confirmation.

- Historical explicit direction kept `userId` in protected deposit input because context could fail. Current GraphQL/mobile derive identity from the authenticated principal, and the current review skill recommends context-based scoping.
- Fidelity onboarding and API documents exist, but the current Fidelity payment boundary is empty; Paystack is the implemented deposit provider.
- Historical Oye verification expected a real default model and missing-key failure. The website-grounded implementation now applies the actual default when `OLLAMA_MODEL` is absent; missing provider configuration remains a separate runtime validation concern.
- Resend is the default and Gmail was preserved as requested, but similar string coercion weakens the current missing-key guard.
- Historical sessions reported passing builds/tests, but the current working tree contains extensive later uncommitted changes and was not re-tested during this read-only harvest.
- Repository skills contain some legacy/example naming and conventions that do not exactly match all live files; current code plus explicit user corrections outrank generic examples.
- The broad July 13 “high risk” audit is a historical snapshot; later remediation and current source repaired many findings.
- The auto-top-up lookup helper still supports an internal ownerless path when no user ID is supplied. Public GraphQL paths are scoped, but the helper is not universally fail-closed.
- The reviewed historical wallet design separated stable fingerprint material from rotating encryption keys; the current dirty working tree derives both from one scalar root and accepts only the active envelope version. Reconcile this material change before deployment.
- Temporary plaintext provider-credential compatibility and its migration remain incomplete; authentication challenge identifiers and shared adaptive throttling are now implemented in the dirty working tree.
- Likely historical JWT access/refresh, Rollbar, and Expo credentials require verified provider-side rotation and an explicit Git-history decision; values are intentionally excluded from the vault.
- Password reset currently revokes session records separately before password/legacy-token update, so full session-family revocation and password mutation are not one database transaction.
- Historical payment review required monotonic successful BCL finalization, but current `bclSync/finalizeDeposit.ts` updates by transaction ID without an exact expected processing/sync-state predicate.
- Startup-order tests now require awaited migrations and model index builds before readiness, replacing the prior unawaited post-listen behavior.
- Current source still contains unchanged caught-error rethrows despite the accepted one-deliberate-mapped-error-per-catch convention.
- `getAutoTopUpById` still permits an ownerless internal lookup fallback when identity is omitted, even though public paths are owner-scoped.
- Current logger/deposit/email boundaries still include an unredacted Winston path plus a `productions` typo, public client-supplied `depositCash`, and weak Resend missing-configuration/failure semantics.
- Sentry and wallet-encryption changes are present only in the dirty working tree, and the historical security plan is deleted locally despite remaining in `HEAD` history.
- The current dirty working tree replaces bulk result-order settlement mapping and startup provider migration with manual one-portfolio staging/production scripts. Live provider execution and recovery after a provider-success/local-write-failure boundary remain operator-owned checks.
- A later interpretation exposed Grow Wealth through a raw-`JSON` GraphQL query and added phone-format lookup variants. The user's review explicitly rejected both. The 2026-09-28 authorization supersedes only the service-only Grow Wealth boundary with typed existing-customer reads; raw JSON remains rejected, and frontend phone input remains canonical `+233…`.
- The intermediate withdrawal design required account, amount, and comment in both OTP request and completion so a hash could be recomputed. The persisted pending-withdrawal resource supersedes that duplication; completion now sends only the opaque OTP request ID and code.

## Confidence

High for current static architecture, explicit session corrections, and financial-flow ownership; medium for runtime/deployment status because the working tree is dirty and no commands or external integrations were executed.

## Open Questions

- Shield has no configured `fallbackError`, so denied GraphQL operations currently surface as `INTERNAL_SERVER_ERROR` and report to Sentry (verified 2026-09-29). Should denials return `UNAUTHORIZED`/`FORBIDDEN` instead?
- What exact BCL supervision descriptions represent approval and rejection? Only pending is confirmed; final-outcome mapping and live verification remain open.

- Deposit identity is currently principal-derived across backend and mobile; any reversal would require an explicit product/security decision and coordinated contract migration.
- Is Fidelity still planned beside Paystack, and has the exact collection/direct-debit capability been confirmed?
- Should Oye/Resend configuration validation be repaired without changing the user-selected module layout?
- When will the current security/runtime work be committed and revalidated as a reproducible release candidate?
- How will dedicated settlement-account uniqueness and stable portfolio mapping be enforced?
- What provider idempotency/reconciliation contract prevents duplicate subaccounts after partial failure and retry?
- Which BCL operations, eligibility rules, and account lifecycle will support Grow Wealth onboarding and portfolio creation for new customers?
- Which direction is the BCL `CurrencyRate` quoted in, and must rate requests match the customer's KYC currency? The user is asking BCL.
- Support attachments remain unscheduled; news stays out of the backend because the app scrapes Bora's website.
- Does Hubtel's `batch/simple/send` endpoint work on `smsc.hubtel.com`, and what is the production SMS rate limit? Campaign SMS stays on hold until the user answers this. Should transactional SMS be prioritized over marketing SMS in the queue?
- When will the welcome, sign-in, KYC, deposit, and withdrawal notifications move into the inbox? Deposit and withdrawal code needs explicit approval to touch.
