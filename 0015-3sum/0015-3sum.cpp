class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> temp;
        sort(nums.begin(), nums.end());

        for(int i=0; i<nums.size()-2; i++) {
            int l=i+1, r=nums.size()-1;

            while(l<r) {
                int target = nums[i] + nums[l] + nums[r];
                if(target == 0){
                    temp.insert({nums[i], nums[l], nums[r]});
                    l++;
                    r--;
                }
                else if(target < 0)
                    l++;
                else
                    r--;
            }
        }
        return vector<vector<int>>(temp.begin(), temp.end());
    }
};