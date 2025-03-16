# Multilingual Reasoning

Tasks require to reason with another language except English.

**Authors:** Dongkeun Yoon (dkyoon@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
과일 가게에는 복숭아, 망고, 그리고 사과, 총 3개의 과일을 팔고 있습니다. 복숭아는 사과보다 비쌉니다. 망고가 가장 저렴합니다.
선택지:
(A) 복숭아가 두번째로 비쌉니다. (B) 망고가 두번째로 비쌉니다. (C) 사과가 두번째로 비쌉니다.
정답을 말하기 전, 생각을 단계별로 차근차근 먼저 말하세요.

Output:
이 문제를 해결하기 위해, 과일의 가격을 순서대로 배열해야 합니다. 망고는 가장 저렴하다고 주어졌으며, 복숭아는 사과보다 비싸다고 합니다. 따라서 가장 저렴한 과일은 망고이며, 복숭아는 사과보다 비싸기 때문에 가장 비싼 과일일 가능성이 높습니다. 이 정보를 바탕으로 복숭아가 가장 비싸고 망고가 가장 저렴하다면, 사과는 이 두 과일 사이에 위치하게 됩니다. 즉, 사과는 두 번째로 비싼 과일입니다. 따라서 정답은 (C) 사과가 두번째로 비쌉니다.
```

## What is the task trying to measure?

The task measures the language model's ability to perform reasoning tasks in languages other than English. It evaluates the language model's capability to follow instructions, analyze information, and provide logical step-by-step reasoning in various languages.
## Motivation

This task test whether the language model is able to generalize its reasoning capabilities to other languages.


## Related work
[1]: Shi, F., Suzgun, M., Freitag, M., Wang, X., Srivats, S., Vosoughi, S., ... & Wei, J. (2022). Language models are multilingual chain-of-thought reasoners. arXiv preprint arXiv:2210.03057.
