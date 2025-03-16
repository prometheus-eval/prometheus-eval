# Recognizing and Clarifying the Ambiguity

This task deals with ambiguous questions, where multiple answers may arise from sub-conditions. By giving models a question with the ambiguity, we evaluate the models' ability to provide accurate responses, recognizing and concretizing the ambiguity.

**Authors:** Chaeeun Kim

## Example

A sample query in a zero-shot setting:

```
Input:
What is the name of the actor who played the role of James Rhodes in 'Iron Man'?

Output:
The cast of the Iron Man series changes depending on the series. The character James Rhodes in the first 'Iron Man' movie (2008) was originally portrayed by actor Terrence Howard. However, the role was later recast, and Don Cheadle took over the role of James Rhodes in subsequent Marvel Cinematic Universe (MCU) films. Thus, the character James Rhodes was played by Don Cheadle in 'Iron Man 2' (2010).
```

## What is the task trying to measure?

Through this task, we assess whether the model can clarify the ambiguity and respond clearly on the ambiguous questions.

## Motivation

We often pose ambiguous questions without realizing their inherent ambiguity. When the model encounters such ambiguous questions, it is expected to discern and specify the ambiguity, ultimately providing an accurate response. Regarding this, [AmbigQA](https://yunamom.tistory.com) highlights the importance of clarifying the ambiguity in questions and exploring various types of ambiguity, such as time-dependency, entity references, and event references. Based on these types of ambiguity, we have created this task with various instances to address and understand different forms of ambiguity.

## Related work

- [AmbigQA: Answering Ambiguous Open-domain Questions](https://arxiv.org/abs/2004.10645) (Sewon Min, 2020)
