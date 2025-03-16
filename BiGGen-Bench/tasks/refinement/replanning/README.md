# Hypothesis Proposal

This is the tasks that requires to regenerate a plan given certain observations from the environment.

## What is the task trying to measure?

This task aims to measure the ability of a language model to identify and improve deficiencies in a given plan. Deficiencies in a plan refer to ambiguity, impracticality, inefficiency, and so on. For example, if the steps of an initial plan are unclear and it is not clear what actions should be taken, the language model should capture this and generate more specific instructions. In addition, we also evaluate the ability of the language model to revise the initial plan when a new condition arrives. 

## Design considerations

To measure both mentioned abilities, we composed three evaluation data with the structure (goal, condition, initial plan, problem, instruction), and two evaluation data with the structure (initial goal, plan, new goal, instruction). In the former case, the main purpose is to resolve the ambiguity in the initial plan. In the latter case, the objective is to modify the initial plan considering the new goal.

## Data source

All goals and conditions were extracted from the COPLAN Dataset.

## References

Brahman, F., Bhagavatula, C., Pyatkin, V., Hwang, J.D., Li, X.L., Arai, H.J., Sanyal, S., Sakaguchi, K., Ren, X., & Choi, Y. (2023). PlaSma: Making Small Language Models Better Procedural Knowledge Models for (Counterfactual) Planning. *ArXiv, abs/2305.19472*.