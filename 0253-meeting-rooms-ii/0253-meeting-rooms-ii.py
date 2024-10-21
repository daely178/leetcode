class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x:x[1])

        mh = []
        heapq.heappush(mh, intervals[0][1])

        for interval in intervals[1:]:
            if mh[0] <= interval[0]:
                heapq.heappop(mh)

            heapq.heappush(mh, interval[1])

        return len(mh)

'''
    check overlap
    [0,                 30], <- room 1
        [5,10],              <- room 2
                 [15,20]

    [2. 4]
            [7. 10]

    q [ 10, 30, ]
    if 30 <= 5

    [[2,    11],
        [6,     16],
           [11,   16]]
'''        