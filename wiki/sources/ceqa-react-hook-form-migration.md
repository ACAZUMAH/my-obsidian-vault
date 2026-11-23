---
type: source
status: active
created: 2026-10-31
updated: 2026-10-31
tags: [ceqa, call-center, keks, forms, react-hook-form, yup, formik]
sources:
  - ../../raw/sources/2026-10-31-ceqa-react-hook-form-migration.md
confidence: high
---

# C.E.Q.A React Hook Form Migration

## Source

- Raw file: [C.E.Q.A React Hook Form migration](../../raw/sources/2026-10-31-ceqa-react-hook-form-migration.md)
- Date: 2026-10-30 to 2026-10-31
- Author: user, through C.E.Q.A Claude Code sessions
- Ingested: 2026-10-31

## Core Claims

- User decision: Formik is unmaintained, so Call Center Web App and Keks Admin Portal move to React Hook Form with the Yup resolver. Yup schemas stay.
- User correction: "follow how I do things already". The migration is a library swap that keeps the existing form structure: private module-level Yup schema, named `use…Form` hook returning the real form, screen-owned submission, and each button's existing gating. Verify a defect claim in code before presenting it.
- User choices: enforce the call-center delivery-location rule on the address field; bind Keks controls with `register` (inputs that accept `ref`) and `Controller` (selectors, radios, checkboxes, switches, phone input) without new wrapper components.
- User instruction: replace the Formik rules with the React Hook Form convention in the development manual and both project pages.

## Useful Details

- `onTouched` mode reproduces `touched ? error : undefined`; use `errors.x?.message`. A form whose Formik config validated on change and blur without touch gating maps to `mode: "all"`.
- Programmatic writes use `setValue(name, value, { shouldValidate: true })`; without it `isValid` goes stale.
- After `reset()`, re-check validity with `trigger()` then `clearErrors()` wherever a mounted form gates on `isValid`; RHF keeps the previous `isValid`.
- Edit forms pass memoized record values as `defaultValues` and `values`, without `keepDirtyValues`, matching Formik `enableReinitialize`.
- Infer the form type from the schema or type memo values as the schema type; `ResolverOptions` invariance rejects hand-written value interfaces that differ from the schema.
- Put cross-field rules on a concrete field via `this.parent`; Formik dropped object-level errors that `yupResolver` keeps.
- Commits: call-center `310dbac` (stacked on `c780f8c`), Keks `d80126c`; all forms verified live without submitting.
- The production Keks API accepted CORS preflight from `localhost:5173` and `localhost:3000` only among the ports probed.

## Connections

- [[../projects/call-center-web-app|Call Center Web App]].
- [[../projects/keks-admin-portal|Keks Admin Portal]].
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]].
- [[altin-formik-onsubmit-correction|Altin Formik onSubmit Correction]].
- [[altin-orders-mobile-web-reference|Altin Orders mobile web reference]].

## Contradictions Or Tensions

- Supersedes the requirement to use Formik for forms in the manual's form rules. The structural rules from [[altin-formik-onsubmit-correction|the Formik onSubmit correction]] and [[altin-orders-mobile-web-reference|the cross-project form-structure correction]] remain in force: requests never run from the form library's submit callback, and no form controllers, adapters, or schema folders.
- Other repositories still contain Formik code; only these two applications were migrated.

## Open Questions

- Should the remaining Formik repositories (Altin, LivelyCura, SERLP, Check City) migrate, and in what order?
