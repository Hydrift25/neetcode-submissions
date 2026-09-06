class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checkpoint = 0
        crawler = 0
        maxsubstring = 0
        letterSet = set()
        while crawler < len(s):
            if s[crawler] not in letterSet:
                letterSet.add(s[crawler])
                crawler += 1
                maxsubstring = max(maxsubstring, crawler-checkpoint)
            else:
                letterSet.remove(s[checkpoint])
                checkpoint += 1
        return maxsubstring
            
