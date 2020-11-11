// 139.单词拆分
#include <set>
#include <string>
#include <vector>

using namespace std;

class Solution {
   public:
    bool wordBreak(string s, vector<string>& wordDict) {
        set<string> myset;
        for (auto word : wordDict) {
            myset.insert(word);
        }
        vector<bool> dp = vector<bool>(s.length() + 1);
        dp[0] = true;
        for (int i = 1; i < s.length() + 1; i++) {
            for (int j = 0; j <= i; j++) {
                if (dp[j] == true &&
                    myset.find(s.substr(j, i - j)) != myset.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
    }
};

// int main(int argc, const char** argv) {
//     vector<string> v;
//     v.push_back("apple");
//     v.push_back("pen");
//     cout << Solution().wordBreak("applepenapple", v);
//     return 0;
// }