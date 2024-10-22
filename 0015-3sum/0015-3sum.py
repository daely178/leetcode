class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = set()

        for i in range(n-2):
            j = i + 1
            k = n - 1

            while i < j < k < n:
                target = nums[i] + nums[j] + nums[k]
                if target == 0:
                    result.add((nums[i] , nums[j] , nums[k]))
                    j+=1
                    k-=1
                elif target < 0 :
                    j+=1
                else:
                    k-=1
        return list(result)
'''
    not duplicate triplets
    3 sum = 0

'''