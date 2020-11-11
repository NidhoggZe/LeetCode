class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) return null;
        ListNode curNode = head;
        ListNode curNext = curNode.next;
        while (curNext != null) {
            ListNode t = curNext.next;
            curNext.next = curNode;
            curNode = curNext;
            curNext = t;
        }
        head.next = null;
        return curNode;
    }
}