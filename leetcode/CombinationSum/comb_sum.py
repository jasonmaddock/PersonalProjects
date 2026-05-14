from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def recurse(idx, n_sum, candidates):
            pot_n_sum = n_sum + [candidates[idx]]
            if sum(pot_n_sum) == target:
                return [pot_n_sum,]
            elif sum(pot_n_sum) > target and idx > 0:
                return recurse(idx-1, n_sum, candidates)
            elif sum(pot_n_sum) < target:
                outs = []
                for i in range(0, idx+1)[::-1]:
                    res = recurse(i, pot_n_sum, candidates)
                    if res:
                        outs += res
                return outs
            return


        out = []
        candidates = sorted(candidates)
        for count, n in enumerate(candidates, 1):
            n_sum = recurse(len(candidates) - count, [], candidates)
            if n_sum:
                for i in n_sum:
                    if sorted(i) not in out:
                        out.append(sorted(i))

        return out
