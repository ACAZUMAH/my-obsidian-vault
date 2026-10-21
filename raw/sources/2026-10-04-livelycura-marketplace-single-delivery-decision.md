# LivelyCura Marketplace Single Delivery Decision

Date: 2026-10-04
Source: Direct user decision relaying the product owner's answer, plus follow-up answers in the same conversation

## Decision (user's words)

> Boss has gotten back so this what we going to do, we going to remove the split, multiple stops/routes, so routes and stuff like that because we are trying to simply things so we can lunch it and see how the usage goes and if there is the need to add the multiple stops we build it later. For marketplace orders attach a single delivery task to the market place order. bid orders should not have delivery attach it and facility can not dispatch delivery

## Follow-up answers

1. "No split" means one facility wins the whole marketplace order: a bid must cover every item and the cheapest full bid wins. The multi-winner (LLM/set-cover) award goes away; manual bids must cover every item.
2. LivelyCura pays the rider from the delivery fee the buyer prepaid. The winning facility is not billed or credit-checked for marketplace delivery.
3. The delivery task is created when the bid is accepted. The task's quote becomes the marketplace order's delivery fee, which is added to the item price before the buyer is notified to pay. Dispatch can also be done manually by LivelyCura Admin.
   - Clarified: the automatic rider network request goes out when the buyer's payment is confirmed (not at award), so riders are not tied up by unpaid orders. A rider can accept and wait for the order to become ready. If no rider accepts in the search window, it retries once automatically when the facility marks the order READY; after that, Admin dispatches.
4. Rider pickup moves the bid order to DELIVERING; drop-off moves the bid order to DELIVERED and the marketplace order to COMPLETED. Completing the bid order stays a manual facility step.
5. The winning facility sees the pickup code and rider name read-only on its bid order. Only the winner's staff may see it; it is never sent by SMS. Losing bidders must not see the buyer's contact or tracking.
6. A facility cannot cancel an awarded, paid bid. LivelyCura Admin gets a cancel-and-full-refund action.
7. After a failed delivery, Admin re-dispatches or cancels and refunds; LivelyCura absorbs failed-attempt fees. If a rider cancels (releases) the delivery, it re-dispatches automatically; if that fails, Admin handles it.
   - Clarified: a rider may release an accepted marketplace delivery only until the pickup code is verified. The same task is then offered to other riders automatically, excluding that rider.
8. There is no production data for this flow, so routes are removed in one pass without deprecation or migration staging.

## Design review answers (same day)

The user answered "go with your recommendation" to these:

1. "Cheapest" means the buyer's total: the bid price plus that facility's delivery quote.
2. Substitutes are removed from manual bids for launch.
3. The buyer has 60 minutes after the award to pay; then the order auto-cancels.
4. LivelyCura Admin confirms a parcel returned to the facility after a failed delivery.
5. The buyer may cancel until the rider picks up, including after payment, with an automatic full refund.
6. Bidding facilities see the distance, not the buyer's address; name, phone and tracking are hidden too.
7. Marketplace bid-order checkout always uses LivelyCura's payment account.
8. Delivery-fee accounting entries and a "parcel lost" action are deferred.
9. The user-account access hole (any signed-in user could read or edit other users) is fixed first as a separate change.
