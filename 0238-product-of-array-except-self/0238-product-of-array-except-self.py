class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product_all = 1
        zero_cnt = 0
        zero_id = 0
        ans = [0]*len(nums)
        for idx, num in enumerate(nums):
            if num:
                product_all*=num
            else:
                zero_cnt+=1
                if zero_cnt>1:
                    return ans
                zero_pos = idx
        if zero_cnt:
            ans[zero_pos] = product_all
            return ans
        for i in range(len(nums)):
            ans[i] = product_all//nums[i]
        return ans
'''
    one zero
    two or more zeroes
    same value
    
    count zero and remember index
    if more than one zero, return all zero
    product all except zero
    divide by its num to get product all except nums[i]
'''
