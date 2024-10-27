# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:     

        if not root:
            return None

        queue = [root]
        while queue:
            curr = queue.pop()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)                        

        return root   


'''
1. recursive
2. iterative
    q
'''        