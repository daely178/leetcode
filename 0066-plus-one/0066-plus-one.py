class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        combined = 0
        ans = []

        for digit in digits:
            combined = combined*10 + digit
        
        combined += 1
        while combined:
            ans.append(combined%10)
            combined //= 10
        
        return ans[::-1]

        