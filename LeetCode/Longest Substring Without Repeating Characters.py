class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rs=set()
        res=0
        l=0
        for i in range(0,len(s)):
            while s[i] in rs:
                rs.remove(s[l])
                l+=1
            rs.add(s[i])
            res=max(res,i-l+1)
        return res