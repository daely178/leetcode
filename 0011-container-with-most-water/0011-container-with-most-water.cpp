class Solution {
public:
    int maxArea(vector<int>& height) {
        int ret = 0;
        int r=height.size()-1, l=0;

        while(l<r)
        {
            ret = max(ret, min(height[l], height[r])*(r-l));
            if(height[l]>height[r])
                r-=1;
            else
                l+=1;
        }
        return ret;
    }
};