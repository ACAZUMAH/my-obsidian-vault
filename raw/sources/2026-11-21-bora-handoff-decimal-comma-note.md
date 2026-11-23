# Bora: decimal-comma withdrawal input goes in the next frontend handoff

Date: 2026-11-21
Source: direct owner statement in a Claude Code session on `bora-capital-backend`, after the B15 review. The checker had noted an older app input issue.

## The note the owner approved for the handoff (verbatim)

> yes when we are writing the frontend hand over we can add it to inform him "Side note, app only, your call: on a phone keyboard that uses a decimal comma, typing “500,50” becomes “50050”. The confirm screen shows 50,050 before the customer confirms, so it’s visible, but it’s an older input issue in the app."

## Context

- The customer app's withdrawal amount input (`app/withdrawals/amount.tsx`, `sanitizeAmountInput`) keeps only digits and one point. On a keyboard that types a decimal comma, the comma is removed, so "500,50" becomes 50050.
- This is an app issue, not a backend one. The owner wants the frontend developer told in the next dated frontend handoff; no handoff is written yet.
