class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        par = [-1 for _ in range(n)]
        
        def find(node):
            if par[node] == -1:
                return node
            
            return find(par[node])

        for edge in edges:
            u,v = find(edge[0]), find(edge[1])

            if u != v:
                par[v] = u
            else:
                return False
        
        return len(edges) == n-1
