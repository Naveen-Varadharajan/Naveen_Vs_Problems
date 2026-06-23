class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        co=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[co]=nums[i]
                co+=1
        return co

