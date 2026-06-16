class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.size() == 0) {
            return -1;
        }

        int curr=nums[0], ans=nums[0];

        for(int i=1; i<nums.size(); i++) {
            curr = max(nums[i], nums[i]+curr);
            ans = max(curr, ans);
        }
        return ans;
    }
};