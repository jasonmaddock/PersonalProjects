import pytest

from plus_one import Solution

@pytest.mark.parametrize(
    "digits,expected_result",
    [
        (
            [1,2,3],
            [1,2,4],
        ),
        (
            [4,3,2,1],
            [4,3,2,2]
        ),
        (
            [9],
            [1,0],
        ),
        (
            [8,9,9,9],
            [9,0,0,0],
        ),
    ]
)
def test(digits, expected_result):
    result = Solution.plusOne(Solution, digits)
    assert result == expected_result
    