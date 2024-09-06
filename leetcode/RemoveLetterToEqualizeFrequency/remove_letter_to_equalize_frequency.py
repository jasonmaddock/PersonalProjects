class Solution:
    def equalFrequency(self, word: str) -> bool:
        distinct_letters = set(word)
        frequencies = [word.count(i) for i in distinct_letters]
        if (frequencies.count(1) == len(frequencies)) or (
            frequencies.count(1) == 1
            and frequencies.count(max(frequencies)) == len(frequencies) - 1
        ):
            return True
        if (
            frequencies.count(max(frequencies)) > 1
            or max(frequencies) - min(frequencies) > 1
        ):
            return False
        return True