# Hermes Session Coverage Audit — 2026-07-21

This immutable metadata manifest inventories the Hermes session stores used for the coverage audit. It intentionally excludes message bodies, system prompts, tool payloads, secrets, and private identifiers. A row proves that a record exists; it does not prove that its durable knowledge has been promoted into the vault.

## Scope

- `/Users/acazumah/.hermes/profiles/coder/state.db` (read-only audit)
- `/Users/acazumah/.hermes/state.db` (read-only audit of the default profile)
- Snapshot time: 2026-07-21 17:12 GMT
- Existing state snapshots and empty researcher/personal/devops profile databases were excluded.

## Counts

- Stored sessions: 225
- Sessions containing user messages: 222
- Primary non-subagent sessions containing user messages: 132
- Subagent sessions containing user messages: 90
- Primary sessions with an explicit non-vault project cwd: 16
- By profile: coder=182, default=40
- By source: cli=26, desktop=15, subagent=90, tui=89, unknown=2
- Direct Hermes project sessions explicitly documented as processed before this audit: 1 (`20260710_173537_54b264`, CompFlow).
- Coverage conclusion: the prior vault was not a complete Hermes-conversation harvest. Primary sessions without documented direct-Hermes classification remain pending, and subagent records require duplicate/independent-evidence triage.

## Session Metadata

