# Travel Planning

Tasks that require the LLM to write a travel plan to different destinations with different requirements from the user.

**Authors:** Yoonjoo Lee (yoonjoo.lee@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
Design a travel plan for a tourist traveling to the given destination. The tourist has a list of requirements and you should design your plan such that it satisfies all of these requirements. 

Destination: Paris

Requirements:
 - Total Duration: 2 days and 1 night
 - Transportation: Walk
 - Must Have: Eiffel Tower, Louvre Museum
 - Optional: Croissant, Onion Soup, Notre Dame Cathedral

Output:
Day 1 - Morning:
 - Visit the Louvre Museum (3 hours)
 - Walk to Café de Flore (15 minutes)
Day 1 - Lunch:
 - Café de Flore - Enjoy croissants and French cuisine (1 hour)
Day 1 - Afternoon:
 - Walk to Notre Dame Cathedral (20 minutes)
 - Explore Notre Dame (1.5 hours)
 - Walk to Eiffel Tower (1 hour)
Day 1 - Evening:
 - Visit Eiffel Tower (2 hours)
 - Walk to Le Petit Cler (15 minutes)
Day 1 - Dinner:
 - Le Petit Cler - Try Escargot and French Onion Soup (1.5 hours)

Day 2 - Morning:
 - Leisure time around Eiffel Tower area (1 hour)
 - Walk to Sainte-Chapelle (1 hour)
Day 2 - Midday:
 - Visit Sainte-Chapelle (1 hour)
 - Walk to nearby café (20 minutes)
Day 2 - Lunch:
 - Les Deux Magots - Experience Parisian café culture (1 hour)
Day 2 - Afternoon:
 - Stroll along the Seine River, enjoy local street food and shops (2 hours)
```

## What is the task trying to measure?

The task is designed to measure the ability of the language model to construct plans that satisfies multiple requirements/constraints while considering knowledge about real-world locations, understanding of spatio-temporal relationships regarding locations, and commonsense knowledge of human or tourist preferences.

## Motivation

The motivation behind this task is that it can serve to enhance the capability of language model's to construct complex plans that consider factors and constraints in the real-world. Furthermore, as evidenced by prior human-computer interaction research on facilitating travel planning and the large number of travel planning applications, humans struggle with travel planning and this task can thus enable more pratical applications of language models.

## Related work

Human Computation Tasks with Global Constraints (CHI 2012, https://dl.acm.org/doi/abs/10.1145/2207676.2207708)
Using Generative AI for Travel Inspiration and Discovery (Google for Developers Blog, https://developers.googleblog.com/2023/05/generative-ai-travel-developers.html)