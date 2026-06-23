class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c=0
        for num in nums:
            if num<0:
                c+=1
            if num==0:
                nums.remove(0)

        return(max(c,len(nums)-c))