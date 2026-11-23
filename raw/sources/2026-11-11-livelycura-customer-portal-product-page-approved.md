# LivelyCura customer portal: product page built and approved

Date: 2026-11-11
Source: the owner's decisions and approval in the same Claude Code session on `livelycura-customer-portal`, plus the code built and checked there (paraphrased; quoted phrases are the owner's own words). The work is uncommitted on `feature/portal-ui`; the owner asked not to commit yet.

## Decisions

- After Products, the owner chose the single product page (`/products/:id/:name`) next ("Yes, product page"). They approved the plan and all five additions ("Yes, build it"):
  - A: Add to cart turns into the quantity stepper.
  - B: on phones, Share opens the phone's own share menu.
  - C: "This product is no longer available" with "Browse products" for removed or wrong links.
  - D: Try again on the error screen.
  - E: a sticky buy bar on phones.
- Asked for it, the agent built the page lean, directly in the session, with no multi-agent run. It took about 2.5 hours, after Products had taken most of a day.
- The owner spotted that in dark mode the footer's rounded top showed the page colour instead of the FAQ band colour. They asked that the band fill the curves, as on Home. After the fix they said "nice let's move to the next page".

## What was built

- A product hero in Home's hero composition.
  - From 768px: the name, short description, price (lime SAVE pill), Add to cart or Buy now, and Share sit on the forest band on the left. A large mint photo tile on the right steps out over the band's curved edge, with thumbnails below it.
  - On phones the photo comes first.
- Below the hero:
  - "About this product", with lime-plus bullets;
  - the app card;
  - the FAQs in Home's style, with "What's in the box" last.
- The gallery uses CSS scroll-snap instead of the Embla carousel.
- A product opened from a card is read from the Apollo cache at once with `readFragment`, so the photo morph always has a target.
- Motion: on a direct visit the photo tile rises in; a marker glides across the dots or thumbnails; the Share panel grows out of its button; the FAQs open smoothly; the buy bar slides up. Reduced motion makes all of it instant.
- Footer overlap: a page marks its last band with `data-lc-footer-band`, and the footer's top is pulled over it by `--lc-r-hero` via `:root:has()`. Home's wordmark rise stays Home-only.

## Verification at recording

- Type check, lint, 498 unit tests and the SSR package build passed.
- Checked in the browser at phone and desktop sizes, in light and dark, including a sample product with a description, FAQs and three photos. The not-found screen and the dark-mode footer corners were also checked.
- The motion was not watched by the agent, because the browser pane rendered no frames while hidden.
