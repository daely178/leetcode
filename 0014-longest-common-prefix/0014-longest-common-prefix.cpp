class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() == 0){
            return "";
        }
        for(auto s : strs){
            if(s.size() == 0){
                return "";
            }
        }
        string first = strs[0];
        for(size_t i=0; i<first.size(); i++) {
            for(size_t j=1; j<strs.size(); j++) {
                if (i == strs[j].size() || first[i] != strs[j][i]) {
                    return first.substr(0, i);                    
                }
            }
        }
        return first;
    }
};