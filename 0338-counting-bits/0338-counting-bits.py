class Solution:

    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(1,n+1):
            ans[i] = ans[i&(i-1)]+1
        return ans

'''
    val  0 1 2  3   4   5
         0 1 10 11 100 101 
    
'''        