from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        level = 0
        while len(q) != 0:
            n = len(q)
            curLevel = []
            for i in range(n):
                if level % 2:
                    curNode = q.popleft()
                    curLevel.append(curNode.val)
                    q.append(curNode)
                else:
                    curNode = q.pop()
                    curLevel.append(curNode.val)
                    q.appendleft(curNode)
            res.append(curLevel)

            for i in range(n):
                curNode = q.pop()
                if curNode.right:
                    q.appendleft(curNode.left)
                if curNode.left:
                    q.appendleft(curNode.right)
            
            level += 1

        return res

