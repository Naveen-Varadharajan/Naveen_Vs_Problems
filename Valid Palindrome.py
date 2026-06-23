class Solution:
    def isPalindrome(self, s: str) -> bool:
       s = re.sub("[^a-zA-Z0-9]", "", s).lower()
       t=s[::-1]
       return s==t
        