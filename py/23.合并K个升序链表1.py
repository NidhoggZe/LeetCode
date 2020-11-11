#二分法多路归并
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(A: ListNode, B: ListNode):
            head = ListNode()
            tail = head
            while A is not None and B is not None:
                if A.val < B.val:
                    tail.next = A
                    A = A.next
                    tail = tail.next
                else:
                    tail.next = B
                    B = B.next
                    tail = tail.next
            while A is not None:
                tail.next = A
                A = A.next
                tail = tail.next
            while B is not None:
                tail.next = B
                B = B.next
                tail = tail.next
            
            return head.next

        def mergek(l, r):
            if l == r - 1:
                return lists[l]
            else:
                return merge(mergek(l, (l + r)//2), mergek((l + r)//2, r))
        
        if lists.__len__() == 0:
            return None
        return mergek(0, lists.__len__())
                