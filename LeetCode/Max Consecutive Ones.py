class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        m=0
        for num in nums:
            if num==1:
                c+=1
            else:
                m=max(c,m)
                c=0
        m=max(c,m)
        return m