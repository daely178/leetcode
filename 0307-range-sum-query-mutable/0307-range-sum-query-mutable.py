class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        self.buildTree(nums)

    def buildTree(self, nums: List[int]) -> None:
        # Fill leaves of the tree with nums values
        for i in range(self.n):
            self.tree[i+self.n] = nums[i]

        # Fill non-leaf nodes of the tree with the sum of their children
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        # Update the corresponding leaf node
        index += self.n
        self.tree[index] = val

        # Propagate the change up the tree
        while index > 0:
            left = right = index
            if index % 2 == 0:
                right = index + 1
            else:
                left = index - 1
            self.tree[index // 2] = self.tree[left] + self.tree[right]
            index //= 2

    def sumRange(self, left: int, right: int) -> int:
        # Find the sum in the range [left+n, right+n] in the tree
        left += self.n
        right += self.n
        res = 0
        while left <= right:
            if left % 2 == 1:
                res += self.tree[left]
                left += 1
            if right % 2 == 0:
                res += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# -25,3,-24,-99,1,-91,83,-23,83,27,-79,40

'''
    Time = O(N) - TLE
    
    Pre compile through segment tree

n = 8
id.  0 1 2 3 4 5 6 7
val. 1 2 3 4 5 6 7 8

tree 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

    tree[i] = tree[i*2] + tree[i*2+1]
'''