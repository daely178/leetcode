# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        stack = [(root, 1)]
        maxDepth = 0
        while stack:
            root, depth = stack.pop()
            if root.left:
                stack.append((root.left, depth+1))
            if root.right:
                stack.append((root.right, depth+1))
            maxDepth = max(depth,maxDepth)
        return maxDepth

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        left = self.maxDepth(root.left)+1
        right = self.maxDepth(root.right)+1

        return max(left, right)