class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strSet = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for l in s:
                count[ord(l) - ord('a')] += 1
            strSet[tuple(count)].append(s)
        return list(strSet.values())