import pytest

from search_insert_position import Solution

@pytest.mark.parametrize(
    "nums,target,expected_result",
    [
        (
            [1,3,5,6],
            5,
            2,
        ),
        (
            [1,3,5,6],
            2,
            1,
        ),
        (
            [1,3,5,6],
            7,
            4,
        ),
        (
            [1,3,5,6],
            0,
            0,
        ),
        (
            [1,3,5,6,9],
            9,
            4,
        ),
    ]
)
def test(nums, target, expected_result):
    result = Solution.searchInsert(Solution, nums, target)
    assert result == expected_result