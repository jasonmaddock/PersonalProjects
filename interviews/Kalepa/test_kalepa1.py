from kalepa1 import maximumProfit

import pytest

@pytest.mark.parametrize(
    "nums, er",
    [
        ([3,4,5,3,5,2],
         True),
    ]
)
def test(nums, er):
    r = maximumProfit(nums)
    assert r == er