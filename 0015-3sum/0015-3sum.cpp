class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if(nums.size() < 3)
            return {};
        
        vector<std::vector<int>> res;
        sort(nums.begin(), nums.end());
        for(int i=0; i<nums.size(); i++) {
            int l=i+1;
            int r=nums.size()-1;

            if(i>0 && nums[i] == nums[i-1]) {
                continue;
            }
            if(nums[i] > 0) {
                break;       
            }     
            while(l<r) {
                int target = nums[i] + nums[l] + nums[r];
                if(target > 0) {
                    r-=1;
                }
                else if(target < 0) {
                    l+=1;
                }
                else {
                    res.push_back({nums[i], nums[l], nums[r]});
                    l++;
                    r--;
                    while(l<r && nums[l]==nums[l-1]) {
                        l++;
                    }
                    while(l<r && nums[r]==nums[r+1]) {
                        r--;
                    }
                }
            }            
        }
        return res;
    }
};
