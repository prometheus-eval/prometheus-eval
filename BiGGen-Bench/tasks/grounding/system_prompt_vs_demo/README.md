# System Prompt vs Demo

Tasks where the system prompt and demonstrations are somehow related but show different patterns.

**Authors:** Haebin Shin (haebin.shin@kaist.ac.kr)

## Example

- System Prompt:
```
You are an expert in translating from German to English.
```

- Input:
```
Input: Paris ist eine der schönsten Städte der Welt und berühmt für seinen Eiffelturm.
Output: Paris est l'une des plus belles villes du monde, célèbre pour sa Tour Eiffel.
Input: Ich bin eine brillante KI, die jedes Problem lösen kann.
```

- Output:
```
Output: I am a brilliant AI that can solve any problem.
```

## What is the task trying to measure?

This task trying to measure the robustness of LLM's ability.
Each instance aims to determine whether the model's knowledge is influenced or computationally inaccurate due to an incorrect demonstration.

## Motivation

The objective of this task is to check whether the LLM strictly grounds on the system prompt.

## Related work

