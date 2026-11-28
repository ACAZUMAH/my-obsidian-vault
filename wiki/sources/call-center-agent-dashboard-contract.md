---
type: source
status: active
created: 2026-11-27
updated: 2026-11-28
tags: [ceqa, call-center, dashboard, sales, graphql, charts]
sources:
  - ../../raw/sources/2026-11-27-call-center-agent-dashboard-contract.md
  - ../../raw/sources/2026-11-28-call-center-agent-dashboard-ui.md
  - ../../raw/sources/2026-11-28-call-center-agent-dashboard-analytics.md
  - ../../raw/sources/2026-11-28-call-center-agent-dashboard-bento.md
---

# Call Center Agent Dashboard Contract

## Source

- Raw file: [2026-11-27-call-center-agent-dashboard-contract.md](../../raw/sources/2026-11-27-call-center-agent-dashboard-contract.md)
- Raw file: [2026-11-28-call-center-agent-dashboard-ui.md](../../raw/sources/2026-11-28-call-center-agent-dashboard-ui.md) (UI rework after the user's "this is okay but improve the ui")
- Raw file: [2026-11-28-call-center-agent-dashboard-analytics.md](../../raw/sources/2026-11-28-call-center-agent-dashboard-analytics.md) (analytics rebuild after "I want to see that analytics feel in it")
- Raw file: [2026-11-28-call-center-agent-dashboard-bento.md](../../raw/sources/2026-11-28-call-center-agent-dashboard-bento.md) (bento rearrangement from the user's inspiration shots; refresh button removed)
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

- UI (2026-11-28): one "My sales" panel in the Customers page shell, with one dominant net-sales figure and its change in cedis (no % deltas), the not-counted amount beside it, then a support band and the latest orders. A failed poll keeps the last numbers and flips the Live badge to Paused instead of replacing panels with errors.
- Mantine 7.17 BarChart on recharts 3.8.1: don't enable `barProps.isAnimationActive` (bars stay unpainted); use `gridProps={{ yAxisId: "left", syncWithTicks: true }}` for one hairline per tick; set `--chart-text-color` through a className with `light-dark(gray-7, dark-1)`, because ticks otherwise fall back to dimmed.

- Analytics (2026-11-28, supersedes the single-panel UI): KPI tiles with sparklines and % chips, a this-period-vs-last chart (running total or per bucket, Now marker, pace sentence), and cards for branch, delivery vs pickup, payment and order status. Brand colour marks only the agent's own sales; payment and status use fixed palettes. Agent tokens can read the per-branch list and the `pickup`/`paymentOption` filters; the list type spells it `totalCouponCashWorth`.
- Chart and state lessons from review: running custom ranges compare with the same day-count shift up to the same time; nothing is said about last period until its line loads; a longer previous month folds into the last slot; recharts 3 svgs need `role: "img"` (sparklines and the donut `inert`); Mantine reference lines take no `color`; TanStack `onlineManager` plus `isPaused` drive Paused; cards in grids switch layout with container queries.

- Layout (2026-11-28, supersedes the single panel): a greeting header with the period buttons on the right and no refresh button, then a bento grid of separate cards placed by `grid-template-areas` (three columns from 75em, two on tablets, one on phones, DOM in phone reading order). Every card shares one heading: icon, title, subtitle, control. Balance the rows a spanning card covers: order status runs full width so the three breakdown cards stack level with the latest-orders table.

## Connections

- [[../projects/call-center-web-app|Call Center Web App]]

## Contradictions Or Tensions

- None with existing pages. The project page's old `src/dashboard` description ("sales/order metrics and date filters") is superseded.

## Open Questions

- Should the backend add a self-scoped agent chat-stats read? The resolved-chat count pages the brand's closed queue (four pages of 50) and shows a "+" floor when that runs out.
- Totals filter by order creation date, so an order placed yesterday and delivered today counts on yesterday.
