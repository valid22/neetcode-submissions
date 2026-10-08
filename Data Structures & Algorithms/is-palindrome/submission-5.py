class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = "".join(i.lower() for i in s if i.isalnum())
        return x == x[::-1]