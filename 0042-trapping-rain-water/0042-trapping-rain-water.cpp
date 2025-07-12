class Solution {
public:
    int trap(vector<int>& height) {
        int left=0, right = height.size()-1;
        int maxL=height[left], maxR=height[right];
        int res = 0;

        while(left<right) {
            if(maxL <= maxR) {
                left+=1;
                maxL = max(maxL, height[left]);
                res += (maxL-height[left]);
            } else {
                right -= 1;
                maxR = max(maxR, height[right]);
                res += (maxR-height[right]);
            }
        }
        return res;

        return res;
    }
};