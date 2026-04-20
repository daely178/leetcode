class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        std::unordered_map<char ,int> mp;
        int n = s.size();
        int l=0, res = 0;


        for(int r=0; r<n; r++) {
            if(mp.find(s[r]) != mp.end()) {
                // move l
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

two pointers

 0 1 2 3 4 5 6 7
 a b c a b c b b
           l
             r

 a = 3

 seen a:0, b:1 c:2
*/