# Search Engine

Tasks that involve the use of search engines and generating effective search queries.

**Authors:** Hanseok Oh

## Example

A sample query in a zero-shot setting:

```
Input:
What is the adoption rate of electric vehicles in Europe? Provide the most current trends.  
The current time and date is: 2024 January 24th.

Output:
To find the most current trends regarding the adoption rate of electric vehicles in Europe, I'll use the Search Engine tool. The query needs to be focused on retrieving the latest statistics or reports on this topic. Since we're looking for the most recent information, it's crucial to include terms like "2024", "current", "latest", or "recent" in the query, along with "adoption rate", "electric vehicles", and "Europe". This should help in finding articles, studies, or reports that contain the latest data on electric vehicle adoption in Europe.

Here's how the search query will be formatted:

`<search>electric vehicle adoption rate Europe 2024 current trends</search>`

This query should retrieve documents that provide the latest information on the adoption rate of electric vehicles in Europe as of 2024.
```

## What is the task trying to measure?

The task aims to evaluate the effectiveness of using search engines for information retrieval. It measures the ability to generate precise and relevant search queries, the skill in selecting appropriate sources from search results, and the proficiency in extracting and synthesizing information to provide accurate and concise answers.

## Motivation

The motivation for evaluating the usage of "search eninge" tool stems from the inherent limitations of naive language models in accessing and providing up-to-date or highly specialized information. Language models, while knowledgeable, often rely on pre-existing training data and may not have the latest information or detailed knowledge in niche areas. Therefore, the ability to use search engines effectively becomes crucial. This task aims to compensate for these limitations by leveraging search engines to access the most recent or specific information, ensuring that responses remain relevant, accurate, and comprehensive.

## Related work

* WebGPT: Browser-assisted question-answering with human feedback (https://arxiv.org/abs/2112.09332)
* Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection (https://arxiv.org/abs/2310.11511)
* Enabling Large Language Models to Generate Text with Citations (https://arxiv.org/abs/2305.14627)