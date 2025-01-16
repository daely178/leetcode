class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        i,j=0,0
        merged = []

        while i<len(nums1) and j<len(nums2):
            if nums1[i] > nums2[j]:
                merged.append(nums2[j])
                j+=1
            else:
                merged.append(nums1[i])
                i+=1
        while i<len(nums1):
            merged.append(nums1[i])
            i += 1
        while j<len(nums2):
            merged.append(nums2[j])
            j += 1

        if len(merged)%2:
            return merged[len(merged)//2]
        else:
            return (merged[len(merged)//2]+merged[len(merged)//2-1])/2

# Goal : find mid or mid-1 from merged lists

# nums1[mid-1], nums1[mid]
# nums2[0], nums2[mid]

# if nums2[0] > nums1[max] : find from nums1
# if some of nums2 is winthin nums1

# while i < (m+n)//2

# nums1 = [1,3], nums2 = [2]
# nums1 = [1,2], nums2 = [3,4]
# nums1 = [14,57,66], nums2 = [1,9,15,17,19,21,23,56,57,67,69]
# [1,9,15,17,19,56,57,67,69]
# [1,9,14,15,17,19,56,57,66,67,69]

# if (len1 + len2)%2: mid, else: (mid+(mid-1))/2

# Select longer length of array
# 1. find median of nums1
# 2. find median of nums2
# 3. 