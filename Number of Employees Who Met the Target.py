class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c=0
        for hr in hours:
            if hr>=target:
                c+=1
        return c