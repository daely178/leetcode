class Solution {
public:
    bool isAnagram(string s, string t) {
        std::map<char, int> frequency;
        for(auto c : s){
            frequency[c]++;
        }
        for(auto c:t){
            frequency[c]--;
        }
        for(auto f : frequency) {
            if(f.second !=0){
                return false;
            }
        }
        return true;
    }
};