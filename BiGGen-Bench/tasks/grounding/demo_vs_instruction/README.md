# Demo vs Instruction

This task is **Subjective**. Tasks that where the instruction and demonstrations are somehow related but show different patterns.

**Authors:** Haebin Shin (haebin.shin@kaist.ac.kr)

## Example

A sample query in a 2-shot setting:

- Input:
```
Translate the given sentence to English.

Source: La pomme est colorée en rouge.
Destination: Der Apfel ist rot gefärbt.
Source: La Tour Eiffel est située en France.
Destination: Der Eiffelturm befindet sich in Frankreich.
Source: Je voudrais un expresso, s'il vous plaît
```

- Output:
```
Destination: I'd like an espresso, please.
```

## What is the task trying to measure?

The objective of this task is to check whether the LLM prefers to ground on the demonstrations or the instruction.
Please note that since this task is subjective, a higher score does not necessarily indicate better performance.
The scoring rubric reflects the range of variance in LLM reactions.
Depending on which pattern LLM follows demo or instruction, it will receive a score ranging from 1 to 5.

## Motivation

It is not easy to define which pattern to follow when demonstration and instruction conflict. 
To explore this ambiguity, this task observes the responses generated from the given inputs.

## Related work

