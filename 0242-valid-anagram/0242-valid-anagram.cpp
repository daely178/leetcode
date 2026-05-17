class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> freq;
        for(int i=0; i<s.size(); i++) {
            freq[s[i]]++;
        }
        for(int i=0; i<t.size(); i++) {
            if(freq.find(t[i]) == freq.end()) {
                return false;
            }
            freq[t[i]]--;
            if(freq[t[i]] < 0 ){
                return false;
            }
        }
        for(const auto & pair : freq) {
            if(pair.second != 0) {
                return false;
            }
        }
        return true;
    }
};

/*

map string s

brute force
unordered_map<char, int> freq

f

*/
