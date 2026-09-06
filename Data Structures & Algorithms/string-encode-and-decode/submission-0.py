class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        return s

    def decode(self, s: str) -> List[str]:
        ans = []
        strnum = ""
        strstart = False
        num = 0
        word = ""
        for i in s:
            if i.isdigit() and not strstart:
                strnum += i
                num = 0
            elif i == '#' and not strstart:
                num = int(strnum)
                strnum = ""
                strstart = True
            elif strstart and num > 0:
                word += i
                num -= 1
            if num == 0 and strstart:
                strstart = False
                ans.append(word)
                word = ""
        return ans

