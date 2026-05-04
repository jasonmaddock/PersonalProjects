import pytest

from sum_of_distances import Solution

@pytest.mark.parametrize(
    "nums,expected_result",
    [
        (
            [1,3,1,1,2],
            [5,0,3,4,0],
        ),
        (
            [0,5,3],
            [0,0,0],
        ),
    ]
)
def test(nums, expected_result):
    result = Solution.distance(Solution, nums)
    for i in result:
        assert i in expected_result
        expected_result.pop(expected_result.index(i))
    assert not expected_result