class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        int l = 0;
        unordered_map<char, int> seen;
        
        for(int i=0; i<s.size(); i++) {
            if(seen.find(s[i]) != seen.end())
                l = max(l, seen[s[i]]+1);
            res = max(res, i-l+1);
            seen[s[i]] = i;
        }
        return res;
    }
};

/* 
    0 1 2 3 4 5 6 7
    a b c a b c b b
                p 
  s 3 4 5 6
  m 1 - 2 - 3

*/