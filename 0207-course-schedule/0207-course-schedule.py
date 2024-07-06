class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
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
            nodesVisited += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return nodesVisited == numCourses

'''
    numCourses = 2, prerequisites = [[1,0]]


'''