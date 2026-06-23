class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=len(nums)
        return (a*(a+1)//2)-sum(nums)
