class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    int max = (int)-1e9;

    int maxContri(TreeNode p){
        if (p == null) return 0;
        int l = Math.max(0, maxContri(p.left)), r = Math.max(0, maxContri(p.right));

        max = Math.max(max, p.val + l + r);


        return p.val + Math.max(l, r);
    }

    public int maxPathSum(TreeNode root) {
        maxContri(root);
        return max;
    }
}