class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:           
        intervals.sort()
        merged = [intervals[0]]

        for interval in intervals[1:]:
            if merged[-1][1] >= interval[0]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
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