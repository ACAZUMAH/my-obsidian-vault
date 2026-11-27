---
type: source
status: active
created: 2026-11-27
updated: 2026-11-27
tags: [ceqa, call-center, dashboard, sales, graphql]
sources:
  - ../../raw/sources/2026-11-27-call-center-agent-dashboard-contract.md
---

# Call Center Agent Dashboard Contract

## Source

- Raw file: [2026-11-27-call-center-agent-dashboard-contract.md](../../raw/sources/2026-11-27-call-center-agent-dashboard-contract.md)
- Date: 2026-11-27
- Author: the user, relaying their manager's request; read-only probes from the user's local agent session
- Ingested: 2026-11-27

## Core Claims

- The Call Center dashboard shows only the signed-in agent's own figures, and a sale counts only once the order is fulfilled (`DELIVERED` or `COMPLETED`). It refreshes on its own ("live").
- The brand totals queries (`getTotalCallCenterAgentOrders`, `getTotalCallCenterAgentOrderSales`) return every agent's orders unless `callCenterAgentId` is passed; they honour it for an agent token. Omitting it was why the old dashboard showed wrong numbers.
- Net sales = products − product discounts − coupons, in pesewas; delivery fees are not sales.

## Useful Details

- `getCallCenterAgentSalesReport` and `getChatOperationsReport` are admin-only (401 for agents). Agent support figures come from `getStaffChatQueue`: mine/pool from the default view, resolved chats from `status: "CLOSED"` filtered by `assignee.id` and `updatedAt`.
- `callCenterAgentGetAllCallCenterAgentOrders` needs `allTime: true` or a date range, otherwise it returns nothing.
- Aliased root fields let one request carry all summary totals, or one sales total per chart bucket.

## Connections

- [[../projects/call-center-web-app|Call Center Web App]]

## Contradictions Or Tensions

- None with existing pages. The project page's old `src/dashboard` description ("sales/order metrics and date filters") is superseded.

## Open Questions

- Should the backend add a self-scoped agent chat-stats read? The resolved-chat count pages the brand's closed queue (four pages of 50) and shows a "+" floor when that runs out.
- Totals filter by order creation date, so an order placed yesterday and delivered today counts on yesterday.
