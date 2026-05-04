from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def b_search(nums, target, start_idx):
            length = len(nums)
            if length == 1:
                if nums[0] < target:
                    return start_idx + 1
                else:
                    return start_idx
            n_left = int(length/2)
            n_right = int(length/2)
            left = nums[n_left-1]
            right = nums[n_right]
            if target == left:
                return start_idx + n_left - 1
            elif target == right or target > left and target < right:
                return start_idx + n_right
            elif target > left and target > right:
                return b_search(nums[n_left:], target, start_idx + n_left)
            elif target < left and target < right:
                return b_search(nums[:n_left], target, start_idx)

        return b_search(nums, target, 0)

