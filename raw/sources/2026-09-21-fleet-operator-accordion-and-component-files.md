# Fleet Operator Accordion And Component-File Correction

- Date: 2026-09-21
- Author: User
- Context: LivelyCura Pharmacy Portal Fleet operator forms

## Direct Correction

- Render emergency contacts, identity documents, licenses, and other documents as accordion sections.
- Keep each section's add-more action inside its accordion panel.
- Do not bundle multiple operator editor components in `UpdateOperatorProfileEditors.tsx`; give each component its own file under the owning feature folder.

## Durable Interpretation

Fleet operator profile forms use a compact accordion for repeatable person/compliance records. Each editor remains independently owned and named so future changes do not recreate a component bundle.
