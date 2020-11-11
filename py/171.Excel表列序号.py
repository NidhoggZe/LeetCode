class Solution:
    def titleToNumber(self, s: str) -> int:
        summ = 0
        for c in s:
            summ *= 26
            summ += ord(c) - ord('A') + 1

        return summ