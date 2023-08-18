'''
199. Binary Tree Right Side View
Medium
10.7K
671
Companies
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
import collections

class Solution1: # first try but misunderstanding
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        right_nodes = []
        def _rightSideView(node):
            if node:
                if node.right:
                    right_nodes.append(node.val)
                    _rightSideView(node.right)
                else:
                    right_nodes.append(node.val)
            return right_nodes

        return _rightSideView(root)

class SolutionRecursion:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # exlist1 = [1,2,3,None,5,None,4]
        #    1
        # 2  ,  3 
        #x,5   x,4         
        ans = []

        def _rightSideView(node, level):
            if node == None:
                return

            if level == len(ans):
                ans.append(node.val)
            
            _rightSideView(node.right, level+1)
            _rightSideView(node.left, level+1)
                
        _rightSideView(root, 0)
        return ans
    
class SolutionQ:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
                
        if root == None:
            return None
        ans = []
        q = [root]
        
        while q:
            for i in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(node.val)
        return ans


def tree_creator(values):
    
    Treelists = []

    for i in range(len(values)):
        if values[i] is not None:
            node = TreeNode(values[i])
        else:
            node = None
        if i > 0:
            if i%2: # odd is left
                Treelists[(i-1)//2].left = node
            else:
                Treelists[(i-1)//2].right = node

        Treelists.append(node)
    return Treelists[0]

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
    
s = SolutionQ()


exlist1 = [1,2,3,None,5,None,4]
exlist2 = [1,2,3,4]
#    1
# 2  ,  3 
#x,5   x,4 

head = tree_creator(exlist2)
#head = tree_builder(exlist2)
result = s.rightSideView(head)

printRightTreeNode(result)

#      1
#    2   ,   3 
#  x , 5   x , 4 
# 9,x x,x     x,x

# key points
# 1. look tree from the right side, rightmost value at the same level
# 2. from example, 1,3,4,9

# strategy
# 1. traverse to make from tree to list
# 2. 