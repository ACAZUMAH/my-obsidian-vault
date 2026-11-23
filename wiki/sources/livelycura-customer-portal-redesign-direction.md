---
type: source
status: active
created: 2026-11-09
updated: 2026-11-13
tags: [livelycura, customer-portal, design, redesign, home, products, motion, scroll-animation, seo, conventions]
sources:
  - ../../raw/sources/2026-11-09-livelycura-customer-portal-redesign-direction.md
  - ../../raw/sources/2026-11-09-livelycura-customer-portal-home-scroll-motion.md
  - ../../raw/sources/2026-11-10-livelycura-customer-portal-home-scroll-motion-approved.md
  - ../../raw/sources/2026-11-11-livelycura-customer-portal-products-page-approved.md
  - ../../raw/sources/2026-11-11-livelycura-customer-portal-product-page-approved.md
  - ../../raw/sources/2026-11-11-livelycura-customer-portal-checkout-flow-approved.md
  - ../../raw/sources/2026-11-12-livelycura-customer-portal-account-pages-approved.md
  - ../../raw/sources/2026-11-12-livelycura-customer-portal-get-care-approved.md
  - ../../raw/sources/2026-11-12-livelycura-customer-portal-login-approved.md
  - ../../raw/sources/2026-11-12-livelycura-customer-portal-policy-pages-approved.md
  - ../../raw/sources/2026-11-13-livelycura-customer-portal-cancel-reason-and-commit.md
source_date: 2026-11-09
ingested: 2026-11-09
confidence: high
---

# LivelyCura Customer Portal Redesign Direction

## Source

- Raw file: [LivelyCura customer portal: redesign direction and approved Home plan](../../raw/sources/2026-11-09-livelycura-customer-portal-redesign-direction.md)
- Raw file: [LivelyCura customer portal: scroll animations on Home](../../raw/sources/2026-11-09-livelycura-customer-portal-home-scroll-motion.md)
- Raw file: [LivelyCura customer portal: Home scroll animations approved](../../raw/sources/2026-11-10-livelycura-customer-portal-home-scroll-motion-approved.md)
- Raw file: [LivelyCura customer portal: Products page built and approved](../../raw/sources/2026-11-11-livelycura-customer-portal-products-page-approved.md)
- Raw file: [LivelyCura customer portal: product page built and approved](../../raw/sources/2026-11-11-livelycura-customer-portal-product-page-approved.md)
- Raw file: [LivelyCura customer portal: checkout flow built and approved](../../raw/sources/2026-11-11-livelycura-customer-portal-checkout-flow-approved.md)
- Raw file: [LivelyCura customer portal: account pages built and approved](../../raw/sources/2026-11-12-livelycura-customer-portal-account-pages-approved.md)
- Raw file: [LivelyCura customer portal: Get Care built and approved](../../raw/sources/2026-11-12-livelycura-customer-portal-get-care-approved.md)
- Raw file: [LivelyCura customer portal: Login page frame built and approved](../../raw/sources/2026-11-12-livelycura-customer-portal-login-approved.md)
- Raw file: [LivelyCura customer portal: Privacy and Terms pages built and approved](../../raw/sources/2026-11-12-livelycura-customer-portal-policy-pages-approved.md)
- Raw file: [LivelyCura customer portal: optional cancel reason, header fix, and the redesign commit](../../raw/sources/2026-11-13-livelycura-customer-portal-cancel-reason-and-commit.md)
- Date: 2026-11-09 to 2026-11-13
- Author: The owner (decisions, paraphrased), relayed by the implementing Claude Code session
- Ingested: 2026-11-09

## Core Claims

- The customer portal is restyled page by page, Home first, on `feature/portal-ui` (cut from `develop` at `72b656b`). Nothing merges until the owner says so.
- The web keeps the customer mobile app's colours but has its own design style; the owner said shared colours "doesn't mean it should look exactly like the app". The app's glass controls, green fade hero and app layouts are not ported to the web.
- The chosen direction is "Green Room" (probe B of three): forest `#0B3D2A` hero and footer, bright green `#01CB7D` buttons with forest text, logo lime `#6FEC64` accents, mint `#86E3BD` text on forest, pale mint sections, deep green `#007D4B` for green text on white, self-hosted Gabarito, the family photo in an arch, an oversized wordmark ending the footer, and product rows that swipe on phones and sit four across from 1024px.
- Motion is a few big, smooth signature moments, not scroll-reveal on every section: hero intro on first load, header change on scroll, cart panel growing out of the cart button, product photo flying from card into the product page, theme switch spreading from the toggle, and page cross-fades. It uses CSS and the browser View Transitions API; no animation library is added for Home.
- Refined later on 2026-11-09, after the owner reviewed the built Home: keep all existing motion and add scroll animations ("we also add some scroll animations"). Built as one scroll-scrubbed moment fitted to each section, not one fade-up repeated everywhere: the hero recedes, the Why photo window opens and its kicker pill unrolls, Shop tiles open behind forest doors rolling up left to right (the signature), the first three product rows slide their packshots in, FAQ rows dock, and the footer wordmark rises (Home only, tablet and desktop). Text never moves on its own except the hero copy as the hero leaves; the lime plus turns only at the hero and the Why kicker. The owner approved it after scrolling the built page on 2026-11-10 ("Looks right"), keeping the hero plus's turn; it is still uncommitted on `feature/portal-ui`.
- The Home step restyles the shared header, phone menu, footer, cart panel and product card (they show on every page of the branch), keeps all Home content, and adds only three approved items: the five FAQ facts under "Why LivelyCura", product names shown in title case (data unchanged), and a minus/quantity/plus stepper on the card with a short "Added to cart" message instead of sliding the cart open on every add.
- Imagery is free Unsplash stock until real photos exist. Check stock for foreign signage and prefer real Kumasi photos.

