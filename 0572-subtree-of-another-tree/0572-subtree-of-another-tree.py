# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSame(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

'''
                1
            2        3
        4.     5 6       7



    inorder - L - Root - R
        - 4 - 2 - 5 - 1 - 6 - 3 - 7
    preorder - Root - L - R
        - 1 - 2 - 4 - 5 - 3 - 6 - 7
    postorder - L - R - Root
        - 4 - 5 - 2 - 6 - 7 - 3 - 1
    levelorder

    1. O(MN)
    2. O()

    def isSame(self, p,q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)

    def dfs(self, node, subRoot):
        if node is None:
            return False
        if self.isSame(node, subRoot):
            return True
        
        return self.dfs(node.left, subRoot) or self.dfs(node.right, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)

'''