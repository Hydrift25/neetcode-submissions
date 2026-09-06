class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t2 + t1)
            elif i == '-':
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t2 - t1)
            elif i == '*':
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t2 * t1)
            elif i == '/':
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(int(t2 / t1))
            else:
                stack.append(int(i))
        return stack[0]