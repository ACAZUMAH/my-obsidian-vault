# Bora: deposit and withdrawal flow decisions, decided audit findings, and the approved fix backlog

Date: 2026-11-21 (covers owner statements from 2026-11-19 to 2026-11-21)
Source: direct statements by the user (repository owner) in one Claude Code session on `bora-capital-backend`. Sections 1–3 paraphrase the owner; section 4 quotes the owner's 2026-11-21 decision list verbatim. Repository facts in section 5 come from a read-only review on 2026-11-20/21 of the current backend working tree, the mobile app (`bora-frontend-mobile-app`) and the admin portal (`bora-admin-portal`), each area checked by one agent and re-checked by a second. No secret-bearing file was read. Customer account numbers and transaction references are omitted.

## 1. Owner decisions on the go-live security audit (2026-11-19 and 2026-11-20)

- Signup keeps ONE shared code sent to both email and SMS ("stick to one for all"). Separate codes add friction and, in the owner's view, do not stop an attacker who already controls one channel.
- Existing-investor account linking wrote the BCL identity onto an account before any code was checked. The owner called that a serious bug and approved the fix: the BCL identity is held on the code and linked only when the emailed code is used; the code goes to the email BCL holds; a BCL lookup is accepted only if the returned email and phone match what was asked.
- Signup checks BCL: if the email or phone already belongs to a BCL investor, signup stops and points the person to "Link your account". Reason: otherwise that person cannot create KYC later.
- GraphQL depth stays limited to 5. The owner's purpose for the depth limit is to stop deeply nested resolver queries. The `graphql-depth-limit` package was replaced by an in-house counter with the same rule plus size caps (query text, tokens, fields, repeats of one field, aliases, inline string length), and operations sent by GET are refused. KYC uploads are unaffected because images travel as variables and the 5 MB body limit stays.
- WebSocket messages are capped at 64 KB. Oye gets 10 messages a minute and 100 a day per customer, kept in the database, and a 2,000-character question cap.
- Code cooldowns: signup and sign-in share one bucket; the recovery codes (forgot-password and the existing-customer "Link your account" code) have their own bucket; withdrawal and mobile-wallet codes have NO cooldown, because they are signed-in actions.
- Sign-in stays at 5 attempts per phone number per 15 minutes, to stop SMS and email credit drain. The resulting "anyone who knows the phone number can lock sign-in" risk is accepted; no device-token redesign.
- Explanations must be plain; the owner rejected an overcomplicated explanation of the GraphQL change.

State at recording: everything in this section is implemented in the backend working tree and uncommitted. On 2026-11-20 the full suite passed (196 suites, 1,687 tests) and the build succeeded. The owner commits and deploys the backend themself, including the `depositCash` removal.

## 2. Owner decisions on deposits, withdrawals and the BCL flow document (2026-11-20)

- BCL told Bora that production deposits and withdrawals are not enabled for live accounts, and BCL's API team asked for Bora's deposit and withdrawal flow. Bora's own document described only the manual process. A GH¢1.00 production deposit from 16 Nov 2026 is waiting on BCL.
- The flow document sent to BCL describes only how the app handles deposits and withdrawals: the steps, who alerts the customer, and the fields sent. The owner rejected a first draft as noise: it must not tell Bora or BCL what to do, list Kusantec's own to-dos, mention NIA, limits, or "accept Paystack".
- Bora already accepts Paystack's confirmation as proof of payment; that is why Paystack is integrated.
- The customer bears the Paystack fee, not the fund and not Bora.
- Deposit alerts: after Bora confirms the payment with Paystack and before posting to BCL, Bora alerts the customer "payment received, awaiting confirmation". When the deposit is written to BCL, BCL alerts the customer that it is confirmed and when it will reflect on the portfolio. Bora sends no second alert.
- Withdrawal alerts: Bora alerts the customer that the withdrawal is initiated; BCL sends the confirmation and payment alerts.
- Where a withdrawal is paid is Bora's job: the customer selects a bank account or a Mobile Money wallet. The owner has asked BCL to add payout fields to `addcicashwithdrawal_bcl`; Bora builds its side when BCL adds them.
- Withdrawal limits are set by BCL; do not raise them.
- A custom API domain changes nothing about security; the owner keeps the DigitalOcean URL for now.

