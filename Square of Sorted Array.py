class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r=[]
        for i in nums:
            r.append(i*i)
        return sorted(r)