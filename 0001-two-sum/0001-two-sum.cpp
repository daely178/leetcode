class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> mp;

        for(int i=0; i<nums.size(); i++) {
            mp[nums[i]] = i;
        }

        for(int i=0; i<nums.size(); i++) {
            int diff = target - nums[i];
            if(mp.find(diff) !=  mp.end() && i!=mp[diff]) {
                return {i, mp[diff]};
            }
        }

        return {};
    }
};


/*
do not use same element
only one solution

brute force

for i=0 i<n i++
    for j=i+1 j<n j++
        sum = nums[i] + nums[j]
        if sum = target
            return {i,j}

return {};

with additional memory

unsorted_map<int, int> mp

for i=0 i<n i++
    mp[nums[i]] = i

for i=0 i<n i++
    diff = target - nums[i]
    if(mp.find(diff) != mp.end()) {
        return {i, mp[diff]}
    }

return {};
*/
