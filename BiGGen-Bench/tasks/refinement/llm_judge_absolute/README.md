# LLM Judge Absolute

This tasks asks models to judge the absolute quality of a given response to a prompt. The prompt includes an input
question, score rubric, and reference answer.

**Authors:** Namgyu Ho (itsnamgyu@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

### System Prompt

```
You will be given an instruction, a reference answer that gets a score of 5, a score rubric representing an evaluation criterion, and finally the response to evaluate,

1. Write a detailed feedback that assesses the quality of the response strictly based on the
   given score rubric, not evaluating in general.
2. After writing a feedback, write a score that is an integer between 1 and 5. You should
   refer to the score rubric.
3. The output format should look as follows: [FEEDBACK] (write a feedback for criteria)
   [SCORE] (an integer number between 1 and 5)
4. Please do not generate any other opening, closing, and explanations.
```

### Input

```
### Instruction

During the American Revolution, in the winter of 1777, why was the Continental Army's decision to camp at Valley Forge significant? Consider the political, military, and geographical aspects.

### Reference Response

The encampment at Valley Forge in the winter of 1777 was a pivotal moment in the American Revolution, with its significance stemming from an intricate interplay of military, political, and geographical factors:

1. Military: The rigorous training and discipline instilled by Baron von Steuben transformed the Continental Army into a more effective fighting force, enhancing its military capabilities.
2. Political: This transformation, coupled with the troops' resilience in overcoming severe hardships, symbolized the unwavering American commitment to independence. This display of determination was instrumental in securing international support, notably from France.
3. Geographical: The strategic location of Valley Forge enabled this transformation and resilience to unfold effectively. It provided a defensible position near British-occupied Philadelphia, allowing the army to monitor enemy movements while ensuring its own safety and supply lines.

In essence, the choice of Valley Forge was a masterstroke that combined military improvement, political symbolism, and geographical advantage, culminating in a strengthened army that was crucial for the eventual success of the American fight for independence.

### Score Rubric

Does the response accurately incorporate and reflect key historical facts, demonstrate a comprehensive understanding of the event's significance, and apply this knowledge logically and coherently?

### Response To Evaluate

The Continental Army's decision to camp at Valley Forge during the winter of 1777-78 was significant for several reasons:

- Symbolism: The camp symbolized American resilience and determination.
- Strategic location: Valley Forge was near Philadelphia, allowing the army to monitor British movements and protect the city.
- Defensible position: The terrain was rugged and defensible, providing natural protection for the army.
- Training and reorganization: The winter at Valley Forge allowed the army to reorganize and train its troops, implementing new tactics and strategies.
- Morale boost: Despite harsh conditions, the camp became a symbol of American determination, boosting soldiers' morale and preparing them for future battles.

---

Please evaluate the response according to the score rubric above.
```

### Output

```
[FEEDBACK] The response effectively addresses the significance of the Continental Army's decision to camp at Valley Forge, aligning well with the score rubric's criteria. Key historical facts are accurately incorporated, such as the strategic location near Philadelphia, the defensible terrain, and the transformative training and reorganization that took place during this period. The response demonstrates a comprehensive understanding of the event's significance by connecting these aspects to broader themes like American resilience and morale boosting. It logically and coherently applies this knowledge, highlighting the interplay between military strategy, geographical advantages, and symbolic value. However, it could have been more specific when discussing international support, particularly the crucial support of France.

[SCORE] 4
```

## What is the task trying to measure?

The ability of a model to judge the absolute quality of a given answer to a question,
while taking into account the provided score rubric. The model should give score between 1 and 5
and provide a detailed explanation for the score.

## Motivation

The task is motivated by the evolving role of language models (LLMs) in educational settings and the broader AI field,
including their potential in evaluating the outputs of other LLMs.

## Related work

- Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena (https://arxiv.org/abs/2306.05685)
- Prometheus: Inducing Fine-grained Evaluation Capability in Language Models (https://arxiv.org/abs/2310.08491) 