# Direction: an approved fix is delivered whole; no test people on the shared dev database

Date: 2026-11-19
Source: the owner's messages in a Claude Code session on LivelyCura HRM follow-up 1 (paraphrased; expletives left out), plus the session facts that led to them.

## What happened

- The owner approved a three-part fix ("Yes, all three"): the portal and serlp-mobile list only organizations where the person holds a role, serlp-mobile's sign-in needs a role, and serlp-mobile shows sign-in errors.
- After building it, the agent reported that a review had found four "leftovers" in what people see after losing a role, and asked whether to fix them. After those were fixed, it again left one item as a question (the portal's sign-in refusal for plain staff still lacked the SERLP Loop pointer).
- The agent also offered to create a test person ("Ama", a manager at one organization and plain staff at another) on the shared dev database to check sign-in on screen.
- The owner replied that they had said yes to all three, asked why the agent kept fixing things and leaving leftovers, asked that the lost-access page follow the project's UI, and said not to create any test Ama.

## Direction

- When the owner approves a fix, deliver it whole: every app (portal, serlp-mobile, Loop), screen, message and follow-on effect it touches, including what a review of that fix finds. Do not come back with "leftovers" to ask about. Only genuinely separate features, or decisions that are truly the owner's (such as exact wording), go back as a question.
- Never create test users, employees or organizations on the shared dev database to check a flow on screen, and do not offer to. Verify with tests (integration tests seed their own in-memory data) and with browser checks that use fake client-side state on a separate origin, never the owner's signed-in tab.
