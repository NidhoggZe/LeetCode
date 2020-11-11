//114. 二叉树展开为链表
//从根节点开始往右儿子遍历，如果有左子树就把左子树置为右子树，原右子树接在原左子树的最右侧
#include <stack>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};

class Solution {
   public:
    void flatten(TreeNode* root) {
        TreeNode* p = root;
        while (p != nullptr) {
            if (p->left) {
                TreeNode* r = p->right;
                p->right = p->left;
                p->left = nullptr;
                TreeNode* t = p;
                while (t->right) {
                    t = t->right;
                }
                t->right = r;
            }
            p = p->right;
        }
        return;
    }
};