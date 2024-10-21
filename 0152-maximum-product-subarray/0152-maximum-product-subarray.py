class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        curmin, curmax = nums[0],nums[0]
        res = curmax
        for num in nums[1:]:
            vals = (num, curmin*num, curmax*num)
            curmin, curmax = min(vals), max(vals)
            res = max(res, curmax)
        return res
'''
    rough idea
    for loops and find max for each one

    for num in nums:
        prod = 1
        for num2 in nums[1:]:
            prod*=num2
            ans = max(ans, prod)
    return ans

    or 
    maintain min max for negative value

'''        