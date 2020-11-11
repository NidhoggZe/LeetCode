import java.util.LinkedList;
import java.util.Queue;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Codec {
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        String res = "";
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            if (node == null) {
                res += "n,";
                continue;
            }
            res += Integer.toString(node.val);
            res += ",";
            q.offer(node.left);
            q.offer(node.right);
        }
        return res;
    }

    // Decodes your encoded data to tree.
    TreeNode newNode(String s) {
        if (s.equals("n")) return null;
        else return new TreeNode(Integer.parseInt(s));
    }

    public TreeNode deserialize(String data) {
        String[] vals = data.split(",");
        Queue<TreeNode> q = new LinkedList<>();
        TreeNode root = newNode((vals[0]));
        q.offer(root);
        int i = 1;
        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            if (node == null) continue;
            node.left = newNode(vals[i++]);
            node.right = newNode(vals[i++]);
            q.offer(node.left);
            q.offer(node.right);
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));