---
type: project
status: active
created: 2026-07-21
updated: 2026-11-12
tags: [project, livelycura, customer, web, laboratory-results]
sources:
  - ../sources/livelycura-result-link-environments.md
  - ../sources/livelycura-project-knowledge-harvest-batch-1.md
  - ../sources/customer-portal-support-rendering-conventions.md
  - ../sources/livelycura-customer-portal-redesign-direction.md
confidence: high
---

# LivelyCura Customer Portal

## Summary

Responsive customer web portal for LivelyCura commerce, care, prescriptions, and secure laboratory-result access.

## Purpose

Supports product discovery, cart/checkout/payment, orders, prescriptions, settings, and Ghana-focused customer journeys. It also hosts a public OTP-gated finalized laboratory-report flow.

## Stack

- TypeScript, React 19, Vite 5.
- Mantine 9, Apollo Client, Redux Toolkit, React Router 6.
- Vitest, Storybook, GraphQL Codegen.
- Static client plus top-level crawler SSR package.
- Yarn is used by scripts, but an npm lockfile also exists.

## Architecture

The authenticated support center implements the marketplace customer side of [[../concepts/livelycura-customer-support-architecture|LivelyCura Customer Support Architecture]], while public phone, WhatsApp, and Instagram contact information remains visible before login. Support replies can reach registered browsers through strict case-thread deep links.

`src/app`, `providers`, `redux`, `router`, and `services` compose shared runtime. Customer domains live directly under `src`. `ssr/` is a separate crawler package.

The public `LabResultAccess` route is mounted before and outside `MainLayout`. The feature owns access state, phone and OTP forms, report presentation, explanation, and PDF generation.

## Folder Ownership

- `home`, `product(s)`, `cart`, `checkout`, `payment`, `user-order(s)`: commerce.
- `prescription(s)`, `get-care`, `labResult`: care and results.
- `authentication`, `settings`, `privacy`, `terms`: identity and trust.
- `components`, `layouts`, `hooks`, `helpers`, `services`: shared presentation/runtime.

## Commands

- `yarn start`
- `yarn generate`
- `yarn lint`, `yarn format:check`
- `yarn test`
- `yarn build`
- `yarn ssr`, `yarn build:ssr:local`
- `yarn storybook`

## Runtime/Deployment

Vite static application with Docker/Compose files and a separately buildable SSR package. No current GitHub workflow directory was found in this repository during the batch.

## Durable Conventions

- Current audience and copy are Ghana-focused.
- Extend the portal’s existing theme and interaction language; do not introduce an unrelated visual system. Exception: the owner-directed 2026-11-09 redesign below.
- Public flows may sit outside the authenticated app shell while retaining the product theme and their own task-explaining page header.
- Complex features own focused components, hooks, helpers, interfaces, and PDF code rather than one monolithic page.
- Use the existing `Conditional` component for conditional JSX rather than ternary/null rendering; keep optional child expressions safe. Support CSS belongs in `src/support/styles`. Preserve the user's accepted layout, and show the latest chat in support-history rows rather than the case number. See [[../sources/customer-portal-support-rendering-conventions|Customer Portal Support Rendering Conventions]].
- Redesign (owner decisions, 2026-11-09): restyle one page at a time, Home first, on `feature/portal-ui` (cut from `develop` at `72b656b`); nothing merges until the owner says so. Keep the [[../projects/livelycura-customer-mobile|customer app]]'s colours but give the web its own style: do not port the app's glass controls, green fade hero or app layouts. Direction "Green Room": forest `#0B3D2A` hero and footer, `#01CB7D` buttons with forest text (white fails contrast at 2.1:1), lime `#6FEC64` accents, mint `#86E3BD` text on forest, pale mint sections, `#007D4B` for green text on white, self-hosted Gabarito. Every page was built and approved by 2026-11-12 (Home through Privacy and Terms) and committed on `feature/portal-ui` as `fe03c61` on 2026-11-13, not yet merged; its optional shopper cancel reason needs the backend change to go live first. See [[../sources/livelycura-customer-portal-redesign-direction|Customer Portal Redesign Direction]].
- Products (approved 2026-11-11): keep the search term in browser history state, never in the URL (health searches must not reach analytics page addresses). Load 24 products per page with Show more. Name view-transition elements on the DOM and clear the names when the transition finishes; never use `unstable_useViewTransitionState` or `ScrollRestoration`, which throw under the SSR `StaticRouter`. The crawler copy renders the whole document in one React pass so head tags land in `<head>` (react-helmet-async 3 under React 19). See [[../sources/livelycura-customer-portal-redesign-direction|Customer Portal Redesign Direction]].
- Account pages (approved 2026-11-12): headings sit inside the account band through its head slot; support inbox rows show the latest chat plus the case number and status; never use coloured side-stripe borders; the shopper's cancel (`cancelMarketplaceOrder`) takes no note.
- Busy buttons show a small spinner beside their label (`src/components/green-room/ButtonSpinner.tsx`), never a sweeping bar; owner preference, 2026-11-11.
- Motion is a few big signature moments (hero intro, header change on scroll, cart panel growing out of the cart button, product photo flying into the product page, theme switch spreading from the toggle, page cross-fades), plus, since the owner's 2026-11-09 follow-up, one scroll-scrubbed moment fitted to each Home section (approved after review on 2026-11-10); never one fade-up repeated on every section. Use CSS (scroll-driven animations behind an `@supports` test and a `prefers-reduced-motion: no-preference` gate, starting states only in keyframes) and the View Transitions API, with no animation library for Home. Text does not move on its own. Reveals only enhance content that is already visible, since the crawler SSR copy has no JavaScript; reduced motion is respected; and the first screen at common window heights must not load a half-revealed label.
- Imagery is free Unsplash stock until real photos exist. Check stock for foreign signage (some "African" stock showed Tanzanian signs) and prefer real Kumasi photos.

