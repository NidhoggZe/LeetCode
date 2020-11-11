// 121. 买卖股票的最佳时机
#include <vector>

using namespace std;

class Solution {
   public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 0) return 0;
        int maxp = 0;
        int lowest = prices[0];
        for (int i = 1; i < prices.size(); i++) {
            lowest = lowest < prices[i - 1] ? lowest : prices[i - 1];
            maxp = maxp > prices[i] - lowest ? maxp : prices[i] - lowest;
        }
        return maxp;
    }
};