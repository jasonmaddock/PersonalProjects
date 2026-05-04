import pytest

from interview import solution

@pytest.mark.parametrize(
    "s,expected_result",
    [
        (
            "ACCBBaCcDb",
            6,
        ),
        (
            "AcDbCCBBaC",
            6,
        ),
        (
            "a",
            1,
        ),
        (
            "aaaaaaaaaaaaaaaaaa",
            18,
        ),
        (
            "AaAaAaAaAaAaAaAaAaAa",
            1
        )
    ]
)
def test(s, expected_result):
    result = solution(s)
    assert result == expected_result
