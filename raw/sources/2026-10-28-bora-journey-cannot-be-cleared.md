# Bora: updateFund refuses to clear a stored journey since inception

Date: 2026-10-28
Source: Direct user decision on `bora-capital-backend`, plus the implemented change.

## Decision

The agent reported a gap: an explicit `null` or `[]` for `sinceInceptionJourney` in `updateFund` stored an empty journey, which silently erased the printed GH¢ amounts. The user approved making the backend refuse an explicit `null` or `[]` once a fund has a journey, testing it, and updating the 2026-10-28 frontend handoff to match.

## Implementation

- **The check.** `updateFund` (`src/services/funds/update.ts`) refuses with 400 when both of these hold:
  - the input carries the `sinceInceptionJourney` key, set to `null` or an empty list;
  - the fund's draft facts or published facts already hold a non-empty journey.
- **The message:** "The journey since inception cannot be cleared; send the amounts the fact sheet prints".
- **Other cases:**
  - Leaving the field out still keeps the stored journey.
  - A fund that has never had a journey may still save without one.
- **Schema.** The `FundFactsInput.sinceInceptionJourney` description now says that, once the fund has a journey, null or an empty list is refused. Types were regenerated.
- **Handoff.** The unsent `docs/frontend-handoff-2026-10-28.md` rule and error list were updated.
- **Verification.**
  - Build passes.
  - The full Jest suite (174 suites, 1326 tests) passes. It includes 8 new `fundDraftLifecycle` cases: refusal over a published journey, over a draft journey, and when only the published facts have one; omit keeps; replacement works; `null` and `[]` accepted for a fund without a journey.
  - After the schema description change: build, plus the fund and schema suites (29 suites, 236 tests).
