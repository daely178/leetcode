class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        if(nums.empty()) {
            return vector<int>{};            
        }

        vector<int> res(nums.size());
        int r_product=1;
        res[0]=1;
        for(int i=1; i<nums.size(); i++) {
            res[i] = nums[i-1]*res[i-1];
        }
        for(int i=nums.size()-1; i>=0; i--) {
            res[i] = res[i]*r_product;
            r_product *= nums[i];
        }
        return res;
    }
};

/*
[1,2,3,4]

left
 1,1,2,6
right
 24,12,4,1

 24,12,8,6

 1,1,2,6
 R=1
 for n-1 -> 0
 ans[i] =nums[i]*R
 R*=nums[i]


*/