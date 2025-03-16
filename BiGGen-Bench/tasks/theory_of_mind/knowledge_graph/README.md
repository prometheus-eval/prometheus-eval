# Knowledge Graph

Tasks designed to assess the model's ability to construct a knowledge graph representing both first-order and second-order Theory of Mind.

**Authors:** Miyoung Ko (miyoungko@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
My wife made a trip to Harrison's Grocer, aiming to pick up some fresh flounder, my favorite type of white fish, for our weekend dinner.
To her dismay, the seafood counter was only stocked with cuts of salmon and bluefish.
After a brief consideration and a chat with the fishmonger, she settled for a frozen fillet of cod.
Later, as she recounted her shopping adventure, I assured her with a smile,
"Don't worry, I'm not particular about it; it's the thought and effort that count."

The list of subject, target, target_of_target: [Me, Wife] 

Output:
[Me, Wife, Me, disappointed, not getting desired fish]
[Wife, Me, favour, white fish]
[Wife, Me, prefer, frozen fillet of cod] 
[Me, Wife, consider, my preference]
```

## What is the task trying to measure?

This task measures a model's ability to construct a knowledge graph of individuals' beliefs from various input texts and various second-order belief types. Each instance aims to measure the following abilities: 

- Knowledge graph construction of cyclic second-order beliefs from the story and conversation Q1, Q2)
- Knowledge graph construction of acyclic second-order beliefs from the story, conversation, and debate (Q3, Q4, Q5)

## Motivation

The objective of the task is to evaluate a model's proficiency in constructing knowledge graphs for both first-order and second-order Theory of Mind (ToM) by representing others' beliefs (first-order ToM) and how individuals perceive the thoughts and beliefs of others (second-order ToM) using symbolic representation. Employing symbolic representation of belief states enables more interpretable reasoning involving human mental states and social dynamics.

## Related work

[1] Melanie Sclar, et al. (2023) Minding Language Models' (Lack of) Theory of Mind: A Plug-and-Play Multi-Character Belief Tracker. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL), pp 13960–13980. 
