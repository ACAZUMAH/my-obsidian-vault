---
type: source
status: active
created: 2026-09-16
updated: 2026-09-16
tags: [keks, hrm, api, validation]
sources:
  - ../../raw/sources/2026-09-16-keks-single-employee-put-correction.md
  - ../../raw/sources/2026-09-16-keks-step-validation-correction.md
  - ../../raw/sources/2026-09-16-keks-backend-errors-and-bulk-time-punches.md
---

# Keks Backend Errors And Bulk Time Punches

## Source

- Follow-up raw file: [Single-employee PUT correction](../../raw/sources/2026-09-16-keks-single-employee-put-correction.md)

- Follow-up raw file: [Step validation correction](../../raw/sources/2026-09-16-keks-step-validation-correction.md)

- Raw file: [User correction and contract evidence](../../raw/sources/2026-09-16-keks-backend-errors-and-bulk-time-punches.md)
- Date: 2026-09-16
- Author: User; attached API contract inspected by Codex
- Ingested: 2026-09-16

## Core Claims

- Single-employee edits use PUT /users with the existing internal id and editable employee_id. PATCH /users/bulk belongs to bulk import. Apply create-form improvements consistently to editing.

- Follow established Formik onBlur and touched/error input behavior. Disable Next for an invalid current step; do not bulk-touch fields and jump backward at final submission.

- Show the backend's actual error messages in notifications; use contextual generic text only when the response has no usable message.
- Preserve the user's required-field choices in Yup. Align required markers and request serialization; blank optional values must not become invalid dates, UUIDs, or empty nested contacts.
- Bulk time punches use sequential individual requests with visible progress and outcomes.

## Useful Details

- Required create-user form fields: first name, last name, gender, phone number, role.
- Error formats include errors arrays, error/message strings, and validation detail arrays with field locations.
- Manual override takes employee_id and resolves the outstanding punch request. Deduplicate selected shift owners to avoid repeated punches; HTTP 204 means success.

## Connections

- [[../projects/keks-admin-portal|Keks Admin Portal]]

## Contradictions Or Tensions

- The earlier agent restriction making Employee ID read-only was rejected: it considered only the PATCH schema and missed the documented PUT upsert contract. The user explicitly requires PUT for individual updates.

- Selecting a shift does not make override shift-addressable; the backend decides which pending employee request is recorded.
- Emergency contact is optional, but supplying a contact invokes the backend's nested requirement for its name.

## Open Questions

- No bulk-specific endpoint is supplied; recheck the current API contract before changing this behavior.
