class Solution {
public:
    string longestPalindrome(string s) {
        string res="";
        int longestlen = 0;
        int n=s.size();

        for(int i=0; i<n; i++) {

            // check odd size
            int l=i;
            int r=i;
            while(l>=0 && r<n && s[l]==s[r]) {
                if(longestlen < (r-l+1)) {
                    longestlen = r-l+1;
                    res = s.substr(l, r-l+1);
                }
                l--;
                r++;
            }
            l=i;
            r=i+1;
            while(l>=0 && r<n && s[l]==s[r]) {
                if(longestlen < (r-l+1)) {
                    longestlen = r-l+1;
                    res = s.substr(l, r-l+1);
                }
                l--;
                r++;
            }                        
        }
        return res;
    }
};

/*
sliding window
 babad
 l
  r
 
 cbbd
 l
 r
*/