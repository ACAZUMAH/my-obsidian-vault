# ChopRoute Redux Marketplace State Correction

Date: 2026-08-07
Source: direct user instruction in Codex

> I have just been focusing on the ui and the logic and integrations is totally wrong first of all the the market place and it's orgs has to be saved in redux not a context. update and after that loading the products and the categories should have their own query and files in the home file. so do the redux first

Implementation scope for this stage:

- Move the current marketplace and its access-granted organizations from React context into Redux.
- Do only the Redux correction first.
- Split Home product and category loading into their own Home-owned query files in the next stage.
