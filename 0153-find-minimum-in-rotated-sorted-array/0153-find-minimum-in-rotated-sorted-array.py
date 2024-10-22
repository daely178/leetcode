class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def binary_search(l,r):
            if l<r:
                mid = l+(r-l)//2
                if nums[mid] > nums[r]:  # find min
                    return binary_search(mid+1, r)
                return binary_search(l, mid)
            return nums[l]
        return binary_search(0,len(nums)-1)

'''
    log(n)
    find min value to find the first value of ascending order
    binary search
'''