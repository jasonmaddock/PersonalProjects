import pytest

from string_to_integer import Solution

@pytest.mark.parametrize(
    "s,expected_result",
    [
        (
            "42",
            42,
        ),
        (
            "-042",
            -42,
        ),
        (
            "1337c0d3",
            1337,
        ),
        (
            "0-1",
            0,
        ),
        (
            "words and 987",
            0,
        ),
        (
            "-91283472332",
            -2147483648,
        ),
        (
            "+1",
            1
        )
    ]
)
def test(s, expected_result):
    result = Solution.myAtoi(Solution, s)
    assert result == expected_result