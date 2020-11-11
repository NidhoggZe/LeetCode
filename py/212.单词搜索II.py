class Solution:

    class TreeNode:
        def __init__(self):
            self.sonNum = 0
            self.isEnd = False
            self.next = [None]*26

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
        root = self.TreeNode()
        for word in words:
            p = root
            for i in range(0, len(word)):
                if p.next[ord(word[i]) - ord('a')] == None:
                    p.next[ord(word[i]) - ord('a')] = self.TreeNode()
                    p.sonNum += 1
                p = p.next[ord(word[i]) - ord('a')]
            p.isEnd = True

        m = len(board)
        n = len(board[0])
        res = []

        def dfs(i:int, j:int, lastans:str, lastNode:self.TreeNode):
            if (i < 0 or i >= m or j < 0 or j >= n):
                return
            if board[i][j] == '#':
                return
            curNode = lastNode.next[ord(board[i][j]) - ord('a')]
            curans = lastans + board[i][j]
            if curNode is None:
                return

            if curNode.isEnd == True:
                res.append(curans)
                curNode.isEnd = False
                if curNode.sonNum == 0:
                    lastNode.next[ord(board[i][j]) - ord('a')] = None
                    lastNode.sonNum -= 1
                    return
                

            t = board[i][j]
            board[i][j] = '#'
            dfs(i+1, j, curans, curNode)
            dfs(i-1, j, curans, curNode)
            dfs(i, j+1, curans, curNode)
            dfs(i, j-1, curans, curNode)
            board[i][j] = t

            if curNode.sonNum == 0:
                lastNode.next[ord(board[i][j]) - ord('a')] = None
                lastNode.sonNum -= 1
            return

        for i in range(0, m):
            for j in range(0, n):
                dfs(i, j, '', root)

        return res