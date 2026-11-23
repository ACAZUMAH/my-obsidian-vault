# Bora: the remaining fixes, and the 2026-11-22 handoff made ready to send

Date: 2026-11-22
Source: one Claude Code session on `bora-capital-backend` (branch `feature/updates`). Nothing was committed.

## The owner's instruction (verbatim)

> do all the fixes that's left once, and let me send the md to the frontend guy

## Fixes (uncommitted)

1. **Refunded goal top-ups use customer wording.** `markDepositRefunded` now writes `REFUNDED_CONTRIBUTION_REASON` ("Refunded to you. This top-up was not invested.") to the goal contribution, which the customer reads in the goal history. The staff-side deposit keeps `REFUNDED_FAILURE_REASON` ("Refunded to the customer; not booked at BCL"). No other customer path shows the deposit's reason; the customer `Transaction` type has no such field.
2. **`limit: null` gives the default page.** `getSanitizeLimit` now returns 15 for `null`, `undefined` and blank strings. Before, `Number(null)` was 0, which gave 1 row. The helper has about 22 callers, all of which benefit. The doc examples for `getSanitizePage` were wrong and are corrected.
3. **The `NEW_SIGNIN` schema description is back.** An earlier uncommitted edit had dropped "A sign-in to the account, sent to the account's other signed-in phones." from `src/graphql/general/types.ts`. It is restored and the types are regenerated.
4. **Wallet lists can report a next page.** The final review found that `getWallets` fetched exactly `limit` rows, so `hasNextPage` was never true. This was older code. It now fetches `limit + 1`, like every other list, and its doc gives the real default (15, at most 100). The app sends limit 100 and does not read `hasNextPage`.

**Not changed, by owner decision:**
- the Oye cap of 2,000 characters; the app fits its prompt to it (handoff section 4);
- emails kept exactly as typed, with exact lookups (handoff section 5).

**Still open from earlier:** the BCL client's 403 retry on its own sign-in request (raised 2026-11-21, undecided).

## Verification

- New tests:
  - `tests/unit/common/helpers/pagination.spec.ts`;
  - a wallet paging test in `wallets.spec.ts`;
  - an updated refund assertion in `depositReconciliationActions.spec.ts`.
- Mutation checks, each of which made tests fail with no type errors:
  - writing the staff text to the contribution again;
  - `null` no longer giving the default;
  - a blank string no longer giving the default;
  - wallets without the extra row.
- Full suite (214 suites, 1,975 tests before the wallet test), `tsc`, `yarn build` and Prettier pass.
- A final four-agent review (fixes, changed handoff parts, a whole-document read as the frontend developer, then a skeptic) confirmed 7 of 8 findings, all applied:
  - the wallet paging bug;
  - the page-helper doc examples;
  - the app tests that change with the email lowercasing;
  - the pending deposit card's `FAILED` wording applying to every `FAILED`, not only stored `PROCESSING` entries;
  - "expired" reasons showing the expired-code message;
  - `goal.targetDate` versus `targetSummary.targetDate`;
  - the rewrite-pattern count, 48 others.

## The handoff

`docs/frontend-handoff-2026-11-22.md` is complete and ready for the owner to send. Its sections:

1. the fee;
2. deposit result wording;
3. withdrawal refusals;
4. Oye limits;
5. emails kept exactly as typed;
6. the admin portal transactions APIs;
7. changes that need no client change, now including the refunded goal top-up wording and `limit: null`.

It ends with the side note.
