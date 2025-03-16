# Compositional Planning

Tasks that require devising a high-level plan composed of several low-level tasks.

**Author:** Se June Joo

## Example

Let's take an example where a robot has to clean and organize a cluttered room in a hierarchical manner. 

```
Input:
In a scenario where a robot must clean and organize a cluttered room, devise a high-level plan composed of several low-level tasks. The tasks include picking up toys, vacuuming the floor, and arranging books on a shelf.

Initial State: The room is cluttered with toys on the floor, a dirty carpet, and books scattered around.

Goal: Clean and organize the room with toys in the toy box, a vacuumed carpet, and books arranged on the shelf.

Output:
To clean and organize the room, the robot should execute the following high-level plan composed of low-level tasks:

1. Start by picking up toys from the floor and placing them in the toy box.
2. Vacuum the carpet thoroughly to clean it.
3. Arrange the scattered books in a specific order on the shelf.

This plan demonstrates the robot's ability to break down the complex task of room organization into manageable sub-tasks, efficiently allocating resources and time for each task.
```

## What is the task trying to measure?

The task measures a model's proficiency in employing hierarchical and compositional planning for complex problem solving. It assesses the model's ability to decompose a high-level task into manageable sub-tasks, sequence these tasks logically, and provide a comprehensive high-level plan.

## Motivation

The motivation behind evaluating "Compositional Planning" skills is to test the model's competence in undertaking complex projects requiring hierarchical structure. It aims to determine the model's ability to devise effective strategies, optimize task allocation, and convey planning concepts clearly, thus ensuring its proficiency in supporting technical and project management tasks.

## Related work