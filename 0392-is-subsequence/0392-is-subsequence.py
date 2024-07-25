class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s=="":
            return True


        sId = 0
        tId = 0
        matchCnt = 0

        while tId<len(t) and sId<len(s):

            if t[tId] == s[sId]: # c == c
                sId+=1  # 3 

                if sId == len(s): # 3==3
                    return True                
            tId += 1

        return False
        
'''
    s = "abc", 

    id = 0
    while id<len(t) and t[id] != s[0]:
        id += 1
    if id == len(t):
        return False

    if t[id] == s[0]: s = "abc"         id = 0
        next = 1
        match = 1
        for id2 in range(id+1, len(t)): # id = 1
            if t[id2] == s[next] # c == c
                match+=1 # 3
                next+=1  # 3 
        if match == len(s) # 3==3
            return True

    return False
'''        