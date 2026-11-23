---
type: source
status: active
created: 2026-10-25
updated: 2026-10-25
tags: [livelycura, hrm, employees, custom-fields, privacy, decision]
sources:
  - ../../raw/sources/2026-10-25-livelycura-hrm-employee-record-design.md
source_date: 2026-10-25
ingested: 2026-10-25
confidence: high
---

# LivelyCura HRM Employee Record Design

## Source

- Raw file: [LivelyCura HRM: employee record redesign](../../raw/sources/2026-10-25-livelycura-hrm-employee-record-design.md)
- Date: 2026-10-25
- Author: The user (verbatim messages and plan answers)
- Ingested: 2026-10-25

## Core Claims

- The ERP is general-purpose, not pharmacy-only, so built-in employee fields and defaults are industry-neutral.
- Every organization gets built-in Job details (job title from its own list, employment type, contract/service end, probation end, staff number) and Personal details (other names, date of birth, gender, nationality); first name, last name, phone and email are always required, and the start date stays optional.
- Each organization switches optional built-in fields to Don't ask, Optional or Required, and adds its own questions (custom fields) for anything else, such as emergency contacts, national ID or licences.
- Private details (date of birth, gender, questions marked private) are visible only with a "View private employee details" permission and to the person themselves.
- Staff see their own answers to organization questions in Loop unless HR marks a question "HR only".

## Useful Details

- Organization questions: 8 types, a type that can't change after creation, archive instead of delete, and automatic privacy for special-data labels (religion, ethnicity, health).
- Build phases: job details and foundations; private details; organization choices and questions; reminders.

## Connections

- [[../projects/livelycura-backend|LivelyCura Backend]] holds the employee record and field rules.
- [[livelycura-user-account-vs-employee|User Account Versus Employee Record]]: HR edits stay on the employee record.

## Contradictions Or Tensions

- None.

## Open Questions

- Remaining Employees decisions (leaving record, invite on hire, Loop self-edits, staff with no branch, serlp-mobile scope) are still open.
