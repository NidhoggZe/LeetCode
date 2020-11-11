#每次构造前序的第一位的节点，用hashmap记录节点在中序的位置，通过先序首位在中序的位置得出左右子树节点个数

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
#    ans =[]
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inmap = {}
        for i in range(0, preorder.__len__()):
            inmap[inorder[i]] = i

        def buildNode(prel, prer, inl, inr):
            if prel >= preorder.__len__() or inl >= inorder.__len__() or prel == prer:
                return None
            curNode = TreeNode(preorder[prel])
#            self.ans.append(preorder[prel])
            curNodeInPos = inmap[preorder[prel]]
            rightnum = curNodeInPos - inl

            curNode.left = buildNode(
                prel+1, prel+rightnum+1, inl, curNodeInPos)
            curNode.right = buildNode(
                prel+rightnum+1, prer, curNodeInPos+1, inr)
            return curNode

        return buildNode(0, preorder.__len__(), 0, inorder.__len__())


Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
