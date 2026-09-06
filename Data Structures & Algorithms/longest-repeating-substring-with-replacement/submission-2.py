class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        counts = Counter()
        l = 0
        r = 0
        longest = 0
        while l <= r and r < len(s):
            counts.update([s[r]])
            most_freq = counts.most_common(1)[0][1]
            r += 1
            while (r - l - most_freq) > k:
                counts.subtract([s[l]])
                l += 1
            longest = max(longest, r-l)
        return longest
                

