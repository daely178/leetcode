class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        set<vector<int>> res;
        vector<vector<int>> ans;
        for(int i=0; i<n; ++i) {
            int l=i+1, r=n-1;
            while(l<r) {
                int target = nums[i]+nums[l]+nums[r];
                if(target == 0) {
                    res.insert({nums[i], nums[l], nums[r]});
                    l++;
                    r--;
                } else if(target < 0) {
                    l++;
                } else {
                    r--;
                }
            }
        }
        for(auto c : res){
            ans.push_back(c);
        }

        return ans;
    }
};

/*
sort



*/