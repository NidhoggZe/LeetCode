# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """ 
        head = ListNode(0)
        last_l3 = head
        addone = 0
        while (l1 != None) | (l2 != None) | (addone == 1):
            if l1 is None:
                n1 = 0
            else: 
                n1 = l1.val
                l1 = l1.next
            if l2 is None:
                n2 = 0
            else: 
                n2 = l2.val
                l2 = l2.next
            num = n1 + n2 + addone
            if num >= 10:
                addone = 1
            else:
                addone = 0
            num %= 10
            last_l3.next = ListNode(num)
            last_l3 = last_l3.next
        return head.next
            

