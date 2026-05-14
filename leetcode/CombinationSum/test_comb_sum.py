import pytest

from comb_sum import Solution

@pytest.mark.parametrize(
    "combination,target,expected_result",
    [
        (
            [2,3,6,7],
            7,
            [[2,2,3],[7]],
        ),
        (
            [7,3,2],
            18,
            [[7,7,2,2],[7,3,3,3,2],[7,3,2,2,2,2],[3,3,3,3,3,3],[3,3,3,3,2,2,2],[3,3,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2]],
        ),
        (
            [2,3,5],
            8,
            [[2,2,2,2],[2,3,3],[3,5]],
        ),
        (
            [2,],
            1,
            [],
        ),
    ]
)
def test(combination, target, expected_result):
    result = Solution.combinationSum(Solution, combination, target)
    assert len(result) == len(expected_result)
    for i in result:
        assert i[::-1] in expected_result or i in expected_result