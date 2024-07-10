class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        min_cost = [0]*(len(cost)+1)

        for i in range(2, len(cost)+1):
            one = min_cost[i-1] + cost[i-1]
            two = min_cost[i-2] + cost[i-2]
            min_cost[i] = min(one,two)
        
        return min_cost[-1]

'''
    [1,100,1,1,1,100,1,1,100,1]
     1 or 100 : 1
     100 or 1 : 101 2

'''