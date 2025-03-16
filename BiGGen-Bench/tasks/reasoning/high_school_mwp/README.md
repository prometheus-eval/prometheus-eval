# High School Math Word Problems

Tasks that require to solve secondary level math word problems.

**Authors:** Hyeonbin Hwang (hbin0701@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
ASSISTANT: You are a helpful assistant that logically solves the given problem step by step.

QUESTION: What is the value of \sqrt[3]{72} \times 3^(\frac{2}{3})? Express the answer in the nearest integer without using calculator.
ANSWER: 

Output: 
72 can be rewritten as 2^3 \times 3^2, and therefore \sqrt[3]{72} = 2^{3 \times \frac{1}{3}} \times 3^{2 \times \frac{1}{3}}.
This further simplifies to 2 \times 3^{\frac{2}{3}}.
Now, 9^{\frac{2}{3}} = 3^{2 \times \frac{2}{3}} = 3^{\frac{4}{3}}
Finally, 2 \times 3^{\frac{2}{3}} \times 3^{\frac{4}{3}} = 2 \times 3^2 = 18
```

## What is the task trying to measure?

The taks measures model's ability to apply its foundational knowledge of secondary math to solve various problems. This dataset, like others, is comprised of a range of mathematical problems varying in complexity, covering fundamental concepts from secondary math education, including algebra, probability, and trigonometry.

## Motivation

In current mathematical problem datasets, we often find that problems can be addressed through broader model generalization capabilities. This situation leads to a blurred definition of genuine reasoning in mathematical problem solving. Our task challenges this norm by introducing problems that defy resolution through mere memorization or adaptation from standard mathematical examples. Instead, these problems require higher level application and creative reasoning strategies, potentially leading to more effective solutions. 

## Related work

[Measuring Mathematical Problem Solving With the MATH Dataset](https://arxiv.org/abs/2103.03874) (Hendrycks, 2021)