class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strSet = {}
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for s in strs:
            key = ""
            for l in alpha:
                if l in s:
                    key += l * s.count(l)
            print(key)
            if key in strSet:
                strSet[key].append(s)
            else:
                strSet[key] = [s]
        return list(strSet.values())