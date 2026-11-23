# Bora: an empty exit-fee list means the fact sheet says Nil

Date: 2026-10-26
Source: Investigation of the dev `funds` collection export the user supplied, the admin portal's fact-sheet import code (`develop`), and the user's instruction.

## Findings

- The dev funds were seeded on 2026-10-01 with the 31 Jul 2026 sheets. On 2026-10-23 at about 21:15 UTC, all three were republished through the portal's fact-sheet import with the 30 Sep 2026 sheets. That is the day of portal commit `88655cc`, "fact sheet done".
- So the dev `totalAum` values are the 30 Sep "Fund Size" figures, not errors: Balanced 39,906,621.46, Fixed Income 18,455,211.28, Global Balanced 11,288,682.12. The seed skips existing funds, so re-seeding does not restore the July values.
- The import copies sheet text verbatim (for example "3 Year" and "≤ 1st year"). For "Redemption/Backload Fee Nil" it saves an empty `fees.redemption` list and shows "None (Nil)" in the review (`factSheetParser.ts` `parseTier`, `factSheetChanges.ts`).
- Bora's Balanced 30 Sep sheet labels its price "31ST AUG 2026 Unit Price (NAV per Unit) GH¢ 0.2603". Whether 0.2603 is the 30 Sep or the 31 Aug price is unconfirmed with Bora.

## User decision

An empty `redemptionFees` list means the sheet says Nil: the customer app shows "No exit fee" and never hides the block. A list whose tiers are all 0% means the same. The GraphQL description and section 3 of `docs/frontend-handoff-2026-10-24.md` were corrected, and the handoff examples now use the import's verbatim labels.
