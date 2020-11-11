class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    int max;
    int dfs(TreeNode root) {
        if (root == null) return 0;
        int l = dfs(root.left);
        int r = dfs(root.right);
        
        max = Math.max(max, l + r + 1);

        return Math.max(l, r) + 1;
    }

    public int diameterOfBinaryTree(TreeNode root) {
        max = -1;
        dfs(root);
        return max;
    }
}