class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    TreeNode res;
    int post(TreeNode curNode, TreeNode p, TreeNode q){
        if (curNode == null) return 0;
        boolean fp = false, fq = false;
        int l = post(curNode.left, p, q);
        if (l == 3) return 3;
        int r = post(curNode.right, p, q);
        if (r == 3) return 3;
        if (l == 1 || r == 1 || curNode == p) fp = true;
        if (l == 2 || r == 2 || curNode == q) fq = true;
        if (fp && fq) {
            res = curNode;
            return 3;
        }
        if (fp) return 1;
        if (fq) return 2;
        return 0;
    }


    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        res = null;
        post(root, p, q);
        return res;
    }
}