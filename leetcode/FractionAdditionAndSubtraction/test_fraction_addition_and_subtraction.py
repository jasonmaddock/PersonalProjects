import pytest
from fraction_addition_and_subtraction import Solution

@pytest.mark.parametrize(
    "input,expected_result",
    [
        (
            "-1/2+1/2",
            "0/1",
        ),
        (
            "-1/2+1/2+1/3",
            "1/3",
        ),
        (
            "1/3-1/2",
            "-1/6",
        ),
    ]
)
def test(input, expected_result):
    result = Solution.fractionAddition(Solution, input)
    assert result == expected_result