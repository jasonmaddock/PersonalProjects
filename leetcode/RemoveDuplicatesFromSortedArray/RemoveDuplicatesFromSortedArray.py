class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = set(nums)
        for count, i in enumerate(arr):
            nums[count] = i
        return len(arr)
        