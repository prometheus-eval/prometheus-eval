# Programming

Tasks that leverage programming and coding capability for complex problem solving.

**Authors:** Hanseok Oh

## Example

A sample query in a zero-shot setting:

```
Input:
Help! I’m trying to solve a math problem that my teacher gave me. I have to calculate the integral of f(X) = x^2 from 0 to 5. After acquiring the result, could you also visualize the result for me to understand?


Output:
Certainly! To solve this math problem, I'll first calculate the integral of the function f(x)=x^2 from 0 to 5 using Python. After that, I'll generate a visualization to help you understand the result better. Let's start with the calculation of the integral.

<python> import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Function to integrate
def f(x):
    return x**2

# Calculating the integral of f(x) from 0 to 5
integral_result, _ = quad(f, 0, 5)

# Visualization
x = np.linspace(0, 5, 100)
y = f(x)

plt.fill_between(x, y, color="skyblue", alpha=0.4)
plt.plot(x, y, color="Slateblue", alpha=0.6)
plt.title("Area under the curve f(x) = x^2 from 0 to 5")
plt.xlabel("x")
plt.ylabel("f(x)")

# Save the plot to a file
plt.savefig('/mnt/data/integral_visualization.png')
plt.show()

integral_result

</python>

This code will calculate the integral of f(x)=x^2 from 0 to 5 and also create a plot showing the area under the curve, which represents the integral. The resulting value of the integral will be displayed, and the plot will be saved as an image file.
```

## What is the task trying to measure?

The task measures a model's proficiency in leveraging coding and programming to solve complex mathematical and scientific problems. It assesses algorithmic problem-solving skills, programming proficiency, and the ability to represent and explain mathematical solutions effectively.

## Motivation

The motivation behind evaluating "coding for math" skills is to assess the language model's competence in applying coding and programming to solve complex mathematical and scientific problems accurately. It aims to determine the model's ability to devise precise solutions, optimize code for efficiency, and convey mathematical concepts clearly, thus ensuring its proficiency in supporting technical and mathematical problem-solving tasks.

## Related work

* TORA: A TOOL-INTEGRATED REASONING AGENT FOR MATHEMATICAL PROBLEM SOLVING (https://arxiv.org/abs/2309.17452)

* Program of Thoughts Prompting: Disentangling Computa- tion from Reasoning for Numerical Reasoning Tasks (https://arxiv.org/abs/2211.12588)

* PAL: Program-aided Language Models (https://arxiv.org/abs/2211.10435)