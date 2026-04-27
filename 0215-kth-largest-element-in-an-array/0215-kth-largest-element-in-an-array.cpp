class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::priority_queue<int> pq;

        for(int i=0; i<nums.size(); i++) {
            pq.push(-nums[i]);
            if(pq.size() > k) {
                pq.pop();
            }
        }
        return -pq.top();
    }
};

/*

heap binary tree O(log n)

default max heap -> negative

while(k--)
    pop 


*/