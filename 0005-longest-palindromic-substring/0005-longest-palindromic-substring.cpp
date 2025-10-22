class Solution {
public:
    string longestPalindrome(string s) {
        int maxlen = 0;
        string res = "";
        int l,r;

        for(int i=0; i<s.size(); i++) {
            l=i;
            r=i;
            while(l>=0 && r<s.size() && s[l]==s[r]) {
                if(maxlen < (r-l+1)) {
                    res = s.substr(l, r-l+1);
                    maxlen = r-l+1;
                }
                l--;
                r++;
            }
            l=i;
            r=i+1;
            while(l>=0 && r<s.size() && s[l]==s[r]) {
                if(maxlen < (r-l+1)) {
                    res = s.substr(l, r-l+1);
                    maxlen = r-l+1;
                }
                l--;
                r++;
            }            
        }

        return res;
    }
};

/*
    babad
 l          r
      l
      r

    cbbd
    l
    r
*/