# Multi Source

This task is **Subjective**. Tasks that require to generate based on multiple knowledge sources that might potentially conflict with one another.

**Authors:** Haebin Shin (haebin.shin@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

- Input:
```
Opinion 1: Expert One, Dr. James Forester, remains bullish about the outlook for U.S. stock prices over the next month. He asserts that U.S. corporations' strong earnings, coupled with the Federal Reserve's policy stability, will continue to push the market forward. Furthermore, the continued rollout of Covid-19 vaccinations is serving as another boost to consumer and business confidence, which should be reflected in stock prices.
Opinion 2: Financial expert Sarah Manning holds a more bearish stance. She foresees potential risks emerging from concerns over inflation and rising bond yields, which might lead investors to reevaluate their portfolios. Ms. Manning also raises concerns that the market is overbought and due for a correction, especially for big technology companies that have exceedingly high valuations. She believes that their stock prices may decline in the next month.

Based on these two experts' opinions, what should be my stance on investing in U.S. stocks?
```
- Output:
```
Your decision would depend on your investment goals, timeline, and risk tolerance. If you align with Dr. James Forester's outlook, you would expect U.S. stocks to perform well in the near term, suggesting this may be a good time to invest. Conversely, if you align more with Sarah Manning's stance, you might be cautious and anticipate a potential market correction. It would be advisable to consult with a financial advisor or conduct additional research before making investment decisions.
```

## What is the task trying to measure?

The LLM may either determine which information is accurate or attempt to summarize the conflicting perspectives.
Please note that since this task is subjective, a higher score does not necessarily indicate better performance.
The scoring rubric reflects the range of variance in LLM reactions.
Depending on the knowledge sources to which the LLM is grounded, it will receive a score ranging from 1 to 5.
A score of 3 generally suggests that the response was generated from all sources.

## Motivation

Some instances are motivated by controversial scenarios. We are concentrating on the LLM's response within the given context that might potentially conflict with one another.

## Related work

- https://arxiv.org/abs/2205.12221