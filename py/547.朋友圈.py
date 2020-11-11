from typing import List
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        n = len(M)
        visited = [False] * n
        count = 0
        
        def dfs(i):
            nonlocal visited, n
            if visited[i]:
                return
            visited[i] = True
            for j in range(n):
                if M[i][j] == 1:
                    dfs(j)
            return

        for i in range(n):
            if visited[i] == False:
                count += 1
                dfs(i)
        
        return count