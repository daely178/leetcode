class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());

        vector<vector<int>> res;
        for(auto c : intervals) {
            if(res.empty() || res.back()[1] < c[0])
                res.push_back(c);
            else {
                res.back()[1] = max(res.back()[1], c[1]);
            }
        }
        return res;
    }
};

/*
[[1,3],[2,6],[8,10],[15,18]]

  [1,3] [2,6] = [1,6]

*/