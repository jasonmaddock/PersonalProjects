import pytest

from kalepa1 import maximumProfit

@pytest.mark.parametrize(
    "nums, er",
    [
        ([6,5,4,5,3],
         1),

    ]
)
def test(nums, er):
    r = maximumProfit(nums)
    assert r == er