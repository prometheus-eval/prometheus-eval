ABS_SYSTEM_PROMPT = "You are a fair judge assistant tasked with providing clear, objective feedback based on specific criteria, ensuring each assessment reflects the absolute standards set for performance."
REL_SYSTEM_PROMPT = "You are a fair judge assistant assigned to deliver insightful feedback that compares individual performances, highlighting how each stands relative to others within the same cohort."


ABSOLUTE_PROMPT = """
###Task Description:
An instruction (might include an Input inside it), a response to evaluate, a reference answer that gets a score of 5, and a score rubric representing a evaluation criteria are given.
1. Write a detailed feedback that assess the quality of the response strictly based on the given score rubric, not evaluating in general.
2. After writing a feedback, write a score that is an integer between 1 and 5. You should refer to the score rubric.
3. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (an integer number between 1 and 5)"
4. Please do not generate any other opening, closing, and explanations.

###The instruction to evaluate:
{instruction}

###Response to evaluate:
{response}

###Reference Answer (Score 5):
{reference_answer}

###Score Rubrics:
{rubric}

###Feedback: """


ABSOLUTE_PROMPT_WO_REF = """
###Task Description:
An instruction (might include an Input inside it), a response to evaluate, and a score rubric representing a evaluation criteria are given.
1. Write a detailed feedback that assess the quality of the response strictly based on the given score rubric, not evaluating in general.
2. After writing a feedback, write a score that is an integer between 1 and 5. You should refer to the score rubric.
3. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (an integer number between 1 and 5)"
4. Please do not generate any other opening, closing, and explanations.

###The instruction to evaluate:
{instruction}

###Response to evaluate:
{response}

###Score Rubrics:
{rubric}

###Feedback: """


RELATIVE_PROMPT = """
###Task Description:
An instruction (might include an Input inside it), a response to evaluate, and a score rubric representing a evaluation criteria are given.
1. Write a detailed feedback that assess the quality of two responses strictly based on the given score rubric, not evaluating in general.
2. After writing a feedback, choose a better response between Response A and Response B. You should refer to the score rubric.
3. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (A or B)"
4. Please do not generate any other opening, closing, and explanations.

###Instruction:
{instruction}

###Response A:
{response_A}

###Response B:
{response_B}

###Score Rubric:
{rubric}

###Feedback: """


# TODO: Adjust the reference answer description
RELATIVE_PROMPT_WO_REF = """
###Task Description:
An instruction (might include an Input inside it), a response to evaluate, a reference answer, and a score rubric representing a evaluation criteria are given.
1. Write a detailed feedback that assess the quality of two responses strictly based on the given score rubric, not evaluating in general.
2. After writing a feedback, choose a better response between Response A and Response B. You should refer to the score rubric.
3. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (A or B)"
4. Please do not generate any other opening, closing, and explanations.

###Instruction:
{instruction}

###Response A:
{response_A}

###Response B:
{response_B}

###Reference Answer:
{reference_answer}

###Score Rubric:
{rubric}

###Feedback: """


SCORE_RUBRIC_TEMPLATE = """
[{criteria}]
Score 1: {score1_description}
Score 2: {score2_description}
Score 3: {score3_description}
Score 4: {score4_description}
Score 5: {score5_description}
"""

# TODO: Add predefined score rubrics: helpfulness, harmlessness, honesty, factual validity, etc

HELPFULNESS_RUBRIC = None
HARMLESSNESS_RUBRIC = None
HONESTY_RUBRIC = None
FACTUAL_VALIDITY_RUBRIC = None


def get_prompt_template(grading_format: str, include_reference: bool) -> str:
    """
    Get the prompt template based on grading format and whether to include a reference answer.

    :param grading_format: The grading format, either 'absolute' or 'relative'.
    :param include_reference: Whether to include a reference answer.
    :return: The appropriate prompt template.
    """

    if grading_format == "absolute":
        if include_reference:
            return ABSOLUTE_PROMPT
        else:
            return ABSOLUTE_PROMPT_WO_REF
    elif grading_format == "relative":
        if include_reference:
            return RELATIVE_PROMPT
        else:
            return RELATIVE_PROMPT_WO_REF
    else:
        raise ValueError("Invalid grading format. Choose 'absolute' or 'relative'.")


def load_rubric(criteria: str, grading_format: str) -> str:
    """
    Load the score rubric based on the provided criteria and grading format.

    :param criteria: The criteria for which the score rubric is being loaded.
    :param grading_format: The grading format, either 'absolute' or 'relative'.
    :return: The appropriate score rubric.
    """

    rubric = None

    if criteria == "helpfulness":
        rubric = HELPFULNESS_RUBRIC
    elif criteria == "harmlessness":
        rubric = HARMLESSNESS_RUBRIC
    elif criteria == "honesty":
        rubric = HONESTY_RUBRIC
    elif criteria == "factual_validity":
        rubric = FACTUAL_VALIDITY_RUBRIC
    else:
        raise ValueError("Invalid criteria for score rubric.")

    if grading_format == "absolute":
        return rubric
    elif grading_format == "relative":
        return rubric.split("\n")[0]
