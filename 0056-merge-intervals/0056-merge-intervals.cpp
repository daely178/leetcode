class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> res;

        for(auto interval : intervals){
            if(res.empty() || interval[0] > res.back()[1]){
                res.push_back(interval);
            } else {
                res.back()[1] = max(res.back()[1], interval[1]);
            }
        }
        return res;
    }
};

/*
[[1,3],[2,6],[8,10],[15,18]]

  [1,3] [2,6] = [1,6]

*/