# Historical Text Comprehension

Tasks that require comprehend about a historical text written in a target language and explain about it.

**Authors:** Jinkyung Jo

## Example

A sample query in a zero-shot setting:

```
Input:
Samaki za jadi za Kenya zina sifa tofauti kulingana na eneo na tamaduni. Nyumba za jadi za Wamasai zina tabia ya kuwa na dari lenye umbo la kilele na mara nyingi hazina sakafu. Nyumba hizi kwa kawaida zinajengwa hasa kwa kitambaa. Nyumba za Kiafrika za kisasa hujengwa kutumia mbao na mawe ya matumbawe, na kwa kawaida zina dari nyembamba na umbo la duara la kuvutia. Nyumba za Wakisii zina umbo la duara kwa kawaida, na dari zao zinaweza kutengenezwa kwa majani makubwa yanayofanana na shina. Nyumba za Wajaluo zina nyumba zilizojengwa kwa matofali ya udongo yenye rangi mbili na kwa kawaida zina dari nyembamba na madirisha madogo.\nSwali : Nyumba nne za jadi nchini Kenya na vifaa gani kila nyumba imejengwa navyo?

Output:
Nyumba za Wamasai zinajengwa na kitambaa, nyumba za Kiswaahili zinajengwa na mbao na mawe ya matumbawe, nyumba za Wakikuyu zinajengwa na majani makubwa, na nyumba za Waluo zinajengwa na udongo wa rangi mbili.
```

## What is the task trying to measure?

This task involves reading historical texts, understanding the context, and generating answers to given questions based on the text.

## Motivation

To comprehend historical texts, it is essential to consider the context of a specific period, individuals, events, and more. Moreover, one should possess an understanding of specialized historical knowledge. Therefore, through this task, the ability to comprehend temporal relationships and evaluate whether the model is specialized in the field can be assessed.

## Related work

[SeaEval for Multilingual Foundation Models: From Cross-Lingual Alignment to Cultural Reasoning](https://arxiv.org/abs/2309.04766)