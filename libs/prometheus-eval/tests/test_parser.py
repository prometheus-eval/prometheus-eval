import pytest

from prometheus_eval.parser import parse_output


# Pytest test cases
@pytest.mark.parametrize(
    "output,mode,expected",
    [
        # Absolute mode test cases
        ("Reference (Score 5) two results [RESULT] 3", "absolute", 3),
        ("Reference (Score 5) not results", "absolute", None),
        ("Excellent. [RESULT] 5 out of 5", "absolute", 5),
        ("Poor performance. [RESULT] score of 1", "absolute", 1),
        ("Good job. [Result] 3", "absolute", 3),
        ("Needs improvement. [Result] Score: 2", "absolute", 2),
        ("Well done. [Result] Result: 4", "absolute", 4),
        ("Average. [Result] 4/5", "absolute", 4),
        ("Excellent. [Result] 5 out of 5", "absolute", 5),
        ("Poor performance. [Result] score of 1", "absolute", 1),
        ("Good job. (Score 5)", "absolute", 5),
        ("Good job. [Score 4]", "absolute", 4),
        ("Good job. score: 3", "absolute", 3),
        ("Good job. Score: 3", "absolute", 3),
        ("Good job. score of 1", "absolute", 1),
        ("Good job. [RESULT] (5)", "absolute", 5),
        # Edge cases for absolute mode
        ("The score is definitely not 3.", "absolute", None),
        ("I rate this a perfect 10!", "absolute", None),
        ("Score: 2.5", "absolute", None),
        ("Result: A", "absolute", None),
        # Relative mode test cases
        ("[Response B is not better. [RESULT] A", "relative", "A"),
        ("Result A or B, not results", "relative", None),
        ("Response A is better. [RESULT] A", "relative", "A"),
        ("Prefer Response B. [RESULT] B", "relative", "B"),
        ("Feedback: Both responses are similar... [Response B]", "relative", "B"),
        ("Feedback: Both responses are clear... [Result] Response B", "relative", "B"),
        (
            "Feedback: Both responses are clear... Response B Response A",
            "relative",
            None,
        ),
        ("Feedback: Both responses are clear... [RESULT: B]", "relative", "B"),
        ("Feedback: Both responses are clear... [Result: B]", "relative", "B"),
        (
            "Feedback: Both responses are clear...Response A. [RESULT] B",
            "relative",
            "B",
        ),
        ("After careful consideration, I select Response B.", "relative", None),
        # Edge cases for relative mode
        ("Both responses have their merits.", "relative", None),
        ("Response C is clearly superior.", "relative", None),
        (
            "The better response is obviously B... or is it A? It's hard to decide.",
            "relative",
            None,
        ),
    ],
)
def test_parse_output(output, mode, expected):
    _, result = parse_output(output, mode)
    assert (
        result == expected
    ), f"Failed for input: '{output}', mode: {mode}, expected: {expected}, got: {result}"


# Additional tests for invalid modes and other edge cases
def test_invalid_mode():
    with pytest.raises(AssertionError):
        parse_output("Some output", "invalid_mode")


def test_empty_input():
    assert parse_output("", "absolute") == (None, None)
    assert parse_output("", "relative") == (None, None)


def test_none_input():
    assert parse_output(None, "absolute") == (None, None)
    assert parse_output(None, "relative") == (None, None)
