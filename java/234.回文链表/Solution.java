class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;
        int n = 0;
        ListNode p = head;
        while(p != null){
            p = p.next;
            n++;
        }
        p = head;
        for (int i = 1; i < n/2; i++) {
            p = p.next;
        }
        ListNode p2 = p.next;
        if (n%2 != 0) p2 = p2.next;
        ListNode next = p2.next;
        while (next!=null) {
            ListNode t = next.next;
            next.next = p2;
            p2 = next;
            next = t;
        }
        p = head;
        for (int i = 0; i < n/2; i++) {
            if (p.val != p2.val) return false;
            p = p.next;
            p2 = p2.next;
        }
        return true;
    }
}