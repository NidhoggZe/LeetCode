from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dic = {}
        for i in range(m):
            for j in range(n):
                if matrix[i][j] not in dic:
                    dic[matrix[i][j]] = []
                dic[matrix[i][j]].append([i, j])

        res = [[0]*n for _ in range(m)]
        maxn = 0

        keys = list(dic)
        keys.sort(reverse=True) 
        for num in keys:
            for pos in dic[num]:
                x = pos[0]
                y = pos[1]
                maxp = 0
                if x-1 >= 0 and matrix[x-1][y] > matrix[x][y]:
                    maxp = max(maxp, res[x-1][y])
                if y-1 >= 0 and matrix[x][y-1] > matrix[x][y]:
                    maxp = max(maxp, res[x][y-1])
                if x+1 < m and matrix[x+1][y] > matrix[x][y]:
                    maxp = max(maxp, res[x+1][y])
                if y+1 < n and matrix[x][y+1] > matrix[x][y]:
                    maxp = max(maxp, res[x][y+1])
                
                res[x][y] = maxp + 1
                maxn = max(maxn, maxp + 1)

        return maxn


a = [[9,9,4],[6,6,8],[2,1,1]]
Solution().longestIncreasingPath(a)
