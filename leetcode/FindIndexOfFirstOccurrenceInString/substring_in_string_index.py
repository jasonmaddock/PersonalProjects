class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        for count, i in enumerate(haystack):
            if haystack[count:count+len(needle)] == needle:
                return count
            