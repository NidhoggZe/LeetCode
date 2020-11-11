
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null)
            return null;
        Node p = head;
        while (p != null) {
            Node oldNext = p.next;
            p.next = new Node(p.val);
            p.next.next = oldNext;
            p = p.next.next;
        }

        p = head;
        while (p != null) {
            Node curNode = p.next;
            if (p.random != null)
                curNode.random = p.random.next;
            p = p.next.next;
        }

        p = head;
        Node res = head.next;
        while (p != null) {
            Node curNode = p.next;
            p.next = p.next.next;
            p = p.next;
            curNode.next = p == null ? null : p.next;
        }

        return res;
    }
}
