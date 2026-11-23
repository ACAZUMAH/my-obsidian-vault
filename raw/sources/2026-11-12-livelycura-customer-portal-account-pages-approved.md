# LivelyCura customer portal: account pages built and approved

Date: 2026-11-11 to 2026-11-12
Source: the owner's decisions and approval in the same Claude Code session on `livelycura-customer-portal`, plus the code built and checked there (paraphrased; quoted phrases are the owner's own words). The work is uncommitted on `feature/portal-ui`; the owner asked not to commit yet.

## Decisions

- **Orders.** The owner chose the account orders pages after checkout and approved the plan with all additions:
  - show more orders;
  - order number, placed date and delivery address;
  - payment status chips and "Pay ¢X" on the cards;
  - an "All orders" link and Try again;
  - "Get a new payment link";
  - wording fixes.
- **Cancel dialog.** The owner asked whether cancelling has no note, then said "okay let's remove the note from the ui". In the backend, the shopper's `cancelMarketplaceOrder(id)` accepts only the order id; the old UI asked for a note because it wrongly called the pharmacy's `cancelOrder`. The owner also had the red left border removed from the dialog's order box: "it's an ai flop".
- **Remaining account pages.** The owner pointed out that the account area was unfinished ("prescription, notifications, support and setting you didn't"). They approved a plan for those four pages with all additions:
  - show more prescriptions;
  - pharmacy and medicine names on prescriptions;
  - case number and status chip on support inbox rows;
  - Try again on every error screen.
- **Approval.** The owner checked the built account pages and said "Looks right".

## What was built

- **Account frame:** a forest band under the header with the six tabs (Dashboard, Orders, Prescriptions, Support, Notifications, Settings) as chip links; the lime fill glides between tabs. Each page puts its heading inside the band through a head slot, so forest bands never stack.
- **Orders:** fixes and additions.
  - The order page's Pay button never showed: it fetched `checkoutDirectUrl` but checked `checkoutUrl`. Both pages now use `payment { checkoutUrl expiresAt status }`.
  - Cancel switched to `cancelMarketplaceOrder`.
  - One rule for when Cancel shows on both pages.
  - Paging past the newest 10.
  - One customer-status vocabulary everywhere.
  - Line prices from the stored order line.
  - Real link cards.
- **Prescriptions:** fixes and additions.
  - Removed the dead "View active refill" and "View order" links: refills are pharmacy orders, which the shopper's marketplace order page cannot read.
  - Refill blocked while a refill is in progress.
  - Cards titled by their medicines, with the pharmacy name.
  - All sections open; edit forms reset on Cancel.
- **Notifications:**
  - support-reply notifications (`customer.support_case.detail`) open `/u/support/:id`;
  - opening never waits on mark-read;
  - the side stripe was removed.
- **Support:**
  - forest and mint chat bubbles;
  - the inbox and thread refetch when the tab becomes visible or the connection returns;
  - the related order is shown as an MKT number link;
  - inbox rows show the latest chat plus the case number and a status chip.
- **Settings:** a summary card and a Green Room form. Cancel resets the form, Save works only after a change, and the locked-phone note is shown as text.
- **Shared:** busy buttons use the spinner, and dialogs grow from their button.

## Left open

- **Refill orders:** seeing, paying for and tracking them needs a backend change.
- **Prescription edits:** whether shoppers may edit the pharmacy's prescription (cycle, medicines, note) and reactivate it is an owner decision.
- **Shopper cancel note:** a note on the shopper's cancel would need a backend change.

## Verification at recording

- Type check, lint on changed files and the SSR build passed. 582 unit tests passed across the project.
- The orders pages were not seen live by the agent; account pages need sign-in. The owner checked them themselves.
