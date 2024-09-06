class Solution:
    def convert(self, s: str, numRows: int) -> str:
        bar_offset = (numRows * 2) - 2 or 1
        r_s = ""
        for n in range(numRows):
            diag = 0
            pos = n
            if n != 0 and n != numRows:
                diag = (numRows - (n + 1)) * 2
            while pos < len(s):
                r_s = r_s + s[pos]
                if diag and pos + diag < len(s):
                    r_s = r_s + s[pos + diag]  
                pos += bar_offset
        return r_s