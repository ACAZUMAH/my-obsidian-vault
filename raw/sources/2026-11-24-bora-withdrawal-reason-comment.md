# Bora: customers may give an optional reason for a withdrawal

Date: 2026-11-24
Source: the owner's message, with a screenshot of another Ghanaian investment app's withdrawal screen showing "What is this withdrawal for?" with Bills, Education and Transport. Plus the repository change in a Claude Code session on `bora-capital-backend`, `feature/updates`, on top of `4310bb5`. The change is uncommitted.

## The owner's words (verbatim)

> the request withdrawal input accepts comment input to so we should allow the frontend let the customer add their comments, for eg petra has it which they select what the withdrawal is for, but it's optional

## Decision

- The customer may say what a withdrawal is for. It is optional.
- The reason goes to BCL in `Comment`. This supersedes the 2026-11-21 note that `Comment` is always the literal "Withdrawal".

## Change (uncommitted)

**`requestWithdrawal.comment`** is now optional (`String`), up to 100 characters counted as characters, not UTF-16 units.

**`normalizeWithdrawalComment`** (`src/services/transactions/helpers/normalizeWithdrawalComment.ts`):
- collapses spaces and line breaks;
- stores and sends "Withdrawal" when the comment is left out or blank;
- refuses over 100 characters ("Keep the withdrawal note to 100 characters");
- refuses control characters.

It runs before the code is sent.

**Handoff:** `docs/frontend-handoff-2026-11-24-withdrawal-reasons.md`, a new file per the handoff rule.
- **App change:** an optional reason choice; send it as `comment`, or leave it out.
- **Release order:** backend first, because the previous backend requires `comment`.

**The BCL message:** the payout-field message drafted earlier the same day said `Comment` is always "Withdrawal". That line needs correcting with BCL.

## Verification

- **Full suite:** 219 suites, 2,099 tests. `tsc`, the build and Prettier pass.
- **Mutation checks:** 6, all caught.
- **Gotcha found:** a double quote escaped inside a GraphQL description in a TypeScript template literal (`\"`) becomes a bare quote. That breaks the schema string, and `yarn generate` quietly kept the old types. Use single quotes in schema descriptions.
