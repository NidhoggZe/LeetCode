
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curNode = head
        p = -1
        lastnNode = head
        while (curNode is not None):
            if p != n:
                p += 1
            else:
                lastnNode = lastnNode.next
            curNode = curNode.next
        if p == n:
            lastnNode.next = lastnNode.next.next
            return head
        else:
            return head.next