## 3. Operations (2026-11-21)

- The owner has added the live webhook URL in the Paystack dashboard.
- Before any production deploy after go-live, customers are told in advance about a planned update, and customer actions are blocked during that window.

## 4. Owner decisions on the verified open-issue list (2026-11-21, verbatim)

> A.
>
> 1. customer pays the fee
> 2. let's add that now the alert now going to payment  received and awaiting confirmation
> 3. bcl sends alert so no need for us alert them again
> 4. let's notify the frontend guy when we are writing our frontend hand over, if bcl accepts the transaction then it has gone through and they should have received an alert from bcl already so what do you wan the app to say??
> 5. I proposed this to bcl so let's wait, when they add those fields we will fix it
> 6. let's fix that
>
> B.
>
> 7. fix it
> 8. let's fix it
> 9. when we go live before we do a deploy we will alert the customers we are going to make a plan update so we won't even let them perform actions during that period I am not dumb
> 10. the admin should have a transactions section so see all transactions and the ones that needs reconcilation so let's work on those apis
> 11. let's fix it then, I have already added the webhook to paystack
> 12.  let's fix it
> 13. there is no way bcl will record a withdrawal and not answer back, so this findings doesn't hold it's  noise
> 14. any failed withdrawal message should go back to the frontend except the ones that are server errors
> 15. let's fix it then
> 16. it's all under mini statement / transactions so what do you mean they can see it
>
> C.
>
> 17. Leave it as it is, who do thing are the people verify customer kyc? it's same people and a customer can text them concerning their account and kyc don't you thing they go through and get back to the customer?
> 18. if the app is not showing it leave it as it is
> 19. what are you talking about, all the apis are protect and if you not logged in you request so what do you mean
> 20. skip it, that's not necessary
> 21. How, cus all the logs I have copied to you during error fixes the sensitive data's are not showing all some are stared out
> 22. we not using the docker so don't bring up anything about it.
> 23. they are supposed to only see that when the code they enter is wrong and our server checks the code not bcl

The numbered items answer this list (titles abbreviated):

- A1 the fund pays the Paystack fee; A2 no "payment received" alert; A3 Bora's duplicate "Deposit completed" alert; A4 the app's deposit result screen says "account has been credited"; A5 no payout destination on withdrawals; A6 withdrawal date sent as `YYYY-MM-DD`.
- B7 a deposit can be posted to BCL twice; B8 an auto top-up can charge the customer up to three times; B9 a deploy during a BCL post leaves a deposit stuck; B10 stuck deposits can only be closed by editing the database; B11 a lost webhook means a paid deposit is never posted; B12 BCL's reply is not saved, and short outages become manual cases; B13 BCL not answering a withdrawal; B14 BCL refusals sent with HTTP 200 lose their reason; B15 withdrawal amount format unchecked; B16 nobody can see withdrawal records.
- C17 support agents can read customers' KYC images through the API; C18 customers can read the support staff member's details through the API; C19 5 MB bodies parsed before any check; C20 Sentry quota from fake `Origin` requests; C21 log redaction; C22 development packages in the Docker image; C23 the app shows "That verification code is incorrect" when BCL refuses a withdrawal.
- Not answered on 2026-11-21: the admin portal's broken fund pages (navHistory, SetFundVisibility), the portal's missing fact-sheet PDF upload and journey editor, the withdrawal alert without "GHS", and the withdrawal code SMS not stating what it approves.

## 5. Verified repository facts behind the approved items (2026-11-21)

