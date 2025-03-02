class Solution {
public:
    bool canJump(vector<int>& nums) {
        int remaining = 0;
        for(auto num : nums) {
            if(remaining < 0)
                return false;
            if(num > remaining)
                remaining = num;
            remaining -= 1;
        }
        return true;
    }
};