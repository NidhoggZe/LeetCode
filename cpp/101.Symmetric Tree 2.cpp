//101. 对称二叉树
//队列

using namespace std;
#include <queue>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
   public:
    bool isSymmetric(TreeNode *root) {
        queue<TreeNode *> myp, myq;
        myp.push(root);
        myq.push(root);
        while (!myp.empty() && !myq.empty()) {
            if ((!myp.front() && myq.front()) || (myp.front() && !myq.front()))
                return false;
            if (!myp.front() && !myq.front()) {
                myp.pop();
                myq.pop();
                continue;
            }
            if (myp.front()->val != myq.front()->val) return false;
            myp.push(myp.front()->left);
            myp.push(myp.front()->right);
            myq.push(myq.front()->right);
            myq.push(myq.front()->left);
            myp.pop();
            myq.pop();
        }
        if (myp.empty() && myq.empty()) return true;
        return false;
    }
};