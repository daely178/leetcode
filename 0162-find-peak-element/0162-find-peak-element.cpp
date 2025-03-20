class Solution {
public:
    int findPeakElement(vector<int>& nums) {

        for(int i=0; i<nums.size(); i++) {
            if(i+1 < nums.size() && nums[i] > nums[i+1])
                return i;
        }
        return nums.size()-1;
    }
};