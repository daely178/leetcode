class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numTable = {}
        hq = []
        for num in nums:
            if num in numTable:
                numTable[num] += 1
            else:
                numTable[num] = 0
        for key, count in numTable.items():
            heapq.heappush(hq, (-count, key))
        
        cnt = 0
        ans = []
        while cnt < k:
            freq, val = heapq.heappop(hq)
            ans.append(val)
            cnt += 1
        return ans