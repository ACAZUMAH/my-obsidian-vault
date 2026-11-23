# Bora A1: the customer pays the Paystack fee

Date: 2026-11-22
Source: one Claude Code session on `bora-capital-backend` (branch `feature/updates`).
- The owner decided on 2026-11-20 that the customer bears the Paystack fee, and approved A1 on 2026-11-21 ("customer pays the fee", in [the decision list](2026-11-21-bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md)).
- The owner answered "Yes, A1" when asked to move on to it.
- Nothing was committed.

## Owner decisions (2026-11-22, chosen on question cards)

- **When the fee starts: "On at deploy".** The other option was a switch turned on once the app build that shows fee and total ships. Testers on today's TestFlight builds will see a higher total at Paystack's checkout with no explanation until that build ships. The owner accepted this.
- **Card auto top-ups: "Yes, add the fee".** Every run charges the scheduled amount plus the fee, and the fund gets exactly the amount. This includes schedules created before the change.

## Facts checked before building

- **Rate.** Paystack Ghana charges 1.95% on local cards, Mobile Money, bank and international cards, with no cap or flat fee ([pricing](https://paystack.com/gh/pricing), [support table](https://support.paystack.com/en/articles/2130306)).
- **Split.** On a payment split with one subaccount, `bearer: 'account'` plus `transaction_charge` sends that amount to the main account, which pays Paystack's fee out of it; the subaccount gets the rest ([split docs](https://paystack.com/docs/v2/payments/split-payments/single-split)). Both checkout and saved-card charges accept it.
- **No Paystack shortcut.** Paystack's "pass fees to customers" setting can be turned on from the dashboard only in Nigeria.
- **Today's split.** Production subaccounts have a 0% main-account share and every charge sent `bearer: 'subaccount'`, so the fund paid the fee.
- **Mobile Money.** Mobile Money authorizations are not reusable, so Mobile Money "auto" top-ups are paid through the normal checkout from the reminder.

## Change (uncommitted)

- **One fee quote for every path.**
  - In pesewas: fee = ceil(deposit × 195 ÷ 9805) + 1, using integer arithmetic only.
  - The extra pesewa matches Paystack's own pass-fee formula.
  - Checked for every deposit from 1 to 2,000,000 pesewas: Bora's share is never below Paystack's fee rounded up, it is always above the exact 1.95% of the total, and the fund gets exactly the deposit.
  - Examples: GH¢50 is charged GH¢51.01, GH¢100 is charged GH¢102.00, and GH¢1,000 is charged GH¢1,019.90.
  - The deposit is rounded to whole pesewas, so what Bora stores, BCL books and Paystack charges always agree.
- **Checkout and goal top-ups.** Paystack is asked for the total, with `bearer: 'account'` and `transaction_charge` set to the fee. The deposit stores `feeInSubunit` and `chargedAmountInSubunit`. BCL is told the deposit, and goals are credited the deposit.
- **Card auto top-ups.** The charge has the same shape, through `charge_authorization`.
- **Paystack's amount check** compares with the charged total. Deposits from before the fee are still compared with their amount.
- **Paystack's fee** from its answer is kept in `payment.paystack.fees`.
- **For the app:**
  - the checkout and payment-check replies gain `amount`, `fee` and `total` (both nullable and additive, so old builds are unaffected);
  - a new query `getDepositFeeQuote(amount)` can show the fee before the customer confirms;
  - `AutoTopUp` gains `fee` and `total` per run.
- **For staff (admin portal):** `AdminDeposit.fee`, `AdminDeposit.totalCharged` and `DepositPaystackPayment.fees`.

## Verification

- Full suite (212 suites, 1,958 tests), `tsc`, `yarn build` and Prettier pass.
- **Request bodies.** Tests check what is sent to Paystack for checkout and saved-card charges.
- **End to end:**
  - a fee deposit is booked for exactly the deposit, BCL is told GH¢1,000 and Paystack's fee is kept;
  - a deposit charged only the deposit amount is refused.
- **Auto top-up shape:** the charge, the stored deposit and a contribution of the amount.
- **GraphQL:** the quote query and the auto top-up fee fields. That test caught a real wiring bug: the goals resolver merge dropped type maps, and it was fixed.
- 18 mutations made tests fail, all compiling. One survived at first, a wrong staff total; a test was added and it was re-run.
- An independent review raised 11 findings. 2 were confirmed (missing rounding tests, and inline field resolvers) and fixed; 9 were refuted.

## Owner steps and open items

- **Settlement check.** After deploy, confirm with one small live deposit that the fund's subaccount settles exactly the deposit and Bora's main account keeps the fee minus Paystack's. The tests cannot reach Paystack.
- **Frontend handoff** (when the owner asks):
  - show amount, fee and total on the deposit review screen, using `getDepositFeeQuote` or the checkout reply;
  - show fee and total on auto top-up setup and summary;
  - read the new fields on payment results;
  - keep "Total Investment" meaning the deposit, not what was paid.
- **Customer alerts** still show the deposit amount, not the fee or total paid.
- **Refunds** in the Paystack dashboard: Paystack keeps its fee. Who funds a refund of a split payment is not documented.
