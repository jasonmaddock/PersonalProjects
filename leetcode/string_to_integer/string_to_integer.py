class Solution:
    def myAtoi(self, s: str) -> int:
        read_str = ""
        for char in s:
            if not char.isdigit() and (char not in ("-", "+", " ") or read_str):
                break
            elif char == " ":
                continue
            else:
                read_str += char
        try:
            n = int(read_str)
        except ValueError:
            n = 0
        if n > 2**31 -1:
            n = 2**31 -1
        elif n < -2**31:
            n = -2**31
        return n

