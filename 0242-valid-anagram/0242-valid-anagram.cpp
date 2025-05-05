class Solution {
public:
    bool isAnagram(string s, string t) {
        std::map<char, int> smap;
        map<char, int> freq;
        for(char c : s)
            freq[c] += 1;
        for(char c: t)
            freq[c] -= 1;

        for(auto f : freq){
            if(f.second)
                return false;
        }

        return true;
    }
};