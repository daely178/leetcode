class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int left = 0;

        for (int right = 0; right < nums.size(); right++) {
            if (nums[right] != 0) {
                if(left!=right) {
                    swap(nums[right], nums[left]);
                }
                left++;
            }
        }   
        /*
            [0,1,0,3,12]
            [3,1,0,3,12]
        */
    }
};


/*
    L
        R
0,1,0,3,12
1,0,0,3,12
1,3,0,0,12
1,3,12,0,0


*/
