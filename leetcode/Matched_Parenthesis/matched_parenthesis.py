class Solution:
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        def recurse(analysis_string, count):
            if not analysis_string:
                return True

            if analysis_string[count] not in analysis_dict:
                return False
            if analysis_dict[analysis_string[count]] not in analysis_string:
                return False
            if analysis_string[count+1] != analysis_dict[analysis_string[count]]:
                return recurse(analysis_string, count + 1)
            else:
                analysis_string = analysis_string[:count] + analysis_string[count+2:]
                if not analysis_string:
                    return True
                else:
                    if count != 0:
                        count = count - 1
                    
                    return recurse(analysis_string, count)

        analysis_dict = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        return recurse(s, 0)