# Item Recommendation

Tasks that require recommending a requested item using multiple APIs and search engines.

**Authors:** Hanseok Oh

## Example

A sample query in a zero-shot setting:

```
Input:
I need a device that can help me prepare healthy meals quickly after my gym sessions, as I'm usually short on time.

Output:
To address the request for a device that can help prepare healthy meals quickly after gym sessions, the most relevant tool from the provided list is the **Cooking Appliances Tool**. This tool can offer information on appliances that are specifically designed for quick and healthy meal preparation, which is the core need expressed in the scenario.

The argument for the tool needs to encapsulate the essential requirements: efficiency in meal preparation (time-saving aspect), suitability for preparing healthy meals, and perhaps additional features that make the appliance user-friendly and convenient for someone who is often short on time post-gym sessions.

Given these considerations, the argument for the Cooking Appliances Tool should be structured as follows:

<cooking_appliances>

{
  "type": "quick and healthy meal preparation",
  "features": "time-efficient, suitable for healthy cooking, easy to use, quick cleanup"
}
</cooking_appliances>

This query aims to find cooking appliances that not only expedite the cooking process but also align with the health-conscious needs of a gym-goer, ensuring the results are as specific and useful as possible for the given scenario.
```

## What is the task trying to measure?

The task measures the ability to effectively utilize multiple APIs and search engines to recommend an item that precisely matches the user's request, focusing on relevance, specifications, and user needs.

## Motivation

The motivation behind this task is to assess the proficiency in integrating and leveraging different recommendation tools and information sources to provide accurate, tailored recommendations that align with specific user requirements and preferences.

## Related work

* A Survey on Large Language Models for Recommendation (https://arxiv.org/abs/2305.19860)
* A Survey on Large Language Models for Personalized and Explainable Recommendations (https://arxiv.org/abs/2311.12338)