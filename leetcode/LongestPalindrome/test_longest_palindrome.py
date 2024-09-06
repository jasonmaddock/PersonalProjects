import pytest

from longest_palindrome import Solution

@pytest.mark.parametrize(
    "string,expected_result",
    [
        (
            "babad",
            "bab",
        ),
        (
            "cbbd",
            "bb",
        ),
        (
            "abc",
            "a",
        ),
        (
            "bb",
            "bb",
        ),
        (
            "ccd",
            "cc",
        ),
        (
            "ccc",
            "ccc",
        ),
        (
            "aaaa",
            "aaaa",
        ),
    ]
)
def test(string, expected_result):
    result = Solution.longestPalindrome(Solution, string)
    assert result == expected_result
