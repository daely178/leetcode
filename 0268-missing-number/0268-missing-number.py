class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)+1
        s = 0
        for i in range(n):
            s+=i
        for num in nums:
            s-=num
        return s
        