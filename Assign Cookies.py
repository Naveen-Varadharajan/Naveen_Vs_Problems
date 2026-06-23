class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i=0
        j=0
        c=0

        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                c+=1
                i+=1
                j+=1
            elif g[i]>s[j]:
                j+=1
            else:
                i+=1
        return c