| Profile | Session ID | Started | Source | Parent | U/A/T | CWD | Title |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| coder | `20260621_005833_de3cc9` | 2026-06-21 00:59 UTC | tui | — | 2/3/1 | `/Users/acazumah` | Hermes Model Identification |
| coder | `20260621_010814_92d057` | 2026-06-21 01:13 UTC | cli | — | 3/46/82 | `/Users/acazumah/Documents` | Importing Codebase Skills to Profile |
| coder | `20260621_024625_0d1cb4` | 2026-06-21 02:46 UTC | cli | — | 1/1/0 | `/Users/acazumah/Documents` | Fixing Chakra v3 Selector Collection Error |
| coder | `20260621_024745_952624` | 2026-06-21 02:47 UTC | cli | — | 1/1/0 | `/Users/acazumah/Documents` | Fixing Chakra v3 Selector Crash |
| coder | `20260621_024824_d0e17a` | 2026-06-21 02:48 UTC | cli | — | 3/40/37 | `/Users/acazumah/Documents` | Move Interfaces to Dedicated Folder |
| coder | `20260621_210927_566f24` | 2026-06-21 21:09 UTC | cli | — | 13/146/235 | `/Users/acazumah/Documents` | Evening work session preparation |
| coder | `20260621_234644_f9a795` | 2026-06-21 23:46 UTC | cli | `20260621_210927_566f24` | 12/94/149 | `—` | Evening work session preparation #2 |
| coder | `20260622_115444_d37ddc` | 2026-06-22 12:10 UTC | cli | — | 4/16/36 | `/Users/acazumah/Documents` | Organizing LivelyCura Hermes Skills |
| coder | `20260622_134719_b462b2` | 2026-06-22 13:49 UTC | cli | — | 8/155/198 | `/Users/acazumah/Documents` | Building Portfolio Featured Projects Section |
| coder | `20260622_222345_4a9915` | 2026-06-22 22:23 UTC | cli | `20260622_134719_b462b2` | 1/0/0 | `—` | Building Portfolio Featured Projects Section #2 |
| coder | `20260622_222345_5303fa` | 2026-06-22 22:23 UTC | cli | `20260622_222345_4a9915` | 8/78/123 | `—` | Building Portfolio Featured Projects Section #3 |
| coder | `20260622_223118_351462` | 2026-06-22 22:31 UTC | cli | — | 9/88/162 | `/Users/acazumah/Documents` | Refactoring Swiper Project Carousel |
| coder | `20260622_235842_078510` | 2026-06-23 00:03 UTC | cli | — | 2/0/0 | `/Users/acazumah/Documents` | — |
| coder | `20260623_130432_e0eeb0` | 2026-06-23 13:05 UTC | cli | — | 6/68/90 | `/Users/acazumah/Documents` | Carousel Swiper Motion Update |
| coder | `20260623_163711_6701ea` | 2026-06-23 16:52 UTC | cli | — | 56/125/168 | `/Users/acazumah/Documents` | Animating Skills Section with Framer Motion |
| coder | `20260624_105536_89348f` | 2026-06-24 10:55 UTC | cli | `20260623_163711_6701ea` | 22/149/214 | `—` | Animating Skills Section with Framer Motion #2 |
| coder | `20260624_123800_8292b3` | 2026-06-24 12:45 UTC | cli | — | 3/76/139 | `/Users/acazumah/Documents` | Product lab test badge fix |
| coder | `20260624_150414_7af362` | 2026-06-24 15:10 UTC | cli | — | 5/91/192 | `/Users/acazumah/Documents` | MLS Refresh Button Fix |
| coder | `20260625_122343_c6ac8f` | 2026-06-25 12:23 UTC | cli | `20260624_150414_7af362` | 9/174/262 | `—` | MLS Refresh Button Fix #2 |
| coder | `20260626_114510_a5cc1c` | 2026-06-26 11:45 UTC | cli | `20260625_122343_c6ac8f` | 8/275/393 | `—` | MLS Refresh Button Fix #3 |
| coder | `20260626_140332_cf7d64` | 2026-06-26 14:03 UTC | cli | `20260626_114510_a5cc1c` | 10/288/422 | `—` | MLS Refresh Button Fix #4 |
| coder | `20260627_113946_8a0b7e` | 2026-06-27 11:51 UTC | cli | — | 10/123/199 | `/Users/acazumah/Documents` | GraphQL Product Nullable Field Error |
| coder | `20260627_153636_3d38e3` | 2026-06-27 15:36 UTC | cli | `20260627_113946_8a0b7e` | 11/168/229 | `—` | GraphQL Product Nullable Field Error #2 |
| coder | `20260628_134341_c8f843` | 2026-06-28 14:17 UTC | cli | — | 10/125/238 | `/Users/acazumah/Documents` | Ride Ordering Backend Setup |
| coder | `20260628_230635_e39d3a` | 2026-06-28 23:06 UTC | cli | `20260628_134341_c8f843` | 15/125/216 | `—` | Ride Ordering Backend Setup #2 |
| coder | `20260629_000111_f4ffc6` | 2026-06-29 00:01 UTC | cli | `20260628_230635_e39d3a` | 13/146/282 | `—` | Ride Ordering Backend Setup #3 |
| coder | `20260629_001748_68c46e` | 2026-06-29 00:17 UTC | cli | `20260629_000111_f4ffc6` | 13/123/232 | `/Users/acazumah` | Ride Ordering Backend Setup #4 |
| coder | `20260629_173939_b6748a` | 2026-06-29 17:39 UTC | tui | — | 5/103/202 | `—` | Stock and Sales Review |
| coder | `20260629_193407_346702` | 2026-06-29 19:34 UTC | tui | `20260629_173939_b6748a` | 12/197/359 | `—` | Stock and Sales Review #2 |
| coder | `20260630_230125_403524` | 2026-06-30 23:01 UTC | tui | — | 11/111/180 | `/Users/acazumah/Documents/C.E.Q.A/altin-partner-mobile` | Partner Mobile App Setup |
| coder | `20260701_023719_412401` | 2026-07-01 02:37 UTC | tui | — | 4/44/117 | `/Users/acazumah/Documents/C.E.Q.A/keks-admin-portal` | — |
| coder | `20260707_234054_86cb50` | 2026-07-07 23:41 UTC | tui | — | 3/4/1 | `/Users/acazumah/Documents/C.E.Q.A/keks-admin-portal` | — |
| coder | `20260707_234259_178721` | 2026-07-07 23:43 UTC | tui | — | 13/175/273 | `/Users/acazumah/Documents/LivelyCura/livelycura-check-city-app` | Coding Task Assistance |
| coder | `20260709_202251_e5340a` | 2026-07-09 20:22 UTC | tui | — | 2/52/116 | `—` | Call Center Location Delivery Update |
| default | `20260710_173537_54b264` | 2026-07-10 17:35 UTC | tui | — | 6/38/50 | `/Users/acazumah/Documents/compFlow` | — |
| coder | `20260710_190402_e7ba9f` | 2026-07-10 19:04 UTC | tui | — | 14/96/199 | `/Users/acazumah/Documents/compFlow` | Proper Project Stack Setup |
| coder | `20260711_143433_be702f` | 2026-07-11 14:34 UTC | tui | `20260710_190402_e7ba9f` | 18/124/275 | `—` | Proper Project Stack Setup #2 |
| coder | `20260711_152924_5d0016` | 2026-07-11 15:29 UTC | tui | `20260711_143433_be702f` | 27/164/372 | `—` | Proper Project Stack Setup #3 |
| coder | `20260711_165753_68ff6f` | 2026-07-11 16:57 UTC | tui | — | 4/97/275 | `/Users/acazumah/Documents/compFlow` | Backend Authentication Setup |
| coder | `20260711_221940_e79205` | 2026-07-11 22:19 UTC | tui | `20260711_165753_68ff6f` | 6/164/451 | `—` | Backend Authentication Setup #2 |
| coder | `20260712_021621_84e0f7` | 2026-07-12 02:16 UTC | tui | `20260711_221940_e79205` | 5/119/327 | `—` | Backend Authentication Setup #3 |
| coder | `20260712_031059_c7fd2c` | 2026-07-12 03:10 UTC | tui | `20260712_021621_84e0f7` | 8/144/392 | `—` | Backend Authentication Setup #4 |
| coder | `20260712_102048_b1481f` | 2026-07-12 10:20 UTC | tui | `20260712_031059_c7fd2c` | 6/117/355 | `—` | Backend Authentication Setup #5 |
| coder | `20260712_155404_4a08ff` | 2026-07-12 15:54 UTC | tui | `20260712_102048_b1481f` | 6/82/229 | `—` | Backend Authentication Setup #6 |
| coder | `20260712_183956_816de0` | 2026-07-12 18:39 UTC | tui | `20260629_193407_346702` | 6/86/172 | `—` | Stock and Sales Review #3 |
| coder | `20260712_223001_7e9756` | 2026-07-12 22:30 UTC | tui | `20260711_152924_5d0016` | 19/194/511 | `—` | Proper Project Stack Setup #4 |
| coder | `20260713_000653_15136d` | 2026-07-13 00:06 UTC | tui | `20260712_223001_7e9756` | 5/131/343 | `—` | Proper Project Stack Setup #5 |
| coder | `20260713_173225_73e447` | 2026-07-13 17:32 UTC | tui | `20260630_230125_403524` | 13/95/167 | `/Users/acazumah/Documents/Kusantec/bora-capital-backend` | Partner Mobile App Setup #2 |
| default | `20260713_191745_a48077` | 2026-07-13 19:17 UTC | tui | — | 2/29/140 | `/Users/acazumah/Documents/Kusantec/bora-capital-backend` | — |
| default | `20260713_191819_768838` | 2026-07-13 19:18 UTC | subagent | `20260713_191745_a48077` | 1/12/100 | `—` | — |
| default | `20260713_191819_f0b10b` | 2026-07-13 19:18 UTC | subagent | `20260713_191745_a48077` | 1/9/89 | `—` | — |
| default | `20260713_191819_26a8bd` | 2026-07-13 19:18 UTC | subagent | `20260713_191745_a48077` | 1/15/178 | `—` | — |
| default | `20260713_192516_b3bd12` | 2026-07-13 19:25 UTC | subagent | `20260713_191819_26a8bd` | 2/14/151 | `—` | — |
| default | `20260713_194431_64df24` | 2026-07-13 19:44 UTC | tui | `20260713_191745_a48077` | 6/63/135 | `/Users/acazumah/Documents/Kusantec/bora-capital-backend` | — |
| default | `20260713_205301_72152d` | 2026-07-13 20:53 UTC | tui | `20260713_194431_64df24` | 5/70/129 | `/Users/acazumah/Documents/Kusantec/bora-capital-backend` | — |
| default | `20260713_213541_c58421` | 2026-07-13 21:35 UTC | tui | `20260713_205301_72152d` | 7/88/158 | `/Users/acazumah/Documents/Kusantec/bora-capital-backend` | — |
| default | `20260714_004726_db109b` | 2026-07-14 00:47 UTC | tui | `20260713_213541_c58421` | 8/107/192 | `—` | — |
| default | `20260714_012250_ad27cc` | 2026-07-14 01:22 UTC | tui | `20260714_004726_db109b` | 6/94/163 | `—` | — |
| default | `20260714_012850_992578` | 2026-07-14 01:28 UTC | tui | `20260714_012250_ad27cc` | 6/89/169 | `—` | — |
| default | `20260714_023558_3a7c70` | 2026-07-14 02:35 UTC | tui | `20260714_012850_992578` | 8/99/184 | `—` | — |
| default | `20260714_032503_c35046` | 2026-07-14 03:25 UTC | tui | `20260714_023558_3a7c70` | 7/84/159 | `—` | — |
| default | `20260714_040859_2b8be1` | 2026-07-14 04:08 UTC | tui | `20260714_032503_c35046` | 7/86/161 | `—` | Bora Capital Backend Security Hardening |
| coder | `20260714_133535_83849e` | 2026-07-14 13:35 UTC | tui | — | 8/97/158 | `/Users/acazumah/Documents/Kusantec/bora-capital-backend` | Why the Hermes Chat Disappeared |
| coder | `20260714_183503_dea58d` | 2026-07-14 18:35 UTC | tui | `20260714_133535_83849e` | 4/85/186 | `—` | Why the Hermes Chat Disappeared #2 |
| coder | `20260714_183525_94e0a9` | 2026-07-14 18:35 UTC | subagent | `20260714_183503_dea58d` | 1/9/62 | `—` | — |
| coder | `20260714_183912_6a19ae` | 2026-07-14 18:39 UTC | subagent | `20260714_183503_dea58d` | 1/7/60 | `—` | — |
| coder | `20260714_183912_f8d4bd` | 2026-07-14 18:39 UTC | subagent | `20260714_183503_dea58d` | 1/24/123 | `—` | — |
| coder | `20260714_185052_a2dc32` | 2026-07-14 18:50 UTC | tui | `20260714_183503_dea58d` | 5/128/232 | `—` | Why the Hermes Chat Disappeared #3 |
| coder | `20260714_191715_4cf650` | 2026-07-14 19:17 UTC | tui | `20260714_185052_a2dc32` | 6/164/293 | `—` | Why the Hermes Chat Disappeared #4 |
| coder | `20260714_202812_edffb3` | 2026-07-14 20:28 UTC | tui | `20260714_191715_4cf650` | 7/138/225 | `—` | Why the Hermes Chat Disappeared #5 |
| coder | `20260714_213232_242ff1` | 2026-07-14 21:32 UTC | tui | `20260714_202812_edffb3` | 12/172/281 | `—` | Why the Hermes Chat Disappeared #6 |
| coder | `20260715_002615_32b411` | 2026-07-15 00:26 UTC | tui | `20260714_213232_242ff1` | 9/158/259 | `—` | Why the Hermes Chat Disappeared #7 |
| coder | `20260715_005953_b67276` | 2026-07-15 00:59 UTC | tui | `20260715_002615_32b411` | 11/182/291 | `—` | Why the Hermes Chat Disappeared #8 |
| coder | `20260715_181830_be101e` | 2026-07-15 18:18 UTC | tui | `20260715_005953_b67276` | 10/161/286 | `—` | Why the Hermes Chat Disappeared #9 |
| coder | `20260715_200452_06f795` | 2026-07-15 20:04 UTC | subagent | `20260715_181830_be101e` | 1/20/118 | `—` | — |
| coder | `20260715_201033_443f8f` | 2026-07-15 20:10 UTC | tui | `20260715_181830_be101e` | 8/147/281 | `—` | Why the Hermes Chat Disappeared #10 |
| coder | `20260715_203208_7a74a9` | 2026-07-15 20:32 UTC | subagent | `20260715_201033_443f8f` | 1/14/76 | `—` | — |
| coder | `20260715_203209_6f27b3` | 2026-07-15 20:32 UTC | subagent | `20260715_201033_443f8f` | 1/14/81 | `—` | — |
| coder | `20260715_204220_9f3dd0` | 2026-07-15 20:42 UTC | tui | `20260715_201033_443f8f` | 8/169/285 | `—` | Why the Hermes Chat Disappeared #11 |
| coder | `20260715_204557_aa120b` | 2026-07-15 20:46 UTC | subagent | `20260715_204220_9f3dd0` | 1/3/11 | `—` | — |
| coder | `20260715_204600_cb30e1` | 2026-07-15 20:46 UTC | subagent | `20260715_204220_9f3dd0` | 1/3/12 | `—` | — |
| coder | `20260715_233938_1a601a` | 2026-07-15 23:39 UTC | subagent | `20260715_204220_9f3dd0` | 1/4/7 | `—` | — |
| coder | `20260716_011320_32adde` | 2026-07-16 01:13 UTC | tui | `20260715_204220_9f3dd0` | 15/181/245 | `—` | Why the Hermes Chat Disappeared #12 |
| coder | `20260716_011414_c16be5` | 2026-07-16 01:14 UTC | subagent | `20260716_011320_32adde` | 1/10/50 | `—` | — |
| coder | `20260716_011615_f133bf` | 2026-07-16 01:16 UTC | subagent | `20260716_011320_32adde` | 1/8/35 | `—` | — |
| coder | `20260716_020627_6d5133` | 2026-07-16 02:06 UTC | subagent | `20260716_011320_32adde` | 1/14/72 | `—` | — |
| coder | `20260716_020627_8775c5` | 2026-07-16 02:06 UTC | subagent | `20260716_011320_32adde` | 1/9/37 | `—` | — |
| coder | `20260716_040411_a5d7e6` | 2026-07-16 04:04 UTC | tui | `20260716_011320_32adde` | 10/133/177 | `—` | Why the Hermes Chat Disappeared #13 |
| coder | `20260716_040747_e645b9` | 2026-07-16 04:07 UTC | subagent | `20260716_040411_a5d7e6` | 1/6/33 | `—` | — |
| coder | `20260716_041205_9a9677` | 2026-07-16 04:12 UTC | tui | `20260716_040411_a5d7e6` | 8/141/188 | `—` | Why the Hermes Chat Disappeared #14 |
| coder | `20260716_041610_edd491` | 2026-07-16 04:16 UTC | subagent | `20260716_041205_9a9677` | 1/5/12 | `—` | — |
| coder | `20260716_042002_bbf4de` | 2026-07-16 04:20 UTC | subagent | `20260716_041205_9a9677` | 1/6/31 | `—` | — |
| coder | `20260716_042317_bee1bf` | 2026-07-16 04:23 UTC | tui | `20260716_041205_9a9677` | 11/174/299 | `—` | Why the Hermes Chat Disappeared #15 |
| coder | `20260716_045653_001730` | 2026-07-16 04:56 UTC | subagent | `20260716_042317_bee1bf` | 1/6/25 | `—` | — |
| coder | `20260716_050131_3b8c11` | 2026-07-16 05:01 UTC | subagent | `20260716_042317_bee1bf` | 1/21/68 | `—` | — |
| coder | `20260716_052127_c0e9a7` | 2026-07-16 05:21 UTC | tui | `20260716_042317_bee1bf` | 11/154/288 | `—` | Why the Hermes Chat Disappeared #16 |
| coder | `20260716_052225_3bb05e` | 2026-07-16 05:22 UTC | subagent | `20260716_052127_c0e9a7` | 1/23/101 | `—` | — |
| coder | `20260716_052225_e5630a` | 2026-07-16 05:22 UTC | subagent | `20260716_052127_c0e9a7` | 1/12/72 | `—` | — |
| coder | `20260716_053052_e46a8a` | 2026-07-16 05:30 UTC | subagent | `20260716_052127_c0e9a7` | 1/7/21 | `—` | — |
| coder | `20260716_132850_7d7193` | 2026-07-16 13:28 UTC | subagent | `20260716_052127_c0e9a7` | 1/9/23 | `—` | — |
| coder | `20260716_132850_4f4bea` | 2026-07-16 13:28 UTC | subagent | `20260716_052127_c0e9a7` | 1/9/40 | `—` | — |
| coder | `20260716_134549_6f6505` | 2026-07-16 13:45 UTC | tui | `20260716_052127_c0e9a7` | 12/156/216 | `—` | Why the Hermes Chat Disappeared #17 |
| coder | `20260716_141616_824755` | 2026-07-16 14:16 UTC | subagent | `20260716_134549_6f6505` | 1/8/50 | `—` | — |
| coder | `20260716_141616_6c4845` | 2026-07-16 14:16 UTC | subagent | `20260716_134549_6f6505` | 1/9/54 | `—` | — |
| coder | `20260716_142249_3aba14` | 2026-07-16 14:22 UTC | tui | `20260716_134549_6f6505` | 12/196/240 | `—` | Why the Hermes Chat Disappeared #18 |
| coder | `20260716_144054_fac8c1` | 2026-07-16 14:41 UTC | subagent | `20260716_142249_3aba14` | 1/10/53 | `—` | — |
| coder | `20260716_144053_1c0e34` | 2026-07-16 14:41 UTC | subagent | `20260716_142249_3aba14` | 1/10/53 | `—` | — |
| coder | `20260716_144609_559128` | 2026-07-16 14:46 UTC | tui | `20260716_142249_3aba14` | 7/162/182 | `—` | Why the Hermes Chat Disappeared #19 |
| coder | `20260716_144830_9d75d1` | 2026-07-16 14:48 UTC | subagent | `20260716_144609_559128` | 1/8/38 | `—` | — |
| coder | `20260716_144830_3a5fc0` | 2026-07-16 14:48 UTC | subagent | `20260716_144609_559128` | 1/7/25 | `—` | — |
| coder | `20260716_145633_80e818` | 2026-07-16 14:56 UTC | subagent | `20260716_144609_559128` | 1/5/15 | `—` | — |
| coder | `20260716_145633_02fad2` | 2026-07-16 14:56 UTC | subagent | `20260716_144609_559128` | 1/8/38 | `—` | — |
| coder | `20260716_150130_fcc0ef` | 2026-07-16 15:01 UTC | tui | `20260716_144609_559128` | 8/209/269 | `—` | Why the Hermes Chat Disappeared #20 |
| coder | `20260716_155115_1fa600` | 2026-07-16 15:51 UTC | subagent | `20260716_150130_fcc0ef` | 1/19/87 | `—` | — |
| coder | `20260716_155115_488059` | 2026-07-16 15:51 UTC | subagent | `20260716_150130_fcc0ef` | 1/11/61 | `—` | — |
| coder | `20260716_155115_0b0797` | 2026-07-16 15:51 UTC | subagent | `20260716_150130_fcc0ef` | 1/16/79 | `—` | — |
| coder | `20260716_171024_ddce8b` | 2026-07-16 17:10 UTC | tui | `20260716_150130_fcc0ef` | 2/196/248 | `—` | Why the Hermes Chat Disappeared #21 |
| coder | `20260716_173214_22d63d` | 2026-07-16 17:32 UTC | subagent | `20260716_171024_ddce8b` | 1/12/33 | `—` | — |
| coder | `20260716_173214_2437ce` | 2026-07-16 17:32 UTC | subagent | `20260716_171024_ddce8b` | 1/6/25 | `—` | — |
| coder | `20260716_173700_e3851f` | 2026-07-16 17:37 UTC | tui | `20260716_171024_ddce8b` | 6/185/237 | `—` | Why the Hermes Chat Disappeared #22 |
| coder | `20260716_173752_fd81a8` | 2026-07-16 17:38 UTC | subagent | `20260716_173700_e3851f` | 1/5/17 | `—` | — |
| coder | `20260716_173755_6078bf` | 2026-07-16 17:38 UTC | subagent | `20260716_173700_e3851f` | 1/8/34 | `—` | — |
| coder | `20260716_181502_464de1` | 2026-07-16 18:15 UTC | tui | `20260716_173700_e3851f` | 9/106/152 | `—` | Why the Hermes Chat Disappeared #23 |
| coder | `20260716_181546_2e00d0` | 2026-07-16 18:15 UTC | subagent | `20260716_181502_464de1` | 1/5/8 | `—` | — |
| coder | `20260716_181546_c65a1b` | 2026-07-16 18:15 UTC | subagent | `20260716_181502_464de1` | 1/6/18 | `—` | — |
| coder | `20260716_182027_8f941b` | 2026-07-16 18:20 UTC | subagent | `20260716_181502_464de1` | 1/3/4 | `—` | — |
| coder | `20260716_182027_5fc7a6` | 2026-07-16 18:20 UTC | subagent | `20260716_181502_464de1` | 1/3/6 | `—` | — |
| coder | `20260716_190101_fc7c91` | 2026-07-16 19:01 UTC | tui | `20260716_181502_464de1` | 9/129/177 | `—` | Why the Hermes Chat Disappeared #24 |
| coder | `20260716_193747_0a913b` | 2026-07-16 19:37 UTC | subagent | `20260716_190101_fc7c91` | 1/10/32 | `—` | — |
| coder | `20260716_193747_20bfc5` | 2026-07-16 19:37 UTC | subagent | `20260716_190101_fc7c91` | 1/9/19 | `—` | — |
| coder | `20260716_195151_d31746` | 2026-07-16 19:51 UTC | tui | `20260716_190101_fc7c91` | 10/165/227 | `—` | Why the Hermes Chat Disappeared #25 |
| coder | `20260716_195456_fe2d5c` | 2026-07-16 19:54 UTC | subagent | `20260716_195151_d31746` | 1/7/19 | `—` | — |
| coder | `20260716_195456_98325c` | 2026-07-16 19:54 UTC | subagent | `20260716_195151_d31746` | 1/6/23 | `—` | — |
| coder | `20260716_213123_3e04a2` | 2026-07-16 21:31 UTC | tui | `20260716_195151_d31746` | 7/139/192 | `—` | Why the Hermes Chat Disappeared #26 |
| coder | `20260716_220448_5c8635` | 2026-07-16 22:04 UTC | tui | `20260716_213123_3e04a2` | 5/124/175 | `—` | Why the Hermes Chat Disappeared #27 |
| coder | `20260716_220513_ae849e` | 2026-07-16 22:05 UTC | subagent | `20260716_220448_5c8635` | 1/8/39 | `—` | — |
| coder | `20260716_220513_ae7cea` | 2026-07-16 22:05 UTC | subagent | `20260716_220448_5c8635` | 1/8/39 | `—` | — |
| coder | `20260716_221628_2126ad` | 2026-07-16 22:16 UTC | tui | `20260716_220448_5c8635` | 8/173/252 | `—` | Why the Hermes Chat Disappeared #28 |
| coder | `20260716_224305_4b2a58` | 2026-07-16 22:43 UTC | tui | `20260716_221628_2126ad` | 6/166/249 | `—` | Why the Hermes Chat Disappeared #29 |
| coder | `20260716_224618_1a873c` | 2026-07-16 22:46 UTC | subagent | `20260716_224305_4b2a58` | 1/6/15 | `—` | — |
| coder | `20260716_224618_14fe35` | 2026-07-16 22:46 UTC | subagent | `20260716_224305_4b2a58` | 1/7/12 | `—` | — |
| coder | `20260716_231039_7e0d66` | 2026-07-16 23:10 UTC | subagent | `20260716_224305_4b2a58` | 1/9/21 | `—` | — |
| coder | `20260716_231039_f71924` | 2026-07-16 23:10 UTC | subagent | `20260716_224305_4b2a58` | 1/14/40 | `—` | — |
| coder | `20260716_232659_ef9122` | 2026-07-16 23:26 UTC | tui | `20260716_224305_4b2a58` | 9/144/202 | `—` | Why the Hermes Chat Disappeared #30 |
| coder | `20260716_233024_c6edb3` | 2026-07-16 23:30 UTC | subagent | `20260716_232659_ef9122` | 1/15/30 | `—` | — |
| coder | `20260716_233024_c02cbd` | 2026-07-16 23:30 UTC | subagent | `20260716_232659_ef9122` | 1/8/24 | `—` | — |
| coder | `20260716_235715_eb761b` | 2026-07-16 23:57 UTC | subagent | `20260716_232659_ef9122` | 1/10/31 | `—` | — |
| coder | `20260716_235715_bfffc6` | 2026-07-16 23:57 UTC | subagent | `20260716_232659_ef9122` | 1/8/18 | `—` | — |
| coder | `20260717_000211_40b097` | 2026-07-17 00:02 UTC | tui | `20260716_232659_ef9122` | 15/182/258 | `—` | Why the Hermes Chat Disappeared #31 |
| coder | `20260717_000247_351653` | 2026-07-17 00:02 UTC | subagent | `20260717_000211_40b097` | 1/4/7 | `—` | — |
| coder | `20260717_012053_f6e610` | 2026-07-17 01:20 UTC | subagent | `20260717_000211_40b097` | 1/7/14 | `—` | — |
| coder | `20260717_012053_ec3050` | 2026-07-17 01:20 UTC | subagent | `20260717_000211_40b097` | 1/7/19 | `—` | — |
| coder | `20260717_022802_282505` | 2026-07-17 02:28 UTC | subagent | `20260717_000211_40b097` | 1/8/23 | `—` | — |
| coder | `20260717_022802_dae7c4` | 2026-07-17 02:28 UTC | subagent | `20260717_000211_40b097` | 1/7/18 | `—` | — |
| coder | `20260717_030456_05ca85` | 2026-07-17 03:04 UTC | subagent | `20260717_000211_40b097` | 1/17/109 | `—` | — |
| coder | `20260717_030456_451f29` | 2026-07-17 03:04 UTC | subagent | `20260717_000211_40b097` | 1/11/71 | `—` | — |
| coder | `20260717_030456_d39520` | 2026-07-17 03:04 UTC | subagent | `20260717_000211_40b097` | 1/13/117 | `—` | — |
| coder | `20260717_104556_c85f75` | 2026-07-17 10:45 UTC | tui | `20260717_000211_40b097` | 7/156/234 | `—` | Why the Hermes Chat Disappeared #32 |
| coder | `20260717_111529_f0e89d` | 2026-07-17 11:15 UTC | tui | `20260717_104556_c85f75` | 4/135/198 | `—` | Why the Hermes Chat Disappeared #33 |
| coder | `20260717_120442_3d7a6d` | 2026-07-17 12:04 UTC | tui | `20260717_111529_f0e89d` | 4/177/279 | `—` | Why the Hermes Chat Disappeared #34 |
| coder | `20260717_120500_543cf4` | 2026-07-17 12:05 UTC | subagent | `20260717_120442_3d7a6d` | 1/18/92 | `—` | — |
| coder | `20260717_120500_53a51a` | 2026-07-17 12:05 UTC | subagent | `20260717_120442_3d7a6d` | 1/16/87 | `—` | — |
| coder | `20260717_120500_08a772` | 2026-07-17 12:05 UTC | subagent | `20260717_120442_3d7a6d` | 1/22/124 | `—` | — |
| coder | `20260717_125037_b7fd83` | 2026-07-17 12:50 UTC | tui | `20260717_120442_3d7a6d` | 6/156/255 | `—` | Why the Hermes Chat Disappeared #35 |
| coder | `20260717_132130_8a40fd` | 2026-07-17 13:21 UTC | subagent | `20260717_125037_b7fd83` | 1/28/134 | `—` | — |
| coder | `20260717_160904_8adba5` | 2026-07-17 16:09 UTC | tui | `20260717_125037_b7fd83` | 11/161/224 | `—` | Why the Hermes Chat Disappeared #36 |
| coder | `20260717_181727_d2d2a0` | 2026-07-17 18:17 UTC | tui | `20260717_160904_8adba5` | 11/125/190 | `—` | Why the Hermes Chat Disappeared #37 |
| coder | `20260717_185333_99a99e` | 2026-07-17 18:53 UTC | tui | `20260717_181727_d2d2a0` | 10/111/169 | `—` | Why the Hermes Chat Disappeared #38 |
| coder | `20260717_210544_8446e4` | 2026-07-17 21:05 UTC | tui | `20260717_185333_99a99e` | 14/110/196 | `—` | Why the Hermes Chat Disappeared #39 |
| coder | `20260717_231534_72cf41` | 2026-07-17 23:15 UTC | tui | `20260717_210544_8446e4` | 9/106/156 | `—` | Why the Hermes Chat Disappeared #40 |
| coder | `20260717_235541_b19a5b` | 2026-07-17 23:55 UTC | tui | `20260717_231534_72cf41` | 8/110/153 | `—` | Why the Hermes Chat Disappeared #41 |
| coder | `20260718_001950_896bb0` | 2026-07-18 00:19 UTC | tui | `20260717_235541_b19a5b` | 5/118/157 | `—` | Why the Hermes Chat Disappeared #42 |
| coder | `20260718_003414_a6fd49` | 2026-07-18 00:34 UTC | tui | `20260718_001950_896bb0` | 6/150/180 | `—` | Why the Hermes Chat Disappeared #43 |
| coder | `20260718_005111_f5dcf8` | 2026-07-18 00:51 UTC | tui | `20260718_003414_a6fd49` | 5/125/151 | `—` | Why the Hermes Chat Disappeared #44 |
| coder | `20260718_010140_297ee6` | 2026-07-18 01:01 UTC | tui | `20260718_005111_f5dcf8` | 6/124/149 | `—` | Why the Hermes Chat Disappeared #45 |
| coder | `20260718_010657_7ecbd1` | 2026-07-18 01:06 UTC | tui | `20260718_010140_297ee6` | 7/115/155 | `—` | Why the Hermes Chat Disappeared #46 |
| coder | `20260718_012431_daf649` | 2026-07-18 01:24 UTC | tui | `20260718_010657_7ecbd1` | 7/101/155 | `—` | Why the Hermes Chat Disappeared #47 |
| coder | `20260718_013411_326127` | 2026-07-18 01:34 UTC | tui | `20260718_012431_daf649` | 9/129/208 | `—` | Why the Hermes Chat Disappeared #48 |
| coder | `20260718_021347_9fb223` | 2026-07-18 02:13 UTC | subagent | `20260718_013411_326127` | 1/9/66 | `—` | — |
| coder | `20260718_021347_a6ab13` | 2026-07-18 02:13 UTC | subagent | `20260718_013411_326127` | 1/16/85 | `—` | — |
| coder | `20260718_021347_478188` | 2026-07-18 02:13 UTC | subagent | `20260718_013411_326127` | 1/32/243 | `—` | — |
| coder | `20260718_022352_230954` | 2026-07-18 02:23 UTC | subagent | `20260718_021347_478188` | 2/28/167 | `—` | — |
| coder | `20260718_022740_80c5a4` | 2026-07-18 02:27 UTC | tui | `20260713_173225_73e447` | 7/66/170 | `—` | Partner Mobile App Setup #3 |
| coder | `20260718_023215_ef5e17` | 2026-07-18 02:32 UTC | tui | `20260718_013411_326127` | 5/169/265 | `—` | Why the Hermes Chat Disappeared #49 |
| coder | `20260718_030844_e9e1dc` | 2026-07-18 03:08 UTC | tui | `20260718_022740_80c5a4` | 2/48/143 | `—` | Partner Mobile App Setup #4 |
| coder | `20260718_032701_a0bb20` | 2026-07-18 03:27 UTC | tui | `20260718_023215_ef5e17` | 2/136/225 | `—` | Why the Hermes Chat Disappeared #50 |
| coder | `20260718_035439_fd6fd5` | 2026-07-18 03:54 UTC | tui | `20260718_032701_a0bb20` | 3/148/327 | `—` | Why the Hermes Chat Disappeared #51 |
| coder | `20260718_042843_74753d` | 2026-07-18 04:28 UTC | tui | `20260718_035439_fd6fd5` | 6/100/223 | `—` | Why the Hermes Chat Disappeared #52 |
| coder | `20260718_201747_c255ab` | 2026-07-18 20:17 UTC | tui | — | 6/57/173 | `/Users/acazumah/Documents/C.E.Q.A/altin-partner-mobile` | Casual Greeting with Caleb |
| coder | `20260718_223853_6755f9` | 2026-07-18 22:38 UTC | tui | `20260718_201747_c255ab` | 10/99/241 | `/Users/acazumah/Documents/C.E.Q.A/altin-partner-mobile` | Casual Greeting with Caleb #2 |
| coder | `20260719_015234_50d0c5` | 2026-07-19 01:52 UTC | tui | `20260718_223853_6755f9` | 14/157/352 | `—` | Casual Greeting with Caleb #3 |
| coder | `20260719_035336_d709a6` | 2026-07-19 03:53 UTC | desktop | `20260719_015234_50d0c5` | 14/166/328 | `—` | Casual Greeting with Caleb #4 |
| default | `20260720_193333_054b33` | 2026-07-20 19:33 UTC | desktop | — | 6/89/158 | `/Users/acazumah/Documents/Kusantec/bora-capital-backend` | — |
| coder | `20260720_193333_054b33` | 2026-07-20 19:44 UTC | unknown | — | 3/61/111 | `—` | Migrate Error Logging to Sentry |
| default | `20260720_232004_8ea4d4` | 2026-07-20 23:20 UTC | desktop | — | 3/45/123 | `—` | — |
| coder | `20260720_232004_8ea4d4` | 2026-07-20 23:25 UTC | unknown | — | 0/0/0 | `—` | Hermes Obsidian Second Brain |
| default | `20260721_001007_1b1aea` | 2026-07-21 00:10 UTC | desktop | `20260720_232004_8ea4d4` | 7/58/119 | `—` | — |
| default | `20260721_013536_83fcd9` | 2026-07-21 01:35 UTC | desktop | `20260721_001007_1b1aea` | 5/64/136 | `—` | — |
| default | `20260721_020029_f66b3b` | 2026-07-21 02:00 UTC | desktop | `20260721_013536_83fcd9` | 4/54/132 | `—` | — |
| default | `20260721_030310_b2eb00` | 2026-07-21 03:03 UTC | subagent | `20260721_020029_f66b3b` | 1/9/57 | `—` | — |
| default | `20260721_030310_f5e43e` | 2026-07-21 03:03 UTC | subagent | `20260721_020029_f66b3b` | 1/12/71 | `—` | — |
| default | `20260721_030310_1cc0cd` | 2026-07-21 03:03 UTC | subagent | `20260721_020029_f66b3b` | 1/16/83 | `—` | — |
| default | `20260721_030948_da545b` | 2026-07-21 03:09 UTC | desktop | `20260721_020029_f66b3b` | 2/41/140 | `—` | — |
| default | `20260721_031558_72a825` | 2026-07-21 03:15 UTC | desktop | `20260721_030948_da545b` | 4/47/166 | `—` | — |
| default | `20260721_031617_ee4e93` | 2026-07-21 03:16 UTC | subagent | `20260721_031558_72a825` | 1/38/123 | `—` | — |
| default | `20260721_032543_0fdcc0` | 2026-07-21 03:25 UTC | desktop | `20260721_031558_72a825` | 4/32/79 | `—` | — |
| coder | `20260721_032543_0fdcc0` | 2026-07-21 03:30 UTC | unknown | — | 0/0/0 | `—` | Altin Batch Validation Status |
| default | `20260721_112003_2f277e` | 2026-07-21 11:20 UTC | desktop | `20260721_032543_0fdcc0` | 4/33/155 | `—` | — |
| default | `20260721_112249_06c630` | 2026-07-21 11:22 UTC | subagent | `20260721_112003_2f277e` | 1/12/69 | `—` | — |
| default | `20260721_112249_5609f0` | 2026-07-21 11:22 UTC | subagent | `20260721_112003_2f277e` | 1/8/11 | `—` | — |
| default | `20260721_112249_2b4948` | 2026-07-21 11:22 UTC | subagent | `20260721_112003_2f277e` | 1/13/14 | `—` | — |
| default | `20260721_112900_7e99fb` | 2026-07-21 11:29 UTC | subagent | `20260721_112003_2f277e` | 1/15/30 | `—` | — |
| default | `20260721_113041_3f113d` | 2026-07-21 11:30 UTC | desktop | `20260721_112003_2f277e` | 4/42/167 | `—` | — |
| coder | `20260721_113041_3f113d` | 2026-07-21 11:31 UTC | unknown | — | 0/0/0 | `—` | Portfolio Vault Knowledge Promotion |
| default | `20260721_150209_773080` | 2026-07-21 15:02 UTC | desktop | `20260721_113041_3f113d` | 4/62/158 | `—` | — |
| default | `20260721_151432_9567a2` | 2026-07-21 15:14 UTC | subagent | `20260721_150209_773080` | 1/16/57 | `—` | — |
| default | `20260721_151432_3e2a6d` | 2026-07-21 15:14 UTC | subagent | `20260721_150209_773080` | 1/10/56 | `—` | — |
| default | `20260721_151432_eee232` | 2026-07-21 15:14 UTC | subagent | `20260721_150209_773080` | 1/11/34 | `—` | — |
| default | `20260721_155121_9e9cc3` | 2026-07-21 15:51 UTC | desktop | `20260721_150209_773080` | 4/67/168 | `—` | — |
| default | `20260721_162605_759657` | 2026-07-21 16:26 UTC | desktop | `20260721_155121_9e9cc3` | 4/38/82 | `—` | — |
| default | `20260721_164555_84be3a` | 2026-07-21 16:45 UTC | desktop | `20260721_162605_759657` | 2/35/66 | `—` | — |
| coder | `20260721_164555_84be3a` | 2026-07-21 16:48 UTC | unknown | — | 1/8/19 | `—` | Approved Wiki Project Cleanup |
| coder | `20260721_171151_c0282f` | 2026-07-21 17:11 UTC | subagent | `20260721_164555_84be3a` | 1/5/25 | `—` | — |
| coder | `20260721_171151_8c3f09` | 2026-07-21 17:11 UTC | subagent | `20260721_164555_84be3a` | 1/7/30 | `—` | — |
| coder | `20260721_171151_bd030b` | 2026-07-21 17:11 UTC | subagent | `20260721_164555_84be3a` | 1/8/30 | `—` | — |

## Interpretation Boundaries

- `CWD` may be absent even when a conversation concerns a project; missing cwd is not evidence of irrelevance.
- Generic or empty titles are discovery metadata only. Classification requires reading the relevant user requests and final outcomes.
- Subagent sessions may duplicate a parent task and must not be promoted independently without distinct durable evidence.
- Historical verification must remain attributed to the session until rerun against current code.
