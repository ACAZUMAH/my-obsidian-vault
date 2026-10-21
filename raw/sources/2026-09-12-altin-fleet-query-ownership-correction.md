# Altin Fleet query ownership correction

Date: 2026-09-12
Source: direct user correction in the active Altin Partner Mobile Codex conversation.

The user rejected the implementation again, citing the previously established operation-ownership instruction and pasting the exported `FLEET_OVERVIEW_QUERY` document. That document bundled `online: couriers`, `pending: couriers`, and `preview: couriers` in one `MobileFleetOverview` query.

Existing instruction supplied by the user in this conversation: “Each operation is written completely inside its own hook; do not extract/import GraphQL fragments into a separate graphql folder.”

Assistant remediation interpretation: place complete GraphQL documents inside their owning hooks, remove exported Fleet query constants, and compose independent courier-count and recent-courier reads instead of the aliased overview bundle. This interpretation was implemented in response to the correction; subsequent user acceptance is not established by this source.
