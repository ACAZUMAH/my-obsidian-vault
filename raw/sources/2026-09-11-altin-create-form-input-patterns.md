# Altin create-form and input UI correction

Date: 2026-09-11
Source: direct user correction in Altin Partner Mobile.

## Direct evidence

The user said: “I also spoke about create forms and the ui inputs, looking what you did there that's no how I do my things”. This follows the explicit instruction to reference SERLP for create/update flows and use direct Apollo mutations.

## Scoped interpretation and source verification

The correction applies to visible forms and input presentation as well as hooks. SERLP's FormField uses compact uppercase labels, bordered inputs, inline errors, and its existing theme. CreateCustomer and CreateProduct compose reusable PanelCard groups, a Screen header/footer, and keyboard avoidance around Screen. SearchableSelect uses a field-shaped trigger instead of a large action button. Apply these interaction and composition patterns with Altin tokens, maintaining feature-owned queries, values, validation and payloads.

## Boundaries

Do not treat mutation refactoring alone as satisfying form UI requests. Preserve existing user edits and API contracts; avoid production writes while verifying presentation.
