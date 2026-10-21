# Altin mobile query architecture correction

Date: 2026-09-12
Source: direct user correction in the active Altin Partner Mobile Codex conversation, followed by inspection of the existing mobile source.

## Direct user correction

The user rejected the assistant's preceding fix again and insisted: “stick to my architecture”. The user clarified that the cloned web apps explain the product being built, rather than provide the implementation architecture to copy into mobile. The preceding change had merely relocated gql definitions and retained imperative client.query calls inside generic resource hooks.

## Verified local reference

The existing `src/home/hooks/useOrdersVolume.ts` and `src/home/hooks/useCourierleaderBoard.ts` use a private gql constant in the hook file, direct Apollo useQuery with Pick<Query, ...> and generated operation argument types, useMemo for domain data, and returned Apollo result fields. `src/system/hooks/useSystemQuery.ts` and the referenced SERLP mobile query hooks independently confirm direct useQuery and private module-level documents. SERLP's report-table query uses Apollo fetchMore/updateQuery for pagination.

## Correction to prior interpretation

The earlier assistant-authored rule requiring gql templates inside the function body was not the user's architecture and was rejected. It must not be retained as a durable preference. Hook ownership includes the private document in the same hook file. Fleet should follow the actual local mobile query pattern and compose hooks for overview data. The web clone remains the product, permission and API-contract reference.

Subsequent user acceptance of the revised implementation is not established by this source.
