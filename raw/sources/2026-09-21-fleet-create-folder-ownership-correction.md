# Fleet Create Folder Ownership Correction

- Date: 2026-09-21
- Source: Direct user correction in Codex
- Project: LivelyCura Pharmacy Portal

## Direct Correction

A dedicated Fleet create workflow must own all creation-specific code inside its create folder. A create page must not remain a wrapper around forms, interfaces, or mutation hooks stored in the operator roster feature.

## Verified Resolution

- `src/fleet/createOperator` now owns the page, create form, profile field editors, interfaces, and create mutation hook.
- `src/fleet/operators` no longer contains the create mutation or a shared create/update form. Its profile form is explicitly update-only.
- The focused Fleet navigation test, targeted ESLint, and production Vite build passed.
- Full TypeScript checking remains blocked by pre-existing unfinished Fleet draft screens and Billing contract mismatches; it reported no errors in `createOperator` or the operator update files changed here.
