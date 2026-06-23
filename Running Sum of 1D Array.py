class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run=[]
        t=0
        for n in nums:
            t=t+n
            run.append(t)

        return run
