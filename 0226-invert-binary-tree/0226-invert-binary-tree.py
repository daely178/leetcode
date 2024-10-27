# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root

class Solution2:
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
   queue or deque
   stack

#[4,2,7,1,3,6,9]
# stack = 4 - 2 - 1 - None - None(1.right) - 3 None None - 
# 1.left = None, 1.right = None return 1
# 3.left = None, 3.right = None return 3
# 2.left = 3 2.right = 1

'''        