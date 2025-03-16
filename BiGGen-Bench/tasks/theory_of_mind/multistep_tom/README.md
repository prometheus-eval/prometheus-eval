# Multistep ToM

Tasks that require to do multi-step reasoning to infer the mental state of the opponent. 

**Authors:** Miyoung Ko (miyoungko@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
In a high-stakes game of international diplomacy, Ambassador Chen was negotiating a critical trade agreement with Ambassador Rodriguez. 
During their discussions, Chen noticed Rodriguez frequently touching his necktie whenever the topic of agricultural tariffs was raised. 
This was a stark contrast to his usual confident posture. 
Chen remembered from previous meetings that Rodriguez often displayed this subtle gesture when discussing points where his country had less leverage or when it was willing to make concessions. 
Chen further noticed Rodriguez's careful choice of words, and his avoidance of direct answers regarding agriculture tariffs.

Question: Considering the story, how might Ambassador Chen infer Ambassador Rodriguez's mental state and his belief on his country's position on agricultural tariffs? 
Provide a reasoning step of Chen to infer Rodriguez’s mental state. 

Output:
The reasoning step involves linking observed behavior (touching the necktie) with the specific negotiation topic (agricultural tariffs) and recalling past instances of similar behavior under similar circumstances. 
This pattern recognition allows Chen to infer that Rodriguez's gesture is a non-verbal indication of discomfort or anxiety related to the topic of agricultural tariffs. 
The additional observation of Rodriguez's careful wording and evasion of direct answers further reinforces this inference. 
Therefore, Chen might conclude that Rodriguez is internally apprehensive or uncertain about his country's stance on agricultural tariffs, possibly believing that his country is in a weaker negotiating position.
```

## What is the task trying to measure?

This task assesses a model's capacity to explain the steps of reasoning used to infer the opponent's mental state from various types of input. Each instance measures the following abilities:
- Conducting multi-step reasoning from the story using verbal and non-verbal cues (Q1, Q2).
- Conducting multi-step reasoning from the conversation using verbal and non-verbal cues (Q3).
- Performing multi-step reasoning to explain the thought behind an action (Q4).
- Performing multi-step reasoning to explain the thought behind a character's statement (Q5).

## Motivation

Multi-step Theory of Mind (ToM) involves multi-step reasoning to deduce an opponent's mental state, enhancing the model's capacity to interpret and respond to complex human thought processes and interactions. This task emphasizes the model's ability to analyze the reasoning behind inferring an individual's thoughts or beliefs, integrating cues from both verbal and non-verbal communication, as well as the surrounding context. Successfully completing this task enables the understanding and emulation of human-like cognitive processes, thereby enhancing the model's effectiveness in scenarios requiring nuanced human-like interactions.

## Related work

[1] Nematzadeh et al., (2018) Evaluating Theory of Mind in Question Answering. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP), pp 2392–2400.

[2] Shapira et al., (2023) How Well Do Large Language Models Perform on Faux Pas Tests?. In Findings of the Association for Computational Linguistics: ACL 2023 (Findings of ACL), pp 10438–10451.
