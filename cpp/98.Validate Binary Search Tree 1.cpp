//98. 验证二叉搜索树
#include <cmath>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
   public:
    bool isValidNode(TreeNode *p, long long minn, long long maxn) {
        if (p == nullptr) return true;
        if ((long long)(p->val) <= minn || (long long)(p->val >= maxn)) return false;
        if (isValidNode(p->left, minn, p->val) &&
            isValidNode(p->right, p->val, maxn))
            return true;
        else
            return false;
    }

    bool isValidBST(TreeNode *root) {
        return isValidNode(root, (long long)INT_MIN * 2,
                           (long long)INT_MAX * 2);
    }
};