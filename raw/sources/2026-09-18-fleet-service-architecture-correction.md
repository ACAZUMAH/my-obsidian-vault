# Fleet Service Architecture Correction

- Date: 2026-09-18
- Source: Direct user correction in Codex
- Project: LivelyCura Backend

## Direct Correction

- Fleet services must follow the repository's established service architecture instead of introducing a feature-wide transaction abstraction.
- Each feature service owns its model queries and persistence operations.
- Database operations do not belong in helper files; helpers are for pure validation and transformation.
- A transaction belongs to the concrete operation that needs atomic multi-document writes. Ordinary CRUD must not be forced through one shared transaction function.
- File and function names must describe the domain operation and match the surrounding repository structure.

## Implementation Boundary

This correction applies to the independent Fleet backend currently under construction. It does not change Courier's own idempotency or financial transaction requirements and does not authorize Fleet migrations or rollout work.
