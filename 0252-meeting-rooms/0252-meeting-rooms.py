class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True

        intervals.sort()
        curr = intervals[0]
        for interval in intervals[1:]:
            if curr[1] > interval[0]:
                return False
            curr = interval
        return True

'''
    [[0,30],[5,10],[15,20]]

    0                   30 
        5   10              compare start and end
                15  20
    
    [[0,30],
               [60,          240],
                   [90,120]]

      
'''        