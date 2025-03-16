# Reward Modeling for Reinforcement Learning

The task is to rewrite reward functions based on a given feedback to efficiently solve reinforcement learning tasks.

**Author:** Se June Joo

## Example

A sample instance where the assistant is required to write a reward function to solve a humanoid running problem is provided below:

```
Input:
The Python environment is class Humanoid(VecTask): ...long...
...
Write a reward function for the following task: to make the humanoid run as fast as possible.
...
Generated reward function:
...
We trained a RL policy using the provided reward function code and it seems that the humaniod is frequently falling down.

Output:
Here is a proposed reward function that encourages the humanoid to run as fast as possible without falling:

```python
import torch
from torch import Tensor
from typing import Dict, Tuple

@torch.jit.script
def compute_reward(root_states: Tensor, velocity: Tensor, dt: Tensor) -> Tuple[Tensor, Dict[str, Tensor]]:

    # extract the torso_position
    torso_position = root_states[:, 0:3]
    
    # calculate the torso velocity by differentiating the position with respect to time. 
    torso_velocity = (torch.norm(velocity, dim=-1)).view(-1, 1)
    
    # Scale the torso_velocity to encourage the humanoid to run as fast as possible. 
    speed_reward: Tensor = torso_velocity / dt
    speed_reward_temp: float = 0.1
    scaled_speed_reward: Tensor = torch.exp(speed_reward / speed_reward_temp)
    
    # We want to encourage the humanoid to keep its footing, so we reward if the torso is above a certain position. 
    # extract the z-axis position of the torso
    torso_height = torso_position[:, 2].view(-1, 1)
    torso_height_temp: float = 0.1

    # The height of the humanoid's torso when it is standing up is approximately 1. The height when it is fallen down is approximately 0.2.
    # We give a reward if the height is above 0.2 to encourage the humanoid to stand up and run.
    height_reward = torch.where(torso_height > 0.2, torch.ones_like(torso_height), torch.zeros_like(torso_height))
    scaled_height_reward: Tensor = torch.exp(height_reward / torso_height_temp)

    reward = scaled_speed_reward + scaled_height_reward
    reward_components: Dict[str, Tensor] = {"scaled_speed_reward": scaled_speed_reward, "scaled_height_reward": scaled_height_reward}

    return reward, reward_components
```
...

## What is the task trying to measure?

The task measures the ability of the assistant to incorporate feedback and genretae accurate and efficient reward functions that help achieve the given objectives within reinforcement learning environments.

## Motivation

Reward functions are crucial elements in reinforcement learning as they define the feedback mechanism that guides the learning of the agent. But designing a good working reward function is a hard, making iterative refinement an essential step. 