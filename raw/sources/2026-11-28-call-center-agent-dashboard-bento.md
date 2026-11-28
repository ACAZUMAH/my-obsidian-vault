# C.E.Q.A Call Center: agent dashboard rearranged as a bento grid (2026-11-28)

- Date: 2026-11-28
- Author: the user, in a C.E.Q.A Claude Code session
- Recorded from: the user's message (quoted verbatim below) with three third-party dashboard inspiration shots, and browser checks of the rebuilt layout in the real app shell
- Repository: `call-center-web-app`, `src/dashboard`
- Status when recorded: built and verified in the browser; not committed

## The user's words (verbatim)

- "Here are ui inspos, for you to look at and arrange them dashboard well what you did looks nice but arrangement and the refresh button is not necessary"

## What the inspiration shots had in common (described, not copied)

- A greeting header ("welcome back" plus the user's name) with the date or period control at the top right.
- Separate cards rather than one long panel: a dominant balance or revenue card, smaller KPI cards beside it, the main chart taking two thirds of a row, and a table sharing its row with narrower list cards.
- Each card has the same heading: a small icon, a title and subtitle, and its control on the right.

## What was built

- The refresh button is gone; the figures poll on their own and the hero keeps the Live / Updated label.
- Header: a time-of-day greeting with the agent's username, a one-line subtitle, and the period buttons on the right; custom dates open inline beside them.
- Bento grid using `grid-template-areas`, with the DOM in phone reading order:
  - wide (75em and up): net sales, orders and average order across the top; not counted yet and customer support down the left beside the chart; order status full width; payment, branch and delivery-vs-pickup stacked beside the latest orders;
  - tablet: two columns, with the chart, order status, delivery-vs-pickup and latest orders full width;
  - phone: one column, with orders and average side by side.
- One card heading (icon, title, subtitle, right-hand control) shared by every card; the chart's running-total toggle moved into its heading.

## Layout lessons

- Balance the rows a spanning card covers. With order status beside the payment card, branch and delivery-vs-pickup were stretched about 300px to match the 8-row orders table. Making order status full width and stacking all three breakdown cards beside the table left them level (744px each side).
- Size money figures in narrow cards with container units (`cqi`) on the card, not viewport units: the hero is a third of the row on wide screens and full width on tablets.
