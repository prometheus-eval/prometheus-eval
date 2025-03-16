# Correcting False Presuppositions

Tasks that require to generate accurate information by correcting the flase assumption when language models encounter questions with incorrect presuppositions.

**Authors:** Chaeeun Kim

## Example

A sample query in a zero-shot setting:

```
Input:
I've got a crucial meeting coming up this weekend and I need to get some dress shoes. Normally, I wear size 230 for most sneaker brands, so going with size 230 for dress shoes should work out fine, right?

Output:
It's great that you're preparing for your important meeting! However, it's important to note that shoe sizes can differ between brands and styles. While your sneaker size is 230, it doesn't guarantee the same fit for dress shoes. To ensure the perfect fit, I recommend visiting a shoe store and trying on the dress shoes in person. This way, you can assess the comfort and determine which size is best fitted for you. If you're considering an online purchase, take accurate measurements of your foot and refer to the size chart provided by the online store. This step will help you choose the right size. Good luck with your meeting!
```

## What is the task trying to measure?

In this task, we evaluate the language models' capacity to rectify false presuppositions present in questions.

## Motivation

We often pose questions with false presuppositions, especially when overlooking certain conditions related to specific concepts or principles. When the model encounters such questions, we anticipate it to correct any incorrect assumptions and clarify any points of confusion. 

## Related work

[CREPE: Open-Domain Question Answering with False Presuppositions](https://arxiv.org/pdf/2211.17257.pdf) (Xinyan Yu, 2022)
