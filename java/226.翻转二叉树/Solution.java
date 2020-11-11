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

class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            TreeNode p = queue.poll();
            TreeNode t = p.left;
            p.left = p.right;
            p.right = t;
            if (p.left != null)
                queue.offer(p.left);
            if (p.right != null)
                queue.offer(p.right);
        }
        return root;
    }
}