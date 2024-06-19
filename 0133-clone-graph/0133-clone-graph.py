"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Time : O(m+neighbor)

# Space : O(m) recursive == iterative


class Solution2:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        q = [node]
        nodemap = {}

        while q:
            orgnode = q.pop()

            if orgnode.val not in nodemap:
                nodemap[orgnode.val] = Node(orgnode.val)

            for neighbor in orgnode.neighbors:
                if neighbor.val not in nodemap:
                    nodemap[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)
                nodemap[orgnode.val].neighbors.append(nodemap[neighbor.val])
        
        return nodemap[node.val]

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:     
        
        if not node:
            return node
            
        cloned = {}
        q = [node]

        while q:
            newnode = q.pop()
            if newnode.val not in cloned:
                cloned[newnode.val] = Node(newnode.val)
                
            for neighbor in newnode.neighbors:
                if neighbor.val not in cloned:
                    cloned[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)
                cloned[newnode.val].neighbors.append(cloned[neighbor.val])

        return cloned[node.val]
'''
        1 , 2.  , 3.  , 4
    [[2,4],[1,3],[2,4],[1,3]]
    2 - 4 - 1 - 3
    1 - 3
    2 - 4
'''        