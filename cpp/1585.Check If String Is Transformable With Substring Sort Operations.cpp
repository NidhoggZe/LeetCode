//1585. 检查字符串是否可以通过排序子字符串得到另一个字符串
#include <string>
#include <queue>
using namespace std;

class Solution {
   public:
    bool isTransformable(string s, string t) {
        queue<int> q[10];

        for (int i = 0; i < s.length(); i++) {
            q[char(s[i]) - 48].push(i);
        }
        for (int i = 0; i < t.length(); i++) {
            int n = char(t[i]) - 48;
            if (q[n].empty()) return false;
            auto pos = q[n].front();
            for (int j = 0; j < n; j++) {
                if (!(q[j].empty() || q[j].front() > pos)) return false;
            }
            q[n].pop();
        }
        for (int i = 0; i < 10; i++) {
            if (!q[i].empty()) return false;
        }
        return true;
    }
};