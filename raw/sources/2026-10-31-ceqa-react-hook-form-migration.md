# C.E.Q.A React Hook Form Migration

Date: 2026-10-30 to 2026-10-31
Source: Claude Code desktop sessions in `/Users/acazumah/Documents/C.E.Q.A` (`eb72a8c1-20cd-40d6-a109-61a4868104c5`, continued in `bae009f7-104d-43c7-8c7d-c8eefca3b03b`).

## Direct user evidence

> I noticed react formik have not been maintained for a long time so I want us to migrate to both callcenter and the keks to React Hook Form

When the assistant relayed a subagent claim that several Keks submits "never validate", the user rejected the framing:

> what do you mean it never validates?. Did you really check the code?. there is yup passed to formik with validate on mount so I don't what you are talking about. and follow how I do things already

Choices the user selected in the planning questions:

- Call-center checkout: enforce the delivery-location rule (Formik silently dropped its object-level error) and show it under the address/location control.
- Keks shared controls: `register` for `FieldInput`/`FieldTextarea` (given `ref` support) and `Controller` for selectors, radios, checkboxes, switches and the phone input; no new wrapper components.

The user approved the plan, requested a commit after each stage, and then asked:

> Update the vault: replace the Formik form rules with the React Hook Form convention in the dev manual and both project pages.

## Scoped repository verification

- Library versions: `react-hook-form` 7.91.0 and `@hookform/resolvers` 6.0.2; Yup schemas kept. Formik's last publish was 2.4.9 (2025-11).
- Call Center Web App: login and checkout forms migrated on `feature/react-hook-form`, commit `310dbac`, stacked on the product-discount commit `c780f8c` (both unpushed at recording time).
- Keks Admin Portal: all 21 forms migrated on `feature/react-hook-form`, commit `d80126c` (unpushed at recording time).
- Structure kept from the Formik convention: private module-level Yup schema; named `use…Form` hook returning the real form; screens own submission and read `form.getValues()`; each button keeps its existing `isValid`/`loading` gating. Keks Designation was the one form whose request ran in Formik `onSubmit`; it moved to a `useDesignationForm` hook with a screen-owned handler.
- Mode: `onTouched`, so errors appear after blur, matching the old `touched ? error : undefined` display. The Keks substitution wizard uses `mode: "all"` because its Formik config validated on change and blur and displayed errors without touch gating.
- Edit forms: memoized record values passed as `defaultValues` and `values`. `resetOptions.keepDirtyValues` was rejected because an abandoned edit on one record would carry into the next record opened in the same modal; Formik `enableReinitialize` fully reset.

## Library behaviour verified from source and tests

- `setValue` without `{ shouldValidate: true }` does not refresh `formState.isValid`; Formik `setFieldValue` validated by default.
- `reset()` back to non-empty defaults keeps the previous `isValid`; RHF only revalidates on mount. Fix used: `reset()`, then `await trigger()`, then `clearErrors()`. Formik had the same stale state because `resetForm` cleared errors.
- `ResolverOptions` is invariant over field names and types: a hand-written values interface must match the schema exactly. Working patterns: infer the form type from the schema (`yup.InferType`), type edit-form memo values as the schema type, refine string unions with `yup.string<T>()`, and name transport-only fields in the schema without rules.
- Formik drops object-level Yup test errors (path `''`); `yupResolver` keeps them and they gate `isValid`. Cross-field rules belong on a concrete field via `this.parent`.
- `useForm` re-reads `resolver` every render, so a memoized prop-dependent schema works.
- `form.watch()` re-renders the form host on every change, which matches Formik's whole-form re-render; `useWatch` suits child components reading one field.

## Live verification

All migrated forms were exercised in the browser against the user's own signed-in session without submitting: blur errors, `Controller` bindings, edit refills, stepper gating, guard-before-request submits, and reset revalidation.

## Runtime finding

The production Keks API (`api.keks.work`) answered CORS preflight for `http://localhost:5173` and `http://localhost:3000` and rejected `5175` and `5180` (other ports not probed); from a rejected port, login fails with a CORS error unrelated to application code.
