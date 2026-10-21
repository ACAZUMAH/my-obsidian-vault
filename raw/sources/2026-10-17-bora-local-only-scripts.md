# Bora local-only operational scripts

Date: 2026-10-17
Source: The user's request to stop publishing newly gitignored folders, and the follow-up decisions.

## User request and decisions

The user added `scripts/bootstrap`, `scripts/paystack_staging`, `scripts/paystack_production`, and `scripts/seeds` to `.gitignore`: "I don't want them to go github again so remove them".

Committed tests imported those scripts, so a fresh checkout would fail CI (`yarn build` runs `tsc` over `src`, `tests`, and `scripts`, then `yarn test`). The user chose:

- Make the script tests local-only too: `tests/unit/scripts/bootstrapAdmin.spec.ts` and `tests/unit/scripts/seedFundCatalog.spec.ts` are gitignored and untracked.
- Give fund-service tests a synthetic fixture, `tests/fixtures/fundFacts.ts`, instead of importing the production seed catalog.
- Remove the `paystack:production:setup-balanced` package.json entry; run the script locally with ts-node.

## Implemented

- `git rm --cached` for the 12 script files and the 2 specs; local copies kept.
- A simulated fresh checkout (tracked plus new non-ignored files only) passed `tsc`, `format:check`, and 156 suites (1039 tests).
- No key-like strings were found in the untracked folders. The folders remain in 3 earlier commits on GitHub; untracking does not rewrite history.
