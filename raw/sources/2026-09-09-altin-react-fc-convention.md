# Altin React.FC Component Convention

- Date: 2026-09-09
- Source: direct user correction in the Altin Partner Mobile implementation conversation.

## Direct Evidence

The user asked to change how component interfaces are passed and explicitly instructed: “use react.fc”.

## Context And Scope

This correction concerns the Orders implementation and follows the user's existing requirement to keep component interfaces in separately owned interface files. Use `const Component: React.FC<Props> = (...) => ...`, or `React.FC` when the component has no props, instead of putting the props type on the function parameter. Preserve intervening user edits and existing behavior while applying the convention. Repository inspection showed this declaration style already used by established mobile components and the user's recent Orders edits.
