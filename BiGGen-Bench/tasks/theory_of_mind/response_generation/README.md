# Response Generation

Tasks that require to generate a next response after comprehending and inferring the mental state of the opponent.

**Authors:** Miyoung Ko (miyoungko@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
Emily and John, childhood friends and neighbors, share a passion for gardening, often exchanging plants and tips.
One day, Emily spots a rare flower in John's garden, which she's struggled to grow in her own. Impressed yet envious, she decides to pay John a visit.
The next day, John discovers the rare flower missing from his garden, suspecting a neighbor's involvement.
Later that day, Emily comes to visit John with a pot containing a young plant of the same rare flower, saying she wanted to surprise him with a gift.

Question: What would John's response be, and why would he say that?

Output:
Considering John's recent discovery of his rare flower being plucked and Emily's subsequent gift of the same type of flower, John might feel conflicted because while he might suspect Emily, he also values their long-standing friendship.
John might choose to tactfully express his gratitude for Emily's gift while also sharing his feelings of disappointment about the flower being plucked from his garden.
He could approach the subject by saying something like,
"Thank you for this beautiful plant, Emily. It means a lot, especially since I was sad to find my own flower missing this morning."
```

## What is the task trying to measure?

This task evaluates a model's ability to generate responses by inferring underlying thoughts and emotions from various input texts. Each instance measures the following abilities:

- Response generation from observations while considering the character's awareness (Q1, Q2).
- Predicting the next response of a given character based on a conversation (Q3, Q4).
- Predicting the response as an advisor after reading the story (Q5)

## Motivation

Response generation evaluates a model's capacity to produce responses after comprehending and making inferences about an opponent's mental state. This serves as a benchmark for assessing the model's ability to mimic human-like understanding and interactions. This task emphasizes the significance of language models being able to infer and consider underlying motives, emotions, and relationships in human interactions, thereby testing and enhancing their proficiency in comprehending and engaging in human-like dialogues. It represents a step towards the creation of AI that can interact with humans more accurately in various contexts.

## Related work

[1] Chae et al., (2023) Dialogue Chain-of-Thought Distillation for Commonsense-aware Conversational Agents. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP), pp 5606-5632.

