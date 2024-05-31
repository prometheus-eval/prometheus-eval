# Hypothesis Proposal

Tasks that require to generate a valid yet intriguing scientific hypothesis.

**Authors:** Hyeonbin Hwang (hbin0701@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
ASSISTANT: You are a researcher that provides logical hypothesis based on the given observations.
You are a researcher working on training Language Models. Come up with 3 new hypotheses against following background, and you may freely use your existing knowledge. You should be as detailed as possible.

Background Information)
1) The major downside of fine-tuning is that the new model contains as many
parameters as in the original model.
2) Previous works Li et al. (2018a); Aghajanyan et al. (2020) show that the learned
over-parametrized models in fact reside on a low intrinsic dimension.

ANSWER:

Output:
Low Rank: Weights during model adaptation also has a low 'intrinsic rank' thus neural network can be trained indirectly by optimizing rank decomposition matrices of the dense layers' change during adaption, while keeping the pre-trained weights frozen.
Dimensionality Reduction in Fine-Tuning: Fine-tuning large language models can be more efficient through dimensionality reduction techniques without significantly impacting performance.
Sparse Fine-Tuning: Sparse fine-tuning, updating only a subset of a model's parameters, can achieve similar performance to traditional full-model fine-tuning in language models.
```

## What is the task trying to measure?

We aim to measure whether Language Models can generate valid and intriguing scientific hypothese, including but not limited to:

- Understanding of provided scientific information
- Integration with the model's background knowledge
- Novel and sound hypothesis generation

In this way, we ask the model to provide 3 hypotheses against the given background information and test out whether it can generate novel yet insightful ideas on the matter.

## Motivation

The potential of this task is significant, offering promising avenues for enhancing artificial intelligence's capabilities in scientific reasoning and its contribution to scientific discovery.

To accurately gauge model performance, we delve into a wide array of research papers spanning various domains. Within these papers, we carefully identify and extract foundational elements such as problem definitions, literature reviews, and pivotal data that have shaped the development of specific hypotheses. 
Our aim is to determine if the model can formulate hypotheses that either align or are comparable with those documented in these papers, utilizing the given information. 
For reference answer, we present hypothesis presented in the actual paper along with the ones that are manually curated from GPT-4's outputs.

Below are the list of papers we referred to for each instance.

1. [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)
2. [Let\'s verify step by step](https://arxiv.org/abs/2305.20050)
3. [Scientific journals still matter in the era of academic search engines and preprint archives](https://asistdl.onlinelibrary.wiley.com/doi/abs/10.1002/asi.24326)
4. [Detection and localization of surgically resectable cancers with a multi-analyte blood test](https://pubmed.ncbi.nlm.nih.gov/29348365/)
5. [Audio Matters Too: How Audial Avatar Customization Enhances Visual Avatar Customization](https://dl.acm.org/doi/abs/10.1145/3491102.3501848)

## Related work

[Large Language Models are Zero Shot Hypothesis Proposers](https://openreview.net/forum?id=EAuteBjTMw) (Qi, 2023)