- A1: every Paystack charge sends `bearer: 'subaccount'` (`initializeDepositPayment.ts`, `processDueAutoTopUps.ts`, default in `services/payments/paystack/index.ts`), and production subaccounts are created with a 0% main-account share, so the fund pays the fee while BCL is told `transaction.amount`. Paystack has no API flag that makes the customer pay; Ghana's local fee is 1.95% (Paystack support article 2130306), and the dashboard pass-through is Nigeria-only. Proposed design: charge amount + `ceil(amount × r / (1 − r))`, use `bearer: 'account'` with `transaction_charge` equal to the surcharge so the subaccount settles exactly the deposit, keep `transaction.amount` as the deposit, compare Paystack's amount to the charged total in `applyPaystackStatus`, store Paystack's `fees`, apply the same to auto top-ups, and return amount, fee and total so the app shows them. Confirm settlement with one small live deposit.
- A2/A3: no alert is sent when Paystack success is claimed; `postDeposit.ts` passes `notify: false`; after BCL accepts, `syncSuccessfulDepositToBcl.ts` sends `DEPOSIT_SUCCESSFUL` "Deposit completed" by email, SMS, push and inbox. The atomic claim in `processSuccessfulDeposit.ts` lets exactly one caller win, so the new alert belongs right after a won claim and must not delay the BCL post.
- A4: the app's `deposit/success.tsx` shows "your investment account has been credited" for `SUCCESSFUL`. The app also invents `PROCESSING` when checkout, network or verification fails, so "payment received" copy must apply only when the server returns `PROCESSING`.
- A5: `RequestWithdrawal` has only `accountNumber`, `amount`, `comment`; Mobile Money wallets store the full number and are SMS-verified; bank wallets store only the last 4 digits and no holder name; BCL's withdrawal API has no payout field.
- A6: `verifyWithdrawal.ts` sends `dayjs().format('YYYY-MM-DD')`; deposits already send `DD MMM YYYY`.
- The app always sends the withdrawal `Comment` as the fixed word "Withdrawal" and has no note box; a blank comment would fail with a 500.
- B7: `applyPaystackStatus` writes a non-success status with the filter `status != SUCCESSFUL`, which also matches a claimed `PROCESSING` deposit, and the claim never checks `bclSync.status`, so the deposit can be claimed and posted again. Fix: a non-success answer may change only an unclaimed deposit; the claim requires `bclSync.status` not to exist (not `bclSync`, since `bclSync.attemptCount: 0` is created by default); finalize requires `PROCESSING` with `bclSync IN_PROGRESS`; `recordFailure` in auto top-ups gets the same guard.
- B8: a charge_authorization timeout, or any error after Paystack already returned success, reaches `recordFailure`, which marks it failed; the next 5-minute run charges again with a `-rN` reference, up to 3 times, while the first charge's webhook still posts to BCL. Fix: verify the previous reference with Paystack before charging again; treat unknown outcomes as unknown, not failed.
- B10: deposits in `RECONCILIATION_REQUIRED`, or left `PROCESSING` with `bclSync IN_PROGRESS`, cannot be closed without a database edit, and the hourly alert re-fires on them forever.
- B11: nothing re-checks `PENDING` or `ABANDONED` deposits with Paystack; auto top-ups rely on the webhook alone. A sweep is safe only after B7.
- B12: `transferCash` keeps only one line of text; BCL's HTTP status, `statusCode` and body are dropped; any error, including ones where the request never reached BCL (token failure, connection refused), goes straight to manual reconciliation.
- B14: a BCL refusal returned with HTTP 200 as `{"Message": ...}` is read as the generic "Failed to withdraw cash".
- B15: `amount` is a free string saved and posted to BCL unchanged; only the app cleans input.
- C23: after `verifyWithdrawal` consumes the code, a BCL refusal comes back as `BAD_REQUEST` with BCL's text; the app's `mapVerificationError` matches any message containing "invalid" (e.g. BCL's "Invalid Account Number") and shows "That verification code is incorrect".
- Checked and fine: the deposit `TransactionDate` already uses `DD MMM YYYY`; the "withdrawal request submitted" alert after BCL accepts already exists and nothing duplicates BCL's withdrawal alerts; all 91 mobile app GraphQL operations match the current backend schema.
