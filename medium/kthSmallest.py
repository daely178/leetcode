'''
230. Kth Smallest Element in a BST
Medium
10.4K
188
Companies
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
'''

from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #     root
        # left.   right
        # left < root < right

        values = []

        def inorder(root, k):
            
            if len(values) == k:
                return
            
            if root:
                inorder(root.left, k)                
                values.append(root.val)
                inorder(root.right, k)
        
        inorder(root, k)
        
        #1 <= k <= n <= 104
        return values[k-1]

class SolutionConstantMem:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #     root
        # left.   right
        # left < root < right

        # inorder - dfs
        ans = []
        count = [0]
        count[0] = k

        def inorder(root, count):
            
            if not root:
                return
            
            inorder(root.left, count)     

            count[0] -= 1
            if count[0] == 0:
                ans.append(root.val)
                return           

            inorder(root.right, count)
        
        inorder(root, count)
        
        #1 <= k <= n <= 104
        return ans[0]

# inorder - dfs
# preorder - root left... then right right
# postorder - left subtre right subtree - root


def tree_builder(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = collections.deque([root])
    leng = len(values)
    nums = 1
    while nums < leng:
             node = queue.popleft()
             if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums+1]) if values[nums+1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1
    return root
    
def printRightTreeNode(result):
    for i in range(len(result)):
        print("result[{}] = {}".format(i, result[i]))
    
s = SolutionConstantMem()


exlist1 = [5,3,6,2,4,None,None,1]
#      5
#   3  ,  6 
#  2,4
#1 

head = tree_builder(exlist1)
result = s.kthSmallest(head, k=3)

#printRightTreeNode(result)
print(result)
        
