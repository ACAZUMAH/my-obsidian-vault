# Bora: the deposit and withdrawal work committed, and `scripts/deposits_production` made local-only

Date: 2026-11-22
Source: owner instructions in a Claude Code session on `bora-capital-backend` (branch `feature/updates`).

## The owner's instruction (verbatim)

> commit everything

## The owner's decision

The agent asked whether to include `scripts/deposits_production/`. The folder was untracked but not gitignored. It holds the owner's `inspectDeposit.ts` diagnostic, a README and pasted constants. Every other `*_production` scripts folder (`paystack_production`, `funds_production`, `admin_production`) is gitignored. The owner chose **"Gitignore it"**: add it to `.gitignore` like the other production folders and commit everything else.

## What was done

- `.gitignore` now lists `scripts/deposits_production`, after `scripts/admin_production`.
- Before the commit, the owner removed the `NEW_SIGNIN` enum description from `src/graphql/general/types.ts`, and `yarn generate` dropped its comment from the generated types.
- Checks before committing: `yarn format:check`, `yarn build` and `tsc` passed. The staged diff was scanned for secret patterns; the only matches were the fake `sk_test_key` in two Paystack tests.
- Commit `ca3cfa1`, `feat(transactions): deposit fee, reconciliation and withdrawal fixes`, on `feature/updates`: 177 files.
- The husky pre-commit hook ran the full suite (214 suites, 1,976 tests, all passed), and commitlint passed.
- The commit covers:
  - the go-live audit fixes;
  - A1, A2/A3, A6, B7, B8, B10, B11, B12, B14 and B15;
  - the `depositCash` removal;
  - the email-as-typed revert;
  - the paging and refund-wording fixes;
  - `docs/frontend-handoff-2026-11-22.md`.
- Not pushed.
