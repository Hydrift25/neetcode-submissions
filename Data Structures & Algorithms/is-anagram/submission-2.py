class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        sHash = Counter(s)
        tHash = Counter(t)
        return sHash == tHash