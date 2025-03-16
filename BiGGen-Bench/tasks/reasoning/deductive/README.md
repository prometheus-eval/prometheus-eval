# Deductive Reasoning

Tasks that require to perform deductive reasoning.

**Authors:** Juyoung Suk (juyoung@lklab.io)

## Example

A sample query in a zero-shot setting:

```
Input:
Is the following example a valid deductive argument, and is it sound? Please explain the reasoning behind your assessment.

1. If there’s a rainbow, flights get canceled.
2. There is a rainbow now.
3. Therefore, flights are canceled.

Output:
Let's analyze the argument:

1. Premise: If there’s a rainbow, flights get canceled.
2. Premise: There is a rainbow now.
3. Conclusion: Therefore, flights are canceled.

**Validity Assessment**:
The argument follows a logical form called modus ponens, which states: if P implies Q, and P is true, then Q must be true. Here, P is ""there’s a rainbow"", and Q is ""flights get canceled"". The argument correctly follows this form: it is claimed that if there is a rainbow (P), then flights get canceled (Q); and it is stated that there is a rainbow (P). Therefore, following the form of modus ponens, the conclusion that flights are canceled (Q) is correctly derived from the premises. This makes the argument valid.

**Soundness Assessment**:
For the argument to be sound, both premises must be true. The first premise ""If there’s a rainbow, flights get canceled"" is a questionable statement. This premise seems highly unlikely to be true, as the occurrence of rainbows is not a standard or logical reason for flight cancellations. Rainbows are a common meteorological phenomenon that doesn't generally affect aviation. The second premise ""There is a rainbow now"" could be true, but it depends on the specific situation.

Since the first premise is likely false, the argument, despite being valid, is not sound. A sound argument requires both logical structure (validity) and true premises, which is not the case here.
```

## What is the task trying to measure?

FILL IN ME

## Motivation

FILL IN ME

## Related work

FILL IN ME