class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> mp;
        for(char c : ransomNote)
            mp[c]++;
        for(char c : magazine){
            if(mp[c])
                mp[c]--;
        }

        for(auto f : mp){
            if(f.second != 0)
                return false;
        }
        return true;
    }
};