class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode quick = head;
        ListNode slow = head;
        ListNode meet = null;
        while (quick!=null && quick.next != null){
            quick = quick.next.next;
            slow = slow.next;
            if (quick == slow){
                meet = quick;
                break;
            }
        }
        if (meet == null) return null;
        ListNode p1 = head;
        ListNode p2 = meet;
        while (p1 != p2){
            p1 = p1.next;
            p2 = p2.next;
        }
        return p1;
    }
}

