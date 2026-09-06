class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b == '(' or b == '[' or b == '{':
                stack.append(b)
            if b == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            if b == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            if b == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
        return len(stack) == 0