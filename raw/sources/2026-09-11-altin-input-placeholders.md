# Altin input placeholders

Date: 2026-09-11
Source: direct user correction in the Altin Partner Mobile task.

The user explicitly objected to empty inputs without placeholders and to repeatedly needing to request this basic form behavior. Add useful examples or expected-format guidance to all text inputs, including optional fields and edit fields when cleared. Retain visible labels and do not turn placeholder text into submitted defaults.

Scoped implementation convention: shared FormField and outlet field definitions require an explicit placeholder string, making omissions a TypeScript error. Features own the actual copy. This extends the earlier SERLP form/input correction rather than replacing the existing architecture or API contracts.
