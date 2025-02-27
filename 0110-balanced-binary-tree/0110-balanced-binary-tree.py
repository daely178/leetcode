# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)

        return max(left,right)+1
         
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        left = self.height(root.left)
        right = self.height(root.right)
        
        return abs(left-right)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [(root, False)]
        heights = defaultdict(int)

        while stack:
            curr, visited = stack.pop()
            if visited:
                left = heights[curr.left]
                right = heights[curr.right]
                if abs(left-right) > 1:
                    return False
                heights[curr] = max(left,right)+1
            else:
                stack.append([curr, True])
                if curr.left:
                    stack.append([curr.left, False])
                if curr.right:
                    stack.append([curr.right, False])
        return True

'''
    balanced tree = abs(diff between left and height) <= 1

    getheight

    [3,9,20,null,null,15,7]

'''        