class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        htable = {}
        for id, num in enumerate(nums):
            htable[num] = id

        for id, num in enumerate(nums):
            complement = target - num
            if htable.get(complement) and htable[complement] != id:
                return [id, htable[complement]]