class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        while 0 in nums:
            nums.remove(0)

        nn=len(nums)
        nz=n-nn
        for i in range(nz):
            nums.append(0)
        return nums
