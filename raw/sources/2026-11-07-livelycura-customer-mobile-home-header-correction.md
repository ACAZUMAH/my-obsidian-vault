# LivelyCura customer mobile: Home header follows the inspo layout

Date: 2026-11-07
Source: direct user correction in a `livelycura-customer-mobile` session, plus the code changed and verified in that session (paraphrased).

After the first glass Home build, the user said the agent had not looked at the inspiration closely: from Categories down was right, but the top was not. Their corrections: the location picker stays on the left where it was; the favourite and profile buttons go on the right; the greeting is removed; and the green hero background does not reach the banner, it ends below the search bar.

Implemented (uncommitted, branch `feature/ui-updates`): the green gradient header now holds only the location picker (left), glass Favourites, Notifications (signed-in only, kept from the old header) and Profile buttons (right), and the search and filter row. The support card moved out of the header onto the page directly below it, restyled as a solid green gradient card, since glass over the grey page would leave its white text unreadable. The greeting and its helper were deleted. Verified on the iPhone 17 Pro simulator (iOS 26), including the status-bar strip switching from green to the page grey once the header scrolls away.
