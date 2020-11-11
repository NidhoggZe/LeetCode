//78. 子集
//深搜输出各种子集情况（每个元素分别出现/不出现）
#include <vector>

using namespace std;

class Solution {
    vector<vector<int>> ans;
    vector<int> curans;
    int n;

   public:
    void dfs(int pos, vector<int>& nums) {
        if (pos == n - 1) {
            curans.push_back(nums[pos]);
            ans.push_back(curans);
            curans.pop_back();
            ans.push_back(curans);
        } else {
            curans.push_back(nums[pos]);
            dfs(pos + 1, nums);
            curans.pop_back();
            dfs(pos + 1, nums);
        }
        return;
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        n = nums.size();
        dfs(0, nums);
        return ans;
    }
};