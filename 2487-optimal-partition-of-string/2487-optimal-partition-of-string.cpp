class Solution {
public:
    int partitionString(string s) {
        vector<int> seen(26,-1);
        int start = 0, count = 1;

        for(int i=0; i<s.size(); i++){
            if(seen[s[i]-'a'] >= start)
            {
                count++;
                start = i;
            }
            seen[s[i]-'a'] = i;
        }
        return count;
    }
};