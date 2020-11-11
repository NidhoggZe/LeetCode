class Trie {
    class Node {
        boolean isEnd;
        Node[] next;

        Node() {
            this.isEnd = false;
            this.next = new Node[26];
        }
    }

    /** Initialize your data structure here. */

    Node root;

    public Trie() {
        root = new Node();
    }

    /** Inserts a word into the trie. */
    public void insert(String word) {
        Node p = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (p.next[c - 'a'] == null)
                p.next[c - 'a'] = new Node();
            p = p.next[c - 'a'];
        }
        p.isEnd = true;
    }

    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        Node p = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            Node next = p.next[c - 'a'];
            if (next == null)
                return false;
            p = next;
        }
        return p.isEnd;
    }

    /**
     * Returns if there is any word in the trie that starts with the given prefix.
     */
    public boolean startsWith(String prefix) {
        Node p = root;
        for (int i = 0; i < prefix.length(); i++) {
            char c = prefix.charAt(i);
            Node next = p.next[c - 'a'];
            if (next == null)
                return false;
            p = next;
        }
        return true;
    }
}
