
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    int[] maxrob(TreeNode root) {
        int[] res = {0, 0};
        if (root == null) return res;
        var l = maxrob(root.left);
        var r = maxrob(root.right);
        res[0] = root.val + l[1] + r[1];
        res[1] = Math.max(l[0], l[1]) + Math.max(r[0], r[1]);
        return res;
    }

    public int rob(TreeNode root) {
        var res = maxrob(root);
        return Math.max(res[0], res[1]);
    }
}