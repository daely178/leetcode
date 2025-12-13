class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        long long product=1;
        int n = nums.size();
        int left = 0;
        int ans = 0;
        for(int right=0; right<n; right++) {
            product *= nums[right];

            while(product >= k && left <= right) {
                product /= nums[left];
                ++left;
            }

            ans += (right - left + 1);
        }

        return ans;
    }
};

/*
left, right

10,5,2,6
10, 10,5, 10,5,2, 10,5,2,6, 5, 5,2, 5,2,6, 2, 2,6

*/