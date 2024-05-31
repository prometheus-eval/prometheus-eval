# Multi-Step Tool Usage

Tasks requiring the breakdown of a given task into subtasks and using tools appropriately.

**Authors:** Hanseok Oh

## Example

A sample query in a zero-shot setting:

```
Input:

For my homework, I need to solve the following math problem: "A cylinder has a height of 10 inches and a base radius of 3 inches. Find the volume of the cylinder." To do this, I used a search engine to find the formula for calculating the volume of a cylinder like follows.

<search> quadratic formula</search>

Here is the search result,

<result> (cylinder-volume-and-surface-area) A cylinder's volume is V = πr^2h, and its surface area is 2π r h + 2π r², where V is the volume, r is the radius, and h is the height. Learn how to use these formulas to solve an example problem. | 

(Quadratic formula) 

In elementary algebra, the quadratic formula is a formula that provides the two solutions, or roots, to a quadratic equation. There are other ways of solving a quadratic equation instead of using the quadratic formula, such as completing the square.

Given a general quadratic equation of the form

x = (-b ± √(b^2 - 4ac)) / (2a) | 

None

</result>

Finalize the answer based on this formula and create a plot to visualize the cylinder and explain the calculation.

Output:

To finalize the answer for the volume of the cylinder and to create a visualization, we need to follow these steps:

1. **Calculate the Volume of the Cylinder**:
    - The correct formula for the volume of a cylinder is \( V = \pi r^2 h \), as indicated in the search result.
    - For a cylinder with a height (h) of 10 inches and a base radius (r) of 3 inches, the volume calculation will be \( V = \pi \times 3^2 \times 10 \).
    - This calculation can be performed using the Calculator tool.
    
    Here's the calculator tool command:
    
    <calculator> 3.14159 | * | 3 | * | 3 | * | 10 </calculator>
    
2. **Visualize the Cylinder with a Python Plot**:
    - To visualize the cylinder, we will use Python to create a 3D plot that represents its dimensions.
    - This visualization will help in understanding the physical shape and size of the cylinder based on the given dimensions.
    
    Here's an example of the Python code for the visualization:
    
    <python>import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np
    
    height = 10
    radius = 3
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(-radius, radius, 100)
    z = np.linspace(0, height, 100)
    X, Z = np.meshgrid(x, z)
    Y = np.sqrt(radius**2 - X**2)
    
    ax.plot_surface(X, Y, Z, alpha=0.3, color='blue')
    ax.plot_surface(X, -Y, Z, alpha=0.3, color='blue')
    
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('3D plot of a Cylinder')
    
    plt.show()
    
    </python>
    

This Python script will generate a 3D representation of the cylinder, showing its height and radius as per the problem's specifications. Combining the calculated volume and the visual representation provides a comprehensive answer to the homework problem.

```

## What is the task trying to measure?

The task is trying to measure the ability to break down a given complex task into subtasks and utilize various tools appropriately to accomplish those subtasks effectively. It assesses the skill of task decomposition and tool utilization.

## Motivation

The motivation behind this task is to evaluate an individual's problem-solving and decision-making skills when faced with a multi-step task. It aims to assess their capacity to strategically use available tools to achieve specific objectives, highlighting their adaptability and resourcefulness in problem-solving scenarios.

## Related work

* ART: Automatic multi-step reasoning and tool-use for large language models (https://arxiv.org/abs/2303.09014)