import pytest

from prometheus_eval import PrometheusEval  # Adjust the import path as necessary


@pytest.fixture(scope="module")
def judge():
    # Initialize PrometheusEval once for all tests in this module
    print("Setting up PrometheusEval")
    judge_instance = PrometheusEval(is_test=True, dtype="auto")
    yield judge_instance
    # If there's any cleanup needed, it can be done here
    print("Tearing down PrometheusEval")


def test_init(judge):
    assert (
        hasattr(judge, "model_id")
        and hasattr(judge, "num_gpus")
        and hasattr(judge, "download_dir")
    )
    assert hasattr(judge, "absolute_grade_template") and hasattr(
        judge, "relative_grade_template"
    )


def test_absolute_grade_with_valid_input(judge):
    instructions = ["Describe the process of photosynthesis."]
    responses = [
        "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods."
    ]
    rubric = "Detailed explanation of biological processes."
    reference_answers = None

    feedbacks, scores = judge.absolute_grade(
        instructions=instructions,
        responses=responses,
        rubric=rubric,
        reference_answers=reference_answers,
        params={},
    )
    assert len(feedbacks) == len(responses)
    assert all(isinstance(score, int) for score in scores)


def test_absolute_grade_with_invalid_input(judge):
    instructions = ["Explain quantum mechanics."]
    responses = []  # No corresponding response

    rubric = "Accuracy and completeness of scientific concepts."

    with pytest.raises(ValueError):
        _ = judge.absolute_grade(
            instructions=instructions,
            responses=responses,
            rubric=rubric,
            reference_answers=None,
            params={},
        )


def test_relative_grade_with_valid_input(judge):
    instructions = ["Evaluate these AI responses."]
    responses_A = ["AI can think like humans."]
    responses_B = ["AI uses algorithms to simulate human thinking."]
    rubric = "Assessment of AI capabilities."
    reference_answers = ["AI uses data. AI mimics human cognition."]

    feedbacks, scores = judge.relative_grade(
        instructions=instructions,
        responses_A=responses_A,
        responses_B=responses_B,
        rubric=rubric,
        reference_answers=reference_answers,
        params={},
    )
    assert len(feedbacks) == len(responses_A) and len(scores) == len(responses_A)


def test_relative_grade_with_missing_keys(judge):
    instructions = ["Discuss blockchain technology."]
    responses_A = ["Blockchain is a distributed ledger technology."]
    responses_B = []  # Missing a corresponding response_B
    rubric = "Explanation of technology principles."

    with pytest.raises(ValueError):
        _ = judge.relative_grade(
            instructions=instructions,
            responses_A=responses_A,
            responses_B=responses_B,
            rubric=rubric,
            params={},
        )
