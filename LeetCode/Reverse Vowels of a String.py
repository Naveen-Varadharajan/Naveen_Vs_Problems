class Solution:
    def reverseVowels(self, s: str) -> str:
        nt=len(s)
        vowel=set("AEIOUaeiou")
        s=list(s)
        m=0
        n=nt-1
        while m<n:
            while m<n and s[m] not in vowel:
                m+=1
            while m<n and s[n] not in vowel:
                n-=1  
            s[m],s[n]=s[n],s[m]
            m+=1
            n-=1
        return "".join(s)
        