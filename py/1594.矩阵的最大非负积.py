#在从网格地图左上角开始到右下角结束的所有路径中，找出具有最大非负积的路径。路径的积是沿路径访问的单元格中所有整数的乘积。
#动态规划同时保留到该格的绝对值最大的正数和负数
from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = grid.__len__()
        n = grid[0].__len__()
        dist = [[(0, 0)]*n for _ in range(m)]
        dist[0][0] = (grid[0][0], grid[0][0])
        for i in range(1, m):
            dist[i][0] = (max(grid[i][0]*dist[i-1][0][0], grid[i][0]*dist[i-1]
                              [0][1]), min(grid[i][0]*dist[i-1][0][0], grid[i][0]*dist[i-1]
                                           [0][1]))
        for i in range(1, n):
            dist[0][i] = (max(grid[0][i]*dist[0][i-1][0], grid[0][i]*dist[0]
                              [i-1][1]), min(grid[0][i]*dist[0][i-1][0], grid[0][i]*dist[0]
                                           [i-1][1]))

        for i in range(1, m):
            for j in range(1, n):
                maxpos = max(grid[i][j]*dist[i-1][j][0], grid[i][j]*dist[i-1]
                               [j][1], grid[i][j]*dist[i][j-1][0], grid[i][j]*dist[i][j-1][1])
                maxneg = min(grid[i][j]*dist[i-1][j][0], grid[i][j]*dist[i-1][j]
                            [1], grid[i][j]*dist[i][j-1][0], grid[i][j]*dist[i][j-1][1])
                dist[i][j] = (maxpos, maxneg)

        if dist[m-1][n-1][0] < 0:
            return -1
        else:
            return dist[m-1][n-1][0] % (pow(10,9) + 7)

