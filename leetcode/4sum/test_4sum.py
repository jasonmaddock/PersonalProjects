import pytest

from foursum import Solution

@pytest.mark.parametrize(
    "target,nums,expected_result",
    [
        (
            0,
            [1, 0, -1, 0, -2, 2],
            [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
        ),
        (
            8,
            [2, 2, 2, 2, 2],
            [[2, 2, 2, 2]]
        ),
        (
            4,
            [-5, 5, 4, -3, 0, 0, 4, -2],
            [[-3, -2, 4, 5], [-5, 0, 4, 5]]
        ),
    ]
)
def test(target, nums, expected_result):
    result = Solution.fourSum(Solution, nums, target)
    assert result == expected_result