//49. 字母异位词分组
#include <vector>
#include <string>
#include <algorithm>
#include <map>
//#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, unsigned int> mymap;
        vector<vector<string>> res;
        for(auto str : strs) {
            int list[26];
            for (int i = 0; i < 26; i++) {
                list[i] = 0;
            }
            for(auto c : str) {
                list[int(c) - 97]++;
            }
            string temp = "";
            for (int i = 0; i < 26; i++) {
                temp += char(list[i]+97);
            }
            auto exist = mymap.find(temp);
            if (exist == mymap.end()) {
                vector<string> newres = {str};
                res.push_back(newres);
                mymap[temp] = res.size()-1;
            }
            else{
                res[exist->second].push_back(str);
            }
        }
        return res;
    }
};

// int main(int argc, const char** argv) {
//     vector<string> a = {"eat","tea","tan","ate","nat","bat"};
//     Solution().groupAnagrams(a);
//     return 0;
// }