# Rationale Revision

This task asks models to revise incorrect rationales within a given step-by-step answer to a complex question.
The answer contains a reasoning chain that contains at least one incorrect rationale.
The final answer may be correct, despite the reasoning chain being incorrect.

**Authors:** Namgyu Ho (itsnamgyu@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

### Input

---

Here is a question and a step-by-step answer. Identify *all* incorrect rationale(s) and revise the entire reasoning
chain to produce a correct final answer. Explain why the incorrect rationale(s) are incorrect and how you revised
them.

# Question

A farmer has a field of wheat. If the field yields 800 kilograms of wheat, and each kilogram of wheat contains 340 grams
of carbohydrates. If the farmer uses 20% of the carbohydrates to produce bread, each loaf of which requires 150 grams of
carbohydrates, how many full loaves of bread can the farmer produce? Explain step by step.

# Answer

First, calculate the total carbohydrates from the wheat. Multiply 800 kilograms of wheat by 340 grams of carbohydrates
per kilogram, resulting in 272,000 grams of carbohydrates. Then, 20% of 272,000 grams is used for bread, which is 54,400
grams. Since each loaf requires 150 grams, the farmer can make 54,400 / 150 = 363 loaves of bread.

---

### Output

```
The mistake made here is in the calculation of the number of loaves of bread. The error occurs in the division of
54,400g by 150g per load. The answer states that 54,400g divided by 150g per loaf equals 363 loaves of bread.
This calculation is incorrect. The correct calculation should be 54,400g / 150g per loaf = 362.67. Since the
question asks for the number of *full* loaves of bread, the answer should be rounded down to the nearest whole number.
Therefore the correct answer is 362 loaves of bread.
```

## What is the task trying to measure?

The ability of a model to discern incorrect rationales in a reasoning chain, and to revise the incorrect rationales
to produce a correct answer. The model should be able to identify cases where the final answer is correct but for the
wrong reasons (i.e., contains incorrect rationales). The model should also provide detailed feedback on why the
incorrect rationales are incorrect.

## Motivation

The motivation behind tasks like Rationale Revision is to mirror and measure an important cognitive skill: critical
thinking. In real-world decision-making, reasoning is not only about reaching conclusions but also about understanding
and refining the underlying thought processes that lead to those conclusions. Such tasks target a model's ability to
practice metacognition—thinking about one's thinking—which is a key element of advanced learning and problem-solving.

## Related work

- Verify-and-Edit: A Knowledge-Enhanced Chain-of-Thought Framework (https://arxiv.org/abs/2305.03268)
- Learning From Mistakes Makes LLM Better Reasoner (https://arxiv.org/abs/2310.20689)