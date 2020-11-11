# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 =  ListNode()
        head = l3
        while (l1 is not None) and (l2 is not None):
            if l1.val < l2.val:
                l3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            l3 = l3.next
        
        if (l1 is None):
            while (l2 is not None):
                l3.next = ListNode(l2.val)
                l2 = l2.next
                l3 = l3.next
        if (l2 is None):
            while (l1 is not None):
                l3.next = ListNode(l1.val)
                l1 = l1.next
                l3 = l3.next

        return head.next