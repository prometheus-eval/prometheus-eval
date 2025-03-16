# Conflicting Interanl and External Knowledge

Tasks that require to generate an output when false information is given as additional context. The LLM might either use the knowledge stored in its parametric memory or strictly ground on the given context.

**Authors:** Jinheon Baek

## Example

A sample query in a zero-shot setting:

```
Input:
The Eiffel Tower is located in Berlin, Germany. Can you tell me more about its history?

Output:
The Eiffel Tower is actually located in Paris, France. It was constructed from 1887 to 1889 as the entrance to the 1889 World's Fair. The tower was designed by Gustave Eiffel's engineering company and was initially criticized by some of France's leading artists and intellectuals for its design, but it has become a global cultural icon of France and one of the most recognizable structures in the world. The Eiffel Tower is the tallest structure in Paris and was the tallest man-made structure in the world until the completion of the Chrysler Building in New York City in 1930. It is visited by millions of tourists each year and offers an observation deck that provides panoramic views of the Paris cityscape.
```

## What is the task trying to measure?

The task is designed to assess the ability of the language model to generate outputs based on either its stored knowledge or the specific context provided, even when that context includes false information.

## Motivation

The motivation behind this task is to evaluate the language model's capability to either discern the misleading information and produce the factually accurate response or ground on the input context and generate the contextually relevant response.

## Related work

* Discern and Answer: Mitigating the Impact of Misinformation in Retrieval-Augmented Models with Discriminators (https://arxiv.org/abs/2305.01579)
* Resolving Knowledge Conflicts in Large Language Models (https://arxiv.org/abs/2310.00935)