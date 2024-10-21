class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        zero_cnt = 0
        zero_pos = 0
        product_all = 1

        # More than 2 zero : return all zero
        # 1 zero : Find zero position and put calculated value for zero position in result array
        # Non zero : divide product all by each num

        for id, val in enumerate(nums):
            if val == 0:
                zero_cnt += 1

                if zero_cnt > 1:
                    return ans
                zero_pos = id
            else:
                product_all *= val

        if zero_cnt==1:
            ans[zero_pos] = product_all
            return ans
        
        for index in range(len(nums)):
            ans[index] = product_all//nums[index]

        return ans
