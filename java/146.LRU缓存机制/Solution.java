import java.util.HashMap;
import java.util.Map;

class LRUCache {
    class Node {
        int key;
        int val;
        Node next;
        Node last;

        Node() {
        }

        Node(int key, int val, Node last, Node next) {
            this.key = key;
            this.val = val;
            this.next = next;
            this.last = last;
        }
    }

    int capacity;
    int size;
    Node head, tail;
    Map<Integer, Node> cache;

    void moveToHead(Node curNode) {
        curNode.last.next = curNode.next;
        curNode.next.last = curNode.last;
        curNode.next = head.next;
        curNode.last = head;
        head.next = curNode;
        curNode.next.last = curNode;
    }

    public LRUCache(int capacity) {
        this.capacity = capacity;
        size = 0;
        head = new Node();
        tail = new Node();
        head.next = tail;
        tail.last = head;
        cache = new HashMap<Integer, Node>();
    }

    public int get(int key) {
        if (cache.containsKey(key)) {
            moveToHead(cache.get(key));
            return cache.get(key).val;
        } else
            return -1;
    }

    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            Node curNode = cache.get(key);
            curNode.val = value;
            moveToHead(curNode);
        } else {
            if (size == capacity) {
                cache.remove(tail.last.key);
                tail.last.last.next = tail;
                tail.last = tail.last.last;
                size--;
            }
            Node curNode = new Node(key, value, head, head.next);
            head.next = curNode;
            curNode.next.last = curNode;
            cache.put(key, curNode);
            size++;
        }
        return;
    }

}

class test {
    public static void main(String[] args) {
        LRUCache cache = new LRUCache(2);
        cache.put(1, 1);
        cache.put(2, 2);
        cache.get(1); // 返回 1
        cache.put(3, 3); // 该操作会使得关键字 2 作废
        cache.get(2); // 返回 -1 (未找到)
        cache.put(4, 4); // 该操作会使得关键字 1 作废
        cache.get(1); // 返回 -1 (未找到)
        cache.get(3); // 返回 3
        cache.get(4); // 返回 4
    }
}

/**
 * Your LRUCache object will be instantiated and called as such: LRUCache obj =
 * new LRUCache(capacity); int param_1 = obj.get(key); obj.put(key,value);
 */