from typing_extensions import List
from itertools import combinations, chain

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # def powerset(iterable):
        #     "powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        #     s = list(iterable)
        #     return chain.from_iterable(combinations(s, r) for r in range())
        
        # solutions = set(tuple(sorted(i)) for i in powerset(nums) if sum(i) == target)
        # solutions = [list(i) for i in solutions]
        # return solutions
        combos = []
        for a, i in enumerate(nums[:-3]):
            for b, j in enumerate(nums[1:-2]):
                if b == a - 1:
                    continue
                for c, k in enumerate(nums[2:-1]):
                    if c == b + 1 or c == a - 2:
                        continue
                    for d, l in enumerate(nums[3:]):
                        if d == c - 1 or d == b - 2 or d == a - 3:
                            continue
                        candidate = [i, j, k, l]
                        if 0 in candidate:
                            pass
                        total = sum(candidate)
                        if (total == target) and (sorted(candidate) not in combos):
                            combos.append(sorted(candidate))
        return combos
 
