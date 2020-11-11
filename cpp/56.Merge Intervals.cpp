//56. 合并区间
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
   public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.size() == 0) {
            return intervals;
        }
        sort(intervals.begin(), intervals.end());
        vector<int> curInterval = intervals[0];
        vector<vector<int>> res = {};
        for (auto itv : intervals) {
            if (itv[0] <= curInterval[1]) {
                curInterval[1] = max(curInterval[1], itv[1]);
            } else {
                res.push_back(curInterval);
                curInterval = itv;
            }
        }
        res.push_back(curInterval);
        return res;
    }
};