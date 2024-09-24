import pytest

from integer_to_roman import Solution

@pytest.mark.parametrize(
    "num,expected_result",
    [
        (
            3749,
            "MMMDCCXLIX",
        ),
        (
            58,
            "LVIII",
        ),
        (
            1994,
            "MCMXCIV",
        )
    ]
)
def test(num, expected_result):
    result = Solution.intToRoman(Solution, num)
    assert result == expected_result