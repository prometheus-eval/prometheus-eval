# Robust Translation

Tasks that test the language model's abilities to translate non-English terms with no direct English counterpart.

**Authors:** Dongkeun Yoon (dkyoon@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
Translate the Korean term '눈치를 보다' into English.

Output:
The Korean term '눈치를 보다' translates to 'to read the room' or 'to gauge others' feelings' in English. It describes the act of being sensitive to others' moods, reactions, and social dynamics, often to behave appropriately or make decisions based on these social cues. It's a concept that is deeply rooted in Korean social interactions, emphasizing the importance of non-verbal communication and social harmony.
```

## What is the task trying to measure?

The task measures the language model's abilities to provide translations that are not only accurate but also culturally and semantically appropriate for native speakers of the target language. It assesses the model's proficiency in capturing the cultural and contextual nuances of the source language, going beyond literal translations to convey the richness and depth of meaning in phrases or terms.

## Motivation

The motivation behind this task is to ensure that AI language models can produce translations that are not only technically correct but also culturally sensitive and semantically meaningful.

## Related work

[1]: He, Z., Liang, T., Jiao, W., Zhang, Z., Yang, Y., Wang, R., ... & Wang, X. (2023). Exploring Human-Like Translation Strategy with Large Language Models. arXiv preprint arXiv:2305.04118.

[2]: Zeng, J., Meng, F., Yin, Y., & Zhou, J. (2023). Improving Machine Translation with Large Language Models: A Preliminary Study with Cooperative Decoding. arXiv preprint arXiv:2311.02851.
