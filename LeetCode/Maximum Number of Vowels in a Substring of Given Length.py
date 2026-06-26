class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel=set("aeiou")
        c=ans=0
        #Brute
        # for i in range(0,len(s)-k+1):
        #     j=i
        #     while(j<i+k):
        #         if  s[j] in vowel:
        #             c+=1
        #         j+=1
        #     ans=max(anc,c)
        #     c=0

        # return ans
        for i in range(k):
            if s[i] in vowel:
                c+=1
        ans=c
        for i in range(k,len(s)):
            if s[i] in vowel:
                c+=1
            if s[i-k] in vowel:
                c-=1
            ans=max(ans,c)
        return ans

            