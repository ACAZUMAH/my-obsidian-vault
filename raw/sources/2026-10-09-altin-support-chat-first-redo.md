# Altin Partner Support Chat-First Redo — 2026-10-09

Sanitized record of user decisions and the resulting redesign of Altin Partner Mobile Support in a Claude Code session. No credentials, tokens, or personal identifiers are included.

## User decisions

- Asked before the redo, the user decided that the ticket subject is derived from the category the member selects; members do not type a subject.
- The user decided that if an order already has an issue, there is no need to raise another one: reporting an issue on that order opens the existing conversation.

## What was built

- Support now follows Check City's chat-first Support (`livelycura-check-city-app/src/support`).
  - **List:** header action for a new conversation, one scope line, compact rows. Search, filters and the footer button are gone.
  - **New conversation:** a topic sheet, a welcome block, an optional order card, and one shared composer. The subject is `<Category> support` or `Help with order <reference>`. The first message creates the ticket.
  - **Conversation:** the thread is the screen, an inverted list with a centred context block. Own bubbles are brand red with meta underneath. The composer is docked and sits on the keyboard. There are no success toasts.
- Order details' Report an issue opens a new conversation with the order, after looking up a live ticket (open, in progress or resolved) on that order. If one exists, it opens instead. The separate order-issue form was removed.
- Removed:
  - the order picker and linking or unlinking orders;
  - the status-history and details cards;
  - the Formik reply and create forms;
  - add tiles and success toasts.
- Removed files went to a local backup folder instead of being deleted. The agent's tool policy blocked deleting untracked files, which cannot be recovered.

## Review and verification

- An adversarial review confirmed 35 findings. Fixed:
  - a mutation refetch that hid the composer mid-send;
  - the keyboard closing on every send;
  - a duplicate conversation route on redirect;
  - truncated UUIDs shown as order references;
  - brand-icon-well violations, dead fields, an off-scale font, sheet geometry and accessibility labels.
- Left for the user to decide:
  - live updates (Check City subscribes; the Altin Apollo client has no WebSocket link);
  - photo-library attachments;
  - a new-conversation action on closed tickets;
  - a backend create-time guard, because a member cannot see colleagues' tickets without VIEW_SUPPORT_TICKETS.
- Checked on the iOS simulator without sending anything: the list, an existing conversation, the topic sheet, a new conversation, and order support from an order without a ticket.
