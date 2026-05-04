from typing import List

# [1,3,1,1,2]
# [5,0,3,4,0]

class Solution:
    def distance1(self, nums: List[int]) -> List[int]:
        distances = []
        for count, i in enumerate(nums):
            dists = [abs(count-j) for j, x in enumerate(nums) if x == i]
            distances.append(sum(dists))
        return distances

    def distance(self, nums):
        groups = {}

        for i, x in enumerate(nums):
            if x not in groups:
                groups[x] = []
            groups[x].append(i)

        ans = [0] * len(nums)

        for indices in groups.values():
            prefix = 0
            total = sum(indices)
            n = len(indices)

            for k, idx in enumerate(indices):
                left = idx * k - prefix
                right = (total - prefix - idx) - idx * (n - k - 1)
                ans[idx] = left + right
                prefix += idx

        return ans


            

        