# LivelyCura Fleet Jobs Naming Decision

Date: 2026-10-10
Source: Direct user instruction and answers in a Claude Code task.

> we going to change the naming convention of the job under the fleet to fleetJobs so do that for all backend, pharmacy and serlp mobile, that includes file names, apis, schemas, frontend components and etc

Answers to the clarifying questions in the same task:

- Stored data. Question: six Fleet records (fuel, expenses, inspections, maintenance, defects, incidents) store a `jobId` link, and the audit trail stores the job entity type as "Job". Answer: "Rename, no migration". `jobId` becomes `fleetJobId` in Mongoose, GraphQL and all clients, and the audit value becomes "FleetJob". Fleet is pre-production, so existing development records lose old links.
- URLs and labels. Answer: "Keep URLs and labels". `/fleet/jobs` paths, mobile deep links and the visible "Jobs" labels stay. The rename is code-only.
