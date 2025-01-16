class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> merged;

        int i=0, j=0;
        int m = nums1.size(), n = nums2.size();

        while (i<m && j<n) {
            if (nums1[i] < nums2[j]){
                merged.push_back(nums1[i++]);
            }
            else {
                merged.push_back(nums2[j++]);
            }
        }
        while (i<m){
            merged.push_back(nums1[i++]);
        }
        while (j<n) {
            merged.push_back(nums2[j++]);
        }

        int center = (int)(merged.size()/2);

        if (merged.size()%2)
            return (double)merged[center];
        
        return (double)(merged[center]+merged[center-1])/2;
    }
};