class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = s.__len__()
        for i in range(0, n):
            j = 0
            while (i - j >= 0 and i + j < n):
                if s[i-j] == s[i+j]:
                    count += 1
                else:
                    break
                j += 1
            j = 0
            while (i - j >= 0 and i + 1 + j < n):
                if s[i-j] == s[i+1+j]:
                    count += 1
                else:
                    break
                j += 1

        return count
