//114. 二叉树先序展开为链表
//用栈的话基本就是先序遍历，跟94一起看
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
        if (!root) return;
        TreeNode* last = root;
        stack<TreeNode*> s;
        while (last->left || last->right || !s.empty()) {
            if (last->right) s.push(last->right);
            if (last->left) {
                last->right = last->left;
                last->left = nullptr;
                last = last->right;
            } else {
                last->right = s.top();
                s.pop();
                last = last->right;
            }
        }
        return;
    }
};