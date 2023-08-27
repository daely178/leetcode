'''
621. Task Scheduler
Medium
8.8K
1.8K
Companies
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
'''
from typing import List
from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length = len(tasks)
        if n == 0:
            return length
        
        taskdict = defaultdict()
        for task in tasks:
            if taskdict.get(task) == None:
                taskdict[task] = 0
            else:
                taskdict[task] += 1
        dictkeycnt = len(taskdict)
        ans = []
        usedcnt = n
        # k = window size
            
        return len(ans)

        for _ in range(dictkeycnt):
            cooldownTimer = n
            prev = None
            for key, count in taskdict.items():
                
                if count > 0:
                    
                    if cooldownTimer == 0 or prev == key:
                        ans.append("Idle")
                        cooldownTimer = n
                        
                    ans.append(key)
                        
                    usedcnt -= 1
                    taskdict[key] -= 1
                                        
                    prev = key
                        
          # index : 0 = task1 and count 5
          # index : 1 = task2 and count 3
          # index : 2 = task3 and count 1 

s = Solution()

res = s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2)


'''

        if n == 0:
            return length
        
        taskdict = defaultdict()
        for task in tasks:
            if taskdict.get(task) == None:
                taskdict[task] = 0
            else:
                taskdict[task] += 1
        dictkeycnt = len(taskdict)
        ans = []
        usedcnt = n
        # k = window size
            
        return len(ans)

        for _ in range(dictkeycnt):
            cooldownTimer = n
            prev = None
            for key, count in taskdict.items():
                
                if count > 0:
                    
                    if cooldownTimer == 0 or prev == key:
                        ans.append("Idle")
                        cooldownTimer = n
                        
                    ans.append(key)
                        
                    usedcnt -= 1
                    taskdict[key] -= 1
                                        
                    prev = key
                        
          # index : 0 = task1 and count 5
          # index : 1 = task2 and count 3
          # index : 2 = task3 and count 1 
'''          