- Products (the list and category pages) was built second and approved by the owner on 2026-11-11 ("I checked everything it's okay"). It has a forest head with the trail, the category h1 and search; a sticky chip strip below 1024px and a sticky sidebar above; and two cards per row on phones. Approved additions: 24 products at a time with Show more, a result line with a clear-search button, an "All …" first category item, and rescue buttons with a forest-arch drawing on the empty and error screens. Each part has its own motion; the category switch with View Transitions is the signature. Uncommitted on `feature/portal-ui`; the owner said not to commit yet.
- The single product page was built third, lean and directly in the session, and approved on 2026-11-11 ("nice let's move to the next page"). It is a product hero in Home's hero composition: the buy box on the forest band, and a photo tile stepping out of the band's edge (photo first on phones). Below it: About, the app card and FAQs. Approved additions: the quantity stepper, the phone share menu, a "no longer available" screen, Try again, and a phone buy bar.
- The checkout flow (checkout, price-range checkout, payment result pages and the sign-in pop-up) was built fourth and accepted on 2026-11-11. The owner's feedback: busy buttons show a small spinner beside the label, never a sweeping bar ("I don't like the bar loaders on the button"); the line under Products' search box stays.
- The whole account area was built fifth and approved on 2026-11-12 ("Looks right"): the account frame with chip tabs and a head slot in the band, Dashboard, Orders, Prescriptions, Notifications, Support and Settings. Real bugs were fixed on the way: the order page's Pay button never showed, Cancel used the pharmacy's mutation, refill links led to an error page, and support-reply notifications could not be opened. The shopper's cancel takes no note, so the note field was removed; side-stripe accent borders are out ("it's an ai flop").
- Get Care was built sixth and approved on 2026-11-12 ("Looks right"): a forest head holding the three contact cards as links, the phone number shown, a call link that dials without a blank tab, and WhatsApp wording fixed.
- The Login page frame was built seventh and approved on 2026-11-12 ("Looks right"): a forest band with the sign-in card stepping out of its edge, and the sign-in messages in the forest toast.
- Privacy and Terms were built last and approved on 2026-11-12 ("Looks right"), completing the redesign. Both share one reading layout: a forest head, then a sticky mint "On this page" panel (no side line) beside a column of about 68 characters. Approved additions: "On this page" for Privacy from its own headings, and a lime marker that slides to the section being read. Privacy gained its tab title; the words on both pages are unchanged.
- Shopper cancel reason (2026-11-12, reversing the earlier "no note" call): optional, up to 500 characters, read only by LivelyCura. The backend's `cancelMarketplaceOrder` keeps `id` and gains an optional `data: { note }`, stored as `cancellation.note` (uncommitted on the backend's `feature/hrm`); the web dialog and the customer mobile app send it, and the app's Cancel was moved off the pharmacy's cancel. The backend must go live first: the clients' documents name the new input, so an old server rejects every cancel.
- Header doubling fix (2026-11-13): the old header's view-transition snapshot includes the settled layer's shadow (about 22px below the bar) and was drawn lower, showing its buttons under the new header; `::view-transition-old(lc-site-header)` is hidden.
- The whole redesign was committed on `feature/portal-ui` as `fe03c61` on 2026-11-13 (461 files), not pushed or merged.

## Useful Details

