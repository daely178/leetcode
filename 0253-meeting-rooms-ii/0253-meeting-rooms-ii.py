class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x:x[0])

        pq = []
        heapq.heappush(pq, intervals[0][1])

        for interval in intervals[1:]:
                        
            if pq[0] <= interval[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, interval[1])
                    

        
        return len(pq)



'''
    [0,                 30],
        [5,10],
                 [15,20]

'''        