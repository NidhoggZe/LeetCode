//55. 跳跃游戏
#include <vector>

using namespace std;

class Solution {
   public:
    bool canJump(vector<int>& nums) {
        int furthest = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (i > furthest) return false;
            furthest = furthest > i + nums[i] ? furthest : i + nums[i];
        }
        return true;
    }
};