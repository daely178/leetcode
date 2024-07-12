class Solution:
    def rob(self, nums: List[int]) -> int:

        prev, prevprev = 0,0
        for val in nums:
            best = max(val+prevprev, prev)
            prev,prevprev = best, prev
        return max(prev, prevprev)

'''
    constrains : alert if robbing adjacent houses
    return max amount without alert

    [1,2,3,1] 1+3

    [2,7,9,3,1] 2+9+1
'''