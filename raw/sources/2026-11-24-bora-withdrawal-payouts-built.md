# Bora: withdrawal payouts to a chosen bank account or Mobile Money wallet, built and pushed

Date: 2026-11-24
Source: owner answers and instruction in a Claude Code session on `bora-capital-backend`, plus the agent's production check of BCL's bank list. The change is commit `4310bb5` on `feature/updates`, pushed.

## The owner's words (verbatim)

> okay, let's but what you want us to build, but also make a production request to the bcl request to get banks and let's see if the returned banks has codes on production, if it does we can use the bank codes instead of ids, you should pull the mobile aps latest changes and so we can know stuff the frontend guy has done and we make an update we can just check and tell him what to do
>
> 1. let's check the production api first and if codes are there then we can go on with codes
> 2. what network codes are you talking about I don't get it
> 3. I am not sure about that, it can be, also it might also differ for e.g I can use Caleb Azumah on bora but bank is asakwin azumah or caleb asakwin it's still the same person, so I don't think we should do that check
> 4. yes, +233XXXXXXXXX is the right format
>
> so do it and let's build what is there to build and send the fields to them then push

## BCL's bank list (agent, read-only, 2026-11-24)

- **Production:** `POST /api/partner/fetchbanks` answers HTTP 201 with `{}` for every request (no filter, `BankID` 0, "", "0" or 1), and `GET` answers 405. Production BCL has no bank list.
- **Staging:** returns 55 banks with only `BankID` (a number) and `BankName`.
- **No `BankCode` exists in either.** The app's saved `bankCode` (from `getBanks.code`) has always been empty, so banks are identified by `BankID`.
- **The read-only script** is gitignored: `scripts/bcl_production/fetchBanks.ts`, using the `PROD_BCL_` values.

## Decisions

- **Banks:** identified by BCL's `BankID`, because there are no codes.
- **No name check:** payout accounts are never checked against the investor's name, and Bora sends BCL no payout account name.
- **Number format:** the Mobile Money wallet number is sent as `+233XXXXXXXXX`.
- **Network codes:** `MTN`, `TELECEL`, `AT`. The agent chose these and explained them to the owner. Vodafone Ghana is now Telecel and AirtelTigo is now AT, and the old names map to the new ones.

## Fields sent to BCL

`addcicashwithdrawal_bcl` keeps `PrimaryEmail`, `MobileNumber`, `AccountNumber`, `TransactionDate`, `Amount` and `Comment`, and adds:
- **Bank account:** `PayoutType` `BANK`, `PayoutAccountNumber`, `PayoutBankID` (number) and `PayoutBankName`.
- **Mobile Money:** `PayoutType` `MOBILE_MONEY`, `PayoutAccountNumber` (`+233XXXXXXXXX`) and `PayoutNetwork` (`MTN`, `TELECEL` or `AT`).
- Fields that don't apply to the type are not sent.

## Built (`4310bb5`)

**Bank wallets**
- They store the full account number in `accountNumberEncrypted` (`select: false`).
  - It uses the wallet-credential AES-GCM envelope with provider context `bank-account-number`, bound to the owner.
  - The number must be 6–20 digits; spaces and hyphens are removed.
- They store `bankId` and `bankName`, checked against `getBanks`.
- Older bank wallets keep only the last 4 digits, so `canReceivePayouts` is false and the customer adds them again.

**Mobile Money wallets**
- An unknown network is refused with "Choose MTN, Telecel or AT as the network".
- A removed number can be added back and verified again, instead of answering 409.

**`requestWithdrawal`**
- It takes an optional `walletId` and checks it before the code is sent.
- It stores `withdrawalRequest.payout`: wallet ID, type, last 4 digits, bank ID and name or network. The full number is never stored there.

**`verifyWithdrawal`**
- It re-reads the wallet, filtered by owner.
- A removed or changed wallet is refused before BCL is asked, and the request is marked FAILED.
- Only then does it decrypt the bank number and send the payout fields.

**`Wallet`** gains `bankId`, `bankName` and `canReceivePayouts`.

**Handoff:** `docs/frontend-handoff-2026-11-24-payouts.md`.
- **Release order:** backend first, then the app.
- Current builds cannot add a bank account, because they send no `bankId`. In production, BCL's empty list already blocks adding bank accounts.

**The app repository:** pulled to `origin/develop` `3438237`, merged with the owner's unpushed local commit; not pushed. Its wallet and withdrawal screens have no payout step yet.

## Verification

- **Full suite:** 218 suites, 2,085 tests. `tsc`, the build and Prettier pass.
- **Mutation checks:** 25, all caught by tests without type errors.
- **Independent review:** three lenses, each finding re-checked by a skeptic. 5 findings, 2 confirmed, both fixed:
  - the handoff's release order wrongly said current builds keep working;
  - a refused legacy Mobile Money wallet was told to "add it again", which a 409 blocked.
- **Rejected with evidence:**
  - BAD_GATEWAY on a payout decryption failure (the documented server-failure contract);
  - the ciphertext kept after a soft delete (same as card authorizations);
  - legacy unverified Mobile Money wallets.

## Still open

- BCL must load the production bank list.
- BCL must confirm that `BankID` is enough for a bank transfer, or say whether it needs a branch or sort code.
- BCL must add the payout fields.
