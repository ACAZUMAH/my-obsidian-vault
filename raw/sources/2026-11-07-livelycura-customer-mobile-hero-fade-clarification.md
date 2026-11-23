# LivelyCura customer mobile: Home hero fades into the banner

Date: 2026-11-07
Source: direct user clarification in a `livelycura-customer-mobile` session, plus the code changed and verified in that session (paraphrased; one short quote).

After the second Home header pass, the user said the hero still did not follow the inspo: the background is "supposed to blurred at the bottom and stretched into the home banner". This corrects the agent's reading of the earlier remark that the hero background "doesn't reach the banner". The green does not stop with a hard edge above the banner. It stays solid behind the controls and fades softly into the page behind the banner.

Implemented (uncommitted, branch `feature/ui-updates`): `HomeHeader` renders one absolute `LinearGradient` backdrop behind the controls and the banner. It runs from `primary` to `#00A86B`, solid down to the measured bottom of the search bar, then to transparent by the banner's bottom. The rounded hard bottom edge was removed and the support banner moved back into the hero, over the fade. The status-bar strip switches to the page grey once the solid part has scrolled away. Verified on the iPhone 17 Pro simulator (iOS 26).
