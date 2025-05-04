class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<vector<int>> res(k);
        std::priority_queue<vector<int>> q;

        for(auto p : points) {
            q.push({p[0]*p[0]+p[1]*p[1], p[0], p[1]});
            if(q.size() > k)
                q.pop();
        }

        for(int i=0; i<k; i++){
            vector<int> p = q.top();
            q.pop();
            res[i] = {p[1], p[2]};
        }
        return res;
    }    
};