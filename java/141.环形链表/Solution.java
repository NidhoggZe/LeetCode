class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode quick = head;
        ListNode slow = head;
        boolean meet = false;
        while (quick != null && quick.next != null) {
            quick = quick.next.next;
            slow = slow.next;
            if (quick == slow) {
                meet = true;
                break;
            }
        }

        return meet;
    }


}

