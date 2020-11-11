//96. 不同的二叉搜索树
//1...n 为节点组成的二叉搜索树的种类数为卡塔兰数h(n)=h(n-1) * (4*n-2) / (n+1)，h(0)=1,  h(1)=1
#include <vector>

using namespace std;

class Solution {
public:
    int numTrees(int n) {
        vector<int> G(n + 1, 0);
        G[0] = 1;
        G[1] = 1;

        for (int i = 2; i <= n; ++i) {
            for (int j = 1; j <= i; ++j) {
                G[i] += G[j - 1] * G[i - j];
            }
        }
        return G[n];
    }
};