- Motion rationale: most of the Ghana audience is on Android phones (about a quarter Tecno, Infinix or itel); the crawler SSR copy is static HTML without JavaScript, so reveals may only enhance content that is already visible; and some users ask for reduced motion.
- Contrast: white on `#01CB7D` is 2.1:1, which is why bright-green buttons carry forest text and green text on white uses `#007D4B`. Gabarito ships as one self-hosted variable file of about 18 KB.
- Fixes bundled into the Home step: header "Get Care" linking to `/products`, the drawer title typo "LiveryCura", the footer Home link doing a full reload, footer account links without `href`, missing labels and alt text, the cart badge showing 0, the cart drawer reopening after reload (persisted opened flag), and brand-green contrast failures.
- Prerequisite for view transitions: the router is rebuilt on every login-state change and must be created once first. On `develop`, `AppRouter` in `src/router/router.tsx` calls `createBrowserRouter` during render and force-updates when the login state changes.
- Stock-photo lesson: some Unsplash "African" photos showed Tanzanian signage (a "Tsh 500" price sign, a "...Salaam" bus).
- Scroll mechanics: plain CSS scroll-driven animations (`animation-timeline: view()` with `animation-range`), no JavaScript or library. Every rule sits inside `@supports (animation-timeline: view()) and (animation-range: entry 0% entry 100%)` plus `@media screen and (prefers-reduced-motion: no-preference)`, with starting states only in keyframes (backwards fill), so Firefox, reduced motion and print show the finished page. Elements inside `overflow: hidden`/`auto` boxes read a timeline named on an ancestor, and Home's wrapper must keep `overflow-x: clip`.
- Products conventions: the search term lives in browser history state, never in the URL, so health searches stay out of analytics page addresses. Back restores the list's place and search for that history entry only. View-transition names are set on DOM elements and cleared when the transition finishes, never through `unstable_useViewTransitionState` or `ScrollRestoration`, which throw under the SSR `StaticRouter`.
- SSR head-tag fix (2026-11-11, affects every page): react-helmet-async 3 under React 19 renders head tags in place and leaves its server context empty. The crawler copy rendered the app to a string and placed it in `#root`, so every title, description, canonical, robots and og tag sat in `<body>`. It now renders the whole document (`ssr/app/Html.tsx` around the app) in one React pass after `getDataFromTree`, and React moves the tags into `<head>`; JSON-LD stays in the body.
- Product page conventions: a product opened from a card is read with `readFragment`, because Apollo cannot map `getMarketplaceProduct(id)` to the cached `MarketplaceProduct` without a type policy; the photo morph then always has a target. The gallery is CSS scroll-snap, not Embla. A page's last band can sit under the footer's rounded top by marking it `data-lc-footer-band`; only Home gets the wordmark rise.
- Scroll lesson: a scrubbed reveal freezes part-way when the page loads with the element near the bottom edge. The kicker pill first loaded with a cut label at 1080p window heights, so its range was moved; pick ranges so common window heights never load cut text.
- The probes (A "The Dispensary", B "Green Room", C "Daylight") are local HTML outside the repositories at `/Users/acazumah/Documents/LivelyCura/design-probes/portal-home`, served by the `portal-design-probes` entry in `/Users/acazumah/Documents/LivelyCura/.claude/launch.json`.
- Checked at ingest: `feature/portal-ui` exists and its merge-base with `develop` is `72b656b`; the probe folder holds the three probe pages; the launch entry exists; on `develop`, `MainHeader`'s "Get Care" uses `routeEndpoints.PRODUCTS`, `MainDrawer` is titled "LiveryCura", and `src/constants/theme.ts` already contains `#01CB7D` and `#007D4B`.

## Connections

- [[../projects/livelycura-customer-portal|LivelyCura Customer Portal]] carries the conventions.
- [[livelycura-customer-mobile-glass-home-direction|LivelyCura Customer Mobile Glass Home Direction]] is the app design whose colours the web shares but whose style it does not copy.
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]: its frontend rule to honour reduced-motion preferences for decorative transitions applies.

## Contradictions Or Tensions

- The first motion decision said "not scroll-reveal on every section"; the owner later asked for scroll animations too. Best interpretation (high confidence): the two agree, because each section gets its own fitted scroll moment rather than a uniform reveal, and the signature moments stay.
- The project page's older convention to extend the portal's existing theme rather than introduce an unrelated visual system predates this owner-directed restyle. Best interpretation (high confidence): Green Room governs restyled pages on `feature/portal-ui`, and `develop` keeps the existing look until the owner approves a merge. The existing brand greens carry over.

## Open Questions

- When will real photos, ideally from Kumasi, replace the Unsplash stock?
- When will the owner have the Privacy Policy text reviewed? It reads like an unfinished template: the definitions stop after three entries, the code keeps an "Add other definitions..." note, and its February 2025 date is older than the Terms (August 2026). The redesign kept its words unchanged.
- When will `feature/portal-ui` be pushed and merged? It is committed (`fe03c61`), and its cancel reason needs the backend change on `feature/hrm` to go live first.
- Backend follow-ups: refill orders are pharmacy orders that the shopper cannot see or pay for; shopper prescription edit permissions need an owner decision.
- Do later pages get their own scroll moments? Home has them; Products uses state and navigation motion instead, approved on 2026-11-11.
- The Products animations were not watched by the agent, because Chrome skips view transitions while the app window is hidden. The owner checked the page themselves.
