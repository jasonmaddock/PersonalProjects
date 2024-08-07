
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    def recurse(s, analysis_string):
        if not s:
            return True

        if s[0] not in analysis_dict:
            return False
        if analysis_dict[s[0]] not in s:
            return False
        if s[1] != analysis_dict[s[0]]:
            recurse(s[1:], analysis_string)
        else:
            analysis_string = analysis_string.replace(s[0], "", 1) 
            analysis_string = analysis_string.replace(s[1], "", 1)
            if not analysis_string:
                return True
            recurse(analysis_string, analysis_string)

    analysis_dict = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    analysis_string = s
    return recurse(s, analysis_string)

isValid("()[]{}")


        # for i in analysis_s:
        #     if i in analysis_dict:
        #         match = False
        #         for j in analysis_string[analysis_string.index(i)+1:]:
        #             if j in analysis_dict:
        #                 return False
        #             if j == analysis_dict[i]:
        #                 match = True
        #                 analysis_string = analysis_string.replace(i, "", 1)
        #                 analysis_string = analysis_string.replace(j, "", 1)
        #                 break
        #         if match == False:
        #             return False
        # for i in analysis_dict:
        #     if analysis_dict[i] in analysis_string:
        #         return False
        # return True
        # for i in s:
        #     if i in analysis_dict:
        #         for j in s[s.index(i)+1:]:
        #             if j == analysis_dict[i]:
        #                 print(s.index(i) - s.index(j))
        #                 if s.index(i) - s.index(j) > 1:
        #                     print(s[s.index(i+1)], s[s.index(j-1)])
        #                     if s.index(i) - s.index(j) % 2 == 0:
        #                         return False
        #                     elif analysis_dict[s[s.index(i+1)]] != s[s.index(j-1)]:
        #                             return False
        #                 break
        #             return False
        # return True



