import pytest

from zigzag_conversion import Solution

@pytest.mark.parametrize(
    "s,rows,expected_result",
    [
        (
            "PAYPALISHIRING",
            3,
            "PAHNAPLSIIGYIR",
        ),
        (
            "PAYPALISHIRING",
            4,
            "PINALSIGYAHRPI",
        ),
        (
            "A",
            1,
            "A",
        ),
    ]
)
def test(s, rows, expected_result):
    result = Solution.convert(Solution, s, rows)
    assert result == expected_result
    