from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l = matrix[0][0]
        r = matrix[n-1][n-1] + 1
        count = 0
        mid = 0
        while (l < r):
            count = 0
            mid = (l + r) // 2
            x = 0
            y = n - 1
            while (x < n and y >= 0):
                if matrix[y][x] <= mid:
                    x += 1
                    count += y + 1
                else:
                    y -= 1

            if count < k:
                l = mid + 1
            else:
                r = mid

        return l


matrix = [[1,  2], [1, 3]]
k = 3

Solution().kthSmallest(matrix, k)
