from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq=Counter(nums)
        print(freq)
        for num, count in freq.items():
            if count == 1:
                return num