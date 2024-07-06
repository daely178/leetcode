class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        par = {}

        def find(node):
            if node not in par:
                par[node] = node
            while node != par[node]:
                node = par[node]
            return node
        
        for u,v in edges:
            pu, pv = find(u), find(v)
            if pu!=pv:
                par[pv] = pu
            else:
                return [u,v]
        return []

'''
    edges = [[1,2],[1,3],[2,3]]

    1 - 2, 3
    2 - 3
    3 - 1, 2

    par = {1:1, 2:2, 
    find(u) != find(v)
    par[v] = u

    union
    
    
'''