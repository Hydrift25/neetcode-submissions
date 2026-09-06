class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if stack and stack.pop() == pairs[i]:
                    continue
                else:
                    return False
        return len(stack) == 0