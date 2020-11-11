//49. 字母异位词分组
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, unsigned int> mymap;
        vector<vector<string>> res;
        for(auto str : strs) {
            auto temp = str;
            sort(temp.begin(), temp.end());
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