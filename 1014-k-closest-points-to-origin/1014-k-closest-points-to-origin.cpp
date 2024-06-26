class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<vector<int>> maxHeap;
        vector<vector<int>> result(k);

        for (auto& p : points) {
            maxHeap.push({p[0]*p[0]+p[1]*p[1], p[0],p[1]});
            if (maxHeap.size() > k ) {
                maxHeap.pop();
            }
        }

        for (int i=0; i<k; i++) {
            vector<int> top = maxHeap.top();
            maxHeap.pop();
            result[i] = {top[1], top[2]};
        }
        return result;
    }    
};