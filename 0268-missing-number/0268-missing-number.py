class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)+1
        s = ((n-1)*n)>>1
        for num in nums:
            s-=num
        return s
        