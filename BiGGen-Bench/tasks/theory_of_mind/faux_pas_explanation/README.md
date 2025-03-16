# Faux Pas Explanation

Task that requires to detect and explain a faux pas situation. Faux pas is the "uhoh!" emotion most people would feel when the reality of the context is revealed.

**Authors:** Sue Hyun Park (suehyunpark@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
Chloe's mother was organizing a surprise party for Chloe's birthday. She invited Zoe and mentioned, "Keep it a secret, and make sure Chloe doesn't find out!" On the eve of the celebration, while Chloe and Zoe were playing, Zoe accidentally tore her new skirt. "Oops!" exclaimed Zoe, "I planned to wear this at your party." "What party?" asked Chloe. "Let's hurry," suggested Zoe, "and see if my mom can fix the skirt."
In this story, did someone say something that they should not have said, and if so, why? Explain.

Output:
Yes, in this story, Zoe said something that she should not have said. When Chloe asked "What party?" in response to Zoe mentioning her plans to wear her skirt to a party, Zoe inadvertently revealed the surprise party that Chloe's mother was organizing. This was not appropriate because Chloe's mother had specifically asked Zoe to keep the party a secret and make sure Chloe didn't find out. Therefore, by mentioning the party, Zoe broke the promise she made to Chloe's mother and potentially ruined the surprise.
```

## What is the task trying to measure?
This task measures a model's ability to detect a faux pas in a story and explain why. Faux pas is difficult to recognize as it requires social intelligence of the agent, specifically a composite understanding of false beliefs and emotional impact of one's action (See [Motivation](##Motivation)).

This task comprises the following subtasks, designated for each of the 5 instances:

1. **Faux pas detection and explanation**

    `In the story, did someone say something that they should not have said, and if so, why? Explain.`

2. **Comparison of a faux pas story and a control story**

    `Explain the difference in {speaker}'s intention in his statement and how {speaker}'s statement would impact other people in the two situations.`

3. **Comparison of the situation before and after the problematic utterance in the progression of a faux pas story**

    `How would the characters' feelings change before and after {faux pas phrase}?`

4. **Analysis of the likely mental states of each character throughout the story**

    `Describe the mental state of each person in the story as the story progresses.`

5. **Prediction of the change in characters' emotions and actions likely to occur after the given story**

    `How would the {characters} behave or react shortly after?`

## Motivation

*Faux Pas*, which is in French "false step", is defined as follows:
> when a speaker says something without considering if it is something that the listener might not want to hear or know, and which typically has negative consequences that the speaker never intended[^1]

Faux Pas detection is an established theory of mind test in the clinical psychology domain designed for children aged 7-11 instead of 4-6 (common in most theory of mind tests), which is proven to be a more difficult test[^1]. Detecting a Faux Pas requires (1) understanding of ***false-belief***[^2], which is the understanding that one's belief about the world or other people's beliefs may not be true, and (2) appreciation of the **emotional impact** ("uhoh!") when the reality of the context is unveiled.  
A recent study has reported that LLMs struggle with Faux Pas detection, with the highest model scoring more than 0.4 points lower than the average recognition rate of 0.82 by normally developing 9- to 11-year-old children[^3]. Furthermore, extending the task from detection to explanation increases the complexity of evaluation. Besides that manually assessing the long-form output is costly, it is problematic with respect to the ELIZA effect[^4], a phenomenon where a person is susceptible to read far more understanding and human traits than is warranted into the machine-generated output, because the model output can suggest the wrong answer in a persuasive and intelligent way without giving a clear-cut final answer.  
To this end, we intend to explore the model's capability to distinguish differing mental states and emotional reactions in a faux pas reaction, using fine-grained evaluation criteria to assess even long-form explanations from a model.

## Data Source
We use examples from the original faux pas test[^1], but apply the following modifications to prevent possible memorization of content by a model: (1) change the names of the characters (2) rephrase the story, including main objects.

## Related work
[^1]: Baron-Cohen, S., O'Riordan, M., Stone, V., Jones, R., & Plaisted, K. (1999). Recognition of faux pas by normally developing children and children with Asperger syndrome or high-functioning autism. Journal of autism and developmental disorders, 29(5), 407–418. https://doi.org/10.1023/a:1023035012436

[^2]: Bauminger-Zviely, N. (2013). False-Belief Task. In: Volkmar, F.R. (eds) Encyclopedia of Autism Spectrum Disorders. Springer, New York, NY. https://doi.org/10.1007/978-1-4419-1698-3_91

[^3]: Shapira, N., Zwirn, G., & Goldberg, Y. (2023, July). How Well Do Large Language Models Perform on Faux Pas Tests?. In Findings of the Association for Computational Linguistics: ACL 2023 (pp. 10438-10451).

[^4]: Hines, D. (1980). [Review of Computer Power and Human Reason: From Judgment to Calculation, by J. Weizenbaum]. The Journal of Mind and Behavior, 1(1), 123–126. http://www.jstor.org/stable/43852815


