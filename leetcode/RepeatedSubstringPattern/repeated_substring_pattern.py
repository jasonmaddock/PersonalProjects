class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def candidate_test(candidate, s):
            c_len = len(candidate)
            if len(s) % c_len:
                return False
            multi = len(s) / c_len
            for i in range(int(multi)):
                if s[i*c_len:(i+1)*c_len] != candidate:
                    return False
            return True


        candidates = []
        substring = s[0]
        for count, letter in enumerate(s[1:]):
            if substring == s[len(substring):(len(substring)*2)]:
                if candidate_test(s[len(substring):(len(substring)*2)], s):
                    return True
            substring += letter
        return False



