import pytest

from divide_two_integers import Solution

@pytest.mark.parametrize(
    "dividend,divisor,expected_result",
    [
        (
            10,
            3,
            3,
        ),
        (
            7,
            -3,
            -2,
        ),
        (
            -2147483648,
            -1,
            2147483647,
        )
    ]
)
def test(dividend, divisor, expected_result):
    result = Solution.divide(Solution, dividend, divisor)
    assert result == expected_result