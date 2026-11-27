# C.E.Q.A Call Center: agent dashboard shows the signed-in agent's own fulfilled sales, live (2026-11-27)

- Date: 2026-11-27
- Author: the user, relaying their manager's request, in a C.E.Q.A Claude Code session
- Recorded from: the user's messages (quoted verbatim below) and read-only GraphQL probes the session ran from the user's signed-in local agent session against the API that session targets
- Repository: `call-center-web-app`, branch `feature/orders-infinite-scroll`, `src/dashboard`
- Status when recorded: built and verified in the browser; not committed

## The user's words (verbatim)

- "we coming to work on the call center, to rework the dashboard, it's showing wrong info and doesn't display enough info. so the dashboard is supposed to display the info for just the callcenter agent logged in, the sales he made, net sales revenue, customer supports he made and any other info you think is okay to add to the dashboard."
- Manager's request, as relayed: "can we get call center agents to know their individual sales on this dashboard based on fulfilled orders live, just so they know how much they are selling"

## Why the old dashboard was wrong

- `getTotalCallCenterAgentOrders` and `getTotalCallCenterAgentOrderSales` return the active brand's orders, not the caller's (the repository's `docs/CALL_CENTER_ACCOUNT_API.md` §8.2 says so). The dashboard never passed `callCenterAgentId` or `status`, so it showed brand-wide totals including pending and cancelled orders.
- Its "Customer Orders/Sales" cards were brand-wide app orders. Every trend percentage, sparkline and the "Revenue Growth" chart were hard-coded dummy data.

## What the probes showed (agent token, read-only)

- `callCenterAgentId` is honoured on both totals queries for an agent: year-to-date the brand count was 102, the agent's own 64, the agent's fulfilled (`DELIVERED`, `COMPLETED`) 4.
- `allTime: true` sent with `lowerDate`/`upperDate` still respected the dates on the count query.
- `getCallCenterAgentSalesReport` and `getChatOperationsReport` answer 401 "Invalid credentials" for an agent: they are admin-only.
- `callCenterAgentGetAllCallCenterAgentOrders` (self-scoped) returns an empty list unless `allTime: true` or a date range is sent; it ignored `limit` (returned 20) and returned newest first.
- `getStaffChatQueue` for an agent: the default view is the brand's waiting support queue (split into mine/pool by `assignee.id`); `status: "CLOSED"` returns closed support chats with their `assignee`, so an agent's resolved chats can be counted client-side.
- Several aliased root fields in one GraphQL operation work, so one request can carry every dashboard total or every chart bucket.

## What was built

- Every figure is narrowed to the signed-in agent. A sale counts when the order is `DELIVERED` or `COMPLETED`. Net sales = `totalProductsCost` − `totalProductDiscount` − `totalcouponCashWorth` (pesewas).
- Cards: net sales, fulfilled orders, average order value (each against the same elapsed stretch one period back), and in-progress orders with their pending value. A chart of fulfilled net sales by hour/day/month, the agent's support chats (handling now, waiting, resolved in the period), orders taken by outcome, and the agent's latest orders.
- Live: totals refresh every 30 seconds and on window focus, chart and resolved chats every 60 seconds, with a "Live · updated" time and a manual refresh.
