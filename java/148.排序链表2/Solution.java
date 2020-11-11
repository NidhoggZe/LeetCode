class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {

    ListNode cut(ListNode head, int len) {
        while (head != null && len != 1) {
            head = head.next;
            len--;
        }
        if (head == null)
            return null;
        ListNode next = head.next;
        head.next = null;
        return next;
    }

    ListNode merge(ListNode p1, ListNode p2) {
        ListNode dummyHead = new ListNode(), p = dummyHead;
        while (p1 != null && p2 != null) {
            if (p1.val < p2.val) {
                p.next = p1;
                p1 = p1.next;
            } else {
                p.next = p2;
                p2 = p2.next;
            }
            p = p.next;
        }
        while (p1 != null) {
            p.next = p1;
            p1 = p1.next;
            p = p.next;
        }
        while (p2 != null) {
            p.next = p2;
            p2 = p2.next;
            p = p.next;
        }
        return dummyHead.next;
    }

    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null)
            return head;
        ListNode p = head;
        int n = 0;
        while (p != null) {
            p = p.next;
            n++;
        }
        ListNode dummyHead = new ListNode(0, head);

        for (int len = 1; len < n; len *= 2) {
            ListNode sortedTail = dummyHead;
            p = dummyHead.next;
            while (p != null) {
                ListNode p1 = p, p2 = cut(p1, len);
                p = cut(p2, len);
                sortedTail.next = merge(p1, p2);
                while (sortedTail.next != null)
                    sortedTail = sortedTail.next;
            }
        }
        return dummyHead.next;
    }
}