class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = copy.deepcopy(nums)

    def sumRange(self, left: int, right: int) -> int:
        # left <= right
        # 0 <= left <= right < nums.length
        res = 0
        for num in self.nums[left:right+1]:
            res += num
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)