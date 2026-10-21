# Keks Single Employee PUT Correction

Date: 2026-09-16. Source: direct user correction and the supplied OpenAPI contract.

## User Correction

> I fucking uploaded the api openapi json doc to you the patch is for bulk import, put is used to update

## Contract And Scope

The single-employee update UI must use PUT /users (UserUpsert), with the existing record's internal id in the body and editable employee_id as a separate field. The documented id selects an existing user and returns 404 if missing; it cannot create a user. PATCH /users/bulk remains the bulk-import update operation. This is the required application workflow, not a claim that no individual PATCH operation exists in the schema.

The earlier decision to inspect only UserUpdate and declare Employee ID read-only was wrong: it ignored the provided PUT contract. Apply the create-form improvements to editing as well: blur/touched errors, per-step Next gating, optional fields, and contact layout/options. Preserve existing branch and roles in the PUT payload.
