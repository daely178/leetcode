class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        dic = {'a':a, 'b':b, 'c':c}
        hq = []
        res = ''
        for key, val in dic.items():
            if val > 0:
                heapq.heappush(hq, (-val, key))
        
        while hq:
            count, ch = heapq.heappop(hq)
            if len(res)>1 and res[-1] == res[-2] == ch:
                if hq:
                    count2, ch2 = heapq.heappop(hq)                    
                    res += ch2                    
                    if count2 != -1:                        
                        heapq.heappush(hq, (count2+1, ch2))
                    heapq.heappush(hq, (count, ch))
            else:
                res += ch
                if count != -1:
                    heapq.heappush(hq, (count+1, ch))

        return res

'''
    a = 1, b = 1, c = 7
    c = 7, a = 1, b = 1


'''            