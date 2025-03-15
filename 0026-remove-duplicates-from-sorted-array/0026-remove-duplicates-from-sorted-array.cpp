class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        map<int,int> mp;
        for(int num : nums){
            mp[num]++;
        }
        int k=0;
        for(auto it=mp.begin(); it!=mp.end(); it++){
            nums[k++] = it->first;
        }
        return k;
    }
};