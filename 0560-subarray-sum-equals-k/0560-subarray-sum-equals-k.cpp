class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        mp[0] = 1;
        int total=0, count=0;

        for(int n : nums) {
            total += n;
            int target = total-k;
            if(mp.find(target) != mp.end()) {
                count += mp[target];
            }
            mp[total]++;
        }   
        return count;     
    }
};