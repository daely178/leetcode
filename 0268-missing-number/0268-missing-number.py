class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = (n*(n+1))>>1
        for num in nums:
            s -= num
        return s
        