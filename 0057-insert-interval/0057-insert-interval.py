class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        merged = [intervals[0]]
        for interval in intervals[1:]:
            if merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
            
'''
intervals [[1,2],[3,5],[6,10],[12,16]]
newInterval [4,8]

case 1 : [1,2] vs [4,8] 
interval[1] < newInterval[0]
merged.append(interval)

case 2 : [6,10] vs [4,5] 
interval[0] > newInterval[1]
merged.append(newInterval)
newInterval = interval

case 3 : [6,10] vs [4,11] overlapped
       [x  y]
interval [x   y]
           [x    y]

interval[1] >= newInterval[0] or interval[0] <= newInterval[1]
merge
newInterval[0] = min(interval[0], newInterval[0])
newInterval[1] = max(interval[1], newInterval[1])



'''        