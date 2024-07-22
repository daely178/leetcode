class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[1])

        prev = 0
        valid = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[prev][1]:
                prev = i
            else:
                valid += 1
        return valid


'''
    [[1,2],[2,3],[3,4],[1,3]]

    if interval[0] < newInterval[1]
        ans += 1
'''        