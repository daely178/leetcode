class Solution {
public:
    int maxProduct(vector<int>& nums) {

        if(nums.size() == 1)
            return nums[0];

        int res = 0;
        int neg=1,pos=1;
        for(auto num : nums) {
            int a = pos*num;
            int b = neg*num;
            pos = max({a, b, num});
            neg = min({a, b, num});
            res = max(res, pos);
        }
        return res;
    }
};