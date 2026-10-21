# CheckCity Delivery Location Confirmation

- Date: 2026-09-14
- Author: user, with assistant-selected initial thresholds explicitly distinguished below.

## Direct request

> one last thing regarding the delivery fee and location, so in Ghana here some locations have same names so the customers makes a lotta mistakes by mistaking different location for their location when ordering, even tho we already preset for them. so wehn they decide to change the location and we calculate the estimate we need to limit the how far their location is to the branch. so what I want us to do it when do that and the estimate is calculated we check the distance and the delivery price and if it exceeds some certain limit that we show a modal with price and distance ask them to check the location very well that's where they are and are willing to pay

## Threshold clarification

Asked which distance and fee thresholds to use, the user answered:

> suggest that and let's see

Asked whether to retain the existing hard limit, the user answered:

> Keep the 20 km hard limit

## Initial implementation choice

The assistant selected a warning above 10 km or GH₵50, with the existing 20 km hard limit retained. The warning thresholds are initial configurable values, not a user-validated pricing policy.
