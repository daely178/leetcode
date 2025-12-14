class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        int n=numbers.size();
        int l=0, r=n-1;

        while(l<r) {
            const int sum = (numbers[l] + numbers[r]);
            if(target == sum) {
                return vector<int>({l+1, r+1});
            } else if(sum < target) {
                l++;
            } else {
                r--;
            }
        }
        return vector<int>({0,0});
    }
};



/*
non decreasing order
find two numbers adding up to the target where 1<id1<id2<n

sliding window
l,r
[2,7,11,15]
 l
   r
 target = nums[l]+nums[r]
*/
