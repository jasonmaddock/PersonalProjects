import pytest

from remove_element import Solution

@pytest.mark.parametrize(
    "nums,val,expected_result",
    [
        (
            [3,2,2,3],
            3,
            2,
        ),
        (
            [0,1,2,2,3,0,4,2],
            2,
            5,
        ),
    ]
)
def test(nums, val, expected_result):
    result = Solution.removeElement(Solution, nums, val)
    assert result == expected_result
    