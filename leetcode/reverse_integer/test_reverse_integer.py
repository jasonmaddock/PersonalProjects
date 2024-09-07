import pytest

from reverse_integer import Solution

@pytest.mark.parametrize(
    "integer,expected_result",
    [
        (
            123,
            321,
        ),
        (
            -123,
            -321
        ),
        (
            120,
            21,
        ),
    ]
)
def test(integer, expected_result):
    result = Solution.reverse(Solution, integer)
    assert result == expected_result
    