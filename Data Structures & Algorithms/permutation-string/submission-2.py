class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if len(s1) > len (s2):
            return False
        l, r = 0, len(s1)-1
        s1count = Counter(s1)
        s2count = Counter(s2[l:r+1])
        if s1count == s2count:
            return True
        while r < len(s2)-1:
            s2count = +s2count
            s2count.subtract(s2[l])
            l+=1
            r+=1
            s2count.update(s2[r])
            if s1count == s2count:
                return True
        return False
        