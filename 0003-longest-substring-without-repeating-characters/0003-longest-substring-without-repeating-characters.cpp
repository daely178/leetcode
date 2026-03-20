class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l=0,res=0;
        unordered_map<char, int> mp;

        for(int r=0; r<s.size(); r++) {
            if(mp.find(s[r])!=mp.end()) {
                l = max(mp[s[r]]+1, l);                
            }
            res = max(res, r-l+1);
            mp[s[r]] = r;
        }

        return res;
    }
};


/*
longest substring without duplicate



  0 1 2 3 4 5 6 7
  a b c a b c b b
  l
  r

  mp[a] = 0
  mp[b] = 1
  mp[c] = 2

  l = max(mp[s[r]], l)+1
  mp[s[r]] = r

  ans = max(ans, r-l+1)

*/