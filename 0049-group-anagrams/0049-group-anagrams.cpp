class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string, vector<string>> groups;

        for(const string &str : strs) {
            string key = str;
            sort(key.begin(), key.end());
            groups[key].push_back(str);
        }

        vector<vector<string>> ans;

        for(auto &[key, group] : groups) {
            ans.push_back(move(group));
        }

        return ans;
    }
};


/*
strs = ["eat","tea","tan","ate","nat","bat"]


key = sort string
map[key] push back string

loop key,string : groups

*/