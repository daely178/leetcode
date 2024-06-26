class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        pq = [-f for f in freq.values() if f>0]
        heapq.heapify(pq)

        time = 0
        while pq:
            cycle = n + 1
            store = []
            task_count = 0
            while cycle > 0 and pq:
                curr_freq = -heapq.heappop(pq)
                if curr_freq > 1 :
                    store.append(-(curr_freq-1))
                task_count += 1
                cycle -= 1
            for x in store:
                heapq.heappush(pq,x)
            time += task_count if not pq else n+1
        return time
    

        return 0
'''
tasks = ["A","A","A","B","B","B"], n = 2
n = cooling time

occurrence table
A:3
B:3
AB idle 
AB idle 
AB

required idle = max freq task - 1

tasks = ["A","C","A","B","D","B"], n = 1

A:2
B:2
C:1
D:1

ABCDAB

'''        