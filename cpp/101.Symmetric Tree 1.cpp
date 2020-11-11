//101. 对称二叉树

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
   public:
    bool dfs(TreeNode *p, TreeNode *q) {
        if ((!p && q) || (p && !q)) return false;
        if (!p && !q) return true;
        if (p->val != q->val) return false;
        if (dfs(p->left, q->right) && dfs(p->right, q->left)) return true;
        return false;
    }

    bool isSymmetric(TreeNode *root) { return dfs(root, root); }
};