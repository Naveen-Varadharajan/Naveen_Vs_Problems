class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1=set(nums1)
        s2=set(nums2)

        res=[]
        for el1 in s1:
            for el2 in s2:
                if el1==el2:
                    res.append(el1)
        return res