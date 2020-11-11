//136.只出现一次的数字
#include <vector>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int sum = 0;
        for(auto i : nums) {
            sum ^= i;
        }
        return sum;
    }
};