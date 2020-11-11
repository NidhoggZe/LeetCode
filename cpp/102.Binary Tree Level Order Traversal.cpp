// 102. 二叉树的层序遍历
//特点是每层各自放一个vector，采用每次while循环里处理一层的方法

#include <queue>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
   public:
    vector<vector<int>> levelOrder(TreeNode *root) {
        vector<vector<int>> res;
        if (!root) return {};
        int dept = 0;
        queue<TreeNode *> q;
        q.push(root);
        while (!q.empty()) {
            vector<int> curres;
            int curlen = q.size();
            for (int i = 0; i < curlen; i++) {
                curres.push_back(q.front()->val);
                if (q.front()->left) q.push(q.front()->left);
                if (q.front()->right) q.push(q.front()->right);
                q.pop();
            }
            res.push_back(curres);
        }
        return res;
    }
};