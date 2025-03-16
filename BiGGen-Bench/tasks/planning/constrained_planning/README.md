# Constrained Planning

The task involves creating plans considering varying constraints and the capability to improvise and modify existing plans.

**Author:** Se June Joo

## Example

The following is a sample instance in a zero-shot setting where the city's standard evacuation plan needs to be revised due to an unforeseen constraint.

```
Input:
Develop a revised city evacuation plan for a densely populated urban area, considering a scenario where the primary evacuation routes are suddenly rendered unusable. The plan must utilize alternative methods and paths for evacuation.

Initial State: The city has a standard evacuation plan utilizing major roads and highways.

Goal: Revise the evacuation plan to ensure safe and efficient evacuation of citizens using secondary routes and methods due to the primary routes being blocked.

Output:
The revised evacuation plan should consider the following steps:

1. Identify secondary routes such as narrow streets, pedestrian paths, and waterways for evacuation.
2. Utilize public transportation systems, bicycles, and boats for movement.
3. Implement a staged evacuation strategy to minimize congestion and ensure a smooth flow of evacuees.
4. Employ a 'universally quickest flow' model to manage the flow of evacuees efficiently, considering the capacity constraints of refuges and secondary routes.
5. Establish temporary shelters and aid stations along the secondary routes.
6. Communicate the revised plan to residents through various channels, ensuring clear understanding and compliance.

This plan addresses the constrained scenario of primary evacuation routes being blocked, ensuring a safe and orderly evacuation using alternative means.
```

## What is the task trying to measure?

The task measures a model's ability to revise and make plans considering unforeseen constraints. It assesses its capability to make use of alternative strategies and improvise based on the situation.

## Motivation

The motivation is to gauge the model's proficiency in devising plans under constraints and modify existing plans effectively. This aims to determine the model's capability in utilizing resources optimally, adapt to changing situations, and provide precise solutions, thus assisting in decision-making processes.

## Related work