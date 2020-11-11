# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode, val:int) -> int:
            if root is None:
                return val
            else:
                val = dfs(root.right, val)
                val += root.val
                root.val = val
                val = dfs(root.left, val)

            return val

        dfs(root, 0)
        return root
                