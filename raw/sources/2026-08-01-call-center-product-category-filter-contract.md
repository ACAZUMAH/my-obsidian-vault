# Call Center Product Category Filter Contract

Date: 2026-08-01

## Backend Guidance Relayed By The User

- Product category document identifiers belong in `categoryIds`, for example `categoryIds: ["6a69f81786b9baf327d514f2"]`.
- `categoryPaths` accepts category slugs rather than document identifiers, for example `categoryPaths: ["beef"]`.

## Applied Frontend Boundary

- The Call Center category selector currently stores category `_id` values, so it must populate `categoryIds` and clear `categoryPaths`.
- A focused frontend regression verifies the selected `_id` is sent through `categoryIds`.
