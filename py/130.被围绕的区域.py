from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        def dfs(i:int, j:int):
            nonlocal m, n
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if board[i][j] == 'X' or board[i][j] == 'o':
                return
            board[i][j] = 'o'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            return


        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
            

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'o':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'


        return
