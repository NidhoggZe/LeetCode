# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0
        num = 0
        def inOrder(root: TreeNode):
            nonlocal count, num
            if not root or count >= k:
                return

            inOrder(root.left)

            count += 1
            if count == k:
                num = root.val
                return

            inOrder(root.right)
        
        inOrder(root)

        return num

            