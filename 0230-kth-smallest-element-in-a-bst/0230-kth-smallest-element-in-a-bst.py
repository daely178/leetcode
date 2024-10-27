# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val
            current = current.right


# key points
# 1. binary search tree
# 2. kth smallest value (index starts from 1)
# 3. 1 <= k <= n < 10x4

# # F/U : if modify often by insert / delete, how to optimize?

# inorder - dfs
# preorder - root left... then right right
# postorder - left subtre right subtree - root

# strategy
# 1. Recursive DFS but needs O(k) space
# 2. Recursive DFS with O(1) space


'''

        count = [k]
        ans = []

        def _inorder(root):
        
            if root:
                _inorder(root.left)

                count[0] -= 1
                if count[0] == 0:
                    ans.append(root.val)
                    return

                _inorder(root.right)

        _inorder(root)

        return ans[0]
'''