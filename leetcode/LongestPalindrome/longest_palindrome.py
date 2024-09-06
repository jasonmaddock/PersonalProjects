class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome_finder(first, last, s):
            if s[first] == s[last]:
                if first != 0 and last != len(s) -1:
                    return palindrome_finder(first-1, last+1, s)
                else:
                    return s[first:last+1]
            else:
                return s[first+1:last]
            
        longest_palindrome = s[0]
        for count, i in enumerate(s[:-1]):
            pal = False
            candidate = ""
            if i == s[count+1]:
                candidate = palindrome_finder(count, count+1, s)
            if count:
                if s[count-1] == s[count+1]:
                    new_candidate = palindrome_finder(count-1, count+1, s)
                    candidate = new_candidate if len(new_candidate) > len(candidate) else candidate
            if candidate:
                if len(candidate) > len(longest_palindrome):
                    longest_palindrome = candidate
        return longest_palindrome
            
