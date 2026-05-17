class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> seen;
        
        for(int i=0; i<nums.size(); i++) {
            int complement = target - nums[i];
            if(seen.find(complement) != seen.end()){
                return {i, seen[complement]};
            }
            seen[nums[i]] = i;
        }
        return {};
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
