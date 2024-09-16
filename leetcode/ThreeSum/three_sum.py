from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []   
        n = len(nums)
        for a in range(len(nums)-2):
            if nums[a] > 0:
                break
            if a > 0 and nums[a] == nums[a-1]:
                continue
            start = a + 1
            end = n - 1
            while start < end:
                total = nums[a] + nums[start] + nums[end]
                if total == 0:
                    trip = [nums[a] , nums[start], nums[end]]
                    if trip not in triplets:
                        triplets.append(trip)
                    while start < end and nums[start] == trip[1]:
                        start += 1
                    while start < end and nums[end] == trip[2]:
                        end -= 1
                elif total > 0:
                    end -= 1
                else:
                    start += 1
        return triplets
