import pytest
from matched_parenthesis import Solution

@pytest.mark.parametrize(
    "string,expected_result",
    [
        (
            "()",
            True,
        ),
        (
            "[()]",
            True,
        ),
        (
            "()[]{}",
            True,
        ),
        (
            "(]",
            False,
        ),
        (
            "([)]",
            False,
        ),
        (
            "[([]])",
            False
        ),
        (
            "({{{{}}}))",
            False
        ),
        (
            "[[[]",
            False
        )
    ]
)
def test(string, expected_result):
    result = Solution.isValid(Solution, string)
    assert result == expected_result