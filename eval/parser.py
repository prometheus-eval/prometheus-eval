import re

def _parse_output_absolute(output):
    # Extended pattern to match more variations of result presentation
    # pattern = r"""
    #     (?:\[RESULT\]|Score:|score:|Result:|\[Result\]|score of|\(|\[|\])\s*  # Match different prefixes including '[RESULT]', 'Score:', etc.
    #     (?:\[RESULT\]|Score:|score:|Result:|\[Result\]|score of|\(|\[|\])\s*
    #     |(\d+)\s*                               # Catch trailing numbers
    #     |\((\d+)\)                              # Catch numbers within parentheses
    #     |\[(\d+)\]                              # Catch numbers within brackets
    # """
    pattern = r"""(?:\[RESULT\]|Score|\[SCORE\]|\[RESULT\]:|Score:|score:|Result:|\[Result\]|score of)\s*(?:\(\s*|\[\s*|)\s*(\d+)"""
    matches = re.search(pattern, output, re.IGNORECASE | re.VERBOSE)

    if matches:
        # Extract the first group that matches (ignoring None)
        result = next((int(match) for match in matches.groups() if match), None)
        if result is not None:
            feedback = (
                output.split("[RESULT]")[0].strip() if "[RESULT]" in output else output
            )
            return feedback, result

    return None, None


def _parse_output_relative(output):
    # Updated pattern to match [RESULT] A/B, [Response A/B], and [Result] Response A/B formats
    pattern = r"""
        \[RESULT\]\s*(A|B)|                     # Matches [RESULT] A or B directly
        \[RESULT:\s*(A|B)\]|                    # Matches [RESULT: A] or [RESULT: B]
        \[Response\s+(A|B)\]|                   # Matches [Response A] or [Response B]
        \[Result\]\s+Response\s+(A|B)|          # Matches [Result] Response A or B
        \[Result:\s*(A|B)\]|                    # Matches [Result: A] or [Result: B]
        \[Result\]\s*(A|B)|                     # Matches [Result] A or B directly
    """

    matches = re.findall(pattern, output, re.IGNORECASE | re.VERBOSE)

    # Flatten the matches and filter out empty strings, then take the first valid result
    results = [item for sublist in matches for item in sublist if item]
    if not results:
        return None, None

    result = results[0]
    # Attempt to extract feedback based on the presence of "[RESULT]" or falling back to the entire output
    feedback = (
        output.split("[RESULT]")[0].strip()
        if "[RESULT]" in output
        else output.split("\n")[0].strip()
    )

    return feedback, result


def parse_output(outputs, mode: str):
    assert mode in [
        "absolute",
        "relative",
    ], "Invalid mode. Supported modes are: 'absolute' and 'relative'"

    if mode == "absolute":
        return _parse_output_absolute(outputs)

    if mode == "relative":
        return _parse_output_relative(outputs)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        # Absolute mode test cases (a2a, a2r)
        ("Good job. [RESULT] 3", "a2a", 3),
        ("Needs improvement. [RESULT] Score: 2", "a2a", 2),
        ("Well done. [RESULT] Result: 4", "a2a", 4),
        ("Average. [RESULT] 4/5", "a2a", 4),
        ("Excellent. [RESULT] 5 out of 5", "a2a", 5),
        ("Poor performance. [RESULT] score of 1", "a2a", 1),
        ("Good job. [Result] 3", "a2a", 3),
        ("Needs improvement. [Result] Score: 2", "a2a", 2),
        ("Well done. [Result] Result: 4", "a2a", 4),
        ("Average. [Result] 4/5", "a2a", 4),
        ("Excellent. [Result] 5 out of 5", "a2a", 5),
        ("Poor performance. [Result] score of 1", "a2a", 1),
        ("Good job. [3]", "a2a", 3),
        ("Good job. (Score 5)", "a2a", 5),
        ("Good job. [Score 4]", "a2a", 4),
        ("Good job. score: 3", "a2a", 3),
        ("Good job. Score: 3", "a2a", 3),
        ("Good job. score of 1", "a2a", 1),
        ("Good job. [RESULT] (5)", "a2a", 5),
        # Relative mode test cases (r2r)
        ("Response A is better. [RESULT] A", "r2r", "A"),
        ("Prefer Response B. [RESULT] B", "r2r", "B"),
        ("Feedback: Both responses are similar... [Response B]", "r2r", "B"),
        ("Feedback: Both responses are clear... [Result] Response B", "r2r", "B"),
        ("Feedback: Both responses are clear... Response B", "r2r", "B"),
        ("Feedback: Both responses are clear... [RESULT: B]", "r2r", "B"),
        ("Feedback: Both responses are clear... [Result: B]", "r2r", "B"),
        ("Feedback: Both responses are clear... [B]", "r2r", "B"),
        (
            "Feedback: Both responses are clear... based on the given rubric, Response B is a better fit",
            "r2r",
            "B",
        ),
    ]

    def run_tests():
        failed_tests = []  # To keep track of failed tests

        for output, mode, expected in test_cases:
            _, result = parse_output(output, mode)
            if result != expected:
                failed_tests.append((output, mode, expected, result))

        if failed_tests:
            print("Some tests failed:")
            for output, mode, expected, result in failed_tests:
                print(
                    f"  For {mode} input: '{output}', expected: {expected}, got: {result}"
                )
        else:
            print("All tests passed!")

    run_tests()
