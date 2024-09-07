class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            x = x * -1
            neg = True
        rev_n = int(str(x)[::-1])
        if rev_n > 2**31 -1:
            return 0
        if neg:
            rev_n = rev_n * -1
        return rev_n