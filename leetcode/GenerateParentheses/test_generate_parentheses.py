import pytest

from generate_parentheses import Solution

@pytest.mark.parametrize(
    "n,expected_result",
    [
        (
            1,
            ["()"]
        ),
        (
            3,
            ["((()))","(()())","(())()","()(())","()()()"]
        )
    ]
)
def test(n, expected_result):
    result = Solution.generateParenthesis(Solution, n)
    for i in result:
        assert i in expected_result
        expected_result.pop(expected_result.index(i))
    assert not expected_result
