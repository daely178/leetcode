class Solution {
public:
    vector<int> findBuildings(vector<int>& heights) {
        vector<int> res;
        int rightMax = 0;
        for(int i=0; i<heights.size(); i++) {
            while(!res.empty() && heights[res.back()] <= heights[i]){
                res.pop_back();
            }
            res.push_back(i);
        }
        return res;
    }
};

/*
        1 2 3 4 --- ocean
        4 2 3 1
*/