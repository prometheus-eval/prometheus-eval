# Personal assistant

Tasks that schedule a daily plan of user's day considering user's schedule and priorities

**Authors:** Yoonjoo Lee (yoonjoo.lee@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
Schedule a daily plan of my day considering my schedule and priorities.

Tasks: Prepare presentation for Friday's meeting; respond to emails; review quarterly financial report.

Appointments: Dentist appointment at 2 PM; team meeting at 10 AM.

Preferences: Prefers to work on creative tasks in the morning; likes to take a lunch break at 1 PM; enjoys a short walk in the early evening.

Exercise: 30-minute jog; preferably in the morning.

Constraints: Must pick up children from school at 4 PM.

Additional Information: Prefers not to schedule work-related tasks after 6 PM.


Output:
7:00 AM - 7:30 AM: Morning jog (exercise)
7:30 AM - 8:00 AM: Breakfast and preparation for the day 
8:00 AM - 9:30 AM: Work on presentation for Friday's meeting (task, preference)
9:30 AM - 10:00 AM: Respond to urgent emails (task)
10:00 AM - 11:00 AM: Team meeting (appointment)
11:00 AM - 12:00 PM: Continue working on presentation (task)
12:00 PM - 1:00 PM: Review quarterly financial report (task)
1:00 PM - 1:30 PM: Lunch break (preference)
1:30 PM - 2:00 PM: Travel to dentist appointment 
2:00 PM - 3:00 PM: Dentist appointment (appointment)
3:00 PM - 3:30 PM: Travel back from dentist
3:30 PM - 4:00 PM: Prepare for school pick-up 
4:00 PM - 4:30 PM: Pick up children from school (constraint)
4:30 PM - 5:30 PM: Family time / Leisure activities
5:30 PM - 6:00 PM: Evening walk (preference)
6:00 PM onwards: Personal time (additional information)
```

## What is the task trying to measure?

The task is designed to measure the ability of the language model to understand individual user needs, efficiency in time management, adaptability to changes, and reasoning on time calculation.

## Motivation

The motivation behind this task is that it can measure the LM’s ability to effectively manage and personalize an individual's daily schedule and integrate their priorities and adapting to changes. Furthermore, this task can have significant practical implications as the use of LM's for personal assistants increases.

## Related work

FILL IN ME