import pytest
from remove_letter_to_equalize_frequency import Solution

@pytest.mark.parametrize(
    "letters,expected_result",
    [
        (
            "abcc",
            True,
        ),
        (
            "aazz",
            False,
        ),
        (
            "abbcc",
            True,
        ),
    ]
)
def test(letters, expected_result):
    result = Solution.equalFrequency(Solution, letters)
    assert result is expected_result