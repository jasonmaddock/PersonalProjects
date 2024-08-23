from functools import reduce

class Solution:
    def fractionAddition(self, expression: str) -> str:
        def parse_string(s: str) -> list:
            fractions = []
            last_end = 0
            for count, i in enumerate(s[1:]):
                if not i.isdigit() and i != "/":
                    fractions.append(s[last_end:count+1])
                    last_end = count + 1
            fractions.append(s[last_end:])

            formated_fractions = []
            for i in fractions:
                formated_fractions.append(i.split("/"))
            return formated_fractions
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        def lcmm(*args):
            return reduce(lcm, args)

        def common_denominator(fractions):
            denominators = [int(i[1]) for i in fractions]
            lowest_common_denominator = lcmm(*denominators)
            numerator = 0 
            for i in fractions:
                numerator += (int(i[0])*(lowest_common_denominator/int(i[1])))
            if numerator == 0:
                return "0/1"
            simplify = gcd(numerator, lowest_common_denominator)
            return f"{int(numerator/simplify)}/{int(lowest_common_denominator/simplify)}"

        fractions = parse_string(expression)
        return common_denominator(fractions)