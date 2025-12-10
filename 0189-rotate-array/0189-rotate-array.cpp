class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if(nums.size() < 2 || k == 0) {
            return;
        }
        int n = nums.size();
        int l=0, r=n-1;
        k=k%n;
        while(l<r) {
            swap(nums[l], nums[r]);
            l++;
            r--;
        }
        l=0;
        r=k-1;
        while(l<r) {
            swap(nums[l], nums[r]);
            l++;
            r--;
        }
        l=k;
        r=n-1;
        while(l<r) {
            swap(nums[l], nums[r]);
            l++;
            r--;
        }
    }
};

/*

remainder = (index + k) % size
[1,2,3,4,5,6,7] k =3

 5,6,7,1,2,3,4
  

    p - c - n
*/