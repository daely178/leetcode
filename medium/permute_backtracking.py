'''
46. Permutations
Medium
17.7K
284
Companies
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

from typing import List

class Solution: # Heap's algorithm
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.out=[]

        def _permute(msg, i, length):
            if i==length:
                self.out.append("".join(format(msg)))
            else:
                for j in range(i, length):
                    msg[i], msg[j] = msg[j], msg[i]
                    _permute(msg, i+1, length)
                    msg[j], msg[i] = msg[i], msg[j]

        _permute(list(nums), 0, len(nums))
        return self.out
        
        
class SolutionDFSRecursive:
    def permute(self, nums: List[int]) -> List[List[int]]:        
                        
        res = []
        self.dfs(nums, [], res)
        return res        
   
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            print("i={}, self.dfs(nums[:i]+nums[i+1:]={}, path+[nums[i]]={}, res={})".format(i, nums[:i]+nums[i+1:], path+[nums[i]], res))
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

# call stack
            # seq 8   :  i=1    dfs[1,3],    [2],         [1,2,3], [1,3,2]
            # return to 7,6,5,0
            # seq 7   :  i=0    dfs[],       [1,3,2],     [1,2,3], [1,3,2]
            # seq 6   :  i=0    dfs[],       [1,3,2],     [1,2,3]
            # seq 5   :  i=1    dfs[2],      [1,3],       [1,2,3]
            # return to 1 to run next for loop
            # return to 2 but no more to run
            # return to 3 but no more to run
            # seq 4   :  i=0          dfs[], [1,2,3],   [1,2,3]
            # seq 3   :  i=0          dfs[], [1,2,3],   []           
            # seq 2   :  i=0       dfs[3],   [1,2],     []            
            # seq 1   :  i=0    dfs[2,3],    [1],       []
# global    # seq 0   :  i=0 dfs[1,2,3],     [],        []
                        
'''
dfs(nums = [1, 2, 3] , path = [] , result = [] )
|____ dfs(nums = [2, 3] , path = [1] , result = [] )
|      |___dfs(nums = [3] , path = [1, 2] , result = [] )
|      |    |___dfs(nums = [] , path = [1, 2, 3] , result = [[1, 2, 3]] ) # added a new permutation to the result
|      |___dfs(nums = [2] , path = [1, 3] , result = [[1, 2, 3]] )
|           |___dfs(nums = [] , path = [1, 3, 2] , result = [[1, 2, 3], [1, 3, 2]] ) # added a new permutation to the result
|
|____ dfs(nums = [1, 3] , path = [2] , result = [[1, 2, 3], [1, 3, 2]] )
|      |___dfs(nums = [3] , path = [2, 1] , result = [[1, 2, 3], [1, 3, 2]] )
|      |    |___dfs(nums = [] , path = [2, 1, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] ) # added a new permutation to the result
|      |___dfs(nums = [1] , path = [2, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] )
|           |___dfs(nums = [] , path = [2, 3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] ) # added a new permutation to the result
|
|____ dfs(nums = [1, 2] , path = [3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
       |___dfs(nums = [2] , path = [3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
       |    |___dfs(nums = [] , path = [3, 1, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] ) # added a new permutation to the result
       |___dfs(nums = [1] , path = [3, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] )
            |___dfs(nums = [] , path = [3, 2, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] ) # added a new permutation to the result
''' 
            



s = SolutionDFSRecursive()
result = s.permute(nums = [1,2,3])

print(result)

#       1,            2,           3
#  1,2,3 1,3,2  2,1,3 2,3,1   3,1,2 3,2,1