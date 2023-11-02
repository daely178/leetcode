class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp = x
        reversed = 0

        while temp != 0:
            reversed = reversed*10 + temp%10
            temp = temp // 10
        
        if reversed == x:
            return True
        return False
        