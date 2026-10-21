# Altin compact cards, shared composition, and production API

Date: 2026-09-10
Source: direct user messages in the Altin Partner Mobile Codex task.
Scope: durable UI/architecture correction and runtime verification boundary. No live records, private identifiers, screenshots, or credentials are included.

## Direct user evidence

On DeliveryOrderRow density:

> we need a way to just some few info to make the card as small and okay, I mean if they want to view all they can tab to view the details

On actual SERLP reuse:

> a screen reusable component, as many components as possible should be reused that's why I said reference serlp in the first place

On the API environment:

> one thing you should take note,  we using the production api so tread lightly

## Scope interpretation

The later request supersedes the earlier detailed pickup/drop-off card layout: retain separate cards but show only useful scan information, with the complete record in details. Shared presentation should be composed across features while queries, filter state, and navigation keep their feature ownership. The production warning calls for minimal read-only live verification and local tests for artificial/error scenarios, without modifying production records.

This evidence does not establish acceptance of any particular card design, a deployment, or a complete runtime test matrix.
