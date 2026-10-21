# Altin outlet bulk import request

Date: 2026-09-11
Source: direct user request in the Altin Partner Mobile task.

## User instruction

The user explicitly requests adding Outlets bulk import as both an action and an implemented feature. This supersedes the earlier exclusion of bulk import from the first Outlets pass.

## Reference contract

The cloned partner web app exposes bulk import when the membership can both create and update outlets. Its CSV flow supports upload/paste, validation and review, with at most 500 outlets in an atomic organization.outlet.bulkUpsert call. Rows match by id, then externalId; unmatched rows create new outlets. Required columns are name, latitude, longitude and addressLine1.

## Durable implementation decision

One permission-filtered action feeds both the Outlets overview Quick actions and drawer. The sibling outletBulkImport feature owns its UI, parser, file service and complete operation hook, reusing shared presentation and outletForm validation. The previous prohibition on production mutation testing remains in force.
