class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True

        intervals.sort(key=lambda x:x[0])        

        mh = []
        heapq.heappush(mh, intervals[0][1])

        for interval in intervals[1:]:
            if mh[0] <= interval[0]:
                heapq.heappop(mh)
            else:
                return False
            heapq.heappush(mh, interval[1])

        return True if len(mh)==1 else False


'''
    [[0,30],[5,10],[15,20]]

    0                   30 
        5   10              compare start and end
                15  20
'''        