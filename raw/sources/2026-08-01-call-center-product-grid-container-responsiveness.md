# Call Center Product Grid Container Responsiveness

Date: 2026-08-01

## User Requirement

> I want the grid items to be this way { base: 1, sm: 3, md: 3, lg: 4, xl: 5 } but it's stack at 5 even when I drag the resizable close to the left

## Applied Frontend Boundary

- The product grid is nested inside a horizontally resizable Products panel.
- Its 1/3/3/4/5 column progression must respond to the Products panel's current width rather than the browser viewport.
- Mantine `SimpleGrid` container-query mode preserves the theme breakpoints while allowing drag-resize changes to reflow the cards.
