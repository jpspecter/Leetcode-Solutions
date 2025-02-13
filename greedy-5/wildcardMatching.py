#Time: O(n)
#Space: O(1)
#Program ran on leetcode successfully

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sPtr = 0
        pPtr = 0
        match = 0
        star = -1            
        while (sPtr < len(s)):
            if (pPtr < len(p) and (p[pPtr] == '?' or s[sPtr] == p[pPtr])):
                sPtr+=1
                pPtr+=1
            elif (pPtr < len(p) and p[pPtr] == '*'):
                star = pPtr
                match = sPtr
                pPtr+=1
                
            elif (star != -1):
                pPtr = star + 1
                match+=1
                sPtr = match
            else:
                return False
        while (pPtr < len(p) and p[pPtr] == '*'):
            pPtr+=1

        return pPtr == len(p)