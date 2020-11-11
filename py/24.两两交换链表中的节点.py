class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyhead = ListNode(0, head)
        def swap2(dummyhead: ListNode):
            if (not dummyhead.next) or (not dummyhead.next.next):
                return None
            rest = dummyhead.next.next.next
            dummyhead.next.next.next = dummyhead.next
            dummyhead.next = dummyhead.next.next
            dummyhead.next.next.next = rest
            return dummyhead.next.next

        head = dummyhead
        while head:
            head = swap2(head)
    
        return dummyhead.next