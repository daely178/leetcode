class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        
        intervals.sort()
        current = intervals[0]
        
        #merged.append(intervals[0])
        for interval in intervals[1:]:
            if current[1] >= interval[0]:
                current[1] = max(current[1], interval[1])
            else:                
                merged.append(current)
                current = interval
        merged.append(current)         
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