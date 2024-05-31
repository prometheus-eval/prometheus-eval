# Simulating System or User Behaviors

Tasks that require the LLM to function as a simulator of the requested target (e.g., user or a terminal system).

**Authors:** Jinheon Baek

## Example

A sample query in a zero-shot setting:

```
System:
You should act as a Linux terminal, which will reply with what the terminal should show given a command. In addition, let assume that you have a notes.txt file in the current directory, which is composed of the following texts:

Meeting at 10am with the design team.
Remember to email the report to John.

To-Do:
1. Finalize presentation slides for Monday's meeting.
2. Call the marketing department about the new campaign.
3. Buy coffee beans on the way home.

Shopping List:
- Milk
- Bread
- Coffee beans
- Apples

Important Dates:
- Feb 12: Sarah's birthday
- Feb 20: Marketing campaign launch
- Mar 01: Annual general meeting

Notes from Last Meeting:
- Increase social media presence
- Focus on user experience in the new design
- Schedule a follow-up meeting with the IT department

Remember to review the budget report by Wednesday.
Yoga class at 6pm on Thursday.
Dinner with Emily and Tom this Saturday.

Input:
grep "design" notes.txt

Output:
Meeting at 10am with the design team.
- Focus on user experience in the new design
```

## What is the task trying to measure?


The task is designed to measure the ability of the language model to accurately simulate the behavior or responses of the specified target, such as a user or a terminal system.

## Motivation

The motivation behind this task is to assess and enhance the capability of the language model to understand and replicate specific user behaviors or system functions, thereby checking and improving its utility and adaptability in varied scenarios.

## Related work

* Unlocking the Potential of User Feedback: Leveraging Large Language Model as User Simulator to Enhance Dialogue System (https://arxiv.org/abs/2306.09821)
* Building A Virtual Machine inside ChatGPT (https://www.engraved.blog/building-a-virtual-machine-inside/)