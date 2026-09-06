class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanums = "".join(c for c in s if c.isalnum())
        for i in range(len(alphanums)):
            if alphanums[i].lower() != alphanums[-i-1].lower():
                return False
        return True