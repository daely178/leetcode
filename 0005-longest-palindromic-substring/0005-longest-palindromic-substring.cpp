class Solution {
public:
    string longestPalindrome(string s) {
        int m = s.size();
        int maxlen = 0;
        string res="";
        for(int i=0; i<s.size(); i++) {            

            // odd case
            // babad
            int l=i, r=i;
            while (l >= 0 && r < m && s[l] == s[r]) {
                if ((r - l + 1) > maxlen) {
                    maxlen = r - l + 1;
                    res = s.substr(l, r - l + 1);
                }
                l--;
                r++;
            }       
            l = i;
            r = i + 1;
            while (l >= 0 && r < m && s[l] == s[r]) {
                if ((r - l + 1) > maxlen) {
                    maxlen = r - l + 1;
                    res = s.substr(l, r - l + 1);
                }
                l--;
                r++;
            }          
        }
        return res;
    }
};