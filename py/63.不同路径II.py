from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0]*n for _ in range(m)]

        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
        else:
            dp[m - 1][n - 1] = 1

        for i in range(m - 2, -1, -1):
            if obstacleGrid[i][n - 1] == 0:
                dp[i][n - 1] = 1
            else:
                break

        for j in range(n - 2, -1, -1):
            if obstacleGrid[m - 1][j] == 0:
                dp[m - 1][j] = 1
            else:
                break

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]


Solution().uniquePathsWithObstacles([[0,0],[1,1],[0,0]])
