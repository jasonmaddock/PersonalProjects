import pytest

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        combos = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
            }
        
        return_list = []
        for digit in digits:
            if not return_list:
                [return_list.append(letter) for letter in combos[digit]] 
            else:
                added_letters = []
                added_count = 0
                count = 0
                for result_letters in return_list:
                    for i in combos[digit]:
                        added_letters.append(return_list[count])
                        added_letters[added_count] = added_letters[added_count] + i
                        added_count += 1
                    count += 1
                return_list = added_letters
        return return_list
    
    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        combos = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
            }
        
        if not digits:
            return []
        return_list = combos[digits[0]]
        for i in digits[1:]:
            return_list = self.multiply_list(return_list, combos[i])
        return sorted(return_list)
    
    def multiply_list(return_list, char_list):
        to_add = []
        for i in char_list:
            for j in return_list:
                to_add.append(j+i)
        return to_add
        

@pytest.mark.parametrize(
        "digits,expected_result",
        [
            (
                "23",
                ["ad","ae","af","bd","be","bf","cd","ce","cf"],
            ),
            (
                "",
                [],
            ),
            (
                "2",
                ["a","b","c"]
            ),
            (
                "234",
                ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"],
            )
        ]
)        
def test(digits, expected_result):
    obj = Solution.letterCombinations2(Solution, digits)
    assert obj == expected_result
    
if __name__ == "__main__":
    test()