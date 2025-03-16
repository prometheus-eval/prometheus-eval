# Self Correction

This task asks models to improve a given response to a prompt. No additional context is provided.

**Authors:** Namgyu Ho (itsnamgyu@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

### Input

```
Review your previous answer to the given question and improve it.

### Question

In a game, Alex has a 40% chance of scoring a goal each time he takes a shot. If Alex takes 5 shots in a game, what is the probability that he scores exactly 2 goals? Explain your reasoning. Your final answer should be in the form of a percentage, with two decimal places, like this: XX.XX%.

### Previous Answer

To find the probability that Alex scores exactly 2 goals out of 5 shots, we can use the binomial probability formula. The binomial probability formula is:

P(X = k) = (n choose k) * (p^k) * ((1 - p)^(n - k))

Where:

- P(X = k) is the probability of getting exactly k successes (in this case, 2 goals).
- n is the number of trials (in this case, 5 shots).
- k is the number of successes (in this case, 2 goals).
- p is the probability of success on an individual trial (in this case, 0.4 or 40%).

Let's plug these values into the formula:

P(X = 2) = (5 choose 2) * (0.4^2) * ((1 - 0.4)^(5 - 2))

First, let's calculate (5 choose 2):

(5 choose 2) = 5! / (2!(5 - 2)!) = (5 * 4) / (2 * 1) = 10

Now, plug the values into the formula:

P(X = 2) = 10 * (0.4^2) * (0.6^3)

P(X = 2) = 10 * (0.16) * (0.216)

P(X = 2) = 3.456%

So, the probability that Alex scores exactly 2 goals out of 5 shots is approximately 3.46%.
```

### Output

```
To find out the probability that Alex scores exactly 2 goals out of 5 shots, we can use the binomial probability formula:

\[ P(X = k) = (n choose k) * (p^k) * ((1 - p)^(n - k)) \]

Where:

- \( P(X = k) \) is the probability of getting exactly k successes (in this case, 2 goals).
- \( n \) is the number of trials (in this case, 5 shots).
- \( k \) is the number of successes (in this case, 2 goals).
- \( p \) is the probability of success on an individual trial (in this case, 40% or 0.4).

Let's calculate it step by step:

1. First, calculate \( (5 choose 2) \), which is the number of ways to choose 2 successes in 5 trials. It's calculated as 5! / (2! * (5 - 2)!), which is (5 * 4) / (2 * 1) = 10.
2. Next, calculate \( 0.4^2 \), which is the probability of scoring a goal twice: 0.4 * 0.4 = 0.16.
3. Then, calculate \( (1 - 0.4)^{5 - 2} \), which is the probability of not scoring a goal in the remaining shots: 0.6 * 0.6 * 0.6 = 0.216.
4. Now, multiply these values together: 10 * 0.16 * 0.216 = 0.3456.
5. Finally, convert this to a percentage: 0.3456 * 100 = 34.56%.

So, the probability that Alex scores exactly 2 goals out of 5 shots is approximately 34.56%.
```

## What is the task trying to measure?

The ability of a model to identify the original intent of a prompt and to revise the response to better achieve the
intent. Each instance comes with specific points of improvement, which are not given to the model. The intent of the
prompt and the points of improvement should be reasonably clear to humans.

## Motivation

The ability to self-correct is an essential component of generative language models that aim to provide not only
accurate information but also to refine their outputs when errors or suboptimal responses are identified. This
capability is indicative of advanced comprehension, self-assessment, and the continuous improvement of models, making
them more reliable and useful across various applications.

## Related work

- Large Language Models Cannot Self-Correct Reasoning Yet (https://arxiv.org/abs/2310.01798)
- Large Language Models Can Self-Improve (https://arxiv.org/abs/2210.11610)