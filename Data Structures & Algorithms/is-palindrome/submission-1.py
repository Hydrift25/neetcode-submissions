class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanums = "".join(c.lower() for c in s if c.isalnum())
        return alphanums == alphanums[::-1]