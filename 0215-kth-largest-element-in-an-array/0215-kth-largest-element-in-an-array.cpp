class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<vector<int>> maxHeap;
        
        for(auto &p : nums) {
            maxHeap.push({-p});
            if (maxHeap.size() > k){
                maxHeap.pop();
            }
        }
        return -maxHeap.top()[0];
    }
};