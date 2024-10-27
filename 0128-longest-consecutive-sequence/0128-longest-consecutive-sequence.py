class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums2 = sorted(set(nums))
        maxSeq = 0
        while nums2:
            num = nums2.pop()-1
            count = 1
            while num in nums2:
                nums2.pop()
                num-=1
                count += 1
            maxSeq = max(maxSeq, count)

        return maxSeq

class Solution:
   def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for num in s:
            if num-1 not in s:
                count = 0
                while num+count in s:
                    count +=1
                res = max(res, count)
        return res