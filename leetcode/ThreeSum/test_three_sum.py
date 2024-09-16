import pytest

from three_sum import Solution

@pytest.mark.parametrize(
    "nums,expected_result",
    [
        (
            [-1,0,1,2,-1,-4],
            [[-1,-1,2],[-1,0,1]],
        ),
        (
            [0,1,1],
            [],
        ),
        (
            [0,0,0],
            [[0,0,0]],
        ),
        (
            [3,0,-2,-1,1,2],
            [[-2,-1,3],[-2,0,2],[-1,0,1]],
        )
    ]
)
def test(nums, expected_result):
    result = Solution.threeSum(Solution, nums)
    for i in result:
        assert i in expected_result
        expected_result.pop(expected_result.index(i))
    assert not expected_result