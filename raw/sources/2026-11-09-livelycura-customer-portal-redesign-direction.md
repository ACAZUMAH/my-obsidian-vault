# LivelyCura customer portal: redesign direction and approved Home plan

Date: 2026-11-09
Source: the owner's decisions in a Claude Code session on `livelycura-customer-portal`, relayed by that session for recording (paraphrased; the one quoted phrase is the owner's own words).

## Redesign started

The owner started a page-by-page restyle of the customer web portal (`livelycura-customer-portal`), Home first. The work is on branch `feature/portal-ui`, cut from `develop` at `72b656b`. Nothing merges until the owner says so.

## Correction: same colours, its own style

The website keeps the same colours as the customer mobile app, but its design style must be its own; the owner said keeping the colours "doesn't mean it should look exactly like the app". The app's glass controls, green fade hero and app layouts are not ported to the web.

## Motion

The portal gets a few big, smooth signature moments rather than a scroll-reveal on every section:

- a hero intro on first load;
- the header changing on scroll;
- the cart panel growing out of the cart button;
- the product photo flying from its card into the product page;
- the theme switch spreading out from the toggle;
- page cross-fades.

Reasons: most of the Ghana audience is on Android phones (about a quarter on Tecno, Infinix or itel); the crawler SSR copy is static HTML without JavaScript, so any reveal must enhance content that is already visible; and some users ask for reduced motion. No animation library is added for Home; the motion uses CSS plus the browser View Transitions API.

## Imagery

Free Unsplash stock photos are used for now, with real photos later. Some Unsplash "African" stock photos turned out to show Tanzanian signage (a "Tsh 500" price sign and a bus marked "...Salaam"). Lesson: check stock photos for foreign signage, and prefer real Kumasi photos.

## Direction probes and the owner's pick

Three high-fidelity HTML direction probes were built: A "The Dispensary", B "Green Room" and C "Daylight". The owner picked B, "Green Room":

- forest `#0B3D2A` hero and footer;
- bright green `#01CB7D` buttons with forest text, because white on `#01CB7D` fails contrast at 2.1:1;
- the logo's lime `#6FEC64` for accents;
- mint `#86E3BD` text on forest;
- pale mint sections;
- deep green `#007D4B` for green text on white;
- the Gabarito typeface, self-hosted as one variable font file of about 18 KB;
- the family photo in an arch;
- an oversized wordmark ending the footer;
- product rows that swipe on phones and sit four across from 1024px.

The probes live locally, outside the repositories, at `/Users/acazumah/Documents/LivelyCura/design-probes/portal-home`, served by the `portal-design-probes` configuration in `/Users/acazumah/Documents/LivelyCura/.claude/launch.json`.

## Approved Home plan

- The header, phone menu, footer, cart panel and shared product card are restyled with Home, because they show on every page of the branch.
- All Home content is kept.
- Approved additions: the five FAQ facts shown under "Why LivelyCura"; product names displayed in title case (the data is unchanged); and the product card's Add button becoming a minus, quantity and plus stepper with a short "Added to cart" message, instead of sliding the cart open on every add.
- Approved fixes bundled into the Home step: the header's "Get Care" linking to `/products`; the drawer title typo "LiveryCura"; the footer Home link doing a full page reload; footer account links without an `href`; missing labels and alt text; the cart badge showing 0; the cart drawer reopening after a reload because its opened flag is persisted; and brand-green contrast failures.
- Technical prerequisite: the router is rebuilt on every login-state change, so it must be created once before view transitions are added.
