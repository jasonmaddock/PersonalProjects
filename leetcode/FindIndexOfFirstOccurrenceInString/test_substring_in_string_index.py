import pytest

from substring_in_string_index import Solution

@pytest.mark.parametrize(
    "haystack,needle,expected_result",
    [
        (
            "sadbutsad",
            "sad",
            0,
        ),
        (
            "hello",
            "ll",
            2,
        ),
        (
            "a",
            "a",
            0,
        ),
        (
            "leetcode",
            "leeto",
            -1,
        ),
    ]
)
def test(haystack, needle, expected_result):
    result = Solution.strStr(Solution, haystack, needle)
    assert result == expected_result