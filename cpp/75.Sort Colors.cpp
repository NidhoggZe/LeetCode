//75. 颜色分类
//荷兰国旗问题,扫描一遍数组，按要求往头&尾扔扫（也就是换）描到的符合要求的数
#include <vector>

using namespace std;

class Solution {
   public:
    void sortColors(vector<int>& nums) {
        int i = 0, l = -1, r = nums.size();
        while (i < r) { //边界条件，因为从左侧扫描跟右侧碰头
            int t;
            if (nums[i] == 0) {
                t = nums[l + 1];
                nums[l + 1] = nums[i];
                nums[i] = t;
                l++;
                if (l >= i) { //这里注意，因为是从左侧开始扫描的
                    i++;
                }
            } else if (nums[i] == 1)
                i++;
            else {
                t = nums[r - 1];
                nums[r - 1] = nums[i];
                nums[i] = t;
                r--;
            }
        }
        return;
    }
};