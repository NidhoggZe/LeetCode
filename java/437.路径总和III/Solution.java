
import java.util.HashMap;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    int res;

    void dfs(TreeNode root, HashMap<Integer, Integer> map, int target, int tillnow){
        if (root == null) return;
        tillnow += root.val;
        res += map.getOrDefault(tillnow - target, 0);
        
        map.put(tillnow, map.getOrDefault(tillnow, 0) + 1);

        dfs(root.left, map, target, tillnow);
        dfs(root.right, map, target, tillnow);

        map.put(tillnow, map.get(tillnow) - 1);

        return;
    }

    public int pathSum(TreeNode root, int sum) {
        if (root == null) return 0;
        res = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        dfs(root, map, sum, 0);
        return res;
    }
}