# Bora existing-customer account ownership

Date: 2026-10-12
Source: a review item (CAL-05) the user asked to verify, the agent's repository inspection, and the user's design proposal and approval ("go").

Finding: existing Bora clients could see their BCL accounts but could not use them. The account lists come live from BCL by `identityId` (`fetchciaccounts_bcl`). Deposits, transfers, withdrawals, goal creation, and transaction history and statements check `userOwnsAccount`, which only reads the local `portfolioAccountNumbers` list. Only `createCISPortfolioAccount` (an account opened in the app) ever filled that list. No CAL-05 fix existed in any local or remote branch, stash, or worktree.

The user proposed saving account numbers during existing-customer onboarding, so transactions need no BCL lookup. The agent noted that onboarding alone misses customers who had already onboarded and accounts opened outside the app later. It proposed also saving on every BCL account read, which costs no extra BCL call. The user approved.

Implemented:

- `rememberPortfolioAccountNumbers` ($addToSet with $each, trimmed and deduplicated, add-only, logs instead of throwing).
- Called from `getCISPortfolioAccounts`, `getCISPortfolioAccountsWithNav`, and `getCISPortfolioAccount` with the account numbers BCL returned for the user's identity.
- `completeExistingCustomerOnboarding` now uses `setPasswordWithCode`, which `resetPasswordWithCode` was split into so it returns the user, and then lists the customer's accounts. A BCL failure there is logged and does not fail onboarding.
- `userOwnsAccount` stays a local check. Accounts are never removed from the list; BCL still rejects transactions on closed accounts.
