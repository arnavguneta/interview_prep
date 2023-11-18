class MinStack:
    # keep track of min in the entire stack by tracking the overall min per push/pull operation
    def __init__(self):
        self._stack = []
        self._min_stack = []
        
    def push(self, val: int) -> None:
        self._min_stack.append(min(val, self._min_stack[-1] if self._min_stack else val))
        self._stack.append(val)

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()