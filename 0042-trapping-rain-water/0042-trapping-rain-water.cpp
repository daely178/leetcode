class Solution {
public:
    int trap(vector<int>& height) {
        int left=0, right=height.size()-1;
        int maxL=height[left], maxR=height[right];

        int res=0;

        while(left<right) {
            if(maxL <= maxR) {
                left+=1;
                maxL = max(maxL, height[left]);
                res += (maxL-height[left]);
            } else {
                right-=1;
                maxR = max(maxR, height[right]);
                res += (maxR-height[right]);
            }
        }
        return res;
    }
};

/*

        [0,1,0,2,1,0,1,3,2,1,2,1]
maxL.    0 0 1 1 2 2 2 2 3 3 3 3    
maxR.    3 3 3 3 3 3 3 2 2 2 1 0  
min(L,R) 0 0 1 1 2 2 2 2 2 2 1 0
height(i)- min(L,R)
         0 0 1 1 0 2 1 0 0 1 0 0


        [0,1,0,2,1,0,1,3,2,1,2,1]

         0 1 
max l                  3 
max r                    2             
res      0 0 1 0 1 2 1 0 0 1 0 0 
*/
