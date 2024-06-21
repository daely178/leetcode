class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            #if s1 != s2:
            heapq.heappush(stones, s1-s2)
        
        return -heapq.heappop(stones) if stones else 0

        