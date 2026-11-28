# C.E.Q.A Call Center: agent dashboard UI rework and Mantine BarChart lessons (2026-11-28)

- Date: 2026-11-28
- Author: the user, in a C.E.Q.A Claude Code session
- Recorded from: the user's message (quoted verbatim below), a multi-agent design panel (4 critiques, 3 proposals, 2 judges, 1 spec), an adversarial review of the result, and browser checks in the real app shell with a live agent session
- Repository: `call-center-web-app`, `src/dashboard`
- Status when recorded: built and verified in the browser; not committed

## The user's words (verbatim)

- On the first per-agent dashboard: "this is okay but improve the ui"

## Layout the panel chose (both judges)

- One radius-xl "My sales" panel copying the Customers page shell: header (48px brand ThemeIcon, h2-size 900 title, uppercase eyebrow), a gray period strip, then a hero.
- The hero shows one dominant figure, "Net sales today/this week/…", with the change in cedis and the direction in words ("GH¢120.00 more than this time yesterday"), no percentages. Then "4 of 64 orders fulfilled · GH¢70.00 average", and the amount "not counted yet" with the waiting and cancelled counts. The chart sits beside it at lg and below it on smaller screens.
- Removed: four equal KPI cards, the "Orders taken" panel, the greeting, and per-card % deltas, which mislead on one agent's small counts.
- A support band row, then "Your latest orders" in the customer order-history table style. It switches to the Orders page mobile cards at 48em and hides Branch from 48 to 62em.
- Live status is a dot Badge ("Live"/"Paused") plus "Updated N min ago". A failed poll keeps the last numbers and shows Paused; it does not replace panels with error alerts.

## Mantine 7.17 BarChart on recharts 3.8.1: what the browser showed

- Passing `barProps={{ isAnimationActive: true }}` overrides Mantine's default `false`, and the bars are never painted: the axis renders, the bars don't. Leave bar animation off.
- `gridAxis="x"` is horizontal lines, `"y"` is vertical.
- Horizontal hairlines only lined up with the y ticks after `gridProps={{ yAxisId: "left", syncWithTicks: true }}`. Without it, 3 ticks drew 2 lines.
- Tick text falls back to `--mantine-color-dimmed` because BarChart sets no `--chart-text-color`, which fails contrast. Set the variable through a className with `light-dark(gray-7, dark-1)`. The `textColor` prop takes one colour for both themes.
