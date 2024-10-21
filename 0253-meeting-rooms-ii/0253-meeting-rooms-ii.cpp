class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if (intervals.size() == 0) {
            return 0;
        }
        
        // Sort intervals based on their end time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        priority_queue<int, vector<int>, greater<int>> mh;
        
        for (const auto& interval : intervals) {
            if (!mh.empty() && mh.top() <= interval[0]) {
                mh.pop();
            }
            mh.push(interval[1]);
        }
        
        return mh.size();
    }
};