from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        row = False
        col = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        row = True
                    if j == 0:
                        col = True
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        if row:
            for j in range(n):
                matrix[0][j] = 0

        if col:
            for i in range(m):
                matrix[i][0] = 0

        return
                    