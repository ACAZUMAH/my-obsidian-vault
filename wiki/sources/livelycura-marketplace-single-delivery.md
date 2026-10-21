---
type: source
status: active
created: 2026-10-04
updated: 2026-10-06
tags: [livelycura, marketplace, courier, delivery, decision]
sources:
  - ../../raw/sources/2026-10-06-livelycura-courier-cleanup-decisions.md
  - ../../raw/sources/2026-10-04-livelycura-marketplace-single-delivery-decision.md
confidence: high
---

# LivelyCura Marketplace Single Delivery

## Source

- Raw file: [Marketplace single delivery decision](../../raw/sources/2026-10-04-livelycura-marketplace-single-delivery-decision.md)
- Date: 2026-10-04
- Author: User, relaying the product owner's decision
- Ingested: 2026-10-04

## Core Claims

- Launch scope removes split fulfillment and every multi-stop courier route: parent/child tasks, manual multi-pickup routes, and grouped marketplace routes. Multi-stop may be rebuilt later if usage needs it.
- One facility wins a whole marketplace order. Bids must cover every item; the cheapest full bid wins.
- A marketplace order owns exactly one delivery task. Bid orders carry no delivery task, and facilities cannot dispatch, re-dispatch, or manually move marketplace delivery statuses.
- The task is created at award. Its quote is the marketplace order's delivery fee, added before the buyer is asked to pay.
- LivelyCura pays the rider from the buyer's prepaid delivery fee; the winning facility is never billed or credit-checked for it.
- The automatic rider request goes out when the buyer's payment is confirmed. One automatic retry runs when the facility marks the order READY; after that, LivelyCura Admin dispatches manually.
- A rider may release an accepted marketplace delivery until pickup is verified; it is then automatically re-offered to other riders. Re-dispatch reuses the same task, so the paid fee never changes.
- Rider pickup moves the bid order to DELIVERING. Drop-off moves the bid order to DELIVERED and the marketplace order to COMPLETED. Bid completion stays a manual facility step.
- Only the winning facility's staff see the pickup code and rider name, read-only on the bid order. Pickup codes are never sent by SMS. Losing bidders cannot read the buyer's contact or tracking.
- Facilities cannot cancel an awarded, paid bid. Admin owns cancel-with-full-refund and failed-delivery handling; LivelyCura absorbs failed-attempt fees.
- The award ranks full-coverage bids by the buyer's total (bid price plus that facility's delivery quote). Manual-bid substitutes are removed for launch.
- The buyer has 60 minutes after award to pay before the order auto-cancels, and may cancel with a full refund until the rider picks up.
- After a failed delivery the parcel returns to the facility on the same task; Admin confirms the return before re-dispatch or refund.
- Bidding facilities see only the distance, never the buyer's address, name, phone, or tracking. Bid-order checkout always uses LivelyCura's payment account.
- Follow-up decisions (2026-10-06): customers cancel their own non-marketplace orders only while PLACED or ACCEPTED, while marketplace buyers keep cancel-until-pickup; a delivery cancelled during preparation is replaced immediately and re-offered to riders automatically if one was already requested or assigned; customers receive the tracking link by SMS at pickup, and the public tracking page shows status, timeline and ETA only. Source: [2026-10-06 decisions](../../raw/sources/2026-10-06-livelycura-courier-cleanup-decisions.md).

## Useful Details

- No production data exists for marketplace delivery or courier routes, so removal happens in one pass without deprecated GraphQL fields or migrations beyond development-data cleanup.
- Before the decision, every marketplace delivery side effect rode on the bid order's task (`task.orderId`, `Order.deliveryTaskId`). Moving the task to the marketplace order requires marketplace-specific pickup, drop-off, cancel, failed-attempt, and payer paths.
- Nothing pays facilities for marketplace items yet; that gap predates this decision and is outside its scope.

## Connections

- [[../projects/livelycura-backend|LivelyCura Backend]]
- [[../projects/livelycura-admin-portal|LivelyCura Admin Portal]]
- [[../projects/livelycura-courier-mobile|LivelyCura Courier Mobile]]
- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]]
- [[../projects/serlp-mobile|SERLP Mobile]]
- [[livelycura-independent-fleet-and-platform-dispatch|LivelyCura Independent Fleet And Platform Dispatch]]

## Contradictions Or Tensions

- Supersedes the multi-pickup route design: one courier handling several pickup stops, per-business grouped marketplace routes, and the earlier proposal of one parent task with child stops per marketplace order.
- Supersedes split marketplace fulfillment, where several facilities could each win part of an order.

## Open Questions

- How are facilities paid for marketplace items?
- Delivery-fee accounting entries and a "parcel lost" action are deferred; when should they be built?
