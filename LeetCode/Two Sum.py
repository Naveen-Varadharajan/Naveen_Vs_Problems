class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            m=target-nums[i]
            if m in dic:
                return [dic[m],i]
            dic[nums[i]]=i
                