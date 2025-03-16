10 tasks related to assessing the tool usage capabilities of LLMs.
For a detailed understanding of tool usage, please refer to this [survey paper](https://arxiv.org/abs/2302.07842).

Name | Description | Data Annotator (Group A) | Data Reviewer (Group A) | Data Annotator (Group B) | Related paper 
---- | ----------- | -------------------- | -------------------- | --------------- | --------------- |
[web_browsing](web_browsing/) | Tasks that require generating actionable items while browsing through the web | Hyungjoo Chae | Sejune Joo, Juyoung Suk | ? | [link1](https://arxiv.org/abs/2307.13854), [link2](https://arxiv.org/abs/2306.06070)
[tool_making](tool_making/) | Tasks that require creating new set of tools for problem-solving | Hyungjoo Chae | Sejune Joo, Juyoung Suk | ? | [link](https://arxiv.org/abs/2305.17126)
[compositional_tools](compositional_tools/) | Tasks that require combining an existing set of tools to build a higher-level compositional tool to solve a problem | Hyungjoo Chae | Sejune Joo, Juyoung Suk | ? | [link1](https://arxiv.org/abs/2304.09842), [link2](https://arxiv.org/abs/2310.03720)
[human_intervention](human_intervention/) | Tasks that require solving a task with an ethical issue in between. The model should pause and ask the human to make the decisions. In other words, making the human decide is a tool itself! | Hyungjoo Chae | Sejune Joo, Juyoung Suk | ? | NOT AVAILABLE
[vision_tasks](vision_tasks/) | Tasks that require utilizing vision models from huggingface to solve a task that require understanding a given image as the intermediate step to solve a more complex problem | Hyungjoo Chae | Sejune Joo, Juyoung Suk | ? | [link](https://arxiv.org/abs/2303.17580)
[coding_for_math](coding_for_math/) | Tasks that require to use a coding terminal to solve a math word problem | Hanseok Oh | Seongyun Lee, Guijin Son | ? | [link1](https://arxiv.org/pdf/2211.10435.pdf), [link2](https://arxiv.org/abs/2309.17452), [link3](https://arxiv.org/abs/2211.12588)
[multi_step](multi_step/) | Tasks requiring the breakdown of a given task into subtasks and using tools appropriately | Hanseok Oh | Seongyun Lee, Guijin Son | ? | [link](https://arxiv.org/abs/2303.09014)
[search_engine](search_engine/) | Tasks that involve the use of search engines and generating effective search queries | Hanseok Oh | Seongyun Lee, Guijin Son | ? | [link](https://arxiv.org/abs/2112.09332)
[api_documentation](api_documentation/) | Tasks that require reading through a set of documentations to write a piece of code that uses multiple APIs | Hanseok Oh | Seongyun Lee, Guijin Son | ? | [link1](https://arxiv.org/abs/2307.16789), [link2](https://arxiv.org/abs/2308.00675)
[item_recommendation](item_recommendation/) | Tasks that require recommending a requested item using multiple APIs and search engines. | Hanseok Oh | Seongyun Lee, Guijin Son | ? | [link1](https://arxiv.org/abs/2305.19860), [link2](https://arxiv.org/abs/2311.12338)
