class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if(nums.size() < 3)
            return {};
        
        set<std::vector<int>> res;
        sort(nums.begin(), nums.end());
        for(int i=0; i<nums.size(); i++) {
            int l=i+1;
            int r=nums.size()-1;
            while(l<r) {
                int target = nums[i] + nums[l] + nums[r];
                if(target > 0)
                    r-=1;
                else if(target < 0)
                    l+=1;
                else {
                    res.insert({nums[i], nums[l], nums[r]});
                    l++;
                    r--;
                }
            }            
        }
        return vector<vector<int>>(res.begin(), res.end());
    }
};

/*
    nums[i] + nums[j] + nums[k] = 0
    i!=j!=k

    brute force
    for i=0 i<n
        for j=i+1 j<n-1;
            for k=j+1 k<n-2;
*/