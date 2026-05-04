class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        for count, i in enumerate(sorted_nums):
            if i == k or i > k:
                return count