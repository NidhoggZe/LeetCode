from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])

        def inbound(i: int, j: int):
            nonlocal m, n
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            else:
                return True

        def countCell(i: int, j: int):
            nonlocal board
            if board[i][j] == 1 or board[i][j] == 2:
                return 1
            else:
                return 0

        for i in range(m):
            for j in range(n):
                count = 0
                if inbound(i-1, j-1):
                    count += countCell(i-1, j-1)
                if inbound(i-1, j):
                    count += countCell(i-1, j)
                if inbound(i, j-1):
                    count += countCell(i, j-1)
                if inbound(i+1, j+1):
                    count += countCell(i+1, j+1)
                if inbound(i+1, j):
                    count += countCell(i+1, j)
                if inbound(i, j+1):
                    count += countCell(i, j+1)
                if inbound(i-1, j+1):
                    count += countCell(i-1, j+1)
                if inbound(i+1, j-1):
                    count += countCell(i+1, j-1)
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 2
                else:
                    if count == 3:
                        board[i][j] = 3

        for i in range(m):
            for j in range(n):
                if board[i][j] == 3:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0
        
        return
