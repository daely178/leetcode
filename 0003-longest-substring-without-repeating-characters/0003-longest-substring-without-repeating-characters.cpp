class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.empty()) {
            return 0;
        }
        int l=0;
        int res = 0;
        int n = s.size();
        std::unordered_map<char, int> mp;

        for(int r=0; r<n; r++) {
            if(mp.find(s[r]) != mp.end()){
                l = max(l, mp[s[r]]+1);
            }
            mp[s[r]] = r;
            res = max(res, r-l+1);
        }
        return res;
    }
};


/*

   a b c a b c b b
 l 1 2 3 4 5 6 7 8
 r             7
 m.1 2 3 3 3 3 3 3    
*/