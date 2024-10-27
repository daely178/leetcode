# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        stack = [(root,1)]
        maxDepth = 0

        while stack:
            curr,depth = stack.pop(0)
            if curr.left:
                stack.append((curr.left, depth+1))
            if curr.right:
                stack.append((curr.right, depth+1))  
            maxDepth = max(maxDepth, depth)

        return maxDepth            

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        left = self.maxDepth(root.left)+1
        right = self.maxDepth(root.right)+1

        return max(left, right)