class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n=len(accounts)
        wel=0
        for i in range(n):
            wel=max(wel,sum(accounts[i]))
        return wel