class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        par = {}
        
        def find(node):
            if node not in par:
                par[node] = node

            while par[node] != node:
                node = par[node]
            
            return node

        for edge in edges:
            u,v = find(edge[0]), find(edge[1])

            if u != v:
                par[v] = u
            else:
                return False
        
        return len(edges) == n-1
