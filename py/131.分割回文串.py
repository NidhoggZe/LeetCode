from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s == None or s.__len__() == 0:
            return []

        length = s.__len__()

        dp = [[False] * length for _ in range(length)]
        for i in range(0, length):
            dp[i][i] = True
        for i in range(0, length - 1):
            dp[i][i+1] = (s[i] == s[i+1])

        for j in range(1, length):
            for i in range(0, j):
                if s[i] == s[j] and (i + 1 >= j - 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
            
        res = []
        curans = []
        def dfs(l:int):
            if l == length:
                res.append(curans.copy())
                return
            for r in range(l, length):
                if dp[l][r]:
                    curans.append(s[l:r+1])
                    dfs(r+1)
                    curans.pop()
            return

        dfs(0)

        return res

Solution().partition("cbbbcc")