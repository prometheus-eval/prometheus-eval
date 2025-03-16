# Following Lexical Constraints

Tasks that require to generate a response, thoroughly following a given lexical constraints. These constraints can include various limitations such as format, beginning words, or inclusion.

**Authors:** Chaeeun Kim

## Example

A sample query in a zero-shot setting:

```
Input:
Explain Pavlov’s dog experiments as an example of the theory of Classical Conditioning using the following terms: unconditioned stimulus, conditioned stimulus, neutral stimulus, unconditioned response, conditioned response.

Output:
Here is an explanation on Pavlov's dog experiments as an example of the theory of Classical Conditioning using the specified terms:

[Unconditioned response through Unconditioned stimulus]
Pavlov provided an unconditioned stimulus, food, to dogs to elicit a natural response without any prior learning. The food naturally caused salivation in the dogs. When presented with this unconditioned stimulus, the dogs exhibited an unconditioned response of salivating. This response occurred spontaneously without the need for any learning.

[Converting Neutral stimulus to Conditioned stimulus]
Next, a neutral stimulus that initially did not elicit any response was introduced and paired with the unconditioned stimulus to induce a response. This process is known as classical conditioning. In Pavlov's experiment, the neutral stimulus was something like a bell or metronome. This neutral stimulus was associated with the unconditioned stimulus, which is food. Through repeated pairings, the neutral stimulus became a conditioned stimulus.

[Conditioned response through Conditioned stimulus]
As a result of this conditioning, the conditioned stimulus (such as the sound of the bell or metronome) came to elicit a conditioned response. Even without the presence of food, the dogs would salivate in response to the conditioned stimulus, demonstrating that the neutral stimulus had become a conditioned stimulus capable of triggering a conditioned response.

In summary, Classical Conditioning involves the association of a neutral stimulus with an unconditioned stimulus to elicit a conditioned response. The process demonstrates how a previously neutral stimulus can acquire the ability to evoke a response through repeated pairings with a stimulus that naturally triggers a response. Pavlov's experiments provided a foundational understanding of classical conditioning in psychology.
```

## What is the task trying to measure?

In this task, we assess how well language models follow given lexical constraints.

## Motivation

Language models can be utilized in various ways, including data generation. When we want to restrict the responses to a desired format, adhering to lexical constraints becomes a crucial skill. Based on this motivation, we explore whether the language model accurately follows given lexical constraints while generating responses.

## Related work
[COLLIE: Systematic Construction of Constrained Text Generation Tasks](https://arxiv.org/abs/2307.08689) (Shunyu Yao, 2023)

