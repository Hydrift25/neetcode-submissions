class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        i = 0
        while i < len(temperatures):
            if i > 0 and len(stack) > 0:
                temp, ind = stack[-1]
                if temp < temperatures[i]:
                    prevTemp, prevInd = stack.pop()
                    res[prevInd] = i - prevInd
                    continue
            stack.append((temperatures[i],i))
            i += 1
        return res
        

