# Marketplace Admin Conditional Table Rendering Correction

Date: 2026-08-08
Author: User

Marketplace table bodies must use the existing shared `Conditional` component for loading and loaded-data branches. Do not introduce ternary-based loader/data rendering when the surrounding Admin tables already establish `Conditional` as the table-body convention.

This applies to Organization Access, Business Products, and Direct Orders and to later marketplace tables. It preserves one consistent rendering structure across Roles, Orders, Products, Facilities, Categories, and marketplace-scoped tables.
