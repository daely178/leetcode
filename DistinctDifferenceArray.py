from typing import List
from collections import defaultdict

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        visited = []
        prefix = defaultdict(int)
        suffix = defaultdict(int)
        
        for i in range(n):
            for j in range(i+1):
                prefix[nums[j]] += 1

        for i in range(n):
            for j in range(i+1, n-1, 1):
                suffix[nums[j]] += 1
                
        for i in range(n):
            result.append(prefix[nums[i]]-suffix[i])
            
        return result