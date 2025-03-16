# Executable Planning

Tasks that requires generating an executable plan in an environment that doesn't accept open-ended answers

**Authors:** Yoonjoo Lee (yoonjoo.lee@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
Goal: Pick up the blue box.
Room 1: Agent, yellow key, red ball, and a yellow locked chest with a purple key.
Room 2: Green key and a switch.
Room 3: Blue box.
Locked doors between Room 1 & 2 and Room 2 & 3.
Switch in Room 2 unlocks the door to Room 3.

Output:
1. Use the yellow key to unlock the yellow chest in Room 1 and retrieve the purple key.
2. Return the yellow key and take the red ball.
3. Go to Room 2 (still locked).
4. Return to Room 1, leave the red ball, and take the green key.
5. Unlock the door and enter Room 2 with the green key.
6. Place the green key back in Room 2, and take the red ball.
7. Activate the switch in Room 2 with the red ball to unlock the door to Room 3.
8. Return the red ball to Room 1 and retrieve the purple key.
9. Use the purple key to unlock the door to Room 3.
10. Enter Room 3 and retrieve the blue box.

```

## What is the task trying to measure?

The task is designed to measure the ability of the language model to generate plans of actions to achieve a specific goal within a given environment, considering constraints, feasibility, and logical steps rather than just generating text or open-ended responses. 

## Motivation

The task aims to harness Large Language Models' (LLMs) vast world knowledge and natural language flexibility to generate executable plans, reducing the need for domain-specific knowledge and addressing challenges in planning. By integrating LLMs with classical planning, it seeks to offer more efficient and feasible planning solutions in complex real-world environments.

## Related work
SayCanPay: Heuristic Planning with Large Language Models using Learnable Domain Knowledge (AAAI 2024, https://arxiv.org/abs/2308.12682)

Do As I Can, Not As I Say: Grounding Language in Robotic Affordances (CoRL 2022, https://arxiv.org/abs/2204.01691)

