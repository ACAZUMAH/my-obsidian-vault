# Fleet Model Update-Method Correction

- Date: 2026-09-19
- Source: Direct user correction in Codex
- Project: LivelyCura Backend

## Direct Correction

- Fleet services must not mutate loaded Mongoose documents and call document `.save()` for updates.
- Use the owning model and the operation-appropriate update method instead.
- Preserve the existing business checks, transaction boundary, returned updated record, and event/history behavior while changing persistence style.

## Implementation Boundary

This correction applies to Fleet service updates. It does not authorize a shared persistence helper or move database operations out of the feature service that owns them.
