class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;

        int res = nums[0];
        int cur = nums[0];

        for(int i=1; i<nums.size(); i++) {
            cur = max(nums[i], cur+nums[i]);
            res = max(res, cur);
        }

        return res;
    }
};

/*
-2,1,-3,4,-1,2,1,-5,4

res = -2
 -2 vs -2+1
 -1 vs -1+-3
 -1 vs -1 +4
  3 vs 3-1
  3 vs 3 + 2
  5 vs 5+1
  6 vs 6-5
  6 vs 6+4
*/
