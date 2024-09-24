class Solution:
    def intToRoman(self, num: int) -> str:
        def romanticise(digit):
            if digit > 8:
                return "/,"
            elif digit > 4:
                return f".{'/'*(digit-5)}"
            elif digit == 4:
                return "/."
            else:
                return f"{'/'*digit}"
        trans_map = {
            3: ["M", "D", "C"],
            2: ["C", "L", "X"],
            1: ["X", "V", "I"],
        }
        romans = []
        for count, i in enumerate(str(num)[::-1], start=1):
            if count > 3:
                romans.append(f"M"*int(i))
                continue
            chars = romanticise(int(i))
            key = trans_map[count]
            map = [",", ".", "/"]
            for k, m in zip(key, map):
                chars = chars.replace(m, k)
            romans.append(chars)
        return "".join(romans[::-1])

