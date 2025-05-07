class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> dic;
        for(char c : magazine){
            dic[c]++;
        }
        
        for(char c : ransomNote){
            if(dic.find(c) != dic.end() && dic[c] >0){
                dic[c]--;
            }
            else {
                return false;
            }
        }
        return true;
    }
};