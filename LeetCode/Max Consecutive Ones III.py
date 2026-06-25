class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # z=nums.count(0)
        # if z<=k:
        #     return len(nums)
        z=l=r=m=i=0
        while r<len(nums):
            if nums[r]==0:
                z+=1
            
            if z<=k:
                m=max(m,r-l+1)
            else:
                while z>k:
                    if nums[l]==0:
                        z-=1
                    l+=1
            r+=1

        return m