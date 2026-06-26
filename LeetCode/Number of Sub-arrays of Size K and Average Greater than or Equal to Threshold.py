class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:
        c=0
        s=0
        for i in range(k):
            s+=arr[i]
        
        if s//k >=t:
            c+=1
        
        for i in range(k,len(arr)):
            s+=arr[i]
            s-=arr[i-k]
            if s//k >=t:
                c+=1
        return c