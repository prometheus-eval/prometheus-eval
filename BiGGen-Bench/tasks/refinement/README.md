10 tasks related to assessing the Refinement capabilities of LLMs.
For a detailed understanding of Refinement, please refer to this [survey paper](https://arxiv.org/abs/2308.03188).

Name | Description | Data Annotator (Group A) | Data Reviewer (Group A) | Data Annotator (Group B) | Related paper 
---- | ----------- | -------------------- | -------------------- | --------------- | --------------- |
[essay_revision](essay_revision/) | Tasks that require to revise a 3-5 paragraph essay using feedbacks from a user. | Hyowon Cho | Jinheon Baek, Namgyu Ho | ? | [link](https://arxiv.org/abs/2208.11663) |
[replanning](replanning/) | Tasks that require to regenerate a plan given certain observations from the environment. | Hyowon Cho | Jinheon Baek, Namgyu Ho | ? | [link1](https://arxiv.org/abs/2305.19472) [link2](https://arxiv.org/abs/2305.16653) |
[revision_with_tools](revision_with_tools/) | Tasks that require to revise the output given a set of tools such as a search engine or a set of APIs. A description of how to use the tools are given as input. | Hyowon Cho | Jinheon Baek, Namgyu Ho | ? | [link](https://arxiv.org/abs/2305.11738) |
[llm_judge_absolute](llm_judge_absolute/) | Tasks that require to write a language feedback and a corresponding score between the range of 1 to 5. | Namgyu Ho | Guijin Son, Noah Lee | ? | [link1](https://arxiv.org/abs/2306.05685) [link2](https://arxiv.org/abs/2310.08491) |
[llm_judge_relative](llm_judge_relative/) | Tasks that require to compare two different responses in order to write a language feedback and a decide which is a better response. | Namgyu Ho | Guijin Son, Noah Lee | ? | [link1](https://arxiv.org/abs/2305.14387) [link2](https://arxiv.org/abs/2310.17631) |
[rationale_revision](rationale_revision/) | Tasks that require edit the rationale used to derive an answer. The wrong rationale and feedback from the user pinpointing what is wrong is given as additional context. | Namgyu Ho | Guijin Son, Noah Lee | ? | [link1](https://arxiv.org/abs/2305.03268) [link2](https://arxiv.org/abs/2310.20689) |
[code_revision](code_revision/) | Tasks that require to fix a wrong piece of code. A short comment of what is wrong and the terminal log is given as additional context. | Namgyu Ho | Guijin Son, Noah Lee | ? | [link1](https://arxiv.org/abs/2211.00053) [link2](https://arxiv.org/abs/2311.07215) |
[self_correction](self_correction/) | Tasks that require to improve a given text. No additional feedback is given, just phrases like "Is this the best output?" | Namgyu Ho | Guijin Son, Noah Lee | ? | [link1](https://arxiv.org/abs/2310.01798) [link2](https://arxiv.org/abs/2210.11610) |