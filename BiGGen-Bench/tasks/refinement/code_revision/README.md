# Code Revision

This task asks models to revise incorrect code.
A short comment of what is wrong and the terminal log may be provided as additional context.

**Authors:** Namgyu Ho (itsnamgyu@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

### System prompt

You are a helpful, respectful and honest assistant. Help the user revise their code. This includes fixing functional
errors or notable inefficiencies, and improving the modularity and readability of the code when appropriate. You should
explain your understanding of the intent of the code, what needs to be revised and why.

### Input

Please revise the following code snippet.

```python
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
```

Comment: improve the time complexity; do not use any library functions.

Terminal Log: N/A.

### Output

```
```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

The original code does not correctly handle the case for **`num`** being less than 2, as 1 is not a prime number. The
revised code includes a check for this. Additionally, the loop range is optimized to **`int(num**0.5) + 1`** for
efficiency, as a factor of **`num`** will not be greater than its square root.

## What is the task trying to measure?

The ability of a model to identify the original intent of a code snippet and to revise the code to achieve the intent.
The model should also provide detailed feedback on why the original code is incorrect.

The provided comment may be incomplete or incorrect, and the model should be able to identify the correct intent of the
code and the issue that the user is facing.

## Motivation

The task of code revision is critical for assessing the practical capabilities of language models in programming
domains, as it simulates a real-world scenario where developers often revisit and optimize code for efficiency,
correctness, and readability. The ability of a model to perform code revision demonstrates its practical utility in
software engineering tasks by helping developers to improve their codebase, which can lead to better software
performance, reduced resource consumption, and overall higher quality of the software.

## Related work

- Generating Sequences by Learning to Self-Correct (https://arxiv.org/abs/2211.00053)
- Coffee: Boost Your Code LLMs by Fixing Bugs with Feedback (https://arxiv.org/abs/2311.07215)
- Resolving Code Review Comments with Machine
  Learning (https://research.google/pubs/resolving-code-review-comments-with-machine-learning/)