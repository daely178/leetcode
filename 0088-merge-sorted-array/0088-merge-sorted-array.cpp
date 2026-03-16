class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i,j;

        i = m-1;
        j = n-1;

        for(int k=m+n-1; k>=0; k--) { 
            if(j<0) {
                break;
            }
            if(i>=0 && nums1[i] > nums2[j]) {
                nums1[k] = nums1[i--];
            } else {
                nums1[k] = nums2[j--];
            }
        }
    }
};

/*
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

starting from nums1.size()-1

if nums1[i] > nums2[j]
    nums1[k--] = nums1[1]
*/