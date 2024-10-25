class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x:x[1])
        curr = intervals[0]
        overlapped = 0
        for interval in intervals[1:]:
            if interval[0] >= curr[1]:
                curr = interval
            else:
                overlapped += 1

        return overlapped


'''
    [[1,2],[2,3],[3,4],[1,3]]

    [[2,3],[2,4],[4,5]]

   
    case 1 :                   [  3       1]
                           [1     3 ] 
'''        