class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int l = 0;
        int r = nums.size()-1;
        
        while(l<=r) {
            int mid = l+(r-l)/2;

            if(nums[mid] > target) {
                r = mid - 1;
            } else if(nums[mid] < target) {
                l = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
};

/*
O(log n)
binary search

 7 / 2 = 3
 0 1 2 3 4 5 6

mid = l+(r-l)/2

if(nums[mid] > target) {
    r = mid - 1;
} else if(nums[mid] < target) {
    l = mid + 1;
} else {
    return mid;
}

*/