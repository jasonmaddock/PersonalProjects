import pytest

from container_with_the_most_water import Solution

@pytest.mark.parametrize(
    "height,expected_result",
    [
        (
            [1,8,6,2,5,4,8,3,7],
            49,
        ),
        (
            [1,1],
            1,
        ),
        (
            [0,2],
            0,
        ),
        (
            [2,3,10,5,7,8,9],
            36,
        )
    ]
)
def test(height, expected_result):
    result = Solution.maxArea(Solution, height)
    assert result == expected_result