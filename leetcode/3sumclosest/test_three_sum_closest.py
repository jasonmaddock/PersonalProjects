import pytest

from three_sum_closest import Solution

@pytest.mark.parametrize(
    "nums,target,expected_result",
    [
        (
            [-1,2,1,-4],
            1,
            2,
        ),
        (
            [0,0,0],
            1,
            0,
        ),
        (
            [0,1,2],
            0,
            3,
        ),
        (
            [2,3,8,9,10],
            16,
            15,
        ),
    ]
)
def test(nums, target, expected_result):
    result = Solution.threeSumClosest(Solution, nums, target)
    assert result == expected_result
    