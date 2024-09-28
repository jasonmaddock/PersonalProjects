class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def speedy_divider(dividend, divisor):
            count = 0
            modified_divisor = divisor
            if dividend >= divisor:
                count += 1
            while len(str(dividend)) - 1 > len(str(modified_divisor)):
                modified_divisor = int(str(modified_divisor) + "0")
                count = int(str(count) + "0")
            if dividend >= divisor:
                count += speedy_divider(dividend - modified_divisor, divisor)
            return count

        matching_signs = bool(dividend < 0) == bool(divisor < 0)
        dividend = dividend * -1 if dividend < 0 else dividend
        divisor = divisor * -1 if divisor < 0 else divisor
        count = speedy_divider(dividend, divisor)
        if not matching_signs:
            count = count * -1
        if count > (2 ** 31) -1:
            return (2 ** 31) -1
        elif count < -2 ** 31:
            return -2 ** 31
        return count