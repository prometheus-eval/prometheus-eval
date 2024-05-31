# Checklist Generation

Tasks that require to generate a checklist of what each participant of a dialogue is aware of after the conversation. This could include multiple sessions of conversation among various participants.

**Authors:** Miyoung Ko (miyoungko@kasit.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
Jordan, Alex, Taylor and Riley are having debate about ‘The impact of technology on education’.
Jordan: While technology has its place, I'm concerned about its overuse. Isn't there a risk of losing traditional teaching methods that have proven effective?
Alex: That's a common misconception. The integration of tech in education enhances traditional methods, it doesn't replace them.
Taylor: I've seen both sides in my school. Some teachers use tech well, but others struggle, and it can be distracting.
Riley: Indeed, research shows a mixed impact. The effectiveness depends heavily on implementation and training.
Jordan: But what about the social aspect? Are we risking students' ability to interact face-to-face?
Taylor: That's a valid point. Sometimes, it feels like we're more connected to our devices than to each other.
Alex: However, technology also brings collaborative opportunities that weren't possible before.
Riley: The key is balance and understanding the different needs of students.

Create a checklist regarding participants’ perspectives on technology in education.
Checklist: 

Output:
1: Concern about overuse of technology; [Jordan]
2: Values traditional teaching methods; [Jordan]
3: Concerns about social impact on students; [Jordan, Taylor]
4: Enhances traditional teaching methods; [Alex]
5: Technology will bring collaborative opportunities; [Alex]
6: Aware of distractions that can come with technology; [Taylor]
7: Advocates balance and understanding diverse student needs; [Riley]
```

## What is the task trying to measure?

Checklist generation assesses the model's ability to generate an awareness checklist for participants in a dialogue or from observations. Each instance measures the following abilities:

- Generating an awareness checklist from debates and conversations (Q1, Q5).
- Generating an awareness checklist that requires further inference to capture awareness (Q2).
- Generating an awareness checklist from observations (Q3, Q4)

## Motivation

The task of creating awareness checklists for participants in a dialogue aims to enhance the model's proficiency in understanding and interpreting human interactions. This task challenges the model to infer the awareness and comprehension of each participant by focusing on both verbal exchanges and non-verbal cues during multiple conversation sessions. This requires not only understanding spoken content but also sensitivity to unspoken aspects of communication and further inference. The ability to accurately assess and document what each individual is aware of after the conversation is a step toward replicating human cognitive abilities and improving the model's capability for nuanced and empathetic interactions. This advancement enables more effective interactions with humans in complex, multi-faceted communication scenarios.

## Related work

[1] Kim et al., (2023) FANToM: A Benchmark for Stress-testing Machine Theory of Mind in Interactions. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP), pp 14397–14413.

