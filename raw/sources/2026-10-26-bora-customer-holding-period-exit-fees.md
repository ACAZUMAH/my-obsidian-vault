# Bora customers see the recommended holding period and exit fees

Date: 2026-10-26
Source: Direct user requirement on `bora-capital-backend` (`feature/updates`) after reviewing what customers see, plus the implemented change.

## Requirement

The user reviewed the funds against the 31 Jul 2026 fact sheets and found two things customers must know before investing that the app did not receive:

1. **Recommended holding period** ("very important").
2. **Redemption/backload (exit) fee:** what is charged on withdrawal within the first year, within the second year, and after that, in that order.

## Findings

- Both were already stored on every fund (`recommendedHoldingPeriod`, `fees.redemption` as `{ label, percentage }` tiers), editable in the admin portal, and seeded to match the PDFs:
  - Balanced: 3 years; 3% up to 1 year, 2% more than 1 and up to 2 years, 0% after 2 years.
  - Fixed Income: 1 year; one "All periods" 0% tier (the sheet says "Nil").
  - Global Balanced: 5 years; same tiers as Balanced.
- Only the customer read, `getCISFundDetails` / `CISFundDetails`, left them out.
- `totalAum` is the sheet's "Fund Size" line (assets under management). The seed values are exact: 40,187,947.68, 17,670,844.14, and 10,982,665.55.

## Decision and implementation

- `CISFundDetails` gains `recommendedHoldingPeriod: String` and `redemptionFees: [CustomerFundRedemptionFee!]!` (`{ label, percentage }`, in sheet order). The other fees (subscription, management, expense ratio) are not added; the user chose only these two.
- The tiers are display labels. They are not structured enough to compute "the fee if you withdraw today"; that would need stored year bounds per tier and a change to fee entry.
- The contract went into the unsent `docs/frontend-handoff-2026-10-24.md` as section 3 (customer app). The app shows both on the fund screen and before an investment is confirmed.
- Verification: build and full Jest at 172 suites and 1208 tests passing.
