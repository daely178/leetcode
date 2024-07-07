class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        ans = []
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            indegree[pre[0]] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        nodesVisited = 0
        while q:
            node = q.popleft()
            ans.append(node)
            nodesVisited += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    
        return ans if nodesVisited == numCourses else []