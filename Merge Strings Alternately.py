class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ms=""
        i=j=0
        while i<len(word1) and j<len(word2):
            ms+=word1[i]+word2[j]
            i+=1
            j+=1
        
        ms += word1[i:]
        ms += word2[j:]


        return ms