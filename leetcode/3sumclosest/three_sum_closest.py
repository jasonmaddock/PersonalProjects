from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest =  nums[0] + nums[1] + nums[2]
        for count, num in enumerate(nums[:-2], 1):
            l_idx = count
            r_idx = len(nums)-1
            while l_idx < r_idx:
                total = num + nums[l_idx] + nums[r_idx]
                if abs(target - closest) > abs(target - total):
                    closest = total
                if total > target:
                    r_idx -= 1
                elif total < target:
                    l_idx += 1
                else:
                    return total

        return closest
