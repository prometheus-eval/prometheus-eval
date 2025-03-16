# Temporal Grounding

Tasks that require to ground on a given time when additional context is given.

**Authors:** Haebin Shin (haebin.shin@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

Input:
```
### Context:
This is the weather forecast. Thursday starts with the temperature lingering around 59°F in the early morning, ensuring a cool start to the day. By afternoon, expect the mercury to reach 72°F, providing a perfect atmosphere for outdoor activities. As the evening approaches, the temperature is expected to drop slightly to a comfortable 66°F, perfect for a pleasant night.
Friday, the morning chill continues with the thermometer displaying a brisk 61°F. By the afternoon, it will rise to a high of 74°F, providing ample warmth for the day. Come evening, temperatures are expected to fall to a calm 68°F, making it ideal for evening outings.
On Saturday, the day of the Super Bowl, the morning temperature will be slightly cooler at 58°F. However, the afternoon will see a surge in temperature to 76°F, promising a sunny day. As evening draws in, the temperature will descend to 70°F, paving the way for a serene night.

### Question: Record all the temperatures on Super Bowl day chronologically.
```

Output:
```
The temperatures on Super Bowl day, Saturday, are as follows: the morning will start with a temperature of 58°F, the afternoon will see a surge to 76°F, and by evening, it will descend to 70°F.
```

## What is the task trying to measure?

This task assesses whether LLM's understanding of a temporal event: whether LLM can accurately describe information about the event at a specific time.

## Motivation

Most instances are motivated from "Temporal Constarints Satisfaction" and "Ordering Events along a Timeline" described in [Qiu et al. (2023)](https://arxiv.org/abs/2311.08398).


## Related work

- https://arxiv.org/abs/2311.08398