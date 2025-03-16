# Essay Revision

This task requires to revise a 3-5 paragraph essay using feedbacks from a user.

## What is the task trying to measure?

We evaluate through this task whether the language model can effectively modify the text according to our requirements. The requirements can sometimes be intuitive and objective, but sometimes they can be subjective (e.g. make the text more interesting). Additionally, the requirements can be specific or more general. Therefore, our main goal is to assess whether the language model interprets the given instructions well and reflects them in the text.

## Design considerations

Since humans can give any command to the language model, we designed the evaluation dataset to be as diverse as possible yet challenging. Additionally, we ensured that each passage comes from a different domain. Among the five tasks, two require intensive revisions, while three require overall modifications. The final tasks we expect are as follows:

- Modify non-native speaker's text to sound like it was written by a native speaker.
- Simplify difficult text.
- Modify text considering the inclusion of counterfactual information.
- Add new content at specific locations.
- Remove content related to a specific topic.

## Data source

The text to be transformed was extracted from the following sources: wiki, toefl, [The Uppsala Student English corpus](http://hdl.handle.net/20.500.12024/2457).

## References

Schick, T., Dwivedi-Yu, J., Jiang, Z., Petroni, F., Lewis, P., Izacard, G., You, Q., Nalmpantis, C., Grave, E., & Riedel, S. (2022). PEER: A Collaborative Language Model. *ArXiv, abs/2208.11663*.