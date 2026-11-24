# Bora: BCL enables production deposits and withdrawals, asks for our payout field names

Date: 2026-11-24
Source: the owner's message in a Claude Code session, with a pasted chat between the owner and BCL's team (paraphrased here without personal names), plus the agent's read-only mapping of the backend, app and BCL documents.

## The owner's words (verbatim)

> so the bcl has now allow both deposit and withdrawal on production, and concerning the withdrawal payout account selection by the customer, they asking us to send them the fields we will be passing when the customer request withdrawal and select an account for payout

## The chat with BCL (paraphrased, 2026-11-24)

- **Deposits:** they stay on the same endpoint the owner tested earlier.
- **Owner:** the customer must select where a withdrawal is paid, their Mobile Money wallet or bank account. This is in the flow document the owner sent BCL.
- **BCL:** asked whether the bank account will be in Flex (BCL's IMS), or whether Bora will provide fresh details.
- **Owner:** customers save wallet details in the app and select one when they transact, so BCL should add fields for Bora to pass at withdrawal.
- **BCL:** it would have been better if the details came from the IMS, but BCL will add the fields. BCL asked what Bora calls the fields, so the names can align.

## What the agent found (read-only, 2026-11-24)

**Withdrawal today**
- `requestWithdrawal` takes `accountNumber` (the BCL fund account), `amount` and `comment`.
- `addcicashwithdrawal_bcl` gets `PrimaryEmail`, `MobileNumber`, `AccountNumber`, `TransactionDate`, `Amount`, `Comment`. There is no payout field.
- The app's withdrawal flow has no "pay to" step, and the app sends `Comment` as the literal "Withdrawal".

**Bank wallets**
- The app sends the full account number. The backend keeps only `accountNumberLast4` (`createWallet.ts`), so no saved bank wallet can be paid out to today.
- `accountName` is the nickname the customer types in "Name"; it is not a verified holder name.
- `bankCode` is BCL's `BankCode` from `getBanks` (`fetchbanks`). It can be null, and BCL's API document lists only `BankID` and `BankName`. The app fetches `BankID` but does not send it, and the bank name is not stored.
- There is no ownership or name check.

**Mobile Money wallets**
- The full number is stored as `+233XXXXXXXXX` and verified by an SMS code sent to that number.
- `mobileNetwork` is free text. The app sends "MTN", "Vodafone" or "AirtelTigo".
- No registered name is captured.
- Mobile Money wallets saved from Paystack deposits skip the SMS check, keep Paystack's raw number, and carry Paystack's network value.

**BCL's records:** BCL's identity/KYC API holds no structured bank details, only the `imgBankProofString` image. So per-withdrawal payout fields are the only way to pass a destination.

**The flow document:** the document sent to BCL has one generic "Payout account" row. It also describes `Comment` as "The customer's note", while the app sends "Withdrawal".

## Agent's proposal (not yet approved by the owner)

Add these to `addcicashwithdrawal_bcl`, PascalCase like BCL's keys, keeping the existing six:

| Field | Bank account | Mobile Money |
| --- | --- | --- |
| `PayoutType` | `BANK` | `MOBILE_MONEY` |
| `PayoutAccountName` | account holder name | registered wallet name |
| `PayoutAccountNumber` | bank account number | wallet number, `+233XXXXXXXXX` |
| `PayoutBankID` | `BankID` from `fetchbanks` | empty |
| `PayoutBankName` | `BankName` from `fetchbanks` | empty |
| `PayoutNetwork` | empty | `MTN`, `TELECEL` or `AT` |

Questions for BCL:
1. Is `BankID` enough for a bank, or is a branch or sort code also needed?
2. Which network codes does BCL use?
3. Must the payout account be in the investor's name, and does BCL check it?
4. Is the `+233` format right for the wallet number?

**Bora-side work before any of this can be sent:**
- store the full bank account number, encrypted;
- capture a real holder name;
- store `BankID` and `BankName`;
- a fixed network list;
- decide whether Paystack-saved wallets can receive payouts;
- a snapshot of the destination on each withdrawal request;
- the app's "pay to" step.
