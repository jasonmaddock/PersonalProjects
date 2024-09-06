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
            




        #     if count == len(s) - 1 or (not count and s[count] != s[count+1]):
        #         continue
        #     if count:
        #         if (s[count-1] != s[count+1] and s[count] != s[count+1]):
        #             continue
        #     pair = False
        #     if count:
        #         if s[count-1] == s[count+1]:
        #             prev = s[count-1]
        #         else:
        #             pair = True
        #             prev = s[count]
        #     else:
        #         pair = True
        #         prev = s[count]
        #     next = s[count+1]
        #     candidate = ""
        #     search_count = 1
        #     while search_count <= count and search_count <= len(s) - count - 1:
        #         if pair:
        #             prev = s[count+((search_count-1)*-1)]
        #         else:
        #             prev = s[count+(search_count*-1)]
        #         next = s[count+search_count]
        #         if prev != next:
        #             break
        #         search_count += 1
        #     if count:
        #         search_count -= 1
        #     if pair:
        #         candidate = s[count+((search_count-1)*-1): count + search_count + 1]
        #     else:
        #         candidate = s[count+(search_count*-1): count + search_count + 1]
        #     if len(candidate) > len(longest_palindrome):
        #         longest_palindrome = candidate
        # return longest_palindrome

