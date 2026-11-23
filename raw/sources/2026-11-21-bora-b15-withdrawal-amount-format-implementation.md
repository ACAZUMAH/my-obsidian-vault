# Bora B15: withdrawal amount format checked on the server

Date: 2026-11-21
Source: one Claude Code session on `bora-capital-backend` (branch `feature/updates`). The owner approved B15 on 2026-11-21 ("let's fix it then", in [the decision list](2026-11-21-bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md)). The item as written: the server did not check the withdrawal amount's format, so a direct API call could send `-500`, `1e9` or `1,000` straight to BCL; the check is about the format only, and the limits stay with BCL. The owner later answered "Yes, B15" when asked whether to move on to it. Nothing was committed.

## Change (uncommitted)

- New `src/services/transactions/helpers/validateWithdrawalAmount.ts`, exported from the helpers barrel.
  - It accepts only `^(?:0|[1-9]\d*)(?:\.\d{1,2})?$` with a value greater than zero, such as "500", "500.5", "500.50" or "0.01".
  - Anything else is a 400 "Withdrawal amount must be a number greater than zero with up to two decimal places, such as 500 or 500.50".
  - It does not check how much may be withdrawn; that limit is BCL's.
- `requestWithdrawal.ts` calls it first, before the user lookup, the code cooldown, the withdrawal record, the code and the SMS. The stored amount is unchanged, so BCL gets exactly what was checked. The owner's own uncommitted change in that file (`reserveAuthRequest(user._id, OtpPurpose.WITHDRAWAL)`) was kept.

## Verification

- `requestWithdrawalOtp.spec.ts` covers the accepted shapes, and refuses 14 bad shapes (`-500`, `1e9`, `1e+21`, `1,000`, `0`, `0.00`, `500.123`, `500.`, `.5`, `0500`, `+500`, spaces, words, empty) before anything is saved or sent.
- Full suite (200 suites, 1,770 tests), `yarn build` and Prettier pass.
- Five mutations made tests fail with no type errors:
  - the check removed;
  - zero allowed;
  - any number of decimals;
  - leading zeros allowed;
  - the check moved after the user lookup.
- One independent checker found no defects.
  - The customer app always sends `String(Number(cleaned input))`. Its input keeps only digits and one point with at most two decimals. 22.4M typed values and 2M random values were run, and none below 1e21 are rejected; the app's balance check blocks anything that large.
  - No other path creates withdrawal requests or sends amounts to BCL.
  - The error reaches the app as BAD_REQUEST, and the app shows it as "Withdrawal Failed".
  - No app change or handoff is needed.

## Side notes (not B15)

- App: on a keyboard that uses a decimal comma, typing "500,50" becomes "50050". The amount field and the confirm screen both show 50,050, so the customer sees it before confirming. This is an older app input issue.
- Any future "withdraw all" must round the balance down to two decimals before sending.
