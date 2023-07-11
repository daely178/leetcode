'''
125. Valid Palindrome
Easy
7.3K
7.3K
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

Runtime 67 ms Beats 45.4% Memory 17 MB Beats 73.8%
        n = len(s)
        if n == 1:
            return True
        
        left = 0
        right = n-1
        mid = n//2
        s = s.lower()
        
        while left < right:
            
            while left < right and s[left].isalnum() == False:
                left += 1
            while right > left and s[right].isalnum() == False:
                right -= 1
                
            if left > right or s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
    
        return True

'''


from typing import List
from collections import defaultdict

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # 1. length check
        # 2. convert character to lowercase
        # 3. Brute force
        #   2-1. left - mid - right
        #   2-2. Ignore non alphanumeric
        
        #   1 <= s.length <= 2 * 105
        #   s consists only of printable ASCII characters.
        
        n = len(s)
        if n == 1:
            return True
        
        left = 0
        right = 0
        while left < n:
            if s[left].isalnum()==False:
                right += 1
            left += 1
        if right == n:
            return False
        
        left = 0
        right = n-1
        mid = n//2
        s = s.lower()
        
        while left < right:
            
            while left < right and s[left].isalnum() == False:
                left += 1
            while right > left and s[right].isalnum() == False:
                right -= 1
                
            if left > right or s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
    
        return True

s = Solution()
result = s.isPalindrome("A man, a plan, a canal: Panama")

print(result)