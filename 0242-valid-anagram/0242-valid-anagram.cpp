class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> freq;

        for(auto c : s) {
            freq[c]++;
        }
        for(auto c : t) {
            freq[c]--;
        }
        for(auto f : freq) {
            if(f.second != 0) {
                return false;
            }
        }
        return true;

    }
};

/*

map string s

if all count is zero in s map, return true

*/
