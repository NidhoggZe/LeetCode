#小顶堆
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    heap = []

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [None]

        def push(node: ListNode):
            heap.append(node)
            i = heap.__len__() - 1
            while i != 1:
                if heap[i].val < heap[i//2].val:
                    heap[i], heap[i//2] = heap[i//2], heap[i]
                    i //= 2
                else:
                    break
            return
        
        def pop():
            heap[1], heap[-1] = heap[-1], heap[1]
            ans = heap.pop()
            i = 1
            while(i*2 < heap.__len__()):
                if i*2+1 >= heap.__len__():
                    if heap[i*2].val < heap[i].val:
                        heap[i], heap[i*2] = heap[i*2], heap[i]
                    break
                if heap[i*2].val < heap[i].val and heap[i*2].val <= heap[i*2+1].val:
                    heap[i], heap[i*2] = heap[i*2], heap[i]
                    i *= 2
                elif heap[i*2+1].val < heap[i].val and heap[i*2+1].val <= heap[i*2].val:
                    heap[i], heap[i*2+1] = heap[i*2+1], heap[i]
                    i = i*2+1
                else:
                    break
            
            return ans

        head = ListNode()
        tail = head

        for L in lists:
            if L is not None:
                push(L)
        while heap.__len__() > 1:
            tail.next = pop()
            tail = tail.next
            if tail.next is not None:
                push(tail.next)


        return head.next


def createNodes(nums:List[List]):
    heads = []
    for lst in nums:
        Last = None
        for i in range (lst.__len__()-1, -1, -1):
            head = ListNode(lst[i],Last)
            Last = head
            heads.append(head)

    return heads

heads = createNodes([[-6,-3,-1,1,2,2,2],[-10,-8,-6,-2,4],[-2],[-8,-4,-3,-3,-2,-1,1,2,3],[-8,-6,-5,-4,-2,-2,2,4]])

print(Solution().mergeKLists(heads))