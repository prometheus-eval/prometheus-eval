# Competition Math Word Problems

Tasks that require to solve secondary level competition math word problems.

**Authors:** Hyeonbin Hwang

## Example

A sample query in a zero-shot setting:

```
Input:
ASSISTANT: You are a helpful assistant that logically solves the given problem step by step.

QUESTION: Given positive integers x, y, z, that satisfy x^2 + y^2 + z^2 = 560, find value of xyz. You are not allowed to use code.
ANSWER: 

Output: 
Given 560 is divisble by 4, we can rewrite the equation as x^2/4 + y^2/4 + z^2/4 = 140. Assuming x' = 2x, y' = 2y, z' = 2z, then x'^2 + y'^2+ z'2 = 140.
Since 140 is also divisble by 4, apply this logic once more (i.e. x''= 2x') Then, x''^2 + y''^2 + z''^2 = 35. Now this gives x'' = 1, y'' = 3, z'' = 5.
Therefore, x = 4, y = 12, z = 20 and xyz = 960
```

## What is the task trying to measure?

We seek to measure whether the model can truly achieve the level of math competition by introducing some exceptionally challenging problems.

## Motivation

Recent advancements in Large Language Models (LLMs), as demonstrated by their high performance in the MATH dataset (Hendrycks, 2021), have led us to present a set of new and equally or more challenging problems than those found at level 5 of this dataset. These problems are designed to test strategic thinking over the mere recall of advanced theories. As of January 2024, even advanced models like GPT-4 have not been able to solve these problems.

These new problems are slightly modified versions of past Korean Math Olympiad (KMO) questions.

Problem 1 - high school KMO 2023 (first round) \
Problem 2 - high school KMO 2022 (first round) \
Problem 3, 4, 5 - middle school KMO 2021 (first round)

## Related work

[Measuring Mathematical Problem Solving With the MATH Dataset](https://arxiv.org/abs/2103.03874) (Hendrycks, 2021)