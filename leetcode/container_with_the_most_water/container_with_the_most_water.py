from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        i, j = 0, len(height) -1
        while i != j:
            h1 = height[i]
            h2 = height[j]
            vol = min(h1, h2) * (j - i)
            max_vol = vol if vol > max_vol else max_vol
            if h1 > h2:
                j -= 1
            else:
                i += 1
        return max_vol
