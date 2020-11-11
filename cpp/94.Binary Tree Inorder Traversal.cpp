//94. 二叉树的中序遍历
//当前节点为栈top，如果有左儿子，左儿子一直进栈，如果没有，pop直到top有右儿子，然后pop自己push右儿子，栈空的时候停止
#include <stack>
#include <vector>


 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right)
         : val(x), left(left), right(right) {}
 };

 using namespace std;
 class Solution {
    public:
     vector<int> inorderTraversal(TreeNode *root) {
         vector<int> ans = {};
         stack<TreeNode *> s;
         TreeNode *p = root;
         if (root == nullptr) return ans;
         s.push(root);
         while (!s.empty()) {
             p = s.top();
             if (p->left) {
                 s.push(p->left);
                 p = p->left;
             } else {
                 while (!p->right) {
                     ans.push_back(s.top()->val);
                     s.pop();
                     if (s.empty()) return ans;
                     p = s.top();
                 }
                 ans.push_back(p->val);
                 s.pop();
                 p = p->right;
                 s.push(p);
             }
         }
         return ans;
     }
 };