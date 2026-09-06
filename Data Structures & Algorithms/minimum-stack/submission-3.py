class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minim = 0
        if self.mini:
            minim = min(val, self.mini[-1])
        else:
            minim = val
        self.mini.append(minim)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
