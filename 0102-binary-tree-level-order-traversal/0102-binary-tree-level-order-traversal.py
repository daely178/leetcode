# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []

        def helper(node, depth):
            if node:
                if len(ans) == depth:
                    ans.append([])
                ans[depth].append(node.val)
                helper(node.left, depth+1)
                helper(node.right, depth+1)
        helper(root,0)
        return ans


    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([(root, 0)])
        ans = []

        while queue:
            node, depth = queue.popleft()
            if node:
                if len(ans) == depth:
                    ans.append([])

                ans[depth].append(node.val)

                if node.left:
                    queue.append((node.left, depth+1))
                if node.right:
                    queue.append((node.right, depth+1))

        return ans

'''
    inorder - left root right
    preorder - root left right
    postorder - left right root
    levelorder - root left right
'''