class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return
        
        letters = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        res = []

        def backtrack(combi, digit):
            if not digit:
                res.append(combi)
                return
            for c in letters[digit[0]]:
                backtrack(combi+c, digit[1:])

                
        backtrack("", digits)

        return res

'''
digits = "23"
["ad","ae","af","bd","be","bf","cd","ce","cf"]

combi = "a"
'''        