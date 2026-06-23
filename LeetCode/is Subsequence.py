class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=len(s)-1
        j=len(t)-1
        c=0
        while i>=0 and j>=0:
            if s[i]==t[j]:
                c+=1
                i-=1
                j-=1
            else:
                j-=1

        return c==len(s)