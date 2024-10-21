class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxVal, totalMax = nums[0], nums[0]
        for num in nums[1:]:
            maxVal = max(num, maxVal+num)
            totalMax = max(maxVal, totalMax)
        return totalMax
        
'''
        
        -2, 1,-3, 4,-1, 2, 1,-5, 4

        start with first index
        1 vs 1
        -2 vs -3
        -2 vs 4
        3 vs -1
        5 vs 2
        6 vs -5

        continuous subarray with largest sum


'''        