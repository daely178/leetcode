class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        vector<string> words;
        string temp;
        while(ss >> temp) {
            words.push_back(temp);
        }
        if(!words.size()) {
            return "";
        }
        string ans;
        for(int i=words.size()-1; i>=0; i--) {
            if(ans.size())
                ans = ans + " " + words[i];
            else
                ans = words[i];
        }
        return ans;
    }
};