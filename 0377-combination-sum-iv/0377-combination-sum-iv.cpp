class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        memo.clear();
        return cal(nums, target);
    }
private:
    unordered_map<int,int> memo;
    int cal(vector<int>& nums, int target) {
        if(target == 0){
            return 1;
        }
        if(memo.find(target)!=memo.end()){
            return memo[target];
        }
        int result=0;
        for(int num : nums){
            if(target-num>=0){
                result += cal(nums, target-num);
            }
        }
        memo[target] = result;
        return result;
    }
};

/*
    1,2,3
    4
    1 0 0 0
      

    1       2       3
1   2      1. 2    1
1. 1    1
1
*/