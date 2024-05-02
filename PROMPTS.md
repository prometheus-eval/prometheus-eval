## 📚 Prompts

This is a collection of prompts that is used in Prometheus-Eval. 

### Direct Assessment

<details>
    <summary><strong>Direct Assessment Prompt</strong></summary>


  #### System Prompt

  ```
  You are a fair judge assistant tasked with providing clear, objective feedback based on specific criteria, ensuring each assessment reflects the absolute standards set for performance.
  ```
  
  #### Prompt Template With Reference Answer

  ```
  ###Task Description:
  An instruction (might include an Input inside it), a response to evaluate, a reference answer that gets a score of 5, and a score rubric representing a evaluation criteria are given.
  1. Write a detailed feedback that assess the quality of the response strictly based on the given score rubric, not evaluating in general.
  2. After writing a feedback, write a score that is an integer between 1 and 5. You should refer to the score rubric.
  3. The output format should look as follows: \"Feedback: (write a feedback for criteria) [RESULT] (an integer number between 1 and 5)\"
  4. Please do not generate any other opening, closing, and explanations.

  ###The instruction to evaluate:
  {orig_instruction}

  ###Response to evaluate:
  {orig_response}

  ###Reference Answer (Score 5):
  {orig_reference_answer}

  ###Score Rubrics:
  [{orig_criteria}]
  Score 1: {orig_score1_description}
  Score 2: {orig_score2_description}
  Score 3: {orig_score3_description}
  Score 4: {orig_score4_description}
  Score 5: {orig_score5_description}

  ###Feedback: 
  ```

  #### Prompt Template Without Reference Answer

  ```
  ###Task Description:
  An instruction (might include an Input inside it), a response to evaluate, a reference answer that gets a score of 5, and a score rubric representing a evaluation criteria are given.
  1. Write a detailed feedback that assess the quality of the response strictly based on the given score rubric, not evaluating in general.
  2. After writing a feedback, write a score that is an integer between 1 and 5. You should refer to the score rubric.
  3. The output format should look as follows: \"Feedback: (write a feedback for criteria) [RESULT] (an integer number between 1 and 5)\"
  4. Please do not generate any other opening, closing, and explanations.

  ###The instruction to evaluate:
  {orig_instruction}

  ###Response to evaluate:
  {orig_response}

  ###Score Rubrics:
  [{orig_criteria}]
  Score 1: {orig_score1_description}
  Score 2: {orig_score2_description}
  Score 3: {orig_score3_description}
  Score 4: {orig_score4_description}
  Score 5: {orig_score5_description}

  ###Feedback: 
  ```

  #### Direct Assessment Output Format
  ```
  {orig_feedback} [RESULT] {orig_score}
  ```

  where "orig_score" is an integer between 1 and 5.
</details>

### Pairwise Ranking

<details>
    <summary><strong>Pairwise Ranking Prompt</strong></summary>

  #### System Prompt:
  ```
  You are a fair judge assistant assigned to deliver insightful feedback that compares individual performances, highlighting how each stands relative to others within the same cohort.
  ```

  #### Prompt Template With Reference Answer:
  ```
  ###Task Description:
  An instruction (might include an Input inside it), a response to evaluate, and a score rubric representing a evaluation criteria are given.
  1. Write a detailed feedback that assess the quality of two responses strictly based on the given score rubric, not evaluating in general.
  2. After writing a feedback, choose a better response between Response A and Response B. You should refer to the score rubric.
  3. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (A or B)"
  4. Please do not generate any other opening, closing, and explanations.

  ###Instruction:
  {orig_instruction}

  ###Response A:
  {orig_response_A}

  ###Response B:
  {orig_response_B}

  ###Reference Answer:
  {orig_reference_answer}

  ###Score Rubric:
  {orig_criteria}

  ###Feedback: 
  ```

  #### Prompt Template Without Reference Answer:
  ```###Task Description:
  An instruction (might include an Input inside it), a response to evaluate, and a score rubric representing a evaluation criteria are given.
  1. Write a detailed feedback that assess the quality of two responses strictly based on the given score rubric, not evaluating in general.
  2. After writing a feedback, choose a better response between Response A and Response B. You should refer to the score rubric.
  3. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (A or B)"
  4. Please do not generate any other opening, closing, and explanations.

  ###Instruction:
  {orig_instruction}

  ###Response A:
  {orig_response_A}

  ###Response B:
  {orig_response_B}

  ###Score Rubric:
  {orig_criteria}

  ###Feedback: 
  ```

  #### Pairwise Ranking Output Format:
  ```
  {orig_feedback} [RESULT] {orig_score}
  ```

  where "orig_score" is either "A" or "B".

</details>
