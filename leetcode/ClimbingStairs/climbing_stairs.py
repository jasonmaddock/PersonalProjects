class Solution:
    def climbStairs(self, n: int) -> int:
        ######## Recursion is too slow 
        # def recurse(n):
        #     if n < 3:
        #         return n 
        #     return recurse(n-1) + recurse(n-2)
        
        # return recurse(n)
        ################################
        prev2 = 0
        prev1 = 1
        count = 0
        while count != n:
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
            count += 1
        return curr
