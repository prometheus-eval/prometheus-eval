# Thinking for Doing 

Task that require to infer what action the opponent would take on the next step. This requires to first infer what the opponent would be thinking about given the possible observations.

**Authors:** Miyoung Ko (miyoungko@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:
```
Input:
Emma had spent a whole hour building a beautiful castle out of colorful blocks.
Her little castle was a big achievement, standing proudly on the living room floor.
Her younger brother, Max, was watching her.
He was only 3 years old and really wanted to play with the castle too.
But Emma remembered that Max was still learning to be gentle with toys.
She recalled the last time Max's tower of blocks tumbled down. She remembers how upset he was last time his tower of blocks fell.
Suddenly, mother calls them for a snack, and both children leave the room. The castle stayed there, all alone.
Max looked back at it, wishing he could play, but he followed his sister out of the room.

Question: What will Emma do after having a snack, and why, taking into consideration Emily's thoughts about Max?

Output:
Emma will likely move the castle to a safer location or engage Max in a different activity after the snack. She understands that Max might accidentally knock over the castle and remembers how upset he was last time something similar happened.
```


## What is the task trying to measure?

This task measures a model's ability to predict the next action of an opponent based on the opponent's thoughts about a given observation. Each instance aims to measure the following abilities:

- Prediction of the person's thoughts and actions likely to occur after the story (Q1, Q2).
- Prediction of the person's thoughts and actions likely to occur after a conversation between three people (Q3).
- Prediction of the third person's next actions based on the conversation (Q4).
- Inferring the next action by predicting the actions of the other character (Q5)

## Motivation

Following [1], while humans possess the innate ability to infer others' mental states and act pragmatically on these insights—an ability central to ToM—LLMs have traditionally been limited to making inferences without necessarily connecting them to strategic actions. Existing benchmarks, such as ToMi[2], test a model's ability to understand beliefs within a narrative but fall short in assessing how these inferences guide actions in social scenarios. Thinking for doing requires the ability to predict an opponent's next action in a strategic setting by inferring the thought processes of the opponent based on available observations and contextual clues. This involves not only a deep understanding of the rules and dynamics of the specific scenario but also an insight into human behavior and decision-making. Successfully executing this task could greatly enhance the model's capabilities in human-AI interaction, decision-making support, and even in educational applications where understanding and responding to human thought processes is crucial.

## Related work

[1] Zhou et al., (2023) How FaR Are Large Language Models From Agents with Theory-of-Mind?. ArXiv

[2] Lee et al., (2019) Revisiting the evaluation of theory of mind through question answering. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing
and the 9th International Joint Conference on Natural Language Processing (EMNLP), pp 5872–5877.

