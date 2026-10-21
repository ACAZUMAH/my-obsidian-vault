# Bora production CI audit scope

Date: 2026-09-18
Source: direct user instruction in the Bora backend task.

Regarding the workflow step named Audit production dependencies running yarn audit:production, the user instructed: "this shouldn't run on the reusable, it should only run on the production ci so update that".

Durable scope: keep the dependency audit in production CI and out of the reusable workflow shared by pull-request and staging CI. Production deployment must remain gated by the production audit.
