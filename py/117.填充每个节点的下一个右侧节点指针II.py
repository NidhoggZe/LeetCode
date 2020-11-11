
class Node:
    def __init__(self, val: int = 0, left: Node=None, right: Node=None, next: Node=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        while cur:
            dummy = Node()
            pre = dummy
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = cur.left
                if cur.right:
                    pre.next = cur.right
                    pre = cur.right
                cur = cur.next
            cur = dummy.next

        return root
