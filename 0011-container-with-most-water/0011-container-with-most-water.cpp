class Solution {
public:
    int maxArea(vector<int>& height) {
        int area=0;
        int left = 0, right = height.size()-1;
        while(left<right) {
            area = max(area, (min(height[left], height[right])*(right-left)));
            if(height[left] > height[right]) {
                right--;
            } else {
                left++;
            }            
        }
        return area;
    }
};


/*
Find two lines that contains the most water

left ->  <- right

if height[left] > height[right]
    right--
else
    left++

area = max(area, (right-left) * min(height[right], height[left]))

*/