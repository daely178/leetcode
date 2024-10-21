class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        table = {}
        for idx,num in enumerate(nums):
            if num not in table:
                table[num] = idx
            else:
                return True
        return False