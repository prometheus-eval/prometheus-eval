# Following System Prompts

Tasks that require to follow an unusual and challenging system prompt that requires acting beyond as a "Helpful Assistant".

**Authors:** Jinheon Baek

## Example

A sample query in a zero-shot setting:

```
System:
Convert the input text into a mathematical equation, representing the concepts or actions described as mathematical operations or variables.

Input:
The population of a city increases every year by 5%.

Output:
P_{n+1} = P_n \times 1.05, where P_n is the population in year n.
```

## What is the task trying to measure?

The task is trying to measure the ability to understand and respond to unusual and challenging system prompts that go beyond typical helpful assistant tasks.

## Motivation

The motivation behind the task is to assess the AI's capability to handle unconventional and demanding system prompts (which also could be contrasting with input texts), potentially expanding its utility in various creative and complex scenarios.

## Related work

* Is "A Helpful Assistant" the Best Role for Large Language Models? A Systematic Evaluation of Social Roles in System Prompts (https://arxiv.org/abs/2311.10054)