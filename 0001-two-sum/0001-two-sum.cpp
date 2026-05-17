class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> mp;
        for(int i=0; i<nums.size(); i++) {
            mp[nums[i]] = i;
        }
        for(int i=0; i<nums.size(); i++) {
            int diff = target - nums[i];
            if(mp.find(diff) != mp.end() && i!=mp[diff]) {
                return {i, mp[diff]};
            }
        }
        return {-1,-1};
    }
};


/*
brute force
for(i=0 i<n; i++)
    for(j=1; j<n; j++)
        if( target == (nums[i] + nums[j])) {
            return {i,j};
        }

unordered_map<int,int> mp;
for(i=0 i<n; i++)
    mp[nums[i]] = i;
for(i=0 i<n i++) {
    int diff = target-nums[i]
    if(mp.find(diff) != mp.end() && i!=nums[diff]) {
        return {i, mp[diff]}
    }
}
*/
