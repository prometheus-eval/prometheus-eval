# Web Browsing

Tasks that require generating actionable items while browsing through the web.

**Authors:** FILL IN ME

## Example

A sample query in a zero-shot setting:


### Input:
```
OBSERVATION:
[5000] Header: "All 'burgers' results in San Francisco, California"
[5001] Image: Photo of a burger from Maillards Smash Burgers
[5002] Business Listing: 'Maillards Smash Burgers'
[5003] Rating: '4.8 (15 reviews)'
[5004] Category Tags: 'Pop-Up Restaurants', 'Burgers', 'Outer Sunset'
[5005] Snippet: "We got The Box burger fy and drink combo which was super worth it for a bunch of fries and large..."
[5006] Button: 'more'
[5007] Image: Photo of a burger from Uncle Boy’s
[5008] Business Listing: 'Uncle Boy’s'
[5009] Rating: '3.9 (788 reviews)'
[5010] Category Tags: 'Burgers', 'Fast Food', '$$', 'Inner Richmond'
[5011] Snippet: "Back to my burger, the 1/3 lb. meat patty was obviously hand formed and fresh, the seeded bun was..."
[5012] Button: 'more'
[5013] Image: Photo of a burger from Roam Artisan Burgers
[5014] Business Listing: 'Roam Artisan Burgers'
[5015] Rating: '4.0 (1.4k reviews)'
[5016] Category Tags: 'Burgers', '$$', 'Lower Pacific Heights'
[5017] Snippet: "So hungry that I once again ordered the French & Fry Turkey Burger and another burger as well, but..."
[5018] Button: 'more'
URL: https://www.yelp.com/search?find_desc=Burgers&find_loc=San+Francisco%2C+CA

OBJECTIVE:
Find a burger shop in San Francisco with a 4.5+ rating on Yelp.

PREVIOUS ACTION:
type [2012][burger] [1]

NEXT ACTION:
```
### Output
```
Upon reviewing the Yelp search results, 'Maillards Smash Burgers' is identified as the first burger shop with a rating over 4.5, specifically a 4.8 rating. The objective is to note the name of this burger shop. Therefore, the task is complete, and no further actions are required on the webpage.

In summary, the next action I will perform is `stop [Maillards Smash Burgers]` since it meets the objective's criteria with a 4.8 rating.
```

## What is the task trying to measure?
Given an observation which is an accessibility tree of the website, a user query, and previous action history the model has to predict the current action.


## Motivation

FILL IN ME

## Related work

WebArena (https://arxiv.org/pdf/2307.13854.pdf)

Mind2Web (https://arxiv.org/pdf/2306.06070.pdf)
