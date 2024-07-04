class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        par = {}

        def parent(node):
            if node not in par:
                par[node] = node

            while node != par[node]:
                node=par[node]

            return node
        
        for u,v in edges:
            pu, pv = parent(u), parent(v)

            if pu == pv:
                return [u,v]
            else:
                par[pv] = pu

        return []

# n nodes with one additional edge added
#      1
#   2     3

#  5    1     2
# 
#       4     3


# node and edge
# tree vs graph

# parent and child

# [[1,2],[2,3],[3,4],[1,4],[1,5]]

# parent 1, 1, 1, 1, 5 <- starting

# parent 1, 2, 3, 4, 5