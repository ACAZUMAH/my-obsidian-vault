# C.E.Q.A Call Center: agent dashboard rebuilt as an analytics dashboard (2026-11-28)

- Date: 2026-11-28
- Author: the user, in a C.E.Q.A Claude Code session
- Recorded from: the user's message (quoted verbatim below), a multi-agent design panel (3 proposals, 2 judges, a spec and a schema feasibility check), a five-lens adversarial review, read-only agent-token probes, and browser checks in the real app shell
- Repository: `call-center-web-app`, `src/dashboard`
- Status when recorded: built and verified in the browser; not committed

## The user's words (verbatim)

- On the single-panel "My sales" page: "this is nice but we still not yet there, it's a dashboard and I want to see that analytics feel in it"

## Agent-readable data confirmed by probe

- `getTotalCallCenterAgentOrderSalesList` with `callCenterAgentId` and the fulfilled statuses returns per-branch rows that sum exactly to the agent's fulfilled total. Its list type spells the coupon field `totalCouponCashWorth`; the totals type spells it `totalcouponCashWorth`.
- The totals queries also take `pickup` and `paymentOption` (`CASH`, `CREDIT_CARD`, `MOBILE_PAYMENT`, `PMCM_WALLET`). Delivery plus pickup, and every status count, reconciled to the agent's orders.

## What was built

- The panel holds four KPI tiles (net sales, orders fulfilled, average order, not counted yet), each with a sparkline and a change chip. Under them is a "this period vs last" chart: a running total or per-bucket bars, a Now marker, totals in the legend, a pace sentence and the best bucket. Breakdown cards follow: sales by branch, delivery vs pickup, a payment donut with its table, and an order-status stacked bar. The support band and latest orders stay.
- Brand colour marks only the agent's own sales. Payment methods use a fixed palette (indigo, orange, grape, gray) and status uses ordinal teal plus gray, so a red tenant never collides with a category.
- Four aliased operations: summary 8, trend 2 per bucket, previous trend 1 per bucket every 5 minutes, breakdown 20. Trend buckets are capped at 31; custom ranges chart by day up to 31 days, by week up to 31 weeks, then by month. That is about 104 aggregations per minute per agent at worst.

## Review lessons (confirmed defects that were fixed)

- A running custom range must be compared with the same shift the chart uses: move both ends back by the range's day count, up to the same time of day. The first version compared this morning with yesterday evening.
- Say nothing about last period (pace sentence, svg description) until its line has loaded. Otherwise a slow or failed request reads as "no sales yesterday".
- When last month is longer than this month, fold its extra days into the last slot so the dashed line ends on the legend total.
- recharts 3 gives every chart svg `role="application"` and a tab stop. Pass `role: "img"` with a title and description, and keep a screen-reader table. Make sparklines and the donut `inert`.
- Leave `color` off Mantine reference lines so the label uses the chart text ink. On a vertical line, `insideTopLeft` draws the label to the right of the line.
- Use TanStack `onlineManager` and `query.isPaused` so going offline flips Live to Paused. Show skeletons when `isPending && fetchStatus !== "idle"`, not empty states.
- Cards inside responsive grids should switch layout with CSS container queries, not viewport breakpoints. The payment table was cut off from 768 to 1340px.
