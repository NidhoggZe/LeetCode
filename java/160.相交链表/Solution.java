class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int alen = 0, blen = 0;
        ListNode p = headA;
        while (p != null) {
            alen++;
            p = p.next;
        }
        p = headB;
        while (p != null) {
            blen++;
            p = p.next;
        }
        if (alen < blen) {
            p = headA;
            headA = headB;
            headB = p;
            int t = alen;
            alen = blen;
            blen = t;
        }
        int diff = alen - blen;
        for (int i = 0; i < diff; i++) {
            headA = headA.next;
        }
        ListNode res = null;
        while (headA != null) {
            if (headA == headB) {
                res = headA;
                break;
            }
            headA = headA.next;
            headB = headB.next;
        }
        return res;
    }
}