# LivelyCura customer portal: Get Care built and approved

Date: 2026-11-12
Source: the owner's decisions and approval in the same Claude Code session on `livelycura-customer-portal`, plus the code built and checked there (paraphrased; quoted phrases are the owner's own words). The work is uncommitted on `feature/portal-ui`.

## Decisions

- The owner chose Get Care next ("Get Care") and approved the plan with both additions ("Yes, build it"):
  - A: show the phone number "+233 55 774 3430" on the Call card.
  - B: wording fixes: "WhatsApp", "Talk to us on WhatsApp", "Talk to us on Instagram", "Chat on WhatsApp".
- After checking the built page the owner said "Looks right".

## What was built

- A forest head under the header with the h1 "Get Care", the lime plus and the lead sentence.
- The three ways to reach the care team (Call us, WhatsApp, Instagram) are forest cards inside the band. Each card is itself the link.
- The call link dials directly. Before, it used `target="_blank"` on a `tel:` link and opened a blank tab first.
- Signed out: a mint "Track a support request" panel with "Sign in for support". Signed in: the redesigned support centre.
- Motion: the icon circles fill lime once on load, and the cards lift on mouse hover.

## Verification at recording

Type check, lint, 584 unit tests and the SSR build passed. Checked in the browser at desktop and phone sizes.
