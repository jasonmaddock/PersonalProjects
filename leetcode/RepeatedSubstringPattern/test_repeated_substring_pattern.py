import pytest
from repeated_substring_pattern import Solution

@pytest.mark.parametrize(
    "s,expected_result",
    [
        (
            "abab",
            True,
        ),
        (
            "aba",
            False,
        ),
        (
            "abcabcabcabc",
            True,
        ),
        (
            "abaababaab",
            True,
        ),
    ]
)
def test(s, expected_result):
    result = Solution.repeatedSubstringPattern(Solution, s)
    assert result is expected_result