# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def levelorder(node, low=-math.inf, high=math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return levelorder(node.left, low, node.val) and levelorder(node.right, node.val, high)
        
        return levelorder(root)

'''
    left val < root val < right val
    recursive vs iteration

                1
            2        3
        4.     5 6       7

    inorder - left - root - right - recursive
        4-2-5-1-6-3-7
    preorder - root - left - right - recursive
        1-2-4-5-3-6-7
    postorder - left - right -root - recursive
        4-5-2-6-7-3-1
    levelorder - root - left - right with Q
        1-2-3-4-5-6-7
'''