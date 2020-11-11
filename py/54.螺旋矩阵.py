from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        res = []
        left = 0
        right = n - 1
        up = 0
        down = m - 1

        while (up < down and left < right):
            for j in range(left, right):
                res.append(matrix[up][j])
            for i in range(up, down):
                res.append(matrix[i][right])
            for j in range(right, left, -1):
                res.append(matrix[down][j])
            for i in range(down, up, -1):
                res.append(matrix[i][left])
            up += 1
            down -= 1
            left += 1
            right -= 1

        if up == down:
            for j in range(left, right + 1):
                res.append(matrix[up][j])
        elif left == right:
            for i in range(up, down + 1):
                res.append(matrix[i][left])

        return res