class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h=len(nums)-1
        l=0
        while l<=h:
            mid=(l+h)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                h=mid-1
        return -1