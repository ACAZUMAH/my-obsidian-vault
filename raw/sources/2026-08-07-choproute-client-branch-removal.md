# ChopRoute Client Branch Removal

Date: 2026-08-07
Source: direct user instruction in Codex

> remove the branch feature and files since we are not using it again

Implementation scope:

- Remove the client-side branch feature, files, Redux state, hooks, routes, selectors, and branch UI.
- Remove or gate remaining checkout and reorder behavior that selected a facility on the client.
- Preserve customer delivery-location selection and future server-side fulfillment routing as separate concerns.
