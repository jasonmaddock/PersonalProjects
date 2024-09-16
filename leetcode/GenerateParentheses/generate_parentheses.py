from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        base_str = "(" * n + ")" * n
        output.append(base_str)
        for i in range(n, (n*2)):
            for j in output:
                base_str = j
                valid_limit = 1 + ((i-n)*2)
                count = i
                while count > valid_limit:
                    base_str = base_str[:count - 1] + base_str[count-1:count+1][::-1] + base_str[count+1:]
                    count -= 1
                    if base_str not in output:
                        output.append(base_str)
        return output
