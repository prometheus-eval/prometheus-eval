# Following Multiple Instructions for Multi-Tasks in a Single Inference

This tasks require to follow multiple instructions for multi-tasks in a single inference session. We consider varios pairs of tasks, such as (lexical constraint, title generation, translation), (coreference resolution, paraphrasing), and (sorting, arithmetic).

**Authors:** Chaeeun Kim

## Example

A sample query in a zero-shot setting:

```
Input:
Arrange the given names in alphabetical order and assign scores based on their order, starting from 1.
For instance, the top-ranked name, Alexander Bennett, receives 1 point, followed by Amelia Foster with 2 points.
Once scores are assigned, calculate the sum of the squares for individuals whose names end with 'r'.
Names:
  Lucas Turner
  Oliver Thompson
  Emma Lawson
  Alexander Bennett
  Sophia Mitchell
  Henry Carter
  Amelia Foster
  Benjamin Hayes
  Benjamin Turner
  Grace Palmer
  Samuel Reynolds
  Lily Morgan
  Stella Taylor
  Chloe Miller
  Grace Harper
  Harper Smith

Output:
Here’s an arranged name and respective score based on the order. The scores for individuals whose names end with 'r'' are 4, 9, 14, 16.
1. Alexander Bennett - 1
2. Amelia Foster - 2
3. Benjamin Hayes - 3
4. Benjamin Turner - 4
5. Chloe Miller - 5
6. Emma Lawson - 6
7. Grace Harper - 7
8. Grace Palmer - 8
9. Harper Smith - 9
10. Henry Carter - 10
11. Lily Morgan - 11
12. Lucas Turner - 12
13. Oliver Thompson - 13
14. Samuel Reynolds - 14
15. Sophia Mitchell - 15
16. Stella Taylor - 16

The sum of the squares of the scores for individuals whose names end with 'r' is
4^2 + 9^2 + 14^2 + 16^2 = 549
```

## What is the task trying to measure?

In this task, we evaluate whether the model can handle multiple tasks in a single inference, following multiple instructions. If the previous task is incorrectly performed, it can affect the next task; therefore, it is necessary to follow the instructions in order.

## Motivation

Recent research has investigated multiple tasks in language models, frequently executed in a single inference to take advantage of the expanding token length. Addressing complex problems while considering practical factors is becoming increasingly crucial. Based on this motivation, our goal is to assess the capability of a language model to effectively perform multiple tasks within a single inference.

## Related work

[Exploring the Benefits of Training Expert Language Models
over Instruction Tuning](https://arxiv.org/pdf/2302.03202.pdf) (Joel Jang, 2023)
