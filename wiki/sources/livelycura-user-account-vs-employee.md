---
type: source
status: active
created: 2026-10-25
updated: 2026-10-25
tags: [livelycura, hrm, identity, users, employees, decision]
sources:
  - ../../raw/sources/2026-10-25-livelycura-user-account-vs-employee.md
source_date: 2026-10-25
ingested: 2026-10-25
confidence: high
---

# LivelyCura User Account Versus Employee Record

## Source

- Raw file: [LivelyCura: user account and employee record stay separate](../../raw/sources/2026-10-25-livelycura-user-account-vs-employee.md)
- Date: 2026-10-25
- Author: The user (verbatim message)
- Ingested: 2026-10-25

## Core Claims

- One User account, keyed by phone number, serves every LivelyCura client app, including Check City food ordering.
- An Employee record is one organization's copy of the person; creating an employee finds or creates the User so the person can sign in.
- HR edits to an employee's name or email never change the User account; syncing would alter the person's details in unrelated apps.
- Staff-facing screens such as Loop's personal information show the Employee record of the organization being viewed, not the account.

## Useful Details

- Sign-in codes go to the account's own phone and email, which belong to the person.

## Connections

- [[../projects/livelycura-backend|LivelyCura Backend]] owns accounts and employees.
- [[../projects/livelycura-loop-app|LivelyCura Loop App]] shows the employee details.

## Contradictions Or Tensions

- A mistyped phone number at hire links the employee to the wrong account; fixes should re-link the employee record rather than renumber a shared account.

## Open Questions

- None.
