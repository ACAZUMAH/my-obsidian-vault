# LivelyCura Fleet Filter URL Parsing Correction

- Date: 2026-09-25
- Source: direct user correction in the current Codex task.

The user rejected the custom `getFiltersFromParams` handling for Fleet pagination and status filters after the broader Fleet filter-hook correction.

Direct excerpt: “how you passing the limit, page, and status filters on this function getFiltersFromParams is still wrong”.

The established Pharmacy Portal list-hook pattern is the implementation reference: parse `page` and `limit` through the ordinary numeric parser with the list defaults, represent an unselected status or enum filter as `null` or `undefined`, omit it from query variables, and use a clearable select instead of an invented `ALL` enum sentinel.
