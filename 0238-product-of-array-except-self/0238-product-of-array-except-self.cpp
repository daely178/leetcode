class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        int left[n];
        int right[n];

        left[0]=1;
        for(int i=1; i<nums.size(); i++) {
            left[i] = nums[i-1]*left[i-1];
        }
        right[nums.size()-1] = 1;
        for(int i=nums.size()-2; i>=0; i--) {
            right[i] = nums[i+1]*right[i+1];
        }

        vector<int> ret(nums.size());
        for(int i=0; i<nums.size(); i++) {
            ret[i] = left[i]*right[i];
        }

        return ret;
    }
};

/*
O(n) time without division
32 bit
[2,2,3,4]
[24,24,16,12]

  .... i ....
  all product of i's left, i , all product of i's right

left = [1,]
left[i] = left[i-1]*nums[i-1]
right = [1,]
right[i] = right[r+1]*nums[i+1]


left = [1,]
left[i] = left[i-1]*nums[i-1]

right = 1
for(i=size-1; i>=0 i--) {
    left[i] = left[i] * right
    right *= nums[i] // right will have all product of i's right
}
*/