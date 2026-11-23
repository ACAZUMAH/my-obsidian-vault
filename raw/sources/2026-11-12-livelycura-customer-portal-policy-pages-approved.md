# LivelyCura customer portal: Privacy and Terms pages built and approved

Date: 2026-11-12
Source: the owner's decisions and approval in the same Claude Code session on `livelycura-customer-portal`, plus the code built and checked there (paraphrased; quoted phrases are the owner's own words). The work is uncommitted on `feature/portal-ui`.

## Decisions

- The owner asked for the Privacy and Terms pages to be planned together ("Yes, plan them") and approved the plan with both additions ("Yes, build it"):
  - **A.** An "On this page" panel for Privacy, listing its main sections using its own headings (no new words).
  - **B.** A lime marker in "On this page" that slides to the section being read, on both pages.
- After checking the built pages, the owner said "Looks right".

## What was built

- **One shared layout for both pages:** a forest head under the header (kicker where the page had one, the heading with the lime plus, the intro, and the "Last updated" line), then "On this page" beside a reading column of about 68 characters.
- **"On this page":** a light mint panel with no side line. It stays beside the text on computers and sits as a card above the text on phones. Tapping a link scrolls there smoothly (a jump under reduced motion), moves focus to the section and updates the address bar.
- **Terms:** the thin grey line down the side of its section list was removed. Every word kept.
- **Privacy:** a tab title, "Privacy Policy", with its own intro sentence as the search description. Space was added above each section heading, because its sections have no dividing lines. Every word kept.

## Left for the owner

- The Privacy Policy text reads like an unfinished template: its definitions list stops after three entries, the code keeps a leftover "Add other definitions..." note, and its date (February 2025) is older than the Terms (August 2026). Not changed, because it is legal text; it needs a legal review.

## Verification at recording

Type check, 584 unit tests, lint on the changed files, and the SSR build passed. Checked in the browser at desktop and phone sizes, in light and dark.

## Status

With this approval every page in the redesign has been built and approved: Home, Products, the product page, the checkout flow, the account area, Get Care, the Login frame, and Privacy and Terms. All of it is still uncommitted on `feature/portal-ui`.
