# High School Math Proof

Tasks that require to write proofs of secondary level math theorems.

**Authors:** Hyeonbin Hwang (hbin0701@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
ASSISTANT: You are a helpful assistant that logically solves the given problem step by step.

QUESTION: Consider a triangle with three acute angles A, B, C. Also let the vertices at the opposite of these angles be a, b, c respectively. Then, prove that a^2 = b^2 + c^2 - 2bc cos A
ANSWER: 

Output:
Let A be positioned in the origin, B be positioned at (c, 0), and C be positioned at (x, y).
Then, x = b cos A and y = b sin A. Because a is the distance from vertex C to vertex B, we can use the distance formula to get:
a^2 = (x - c)^2 + y^2
a^2 = (b cos A - c)^2 + ( b sin A)^2
a^2 = b^2 cos^2 A - 2bc cos A + c^2 + b^2 sin^2 A
a^2 = b^2 (cos^2 A + sin^2 A) - 2bc cos A + c^2
a^2 = b^2 + c^2 - 2bc cos A
```

## What is the task trying to measure?

The task is designed to assess the models' ability to apply various mathematical proof strategies in establishing the validity of known theorems or concepts. 

## Motivation

The primary goal of this task is to enhance and assess the proficiency of AI models in understanding and resolving intricate mathematical problems by employing logical deduction and the art of crafting proofs. Our objective is to refine the evaluation of the models' ability to construct cogent proofs using more nuanced and detailed criteria. To achieve this, we present a range of problems, each varying in complexity, including a selection of well-known examples. 

## Related work

[NaturalProofs: Mathematical Theorem Proving in Natural Language](https://arxiv.org/abs/2104.01112) (Welleck, 2021)