# Marketplace Admin Table, Filter, And Action Convention

Date: 2026-08-08
Author: User

Marketplace administration tables must follow the established Admin table convention rather than introducing incomplete table variants. Every data table starts with a `#` row-number column and labels its final action-button column `Actions`.

Pages expose query-backed filters that match their data contract. Business Products filters by access-granted organization, canonical category, and publication status. Direct Orders filters by access-granted organization and order status. Marketplace Orders filters by access-granted organization and marketplace-order status. Category list and tree pages filter by category status. Filters, pagination, and search use the existing URL-backed list-filter architecture and flow into GraphQL query variables.

Types remain in owning interface folders, GraphQL operations remain in hooks, domain constants remain in constants, and components remain presentation/orchestration surfaces.
