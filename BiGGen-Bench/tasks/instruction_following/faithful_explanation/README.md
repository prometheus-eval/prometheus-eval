# Faithful Generation

Tasks that require to generate a faithful response, ensuring the content is accurate rather than merely sounding authoritative.

**Authors:** Chaeeun Kim

## Example

A sample query in a zero-shot setting:

```
Input:
Describe the arteries that supply blood to the stomach and their respective origins.

Output:
The blood supply to the stomach is provided by branches of the celiac trunk. The main arteries supplying the stomach and their origins are: 

1. Left Gastric Artery:
    - Origin: It arises directly from the celiac trunk.
2. Right Gastric Artery:
    - Origin: There exists variations depending on person. It typically arises from the proper hepatic artery, gastroduodenal artery, and common hepatic artery.
3. Short Gastric Arteries:
    - Origin: It branches from the splenic artery, another major branch of the celiac trunk.
4. Left Gastroepiploic Artery:
    - Origin: It arises from the splenic artery.
5. Right Gastroepiploic Artery:
    - Origin: It arises from the gastroduodenal artery, a branch of the common hepatic artery.

These arteries create a comprehensive network throughout the stomach, supplying sufficient blood to meet the metabolic needs of the gastric tissues.
```

## What is the task trying to measure?

Through this task, we evaluate whether the language models can generate faithful responses that are accurate and relevant to the given instructions, rather than just looking good.

## Motivation

Language models have been demonstrating an ability to effectively learn the style of writing preferred by humans and generate well-structured text. However, despite the good appearances of responses, they often exhibit completely inaccurate content. This phenomenon is particularly prevalent in weak models, such as open-source models. Some studies have addressed this issue by fine-tuning weak models with outputs from powerful models, such as proprietary ones, to leverage their capabilities. Nevertheless, the accuracy of the responses remains weak, even though they successfully mimic the writing style.

Improving the factuality or accuracy of a model is crucial, but it is not an easy task. We evaluate this task to explore whether the generated responses are trustworthy.

## Related work

[The False Promise of Imitating Proprietary LLMs](https://arxiv.org/pdf/2305.15717.pdf) (Arnav Gudibande, 2023)
