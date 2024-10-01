import pytest

from climbing_stairs import Solution

@pytest.mark.parametrize(
    "n,expected_result",
    [
        (
            2,
            2,
        ),
        (
            3,
            3,
        ),
        (
            4,
            5,
        ),
        (
            5,
            8,
        ),
                (
            6,
            13,
        )
    ]
)
def test(n, expected_result):
    result = Solution.climbStairs(Solution, n)
    assert result == expected_result