//98. 验证二叉搜索树
#include <cmath>
#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
   public:
    bool isValidBST(TreeNode *root) {
        long long last = (long long)INT_MIN * 2;
        stack<TreeNode *> s;
        TreeNode *p = root;
        if (root == nullptr) return true;
        s.push(root);
        while (!s.empty()) {
            p = s.top();
            if (p->left) {
                s.push(p->left);
                p = p->left;
            } else {
                while (!p->right) {
                    if (s.top()->val <= last) return false;
                    last = s.top()->val;
                    s.pop();
                    if (s.empty()) return true;
                    p = s.top();
                }
                if (s.top()->val <= last) return false;
                last = s.top()->val;
                s.pop();
                p = p->right;
                s.push(p);
            }
        }
        return true;
    }
};