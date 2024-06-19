class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        hq = []
        for num in nums:
            heapq.heappush(hq, num)
            if len(hq) > k:
                heapq.heappop(hq)
        return hq[0]