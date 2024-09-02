import re


def _parse_output_absolute(output):
    pattern = r"""
        (?:                        # Start of non-capturing group
            \[RESULT\]|\[SCORE\]|   # Match [RESULT] or [SCORE]
            Score:?|score:?|        # Match Score: or score:
            Result:?|\[Result\]:?|  # Match Result: or [Result]:
            score\s+of              # Match "score of"
        )                           # End of non-capturing group
        \s*                         # Allow any whitespace
        (?:\(|\[|\s)*               # Allow opening brackets or whitespace
        (\d+)                       # Capture the digit(s)
        (?:                         # Start of non-capturing group
            (?:\)|\]|\s|$)|         # Allow closing brackets, whitespace, or end of string
            (?:/\s*5|               # Allow /5 with optional whitespace
               \s*out\s*of\s*5)     # or "out of 5" with flexible whitespace
        )?                          # End of non-capturing group
        (?:\s*$)                    # Match from the end of string 
    """
    match = re.search(pattern, output, re.IGNORECASE | re.VERBOSE)

    if match:
        result = int(match.group(1))
        if 1 <= result <= 5:  # Ensure the result is within the valid range
            feedback = output[: match.start()].strip()
            return output, result

    return None, None


def _parse_output_relative(output):
    explicit_pattern = r"""
        (?:                                # Start of non-capturing group
            \[RESULT\]|\[RESULT:\s*|        # Match [RESULT] or [RESULT:
            \[Response\s+|                  # Match [Response
            \[Result\](?:\s+Response)?|     # Match [Result] or [Result] Response
            \[Result:\s*|                   # Match [Result:
            (?:^|\n)Result:?\s*             # Match Result: at the start of a line
        )                                   # End of non-capturing group
        \s*                                 # Allow any whitespace
        (A|B)                               # Capture A or B
        (?:\])?                             # Allow closing bracket, whitespace, or end of string
        (?:\s*$)                            # Match from the end of string 
    """
    match = re.search(
        explicit_pattern, output, re.IGNORECASE | re.VERBOSE | re.MULTILINE
    )

    if match:
        result = match.group(1).upper()
        feedback = output[: match.start()].strip()
        return output, result

    return None, None


def parse_output(output, mode: str):
    assert mode in [
        "absolute",
        "relative",
    ], "Invalid mode. Supported modes are: 'absolute', 'relative'"

    if output is None:
        return None, None

    if mode == "absolute":
        return _parse_output_absolute(output)
    elif mode == "relative":
        return _parse_output_relative(output)
