class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        intervals.sort()

        merged.append(intervals[0])
        for curr in intervals[1:]:
            if merged[-1][1] < curr[0]:
                merged.append(curr)
            else:
                merged[-1][1] = max(merged[-1][1], curr[1])
        return merged

'''
[[1,3],[2,6],[8,10],[15,18]]

case 1
[1,3],[4,6]
case 2
interval[1] >= newInterval[0]
[1,3],[2,6]
interval[1] = 

if interval[0][1] < interval[1][0]
    append interval[1]
else # interval[0][1] >= interval[1][0]
    append interval[0][0], max(interval[0][1], interval[1][1])
'''        