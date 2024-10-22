class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        l,r =0,n-1
        maxArea = 0
        while l<r:
            maxArea = max(maxArea, min(height[r],height[l]) * (r-l))
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return maxArea

'''
    two pointer
    area = (r-l)*min height (r,l)
'''

