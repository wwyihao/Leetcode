class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1,len(s)//2+1):
            if s[0:i]*(len(s)//i) ==s:
                return True
        return False
