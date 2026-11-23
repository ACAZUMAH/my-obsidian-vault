# LivelyCura customer portal: scroll animations on Home

Date: 2026-11-09
Source: the owner's request in a Claude Code session on `livelycura-customer-portal`, plus the code built and checked in that session (paraphrased; the one quoted phrase is the owner's own words). The work is uncommitted on `feature/portal-ui` and awaits the owner's review.

## Request

After reviewing the rebuilt "Green Room" Home, and before moving to the next page, the owner said the redesign was meant to have nice animations and transitions too. They liked the animations already there and asked to keep them, and "we also add some scroll animations".

## What was built

Home keeps all of its existing motion (first-visit hero intro, header settle on scroll, hovers, cart panel, product photo morph, theme reveal, page cross-fades). It gains seven scroll-scrubbed moments, one fitted to each section rather than one fade-up repeated everywhere:

- Hero: as it scrolls away, the copy lifts a little faster than the page and fades slightly, the family photo sinks and grows inside its arch, and the lime plus winds a quarter turn.
- Why LivelyCura: the rounded photo window opens around the family while the photo holds its size; the kicker pill arrives as a forest dot holding the lime plus, which turns into place as the pill unrolls to show its words.
- Shop (the signature): each category tile comes up behind a forest door that rolls up through the tile, uncovering the photo; tiles side by side open left to right, and the tall first tile is the slow main door. Name plates and focus rings stay above the doors.
- Product rows: on the first three rows the packshots slide onto their tiles from the right; names, prices and buttons stay still.
- FAQ: the question rows dock into the list one by one.
- Footer, Home only, tablet and desktop: the big LivelyCura wordmark rises into place at the end of the page. Phones keep the static footer, because the wordmark is too small there for the rise to be seen.

Rules followed: text never moves on its own (only the hero copy, as the hero leaves); photos, panels and the lime plus carry the motion; the plus turns at two places only (hero and the Why kicker), so state indicators such as the FAQ toggles never spin; loading placeholders never animate.

## How it works

- Plain CSS scroll-driven animations (`animation-timeline: view()` with `animation-range`), no JavaScript and no animation library.
- Every rule sits inside `@supports (animation-timeline: view()) and (animation-range: entry 0% entry 100%)` and `@media screen and (prefers-reduced-motion: no-preference)`. Starting states live only inside keyframes with backwards fill, so browsers without support (Firefox today), reduced-motion users and print see the finished page.
- Elements inside an `overflow: hidden` or `auto` box read a timeline named on an ancestor, because such a box would otherwise capture `view()`. Home's wrapper must keep `overflow-x: clip`; `hidden` or `auto` would silently stop every scroll animation on the page.

## Lesson

A scroll-scrubbed reveal freezes part-way when the page loads with the element near the bottom of the window, and it stays that way until the visitor scrolls. The kicker pill first loaded with its label cut off ("Why LivelyC") at typical 1080p window heights. Its range was moved so that laptops and 1080p, 1200p and iMac windows load it as a dot and 1440p screens load it finished. Choose ranges so the first screen at common window heights never shows cut text.

## Verification at recording

Checked in Chrome 152 at phone, tablet and desktop sizes: every animation follows the scroll, nothing scrolls sideways, the page height never changes, the intro and the scroll layer coexist, and every scroll rule sits behind the reduced-motion gate. Type check, lint, formatting, 173 unit tests, the static build and the SSR build passed. Safari 26, Firefox and real Android phones were not run.