## Constraints

- The public laboratory-result flow omits the main application header, not the page-level explanatory header.
- Online access uses the customer phone plus OTP before exposing a finalized report. An emailed PDF is a separate attached copy.
- Do not turn a generic OTP-request accepted response into an unconditional claim that an SMS was sent. Explain current-link and matching-number requirements and point to the newest result email/SMS because resending revokes earlier links. See [[../sources/livelycura-result-link-environments|Result Link Environments]].
- Internal AI findings and staff-only notes are not customer report content.
- Explanation failure must not block the report.
- View transitions need a router created once. As of 2026-11-09 `AppRouter` (`src/router/router.tsx`) rebuilds it on every login-state change, so that is fixed first.

## Decisions And Rationale

Laboratory results are accessible without a customer account because recipients arrive from a secure delivery link. The standalone route avoids authenticated-app chrome while preserving trust, facility identity, clear instructions, explanation, and PDF download.

The owner picked Green Room on 2026-11-09 from three high-fidelity HTML probes (A "The Dispensary", B "Green Room", C "Daylight"), kept locally outside the repositories at `/Users/acazumah/Documents/LivelyCura/design-probes/portal-home` (launch config `portal-design-probes`). Motion stays in a few moments because most of the Ghana audience uses Android phones (about a quarter Tecno, Infinix or itel), crawlers get static HTML without JavaScript, and some users ask for reduced motion. After reviewing the built Home, the owner asked to keep that motion and add scroll animations; each Home section got one fitted scroll moment, with the Shop tiles' rolling forest doors as the signature, in plain CSS so unsupported browsers (Firefox) and reduced-motion users see the finished page. The Home step also restyles the shared header, phone menu, footer, cart panel and product card because they show on every page. It keeps all Home content, adds only owner-approved items (FAQ facts under "Why LivelyCura", title-case product names for display, an Add stepper with an "Added to cart" message), and bundles the approved fixes listed in the Source Record.

## Verification Expectations

Run codegen, lint/format, Vitest, static build, and SSR build when relevant. Exercise phone, OTP, invalid/expired access, report, explanation retry, PDF download, responsive layout, and direct route loading.

## Evidence

- Current package, router, `src/labResult`, SSR package, Docker/Compose, and README.
- Sessions `019f61b7…` and `019f5cbd…` in [[../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]].
- Owner redesign decisions, 2026-11-09: [[../sources/livelycura-customer-portal-redesign-direction|LivelyCura Customer Portal Redesign Direction]].

## Contradictions

- Both `yarn.lock` and `package-lock.json` exist. Do not regenerate either casually; resolve package-manager ownership explicitly.
- README recommends Node 14 and describes a simpler Vite app, while current package versions and SSR/result features are newer.
- The convention to extend the existing theme predates the 2026-11-09 redesign. Green Room governs restyled pages on `feature/portal-ui`; `develop` keeps the existing look until the owner approves a merge. The existing brand greens (`#01CB7D`, `#007D4B`) carry over.

## Confidence

High for current architecture and laboratory-result decisions; medium for wider portal product positioning.

## Open Questions

- Should Yarn become the sole lockfile authority?
- Should current CI/deployment workflows be restored or documented elsewhere?
- When will real photos, ideally from Kumasi, replace the Unsplash stock?
