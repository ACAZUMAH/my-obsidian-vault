# Altin Outlets Scope and Rounded Statuses

Date: 2026-09-11. Direct user instructions in the Altin Partner Mobile task; implementation inspection by Codex. No production records or credentials are included.

## Direct instructions

> okay now make all the statuses rounded radiuses and let's move to the next app, outlet

Asked whether Outlets should initially cover overview/list/details or also create/edit, the user answered:

> do all this Overview, list, and details first and also include the creating and editing but don't test it against the production API, build the ui and integrate the apis and I will change the api and do the testing my self

## Implementation evidence and boundary

- The local web partner reference gates Outlets routes with VIEW_ALL_OUTLETS; CREATE_OUTLETS and UPDATE_OUTLETS independently gate actions. ADMIN grants these permissions. Mobile applies this to both organization types.
- Outlets owns its overview and sibling list/detail/create/edit features, with a shared outletForm. Each GraphQL operation stays complete inside its hook.
- Status badge presentation now uses the shared round radius. Generic read/pagination/mutation mechanics and presentation primitives are reused across module boundaries without importing Orders business behavior.
- Create/edit use the web field constraints and explicit nulls for optional-field clearing. Coordinates are entered manually. Delete, bulk import, and a map picker were not requested or implemented.
- Verification was offline: TypeScript, formatting, generated-model field checks, and mocked tests. No new Outlets operation was exercised against production; no extra runtime was started. Native and live API behavior remain unverified and reserved to the user after endpoint change.
- A general-agent source reviewer substituted for the specialized design reviewer. The one edit-skeleton finding was resolved in source; this is not a native visual verdict or user acceptance.
