# Fleet Frontend Form And Shared Folder Correction

- Date: 2026-09-21
- Source: Direct user correction in Codex
- Project: LivelyCura Pharmacy Portal

## Direct Correction

- Remove the prematurely introduced `src/fleet/shared` folder; the Pharmacy Portal does not use that ownership pattern for this Fleet rebuild.
- Keep all create-operator behavior inside `src/fleet/createOperator` and all roster/update behavior inside `src/fleet/operators`.
- Follow the existing project form architecture instead of combining Formik setup, validation, payload mapping, mutation coordination, and rendering in one component.
- Fleet forms use a named feature-owned `use…Form` hook with Formik and Yup. The page or modal coordinates mutation and navigation; the form component renders fields from the supplied form object.
- Inspect existing project features before implementing new module structure. Do not invent a generic `shared` dumping folder before a stable reused abstraction exists.

## Verified Resolution

- Create and update operator forms now receive feature-owned Formik objects and contain no inline validation schemas or GraphQL mutations.
- Yup schemas live in `useCreateOperatorForm` and `useUpdateOperatorForm`.
- Create and update payload conversion, document upload operations, and document URL reads live in their owning feature folders.
- Active operator list, create, view, and update code no longer imports `src/fleet/shared`, and that folder was removed.
- Targeted ESLint, the focused Fleet navigation test, and the production Vite build passed.
