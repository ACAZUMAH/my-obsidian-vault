# Altin module actions and consistency correction

Date: 2026-09-11
Source: direct user correction in the Altin Partner Mobile task.

## User evidence

- “there is no ... need to always put org name at the header of each app overview”
- “look at serlp mobile ... if the app has actions the overview should have quick actions section”
- “the orders app has quick for creating orders and you left it out also report an issue on a single order view which you left out”
- The user rejected inconsistent View all presentation between Orders and Outlets, questioned the custom resource hooks, and reported missing outlets on production.
- “on serlp each app drawer has the actions there ... if there are any”
- When asked to explain outlet ownership, the user redirected the agent to the cloned web project in the C.E.Q.A directory.

## Durable interpretation

Reference the cloned web source before asking the user to explain encoded product behavior. Use one feature-owned set of permission-filtered actions for the overview and drawer. Keep shared overview presentation consistent; omit redundant organization headings. Explicit order creation and issue reporting supersede their earlier deferral. The hooks question asks for an explanation; it is not an explicit instruction to delete them.

## Implementation evidence and limits

The web Outlets filter store and query action require the selected organization ID. This establishes the intended contract, not the cause of any missing production record. Do not erase organization scope to make an empty screen populate. Native screenshots or mocked checks do not establish user acceptance. Production writes remain prohibited for development testing.
