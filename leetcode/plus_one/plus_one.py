from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def recurse_add(digit_pos):
            digits[digit_pos] = 0
            if digit_pos != 0 and digits[digit_pos-1] != 9:
                digits[digit_pos-1] += 1
            else:
                if digit_pos != 0:
                    recurse_add(digit_pos-1)
                else:
                    digits.insert(0, 1) 

        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        recurse_add(len(digits)-1)
        return digits