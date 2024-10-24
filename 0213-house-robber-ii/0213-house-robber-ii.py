class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)
        
        def rob2(vals):
            p,pp,best = 0,0,0
            for val in vals:
                best = max(val+pp, p)
                p,pp = best, p
            return best
        
        return max(rob2(nums[:len(nums)-1]), rob2(nums[1:]))
'''
    arranged in a circle
    1th, 2nd, 3rd, 4th - 1th
    alarm if two adjacent houses are robbed
'''        