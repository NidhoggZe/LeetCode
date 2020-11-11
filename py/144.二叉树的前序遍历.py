from typing import List
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            while node is not None:
                res.append(node.val)
                if node.right:
                    stack.append(node.right)
                node = node.left

        return res